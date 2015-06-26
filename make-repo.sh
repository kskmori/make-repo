#!/bin/bash
# Copyright (c) 2013 Takatoshi MATSUO (matsuo.tak@gmail.com)
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of version 2 of the GNU General Public License as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it would be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
# Further, this software is distributed without any warranty that it is
# free of the rightful claim of any third person regarding infringement
# or the like.  Any license provided herein, whether implied or
# otherwise, applies only to this software file.  Patent licenses, if
# any, provided herein do not apply to combinations of this program with
# other software, or any other product whatsoever.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write the Free Software Foundation,
# Inc., 59 Temple Place - Suite 330, Boston MA 02111-1307, USA.

CONF_FILE="make-repo.conf"

### functions ###
get_version() {
    local name
    name=`find $RPMDIRS -maxdepth 1 -type f | grep -v "src\.rpm" | grep "/$1-[0-9].*\.rpm" | sed "s/^.*\/$1-//g" | sed "s/\.x86_64.*//g" | sed "s/\.noarch.*//g"`
    if [ ! -n "$name" ]; then
        echo "$1 file not found" >&2
        exit 1
    fi
    echo "$name"
}
get_filename_rpm() {
    local rpmname="$1"
    local filename=""
    filename=`find $RPMDIRS -maxdepth 1 -type f | grep -v "src\.rpm" | grep "$rpmname-[0-9].*\.rpm"`
    if [ $? -ne 0 ]; then
        echo "$rpmname file not found" >&2
        exit 1
    fi
    if [ `echo -e "$filename" | wc -l` -ge 2 ]; then
        echo "multiple $rpmname file found: $filename" >&2
        exit 1
    fi
    echo "$filename"
}
get_filename_srpm() {
    local rpmname="$1"
    local filename=""
    filename=`find $SRPMDIR -maxdepth 1 -type f | grep "$i-[0-9].*src\.rpm"`
    if [ $? -ne 0 ]; then
        echo "$rpmname src file not found" >&2
        exit 1
    fi
    if [ `echo -e "$filename" | wc -l` -ge 2 ]; then
        echo "multiple $rpmname file found: $filename" >&2
        exit 1
    fi
    echo "$filename"
}

### make pacemaker-all.spec file ###
make_pacemaker_set_sepc() {
    local pkg
    local version

    cat > $SET_SPEC_FILE <<END
Name: pacemaker-all
Version: ${rpm_ver}
Release: ${rpm_release}%{?dist}
Summary: pacemaker set
Group: Environment/Daemons
License: GPL
URL: http://sourceforge.jp/projects/linux-ha/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch

END

    for pkg in ${!REQUIRE_RPM[@]}; do
        if [ -n "${REQUIRE_RPM[$pkg]}" ]; then
            if ! echo "${REQUIRE_RPM[$pkg]}" | grep -q "^[<>=]"; then
                echo "$pkg version is invalid : \"${REQUIRE_RPM[$pkg]}\""
                exit 1
            fi
            if ! version=`get_version $pkg`; then
                exit 1
            fi
            echo "Requires: $pkg ${REQUIRE_RPM[$pkg]} $version" >> $SET_SPEC_FILE
        else
            echo "Requires: $pkg" >> $SET_SPEC_FILE
        fi
    done


    cat >> $SET_SPEC_FILE <<END

%description
This package collects required packages as Pacemaker-set.

%files

%changelog
END

    echo -e "$changelog" >> $SET_SPEC_FILE
}

