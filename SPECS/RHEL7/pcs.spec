%bcond_without clufter
%if %{with clufter}
%{!?clufter_name:    %global clufter_name     clufter}
%{!?clufter_pkg_name:%global clufter_pkg_name python-clufter}
%{!?clufter_version: %global clufter_version  0.3.0}
%{!?clufter_source:  %global clufter_source   %{clufter_name}-%{clufter_version}}
%{!?clufter_script:  %global clufter_script   %{_libexecdir}/%{clufter_name}}
%{!?clufter_bashcomp:%global clufter_bashcomp %{_sysconfdir}/bash_completion.d/%(basename "%{clufter_script}")}
%{!?clufter_check:   %global clufter_check    1}

%{!?clufter_ccs_flatten:     %global clufter_ccs_flatten     %{_libexecdir}/%{clufter_source}/ccs_flatten}
%{!?clufter_editor:          %global clufter_editor          %{_bindir}/nano}
%{!?clufter_ra_metadata_dir: %global clufter_ra_metadata_dir %{_datadir}/cluster}
%{!?clufter_ra_metadata_ext: %global clufter_ra_metadata_ext metadata}
%endif

Name: pcs		
Version: 0.9.137
Release: 13%{?dist}
License: GPLv2
URL: http://github.com/feist/pcs
Group: System Environment/Base
#BuildArch: x86_64
BuildRequires: python2-devel
Summary: Pacemaker Configuration System	
Source0: http://people.redhat.com/cfeist/pcs/pcs-withgems-%{version}.tar.gz
Source1: HAM-logo.png
Patch0: bz1115537-Improve-error-messages-for-scoped-cib-operations.patch
Patch1: bz1156311-Fix-waiting-for-resource-operations.patch
Patch2: bz1170150-Fix-displaying-globally-unique-clones-in-GUI.patch
Patch3: bz1054491-Fix-acl-add-duplicate-names-and-remove-roles-in-GUI.patch
Patch4: bz1179023-Added-support-for-resource-discovery-on-location-con.patch
Patch5: bz1054491-Delete-a-user-group-when-deleting-its-last-role-in-GUI.patch
Patch6: bz1179023-Added-support-for-resource-discovery-on-location-con-2.patch
Patch7: bz1054491-Add-acl-enable-and-disable-commands-3.patch
Patch8: bz1180390-Stop-deleted-resource-before-removing-its-constraint.patch
Patch9: bz1180506-stop-cluster-nodes-in-parallel.patch
Patch10: bz1180506-Warn-if-nodes-stop-will-cause-a-loss-of-the-quorum.patch
Patch11: bz1180506-3-Keep-cluster-quorate-during-destruction-as-long-as-possible.patch

# NOTE: Source20 and Patch200+ belong to python-clufter

BuildRequires: ruby >= 2.0.0 ruby-devel rubygems pam-devel git
BuildRequires: systemd-units rubygem-bundler
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Requires: pacemaker-cli corosync ruby >= 2.0.0 pacemaker
%if %{with clufter}
Requires: %{clufter_pkg_name}
%endif

%description
pcs is a corosync and pacemaker configuration tool.  It permits users to
easily view, modify and created pacemaker based clusters.


# subpackage metadata begin
%if %{with clufter}
%package -n %{clufter_pkg_name}
Group:    System Environment/Base
Summary:  Tool/library for transforming/analyzing cluster configuration formats
License:  GPLv2+
URL:      https://github.com/jnpkrn/%{clufter_name}
# clufter as such module ccs_flatten
BuildRequires:  python-setuptools
%if %{clufter_check}
BuildRequires:  python-lxml
%endif
Requires:       python-lxml
# ccs_flatten
BuildRequires:  libxml2-devel
Requires:       libxml2
# "extras"
Requires:       %{clufter_editor}
Source20:       https://people.redhat.com/jpokorny/pkgs/%{clufter_name}/%{clufter_source}.tar.gz

%description -n %{clufter_pkg_name}
While primarily aimed at (CMAN,rgmanager)->(Corosync/CMAN,Pacemaker) cluster
stacks configuration conversion (as per RHEL trend), the command-filter-format
framework (capable of XSLT) offers also other uses through its plugin library.
# subpackage metadata end
%endif


%prep
%if %{with clufter}
%autosetup -a20 -p1 -S git