### make pacemaker-repo.spec file ###
make_pacemaker_repo_spec() {
    cat > $REPO_SPEC_FILE << END
Name: pacemaker-repo
Version: ${rpm_ver}
Release: ${rpm_release}%{?dist}
Summary: Packages for High-Availability Linux
Group: System Environment/Base
License: GPL
URL: http://sourceforge.jp/projects/linux-ha/
Source0: %{name}-%{version}-%{release}.%{_arch}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%define linux_ha_dir  /opt/linux-ha
%define pm_dir        %{linux_ha_dir}/pacemaker
%define rpm_dir       %{pm_dir}/rpm
%define repodata_dir  %{pm_dir}/repodata
%define repo_dir      %{_sysconfdir}/yum.repos.d

%description
Install Pacemaker repository.

%prep

%setup -q -n %{name}-%{version}-%{release}.%{_arch}

%build

%install
rm -rf \${RPM_BUILD_ROOT}

mkdir -p \${RPM_BUILD_ROOT}%{rpm_dir}
cp -pr rpm/* \${RPM_BUILD_ROOT}%{rpm_dir}

mkdir -p \${RPM_BUILD_ROOT}%{repodata_dir}
cp -pr repodata/* \${RPM_BUILD_ROOT}%{repodata_dir}

mkdir -p \${RPM_BUILD_ROOT}%{repo_dir}
cp -p $YUM_CONF_FILE \${RPM_BUILD_ROOT}%{repo_dir}

%files
%defattr(-,root,root)
%dir %{linux_ha_dir}
%dir %{pm_dir}
%{rpm_dir}
%{repodata_dir}
%config(noreplace) %{repo_dir}/$YUM_CONF_FILE

%clean
rm -rf \${RPM_BUILD_ROOT}

%changelog
* Fri Jul 12 2013 Takatoshi MATSUO
- Initial version
END
}

make_pacemaker_set() {
    local rpmfile

    make_pacemaker_set_sepc
    ### build pacemaker-all ###
    echo "building pacemaker-all ...."
    rpmfile=`LANG=C rpmbuild -bb $SET_SPEC_FILE | grep "Wrote:" | cut -d ":" -f 2`
    if [ ! -n "$rpmfile" ]; then
        echo "rpmbuild failed"
        exit 1
    fi

    echo

    rm -f $REPO_DIR/rpm/pacemaker-all*rpm
    echo "mv $rpmfile ."
    mv $rpmfile $REPO_DIR/rpm/
}

### pacemaker.repo file ###
make_yum_repository() {
    cat >> $REPO_DIR/$YUM_CONF_FILE << END
[linux-ha-ja-pacemaker]
name=linux-ha-ja-pacemaker
baseurl=file:///opt/linux-ha/pacemaker/
enabled=1
gpgcheck=0
END

    echo "Creating yum repository ..."
    cd $REPO_DIR
    createrepo .
    if [ $? -ne 0 ]; then
        echo "createrepo failed" >&2
        cd -
        exit 1
    fi
    cd -
}

# arg1 : dir
check_dir() {
    if [ -d "$1" ]; then
        YN="E"
        echo "$1 dir exists."
        echo "Delete?(d) Skip?(s) Exit?(E) d/s/E"
        read YN

        case "$YN" in
            d)   
                rm -rf "$1"
                return 0
                ;;
            s)   
                return 2
                ;;
            *)   
                echo "Please delete $1 directory"
                exit 1
                ;;
        esac
    fi
    rm -f $1.tar.gz
}

mkdir_and_cp_pacemaker_repo() {
    local rc
    local filename

    check_dir "$REPO_DIR"
    rc=$?
    if [ $rc -ne 0 ]; then
        return $rc
    fi

    if [ -d "$REPO_DIR" ]; then
        YN="N"
        echo "$REPO_DIR dir exists. Delete?(d) Skip?(s) d/s/N"
        read YN

        case "$YN" in
            d)   
                rm -rf $REPO_DIR
                ;;
            s)   
                return 2
                ;;
            *)   
                echo "Please delete $REPO_DIR dir"
                exit 1
                ;;
        esac
    fi

    ### make main repository dir ###
    mkdir -p $REPO_DIR/rpm
    for i in $BIN_FILES; do
        filename=`get_filename_rpm $i`
	if [ $? -ne 0 ]; then exit 1; fi
        echo "copy $filename"
        cp $filename $REPO_DIR/rpm/
    done
    chown root:root -R $REPO_DIR
    chmod 644 $REPO_DIR/rpm/*
}

make_pacemaker_repo() {
    local rpmfile

    mkdir_and_cp_pacemaker_repo || return $?
    make_pacemaker_set

    make_pacemaker_repo_spec
    make_yum_repository

    ### build pacemaker-repo ###
    rm -f /root/rpmbuild/SOURCES/${REPO_DIR}.tar.gz
    echo "Compressing ... ${REPO_DIR}.tar.gz"
    tar zcf /root/rpmbuild/SOURCES/${REPO_DIR}.tar.gz $REPO_DIR

    rpmfile=""
    echo "building pacemaker-repo .... see pacemaker-repo_build.log"
    rpmfile=`LANG=C rpmbuild -bb $REPO_SPEC_FILE 2> pacemaker-repo_build.log | grep "Wrote:" | cut -d ":" -f 2`
    if [ ! -n "$rpmfile" ]; then
        echo "rpmbuild failed"
        exit 1
    fi

    echo
    echo "mv $rpmfile ."
    mv $rpmfile .
}

### make pacemaker-debuginfo-repo ###
make_pacemaker_debuginfo_repo() {
    local filename

    check_dir "$REPO_DEBUG_DIR" || return $?

    mkdir $REPO_DEBUG_DIR
    for i in $DEBUG_FILES; do
        filename=`get_filename_rpm $i`
	if [ $? -ne 0 ]; then exit 1; fi
        echo "copy $filename"
        cp $filename $REPO_DEBUG_DIR
    done
    COMPRESS_DIR="$COMPRESS_DIR $REPO_DEBUG_DIR"
}

### make pacemaker-src-repo ###
make_pacemaker_src_repo() {
    local filename

    check_dir "$REPO_SRC_DIR" || return $?

    mkdir $REPO_SRC_DIR
    for i in $SRC_FILES; do
        filename=`get_filename_srpm $i`
	if [ $? -ne 0 ]; then exit 1; fi
        echo "copy $filename"
        cp $filename $REPO_SRC_DIR
    done
    COMPRESS_DIR="$COMPRESS_DIR $REPO_SRC_DIR"
}

### compress debuginfo-repo, src-repo ###
compress_dir() {
    if [ `echo "$COMPRESS_DIR" | wc -w` -eq 0 ]; then
        return 0
    fi
    for i in $COMPRESS_DIR; do
        chown -R root:root $i
        chmod 644 $i/*
        chmod 755 $i
        echo "Compressing ... $i.tar.gz"
        tar zcf $i.tar.gz $i
    done
}


usage() {
    echo "$0: [-r|--release RELSPEC] [-R|--rpmbuilddir] [rpm_dir]"
    echo "  -r|--release RELSPEC: repository package version"
    echo "      format: RELSPEC=\${rpm_ver}-\${rpm_release}"
    echo "  -R|--rpmbuilddir: build under $HOME/rpmbuild directory for packaging"
    echo "      The following directories are used instead of the current directory or [rpm_dir]."
    echo "         $HOME/rpmbuild/REPOPKG: the output repository packages"
    echo "         $HOME/rpmbuild/RPMS   : binary rpms to be packaged"
    echo "                                 (x86_64 and noarch only; no i386 support yet)"
    echo "         $HOME/rpmbuild/SRPMS  : source rpms to be packaged"
    echo "  --nosrc: skip building source packages for development"
    echo
    echo "Example 1: $0 -r \"1.1.13-1.1\" -R"
    echo "Example 2: rpm_ver=\"1.1.10\" rpm_release=\"1.1\" dist=\"el6\" $0 [rpm_dir]"
}

### main ######################################################################

# configurable options
RPMDIRS=""
SRPMDIR=""
REPO_OUTPUT_DIR=""
RELSPEC=""
opt_rpmdir=""
use_rpmbuiddir=false
buildsrc=true

### parse options ###
OPT=`getopt -o r:R --long release:,rpmbuilddir,nosrc,help -- "$@"`
if [ $? != 0 ] ; then
  exit 1
fi
eval set -- "$OPT"

while true; do
  case "$1" in
      -r|--release) RELSPEC="$2"; echo "WARN: Not implemented yet: -r|--release" 1>&2; shift; shift;;
      -R|--rpmbuilddir) use_rpmbuilddir=true; shift;;
      --nosrc) buildsrc=false; shift;;
      --help) usage; exit 0;;
      --) shift; break;;
      *) echo "Unknown option: $1" 1>&2; usage; exit 1;;
  esac
done
if [ -n "$1" ]; then
    opt_rpmdir="$1"
fi

if [ "$use_rpmbuilddir" ]; then
    RPMDIRS="$HOME/rpmbuild/RPMS/noarch $HOME/rpmbuild/RPMS/x86_64"
    SRPMDIR="$HOME/rpmbuild/SRPMS"
    REPO_OUTPUT_DIR="$HOME/rpmbuild/REPOPKG"
fi
if [ "$opt_rpmdir" ]; then
    if [ ! -d "$opt_rpmdir" ]; then
	echo "rpm directory \"$opt_rpmdir\" not found" >&2
	usage
	exit 1
    fi
    RPMDIRS="$opt_rpmdir"
    SRPMDIR="$opt_rpmdir"
    if [ "$use_rpmbuilddir" ]; then
	echo "WARN: both -R option and [rpm_dir] parameter has specified: continue with overriding by [rpm_dir]"
    fi
fi
if [ -z "$RPMDIRS" ]; then
    echo "Neither rpm directory or -R options specified" >&2
    usage
    exit 1
fi

# to make sure which directories will be used
echo "Packaging options"
echo " RPMDIRS = $RPMDIRS"
echo " SRPMDIR = $SRPMDIR"
echo " REPO_OUTPUT_DIR = $REPO_OUTPUT_DIR"
echo " RELSPEC = $RELSPEC"

### validate ###
# if dist was not specified then use the system default
#  $dist is without a period character in this script.
if [ -z "$dist" ]; then
 dist=`rpmbuild --eval %{dist} | sed 's/^\.//'`
 echo "Use dist='$dist'"
fi

if [ ! -n "$rpm_ver" ] || [ ! -n "$rpm_release" ] || [ ! -n "$dist" ] ; then
    echo "Please specify rpm_ver and rpm_release and dist." >&2
    echo "Example: rpm_ver=\"1.1.10\" rpm_release=\"1.1\" dist=\"el6\" $0 [rpm_dir]"
    exit 1
fi

### read configuration ###
if [ ! -f $CONF_FILE ]; then
    echo "$CONF_FILE not found" >&2
    exit 1
fi

source $CONF_FILE

if [ ! -n "$BIN_FILES" ] || [ ! -n "$DEBUG_FILES" ] || [ ! -n "$SRC_FILES" ] ; then
    echo "Conf file is invalid." >&2
    exit 1
fi

# command check
for i in "rpmbuild createrepo"; do
    which $i > /dev/null 2>&1
    if [ $? -ne 0 ]; then
        echo "$i not found" >&2
        exit 1
    fi
done

# create and move to the build working directory if specified
if [ -n "$REPO_OUTPUT_DIR" ]; then
    mkdir -p $REPO_OUTPUT_DIR
    cd $REPO_OUTPUT_DIR
fi

# global params
SET_SPEC_FILE="pacemaker-all.spec"
REPO_SPEC_FILE="pacemaker-repo.spec"
YUM_CONF_FILE="pacemaker.repo"
REPO_DIR="pacemaker-repo-${rpm_ver}-${rpm_release}.${dist}.x86_64"
REPO_SRC_DIR="pacemaker-src-${rpm_ver}-${rpm_release}.${dist}.x86_64"
REPO_DEBUG_DIR="pacemaker-debuginfo-${rpm_ver}-${rpm_release}.${dist}.x86_64"
COMPRESS_DIR=""



make_pacemaker_repo
make_pacemaker_debuginfo_repo
$buildsrc && make_pacemaker_src_repo
compress_dir

# print total number of packages
set -- $BIN_FILES
num_bin=$#
set -- $DEBUG_FILES
num_debug=$#
set -- $SRC_FILES
num_src=$#

echo "Total number of packages"
echo " BIN_FILES   : $num_bin"
echo " DEBUG_FILES : $num_debug"
echo " SRC_FILES   : $num_src"


echo "done"