# for some esoteric reason, the line above has to be empty
ln -s "%{clufter_source}" "%{clufter_name}"
%else
%autosetup -p1 -S git

# ditto as previous comment
%endif
cp -f %SOURCE1 pcsd/public/images

%if %{with clufter}
pushd "%{clufter_name}" >/dev/null
%{__python} setup.py saveopts -f setup.cfg pkg_prepare              \
                     --ccs-flatten="%{clufter_ccs_flatten}"         \
                     --editor="%{clufter_editor}"                   \
                     --ra-metadata-dir="%{clufter_ra_metadata_dir}" \
                     --ra-metadata-ext="%{clufter_ra_metadata_ext}"
popd >/dev/null
%endif

%build
%if %{with clufter}
pushd "%{clufter_name}" >/dev/null
%{__python} setup.py build
%if "x%{clufter_script}" == "x"
%else
%if "x%{clufter_bashcomp}" == "x"
%else
./run-dev --completion-bash \
  | sed 's|run[-_]dev|%(basename %{clufter_bashcomp})|g' > .bashcomp
%endif
%endif
popd >/dev/null
%endif

%install
rm -rf $RPM_BUILD_ROOT
pwd
make install DESTDIR=$RPM_BUILD_ROOT PYTHON_SITELIB=%{python_sitelib}
make install_pcsd DESTDIR=$RPM_BUILD_ROOT PYTHON_SITELIB=%{python_sitelib} hdrdir="%{_includedir}" rubyhdrdir="%{_includedir}" includedir="%{_includedir}"
chmod 755 $RPM_BUILD_ROOT/%{python_sitelib}/pcs/pcs.py

# Temporary fix for ruby-2.0.0 and rpam
#cp $RPM_BUILD_ROOT/usr/lib/pcsd/gemhome/gems/rpam-ruby19-1.2.1/ext/Rpam/rpam_ext.so $RPM_BUILD_ROOT/usr/lib/pcsd/gemhome/gems/rpam-ruby19-1.2.1/lib

%if %{with clufter}
pushd "%{clufter_name}" >/dev/null
# '--root' implies setuptools involves distutils to do old-style install
%{__python} setup.py install --skip-build --root "%{buildroot}"
%if "x%{clufter_script}" == "x"
%else
# %{_bindir}/%{clufter_name} should have been created
# by install_scripts of setuptools; this hiding from PATH is for TP only
%{__mkdir_p} "%{buildroot}$(dirname "%{clufter_script}")"
%{__mv} -- "%{buildroot}%{_bindir}/%{clufter_name}" "%{buildroot}%{clufter_script}"
%if "x%{clufter_bashcomp}" == "x"
%else
%{__mkdir_p} "$(dirname "%{clufter_bashcomp}")"
%{__install} -- .bashcomp "%{buildroot}%{clufter_bashcomp}"
%endif
%endif
%{__mkdir_p} "%{buildroot}%{_defaultdocdir}/%{clufter_source}"
%{__install} -m 644 -- gpl-2.0.txt doc/*.txt "%{buildroot}%{_defaultdocdir}/%{clufter_source}"
popd >/dev/null
%endif

%check || :
%if %{with clufter}
%if %{clufter_check}
# just a basic sanity check
pushd "%{clufter_name}" >/dev/null
# we need to massage RA metadata files and PATH so the local run works
# XXX we could also inject buildroot's site_packages dir to PYTHONPATH
declare ret=0 ccs_flatten_dir="$(dirname "%{buildroot}%{clufter_ccs_flatten}")"

ln -s "%{buildroot}%{clufter_ra_metadata_dir}"/*."%{clufter_ra_metadata_ext}" \
      "${ccs_flatten_dir}"
PATH="${PATH:+${PATH}:}$(dirname "%{buildroot}%{clufter_ccs_flatten}")" \
./run-check
ret=$?
%{__rm} -f -- "${ccs_flatten_dir}"/*."%{clufter_ra_metadata_ext}"
popd >/dev/null
[ ${ret} = 0 ] || exit "${ret}"
%endif
%endif

%post
%systemd_post pcsd.service

%if %{with clufter}
%post -n %{clufter_pkg_name}
%if "x%{clufter_bashcomp}" == "x"
%else
%if "x%{clufter_script}" == "x"
%{__python} -m %{clufter_name}.__main__ --completion-bash 2>/dev/null \
  | sed 's|%(basename "%{__python}") [-_]m ||g' > "%{clufter_bashcomp}" || :
%else
%{clufter_script} --completion-bash > "%{clufter_bashcomp}" 2>/dev/null || :
%endif
%endif
%endif

%preun
%systemd_preun pcsd.service

%postun
%systemd_postun_with_restart pcsd.service

%files
%defattr(-,root,root,-)
%{python_sitelib}/pcs
%{python_sitelib}/pcs-%{version}-py2.*.egg-info
/usr/sbin/pcs
/usr/lib/pcsd/*
/usr/lib/pcsd/.bundle/config
/usr/lib/pcsd/.gitignore
/usr/lib/systemd/system/pcsd.service
/var/lib/pcsd
/etc/pam.d/pcsd
/etc/bash_completion.d/pcs
/etc/logrotate.d/pcsd
%dir /var/log/pcsd
/etc/sysconfig/pcsd
%{_mandir}/man8/pcs.*

%doc COPYING README

%if %{with clufter}
%files -n %{clufter_pkg_name}
%defattr(-,root,root,-)
%{python2_sitelib}/%{clufter_name}
%{python2_sitelib}/%{clufter_name}-%{clufter_version}-*.egg-info
%{clufter_ccs_flatten}
%{clufter_ra_metadata_dir}

%if "x%{clufter_script}" == "x"
%else
%if "x%{clufter_bashcomp}" == "x"
%else
%verify(not size md5 mtime) %{clufter_bashcomp}
%endif
%{clufter_script}
%endif
%doc %{_defaultdocdir}/%{clufter_source}/*
%endif


%changelog
* Tue Jan 20 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.137-13
- Keep cluster quorate during destruction as long as possible
- Resolves: rhbz#1180506

* Mon Jan 19 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.137-12
- Warn if stopping nodes will cause a loss of the quorum
- Resolves: rhbz#1180506

* Thu Jan 15 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.137-11
- Stop cluster nodes in parallel and keep cluster quorate during pacemaker
  shutdown
- Resolves: rhbz#1180506

* Fri Jan 09 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.137-10
- Stop deleted resource before removing its constraints
- Resolves: rhbz#1180390

* Thu Jan 08 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.137-9
- Added acl enable and disable commands
- Display whether acls are enabled in the 'pcs acl' output
- Resolves: rhbz#1054491

* Wed Jan 07 2015 Chris Feist <cfeist@redhat.cmo> 0.9.137-8
- Configuration of resource-discovery is now available on advanced location
  constraint rules
- Resolves: rhbz#1054491

* Wed Jan 07 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.137-7
- When a role is removed in the GUI the user is now automatically deleted
  if they aren't members of another role
- Resolves: rhbz#1054491

* Mon Jan 05 2015 Chris Feist <cfeist@redhat.com> - 0.9.137-6
- Allowed configuration of resource-discovery option on location constraint
  rules
- Resolves: rhbz#1054491

* Fri Dec 19 2014 Chris Feist <cfeist@redhat.com> - 0.9.137-5
- Fixed error message when creating a user with the same name as a role
- When a role is removed in the GUI the user is now automatically deleted
  if they aren't members of another role
- Resolves: rhbz#1054491

* Wed Dec 17 2014 Tomas Jelinek <tojeline@redhat.com> - 0.9.137-4
- Fixed displaying globally-unique clones in GUI
- Added latest version of clufter package
- Resolves: rhbz#1170150 rhbz#1133897

* Mon Dec 8 2014 Chris Feist <cfeist@redhat.com> - 0.9.137-3
- Added latest version of clufter package
- Resolves: rhbz#1133897

* Mon Dec 8 2014 Tomas Jelinek <tojeline@redhat.com> - 0.9.137-2
- Improved error messages for scoped cib operations
- Fixed waiting for resource commands to finish
- Resolves: rhbz#1115537 rhbz#1156311

* Tue Nov 25 2014 Tomas Jelinek <tojeline@redhat.com> - 0.9.137-1
- Added support for score-attribute in location rules in GUI
- Added ability to wait for resource commands to finish
- Fix clufter doc files installed with executable flag
- Resolves: rhbz#1111368 rhbz#1156311 rhbz#1073075 rhbz#1133897

* Mon Nov 24 2014 Chris Feist <cfeist@redhat.com> - 0.9.136-2
- Added latest version of clufter package
- Resolves: rhbz#1133897

* Wed Nov 19 2014 Chris Feist <cfeist@redhat.com> - 0.9.136-1
- Added support for 'pcs resource restart'
- Added ability to wait for a resource to start after creation
- Fixed issue with backports and ruby 2.0.0p576
- Fix for deleting a resource with a large number of options
- Fix warning when unpacking a pcs config tarball
- Resolves: rhbz#1111368 rhbz#1156311 rhbz#1156597

* Sat Oct 18 2014 Chris Feist <cfeist@redhat.com> - 0.9.135-1
- Added new clufter package
- Rebased to latest upstream sources
- Constraints tables are collapsed properly
- Resolves: rhbz#1111368 rhbz#1145560

* Sat Oct 18 2014 Chris Feist <cfeist@redhat.com> - 0.9.134-1
- Rebased to latest upstream packages
- Resolves: rhbz#1111368

* Fri Oct 17 2014 Chris Feist <cfeist@redhat.com> - 0.9.133-1
- Rebased to latest upstream packages
- Resolves: rhbz#1111368

* Tue Oct 07 2014 Tomas Jelinek <tojeline@redhat.com> - 0.9.132-1
- Rebased to latest upstream packages
- Resolves: rhbz#1111368

* Mon Sep 29 2014 Tomas Jelinek <tojeline@redhat.com> - 0.9.131-1
- Rebased to latest upstream packages
- Resolves: rhbz#1111368
- Added python-clufter subpackage (configuration conversion tool)
- Related:  rhbz#1133897

* Fri Sep 26 2014 Tomas Jelinek <tojeline@redhat.com> - 0.9.130-1
- Rebased to latest upstream packages
- Resolves: rhbz#1111368

* Mon Sep 22 2014 Tomas Jelinek <tojeline@redhat.com> - 0.9.129-1
- Rebased to latest upstream packages
- Resolves: rhbz#1111368

* Thu Sep 18 2014 Tomas Jelinek <tojeline@redhat.com> - 0.9.128-1
- Rebased to latest upstream packages
- Resolves: rhbz#1111368

* Fri Sep 12 2014 Chris Feist <cfeist@redhat.com> - 0.9.127-1
- Rebased to latest upstream packages
- Resolves: rhbz#1111368

* Fri Sep 05 2014 Chris Feist <cfeist@redhat.com> - 0.9.126-1
- Rebased to latest upstream packages
- Resolves: rhbz#1111368

* Tue Mar 25 2014 Chris Feist <cfeist@redhat.com> - 0.9.115-32
- Add ability to set totem options with pcs during cluster setup

* Tue Feb 25 2014 Chris Feist <cfeist@redhat.com> - 0.9.115-31
- Add ability to see group/clone/ms constraints and meta attributes in pcsd

* Mon Feb 24 2014 Chris Feist <cfeist@redhat.com> - 0.9.115-30
- Fix traceback with bad arguments to location rules
- Fix results code when attempting to remove an order that doesn't exist

* Fri Feb 21 2014 Chris Feist <cfeist@redhat.com> - 0.9.115-29
- Don't allow users to clone groups that have already been cloned
- Fix order remove <resource> to remove resources from sets
- Don't allow a user to force-start a group, clone or master/slave
- When using debug-start use proper return code
- Added cluster properties hover text
- Fixed issue with stripping a nil value
- HTML escape resource descriptions

* Wed Feb 19 2014 Chris Feist <cfeist@redhat.com> - 0.9.115-28
- Remove leading/trailing white space in resource descriptions
- Added tooltips for advanced cluster creation options
- Fixed other 'Remove fence devices' button
- When deleting a resource with pcsd use --force to prevent issues
- Add proper tooltip for resource description info icon
- Fix for long cluster names in menu
- Do a better job of detecting when to send a redirect and when to notif
- Don't silently ignore bad operation names

* Tue Feb 18 2014 Chris Feist <cfeist@redhat.com> - 0.9.115-27
- Added --nodesc option to pcs stonith list
- Don't attempt to print metadata for fence_sanlockd

* Tue Feb 18 2014 Chris Feist <cfeist@redhat.com> - 0.9.115-26
- Fixed dialog text when removing a fence device
- Show tool tips for optional fence agent arguments
- Fix bad link on resource remove sprite
- When removing a resource or fence device, show blank info
- Fix resource management issues when pacemaker is not running
- If first node is down, allow other nodes to show resource/stonith forms
- Removing all nodes, now removes cluster configuration
- Added ability to see nodes corosync/pacemaker/pcsd startup settings
- Added extra colspan to improve long cluster name display
- Added ability to configure IPv6 cluster
- Added ability to set corosync transport in GUI
- Added ability to set advanced cluster options on creation
- Renamed last_node_standing to last_man_standing
- On cluster creation color unauthorized nodes in orange
- Added proper redirect when session variable times out
- Fixed traceback when missing authentication tokens

* Mon Feb 17 2014 Chris Feist <cfeist@redhat.com> - 0.9.115-24
- Added support for meta attributes in the GUI
- Moved pcmk_host_list/map/check to optional arguments

* Wed Feb 12 2014 Chris Feist <cfeist@redhat.com> - 0.9.115-23
- Added ability to use 'and/or' with rules
- Fixed stonith optional arguments in pcsd

* Tue Feb 11 2014 Chris Feist <cfeist@redhat.com> - 0.9.115-22
- Fixed selection arrow when selecting new resource on resources page
- Fixed permissions on pcsd.service file

* Thu Feb 06 2014 Chris Feist <cfeist@redhat.com> - 0.9.115-21
- Added support for resource descriptions
- Show all nodes a resource is on for cloned resources
- Improve visibility of dropdown menus
- Keep last attempted login username if login fails

* Tue Feb 04 2014 Chris Feist <cfeist@redhat.com> - 0.9.115-20
- Fixed issue when removing all resources or fence devices
- Fixed duplicate id on fence device page

* Mon Feb 03 2014 Chris Feist <cfeist@redhat.com> - 0.9.115-19
- Fixed issue when creating a cluster from the GUI on a node that isn't in
  the newly formed cluster
- The GUI is now better at keeping track of nodes in the cluster

* Tue Jan 28 2014 Chris Feist <cfeist@redhat.com> - 0.9.115-17
- Fixed issue with cluster properties not displaying properly when running
  pcsd on a node that was not in the cluster being managed
- Fixed /etc/sysconfig/pcsd file for pcsd

* Tue Jan 28 2014 Chris Feist <cfeist@redhat.com> - 0.9.115-1
- Re-synced to upstream sources

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 0.9.114-2
- Mass rebuild 2014-01-24

* Thu Jan 23 2014 Chris Feist <cfeist@redhat.com> - 0.9.114-1
- Re-synced to upstream sources

* Wed Jan 22 2014 Chris Feist <cfeist@redhat.com> - 0.9.113-1
- Re-synced to upstream sources

* Mon Jan 20 2014 Chris Feist <cfeist@redhat.com> - 0.9.112-1
- Re-synced to upstream sources

* Mon Jan 20 2014 Chris Feist <cfeist@redhat.com> - 0.9.111-1
- Re-synced to upstream sources

* Fri Jan 17 2014 Chris Feist <cfeist@redhat.com> - 0.9.110-1
- Re-synced to upstream sources

* Wed Jan 15 2014 Chris Feist <cfeist@redhat.com> - 0.9.108-1
- Re-synced to upstream sources

* Wed Jan 15 2014 Chris Feist <cfeist@redhat.com> - 0.9.107-1
- Re-synced to upstream sources

* Tue Jan 14 2014 Chris Feist <cfeist@redhat.com> - 0.9.106-1
- Re-synced to upstream sources

* Mon Jan 13 2014 Chris Feist <cfeist@redhat.com> - 0.9.105-1
- Re-synced to upstream sources

* Fri Jan 10 2014 Chris Feist <cfeist@redhat.com> - 0.9.104-1
- Re-synced to upstream sources

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.9.100-2
- Mass rebuild 2013-12-27

* Tue Nov 12 2013 Chris Feist <cfeist@redhat.com> - 0.9.100-1
- Re-synced to upstream sources

* Thu Nov 07 2013 Chris Feist <cfeist@redhat.com> - 0.9.99-2
- Re-synced to upstream sources

* Wed Nov 06 2013 Chris Feist <cfeist@redhat.com> - 0.9.98-1
- Re-synced to upstream sources

* Tue Nov 05 2013 Chris Feist <cfeist@redhat.com> - 0.9.96-2
- Re-synced to upstream sources

* Tue Oct 29 2013 Chris Feist <cfeist@redhat.com> - 0.9.96-2
- Re-synced to upstream sources

* Tue Oct 22 2013 Chris Feist <cfeist@redhat.com> - 0.9.95-2
- Re-synced to upstream sources

* Tue Oct 22 2013 Chris Feist <cfeist@redhat.com> - 0.9.94-1
- Re-synced to upstream sources

* Wed Oct 16 2013 Chris Feist <cfeist@redhat.com> - 0.9.91-1
- Re-synced to upstream sources

* Tue Oct 15 2013 Chris Feist <cfeist@redhat.com> - 0.9.92-2
- Re-synced to upstream sources

* Wed Oct 09 2013 Chris Feist <cfeist@redhat.com> - 0.9.91-1
- Re-synced to upstream sources

* Wed Sep 18 2013 Chris Feist <cfeist@redhat.com> - 0.9.84-1
- Re-synced to upstream sources

* Tue Sep 03 2013 Chris Feist <cfeist@redhat.com> - 0.9.77-1
- Re-synced to upstreams sources

* Tue Sep 03 2013 Chris Feist <cfeist@redhat.com> - 0.9.76-1
- Re-synced to upstreams sources

* Fri Aug 09 2013 Chris Feist <cfeist@redhat.com> - 0.9.71-1
- Rebuilt with new upstream sources

* Fri Aug 09 2013 Chris Feist <cfeist@redhat.com> - 0.9.63-1
- Rebuilt with new upstream sources

* Wed Aug 07 2013 Chris Feist <cfeist@redhat.com> - 0.9.62-1
- Rebuilt with new upstream sources

* Tue Aug 06 2013 Chris Feist <cfeist@redhat.com> - 0.9.61-1
- Rebuilt with new upstream sources

* Mon Jul 29 2013 Chris Feist <cfeist@redhat.cmo> - 0.9.60-1
- Rebuilt with new upstream sources
- Added pcsd wizards

* Tue Jul 23 2013 Chris Feist <cfeist@redhat.cmo> - 0.9.58-1
- Rebuilt with new upstream sources

* Tue Jul 23 2013 Chris Feist <cfeist@redhat.cmo> - 0.9.57-1
- Rebuilt with new upstream sources

* Mon Jul 22 2013 Chris Feist <cfeist@redhat.cmo> - 0.9.56-1
- Rebuilt with upstream source
- Added missing bash completion file

* Mon Jul 22 2013 Chris Feist <cfeist@redhat.cmo> - 0.9.55-1
- Rebuilt with upstream source

* Wed Jul 10 2013 Chris Feist <cfeist@redhat.com> - 0.9.54-4
- Fix rpam error after adding systemd macros

* Wed Jul 10 2013 Chris Feist <cfeist@redhat.com> - 0.9.54-3
- Rebuild with proper upstream sources

* Wed Jul 10 2013 Chris Feist <cfeist@redhat.com> - 0.9.54-1
- Rebuild with upstream sources

* Wed Jul 10 2013 Chris Feist <cfeist@redhat.com> - 0.9.53-2
- Added systemd macros

* Tue Jul 09 2013 Chris Feist <cfeist@redhat.com> - 0.9.53-1
- Rebuild with upstream sources

* Mon Jul 08 2013 Chris Feist <cfeist@redhat.com> - 0.9.52-1
- Rebuild with upstream sources

* Mon Jul 01 2013 Chris Feist <cfeist@redhat.com> - 0.9.49-3
- Fix pcsd.conf source file location.

* Mon Jul 01 2013 Chris Feist <cfeist@redhat.com> - 0.9.49-1
- Rebuild with upstream sources

* Tue Jun 18 2013 Chris Feist <cfeist@redhat.com> - 0.9.48-1
- Rebuild with upstream sources

* Wed Jun 12 2013 Chris Feist <cfeist@redhat.com> - 0.9.47-1
- Rebuild with upstream sources

* Mon Jun 10 2013 Chris Feist <cfeist@redhat.com> - 0.9.46-1
- Rebuild with upstream sources

* Wed Jun 05 2013 Chris Feist <cfeist@redhat.com> - 0.9.45-2
- Rebuild with upstream sources

* Mon Jun 03 2013 Chris Feist <cfeist@redhat.com> - 0.9.44-4
- Rebuild with upstream sources

* Thu May 30 2013 Chris Feist <cfeist@redhat.com> - 0.9.44-1
- Rebuild with upstream sources

* Wed May 29 2013 Chris Feist <cfeist@redhat.com> - 0.9.43-1
- Rebuild with upstream sources

* Wed May 29 2013 Chris Feist <cfeist@redhat.com> - 0.9.42-5
- Fix issues with ruby 2.0 build

* Wed May 29 2013 Chris Feist <cfeist@redhat.com> - 0.9.42-1
- Rebuild with upstream sources

* Tue May 07 2013 Chris Feist <cfeist@redhat.com> - 0.9.41-1
- Rebuild with upstream sources

* Tue Apr 30 2013 Chris Feist <cfeist@redhat.com> - 0.9.40-1
- Rebuild with upstream sources

* Wed Apr 17 2013 Chris Feist <cfeist@redhat.com> - 0.9.39-1
- Rebuild with upstream sources

* Tue Apr 09 2013 Chris Feist <cfeist@redhat.com> - 0.9.38-1
- Rebuild with upstream sources

* Wed Apr 03 2013 Chris Feist <cfeist@redhat.com> - 0.9.37-4
- Re-enable gem builds with fix for ruby 2.0.0

* Tue Mar 26 2013 Chris Feist <cfeist@redhat.com> - 0.9.37-2
- Temporarily disable gem builds for ruby 2.0.0

* Wed Mar 20 2013 Chris Feist <cfeist@redhat.com> - 0.9.37-1
- Re-synced to upstream

* Fri Mar 15 2013 Chris Feist <cfeist@redhat.com> - 0.9.35-1
- Re-synced to upstream

* Tue Mar 12 2013 Chris Feist <cfeist@redhat.com> - 0.9.34-1
- Re-synced to upstream
- Updated pcsd location to /usr/lib

* Wed Feb 20 2013 Chris Feist <cfeist@redhat.com> - 0.9.32-1
- Re-synced to upstream

* Mon Feb 18 2013 Chris Feist <cfeist@redhat.com> - 0.9.31-1
- Re-synced to upstream

* Mon Jan 14 2013 Chris Feist <cfeist@redhat.com> - 0.9.30-1
- Updated build to properly manage combined pcs/pcsd

* Wed Jan 02 2013 Chris Feist <cfeist@redhat.com> - 0.9.29-4
- Updated certificate generation code to fix firefox issues

* Fri Dec 07 2012 Chris Feist <cfeist@redhat.com> - 0.9.29-3
- Added in missing pam service

* Thu Nov 29 2012 Chris Feist <cfeist@redhat.com> - 0.9.29-2
- Add pam-devel to BuildRequires

* Thu Nov 29 2012 Chris Feist <cfeist@redhat.com> - 0.9.29-1
- Resync to latest version of pcs/pcsd

* Fri Sep 28 2012 Chris Feist <cfeist@redhat.com> - 0.9.26-1
- Resync to latest version of pcs/pcsd

* Tue Aug 21 2012 Chris Feist <cfeist@redhat.com> - 0.9.15-1.test.1
- Resync to latest version of pcs/pcsd

* Mon Aug 13 2012 Chris Feist <cfeist@redhat.com> - 0.9.14-1.test.1
- Resync to latest version of pcs/pcsd

* Thu Aug 09 2012 Chris Feist <cfeist@redhat.com> - 0.9.13-1.test.1
- Resync to latest version of pcs and rename pcs-gui to pcsd

* Mon Jun 11 2012 Chris Feist <cfeist@redhat.com> - 0.9.5-5.test.1
- Resync to latest version of pcs

* Mon Jun 11 2012 Chris Feist <cfeist@redhat.com> - 0.9.5-4
- Resync to latest version of pcs

* Thu May 24 2012 Chris Feist <cfeist@redhat.com> - 0.9.4-1
- Resync to latest version of pcs
- Move cluster creation options to cluster sub command.

* Mon May 07 2012 Chris Feist <cfeist@redhat.com> - 0.9.3.1-1
- Resync to latest version of pcs which includes fixes to work with F17.

* Mon Mar 19 2012 Chris Feist <cfeist@redhat.com> - 0.9.2.4-1
- Resynced to latest version of pcs

* Mon Jan 23 2012 Chris Feist <cfeist@redhat.com> - 0.9.1-1
- Updated BuildRequires and %doc section for fedora

* Fri Jan 20 2012 Chris Feist <cfeist@redhat.com> - 0.9.0-2
- Updated spec file for fedora specific changes

* Mon Jan 16 2012 Chris Feist <cfeist@redhat.com> - 0.9.0-1
- Initial Build

