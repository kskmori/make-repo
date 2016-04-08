Name: pcs		
Version: 0.9.148
Release: 5%{?dist}
License: GPLv2
URL: http://github.com/feist/pcs
Group: System Environment/Base
ExclusiveArch: i686 x86_64

Summary: Pacemaker Configuration System
Source0: https://tojeline.fedorapeople.org/pkgs/pcs/pcs-%{version}.tar.gz
Patch0: change-cman-to-rhel6-in-messages.patch
Patch1: rhel6.patch
Patch2: bz1298163-01-web-UI-fix-updating-resource-when-there-is-no-stonit.patch
Patch3: bz1297782-01-move-DISABLED_GUI-option-to-etc-sysconfig-pcsd.patch
Patch4: disable-gui.patch
Patch5: bz1298163-02-cluster-properties-rewrite.patch
Patch6: bz1298163-03-fix-updating-cluster-properties-from-web-UI.patch
Patch7: bz1260021-01-fix-syntax-error-in-utilization-attributes-functions.patch
Patch8: bz1305913-01-fix-occasional-deadlock-when-running-processes.patch
Patch9: bz1311159-01-fix-pcsd-permissions-if-pcs_settings.conf.patch

Source1: https://rubygems.org/downloads/backports-3.6.4.gem
Source2: https://rubygems.org/downloads/eventmachine-1.0.7.gem
Source3: https://rubygems.org/downloads/json-1.8.3.gem
Source4: https://rubygems.org/downloads/monkey-lib-0.5.4.gem
Source5: https://rubygems.org/downloads/multi_json-1.11.1.gem
Source6: https://rubygems.org/downloads/open4-1.3.4.gem
Source7: https://rubygems.org/downloads/orderedhash-0.0.6.gem
Source8: https://rubygems.org/downloads/rack-1.6.4.gem
Source9: https://rubygems.org/downloads/rack-protection-1.5.3.gem
Source10: https://rubygems.org/downloads/rack-test-0.6.3.gem
Source11: https://tojeline.fedorapeople.org/rubygems/gems/rpam-ruby19-feist-1.2.1.1.gem
Source12: https://rubygems.org/downloads/sinatra-1.4.6.gem
Source13: https://rubygems.org/downloads/sinatra-contrib-1.4.4.gem
Source14: https://rubygems.org/downloads/sinatra-sugar-0.5.1.gem
Source15: https://rubygems.org/downloads/tilt-1.4.1.gem

BuildRequires: python2-devel rubygems ruby-devel pam-devel
# following for UpdateTimestamps sanitization function
BuildRequires: diffstat

Requires: ruby rubygems ccs
Requires: python-clufter >= 0.55.0
Requires: psmisc initscripts openssl

Provides: bundled(rubygem-backports) = 3.6.4
Provides: bundled(rubygem-eventmachine) = 1.0.7
Provides: bundled(rubygem-json) = 1.8.3
Provides: bundled(rubygem-monkey-lib) = 0.5.4
Provides: bundled(rubygem-multi_json) = 1.11.1
Provides: bundled(rubygem-open4) = 1.3.4
Provides: bundled(rubygem-orderedhash) = 0.0.6
Provides: bundled(rubygem-rack) = 1.6.4
Provides: bundled(rubygem-rack-protection) = 1.5.3
Provides: bundled(rubygem-rack-test) = 0.6.3
Provides: bundled(rubygem-rpam-ruby19) = 1.2.1
Provides: bundled(rubygem-sinatra) = 1.4.6
Provides: bundled(rubygem-sinatra-contrib) = 1.4.4
Provides: bundled(rubygem-sinatra-sugar) = 0.5.1
Provides: bundled(rubygem-tilt) = 1.4.1

%description
pcs is a corosync and pacemaker configuration tool.  It permits users to
easily view, modify and created pacemaker based clusters.

%prep
%setup -q

# -- following borrowed from python-simplejon.el5 --
# Update timestamps on the files touched by a patch, to avoid non-equal
# .pyc/.pyo files across the multilib peers within a build, where "Level"
# is the patch prefix option (e.g. -p1)
UpdateTimestamps() {
  Level=$1
  PatchFile=$2
  # Locate the affected files:
  for f in $(diffstat $Level -l $PatchFile); do
    # Set the files to have the same timestamp as that of the patch:
    touch -r $PatchFile $f
  done
}

%patch0 -p1
UpdateTimestamps -p1 %{PATCH0}
%patch1 -p1
UpdateTimestamps -p1 %{PATCH1}
%patch2 -p1
UpdateTimestamps -p1 %{PATCH2}
%patch3 -p1
UpdateTimestamps -p1 %{PATCH3}
%patch4 -p1
UpdateTimestamps -p1 %{PATCH4}
%patch5 -p1
UpdateTimestamps -p1 %{PATCH5}
%patch6 -p1
UpdateTimestamps -p1 %{PATCH6}
%patch7 -p1
UpdateTimestamps -p1 %{PATCH7}
%patch8 -p1
UpdateTimestamps -p1 %{PATCH8}
%patch9 -p1
UpdateTimestamps -p1 %{PATCH9}

mkdir -p pcsd/vendor/cache
cp -f %SOURCE1 pcsd/vendor/cache
cp -f %SOURCE2 pcsd/vendor/cache
cp -f %SOURCE3 pcsd/vendor/cache
cp -f %SOURCE4 pcsd/vendor/cache
cp -f %SOURCE5 pcsd/vendor/cache
cp -f %SOURCE6 pcsd/vendor/cache
cp -f %SOURCE7 pcsd/vendor/cache
cp -f %SOURCE8 pcsd/vendor/cache
cp -f %SOURCE9 pcsd/vendor/cache
cp -f %SOURCE10 pcsd/vendor/cache
cp -f %SOURCE11 pcsd/vendor/cache
cp -f %SOURCE12 pcsd/vendor/cache
cp -f %SOURCE13 pcsd/vendor/cache
cp -f %SOURCE14 pcsd/vendor/cache
cp -f %SOURCE15 pcsd/vendor/cache

%build

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT PYTHON_SITELIB=%{python_sitelib}
make install_pcsd DESTDIR=$RPM_BUILD_ROOT PYTHON_SITELIB=%{python_sitelib} hdrdir="%{_includedir}" rubyhdrdir="%{_includedir}" includedir="%{_includedir}" initdir="%{_initrddir}"
chmod 755 $RPM_BUILD_ROOT/%{python_sitelib}/pcs/pcs.py

%post
/sbin/chkconfig --add pcsd
if [ $1 -eq 2 ]; then
    /sbin/service pcsd condrestart
fi

%preun
if [ $1 -eq 0 ]; then
    /sbin/chkconfig --del pcsd
    /sbin/service pcsd stop
fi

%files
%defattr(-,root,root,-)
%{python_sitelib}/pcs
%{python_sitelib}/pcs-%{version}-py2.*.egg-info
/usr/sbin/pcs
/usr/lib/pcsd/*
/usr/lib/pcsd/.bundle/config
%{_initrddir}/pcsd
/var/lib/pcsd
/etc/pam.d/pcsd
/etc/bash_completion.d/pcs
/etc/logrotate.d/pcsd
%dir /var/log/pcsd
/etc/sysconfig/pcsd
%{_mandir}/man8/pcs.*
%exclude /usr/lib/pcsd/*.debian

%doc COPYING README

%changelog
* Wed Feb 24 2016 Ivan Devat <idevat@redhat.com> - 0.9.148-5
- Fixed incorrect default permission assignment in pcsd.
- Resolves: rhbz#1311159

* Wed Feb 17 2016 Ivan Devat <idevat@redhat.com> - 0.9.148-4
- Fixed occasional deadlock when running processes
- Resolves: rhbz#1305913

* Tue Feb 02 2016 Ivan Devat <idevat@redhat.com> - 0.9.148-3
- Fixed updating cluster properties from older version of web UI
- Fixed syntax error in utilization attributes functions
- Resolves: rhbz#1298163
- Related: rhbz#1260021

* Tue Jan 19 2016 Ivan Devat <idevat@redhat.com> - 0.9.148-2
- Moved DISABLED_GUI option to /etc/sysconfig/pcsd
- Added backend support for new cluster properties form in web UI
- Fixed multilib .pyc/.pyo issue
- Resolves: rhbz#1297782 rhbz#1298163

* Wed Dec 09 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.148-1
- Rebased to latest upstream packages
- Fixed crashes on one-node clusters
- Resolves: rhbz#1260021 rhbz#1283627

* Thu Nov 05 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.146-1
- Rebased to latest upstream packages
- Rubygems built with RELRO
- Resolves: rhbz#1260021 rhbz#1242158

* Thu Nov 05 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.145-2
- Rubygems built with RELRO
- Resolves: rhbz#1242158

* Thu Oct 22 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.145-1
- Rebased to latest upstream packages
- Added a warning to "pcs cluster setup" when a node is already in a cluster
- Fixes in help text and man page
- Rubygems built with RELRO
- Added option to put a node into maintenance mode
- Ungrouping the last resource from a cloned group no longer produces an invalid CIB
- Removing a resource from a group no longer removes constraints referencing that group
- Fixed session and cookies processing
- Fixed command injection vulnerability
- Added support for exporting cluster configuration to a list of pcs commands using clufter
- Added automatic removal of old config file backups
- Fixed removing a fence device from fence levels on deleting the device
- Resolves: rhbz#1260021 rhbz#1190732 rhbz#1203802 rhbz#1230368 rhbz#1242158 rhbz#1243744 rhbz#1245721 rhbz#1247883 rhbz#1247979 rhbz#1253288 rhbz#1253292 rhbz#1264795 rhbz#1273391 rhbz#1275254

* Tue Apr 14 2015 Chris Feist <cfeist@redhat.com> - 0.9.139-9
- Added fix for missing cookie signature
- Resolves: rhbz#1211566

* Fri Apr 03 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.139-8
- Fixed duplicated nodes in a cluster created by import-cman
- Resolves: rhbz#1171312

* Wed Apr 01 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.139-7
- Fixed tarball creation on import-cman
- Resolves: rhbz#1171312

* Wed Mar 25 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.139-6
- Fixed node standby / unstadby
- Resolves: rhbz#1168982

* Fri Mar 13 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.139-5
- Added dependency on python-clufter
- Resolves: rhbz#1171312

* Thu Mar 05 2015 Chris Feist <cfeist@redhat.com> - 0.9.139-4
- Revert clufter changes since it will be in its own package
- Resolves: rhbz#1171312

* Wed Mar 04 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.139-3
- Added clufter package
- Resolves: rhbz#1171312

* Mon Mar 02 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.139-2
- Added warning when node removal will cause a loss of the quorum
- Resolves: rhbz#1184763

* Tue Feb 17 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.139-1
- Rebased to latest upstream packages
- Fixed constraints removal and node standby/unstandby using remote GUI
- Fixed displaying of fence / resource agent metadata in GUI
- Added Pacemaker Resource defaults and Op defaults to 'pcs config' output
- Fixed 'pcs resource clear' used on cloned group
- Added support for scope option in cib commands
- Added warning when creating a cluster with UDPU transport
- Reload cluster.conf after node addition / removal
- Resolves: rhbz#1185738 rhbz#1168982 rhbz#1174793 rhbz#1187488 rhbz#1190167 rhbz#1190168 rhbz#1191898 rhbz#1193433

* Tue Jan 27 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.138-1
- Rebased to latest upstream packages
- Fixed creating default resource operations
- Added support for RRP and corosync options for cman based clusters
- Allowed scope=configuration in cib commands
- Added support for configuring a cluster remotely using pcsd
- Fixed globally-unique clone resources in pcsd
- Added resource location to resources / stonith devices list
- Fixed formatting of resource / fence agent description
- Fence agent description now contains information about the agent
- Parallelized cluster start and cluster stop
- Added warning when nodes stop will cause a loss of the quorum
- pcs status --full now displays Node attributes and Migration summary
- Resolves: rhbz#1185738 rhbz#1031141 rhbz#1121769 rhbz#1126835 rhbz#1160359 rhbz#1168986 rhbz#1174244 rhbz#1174793 rhbz#1174798 rhbz#1174801 rhbz#1184763 rhbz#1184922

* Wed Aug 27 2014 Chris Feist <cfeist@redhat.cmo> - 0.9.123-9
- Improved detection of RHEL 6 variants
- Resolves: rhbz#1026431

* Fri Aug 15 2014 Chris Feist <cfeist@redhat.cmo> - 0.9.123-8
- Added support for 'pcs acl' and 'pcs config' in bash completion
- Resolves: rhbz#1026987

* Wed Aug 13 2014 Chris Feist <cfeist@redhat.com> - 0.9.123-7
- Fixed error in bash completion when an '|' is used
- Resolves: rhbz#1026987

* Thu Aug 07 2014 Chris Feist <cfeist@redhat.com> - 0.9.123-6
- Fixed issue with sync cluster.conf & adding uid/gid across cluster on RHEL6 w/ pcsd
- Resolves: rhbz#1102836

* Wed Aug 06 2014 Chris Feist <cfeist@redhat.com> - 0.9.123-5
- Fixed support for adding/removing nodes on RHEL6 w/ pcsd
- Resolves: rhbz#1102836

* Thu Jul 03 2014 Chris Feist <cfeist@redhat.com> - 0.9.123-4
- Fixed resource delete for clones of groups with more than one resource
- Fixed unclone of group so all resources are removed
- Resolves: rhbz#1107612 rhbz#1108778

* Tue Jul 01 2014 Chris Feist <cfeist@redhat.com> - 0.9.123-3
- Added ability to upgrade cluster cib and we auto upgrade cib if we're running
  an acl command (except show or help)
- Resolves: rhbz#1112727

* Mon Jun 23 2014 Chris Feist <cfeist@redhat.com> - 0.9.123-2
- Added --full to pcs status to view resources in clones of groups
- Resolves: rhbz#1033538

* Thu Jun 19 2014 Chris Feist <cfeist@redhat.com> - 0.9.123-1
- Added support for pacemaker ACLs
- Resolves: rhbz#1102836

* Mon Jun 16 2014 Chris Feist <cfeist@redhat.com> - 0.9.122-4
- Fixed pcs cluster enable/disable to only enable pacemaker
- Resolves: rhbz#1038107

* Fri Jun 13 2014 Chris Feist <cfeist@redhat.com> - 0.9.122-3
- Disabled GUI
- On upgrade, condrestart pcsd
- Resolves: rhbz#1102836

* Wed Jun 11 2014 Chris Feist <cfeist@redhat.com> - 0.9.121-1
- Don't try to get metadata for fence_check, fence_tool & fence_node
- Cloned M/S groups can now be deleted
- Clone options can now follow --clone
- Cloned resources with globally-unique=true can now be deleted
- Resolves: rhbz#1102836

* Tue Jun 10 2014 Chris Feist <cfeist@redhat.com> - 0.9.120-2
- Use /usr/sbin/pcs for pcs instead of /sbin/pcs
- Use Open4 instead of POpen4 for running commands
- Fixed cluster setup for RHEL6
- Resolves: rhbz#1102836

* Mon Jun 09 2014 Chris Feist <cfeist@redhat.com> - 0.9.118-2
- Re-synced to upstream sources
- Fixed dependency on rubygems
- Fixed pam long timeouts due to fprintd
- Resolves: rhbz#1102836

* Thu Jun 05 2014 Chris Feist <cfeist@redhat.com> - 0.9.117-1
- Fixed gem install order
- Use local gems for install
- Resolves: rhbz#1102836

* Thu Jun 05 2014 Chris Feist <cfeist@redhat.com> - 0.9.116-1
- Re-synced to latest upstream source
- Added support for pcsd
- Resolves: rhbz#1102836

* Tue May 20 2014 Chris Feist <cfeist@redhat.com> - 0.9.101-3
- When creating a resource using --group/--clone/--master put the group
  inside the master/clone/group before putting it into the live CIB
- Resolves: rhbz#1066927

* Wed Dec 04 2013 Chris Feist <cfeist@redhat.com> - 0.9.101-1
- Rebase for new features
- Added ability to set uidgid in cluster.conf
- Stonith level add now properly recognizes nodes
- Resolves: rhbz#1025053 rhbz#1019410

* Fri Oct 11 2013 Chris Feist <cfeist@redhat.com> - 0.9.90-2
- Bump version for 6.4.z stream

* Fri Oct 04 2013 Chris Feist <cfeist@redhat.com> - 0.9.90-1
- Add ability to set node attributes
- Fix issue setting meta attributes on a master when creating a resource

* Mon Sep 30 2013 Chris Feist <cfeist@redhat.com> - 0.9.89-1
- Show location constraint role in pcs status/constraint
- Disable resource before removing
- Misc man/usage fixes

* Thu Sep 26 2013 Chris Feist <cfeist@redhat.com> - 0.9.88-1
- Don't allow order/colocation constraints created for master primitives
- Check in clones for stonith resources
- Clarify 'constraint rule add' in man page/usage
- Fixed minor usage issue with colocation sets

* Fri Sep 20 2013 Chris Feist <cfeist@redhat.com> - 0.9.87-1
- Allow two ordering constraints with same resources
- Improved error messages when trying to master/clone resources
- Updated error message when attempting to move a master/slave without
  --master

* Wed Sep 18 2013 Chris Feist <cfeist@redhat.com> - 0.9.86-1
- Show useful error when attempting to move/ban/clear a resource id when
  using --master

* Wed Sep 18 2013 Chris Feist <cfeist@redhat.com> - 0.9.85-1
- Allow deleting clones/masters from 'resource delete'

* Tue Sep 17 2013 Chris Feist <cfeist@redhat.com> - 0.9.84-1
- Disable groups before removing them

* Mon Sep 16 2013 Chris Feist <cfeist@redhat.com> - 0.9.83-1
- Fix --enable option when setting up a cluster

* Wed Sep 11 2013 Chris Feist <cfeist@redhat.com> - 0.9.82-1
- Show constraint id when printing out location rules
- Improve error messages when adding location rules with errors
- Add ability to remove constraint rules
- Allow move of master/slave resources if --master is present

* Tue Sep 10 2013 Chris Feist <cfeist@redhat.com> - 0.9.81-1
- Fix issues when updating resource with multiple operations with the same
  action
- Fixed constraint rules and improved usage documentation

* Mon Sep 09 2013 Chris Feist <cfeist@redhat.com> - 0.9.80-1
- More fixes for OCF_CHECK_LEVEL issues
- Fix traceback when adding a resourcew with a provider that doesn't exist
- Create proper two_node cluster when only two nodes are specified in cluster
  setup
- Give useful error when bad options are used with 'op'

* Thu Sep 05 2013 Chris Feist <cfeist@redhat.com> - 0.9.79-1
- Fixed OCF_CHECK_LEVEL operation setting in resource update
- Return proper error codes when stopping/starting/enable/disabling resources
- Return proper error code on auth

* Wed Sep 04 2013 Chris Feist <cfeist@redhat.com> - 0.9.78-1
- Fixed error codes and stdout/stderr output on errors from pcs resource
  enable/disable
- Automatically add interval to operations which don't specify an interval

* Tue Sep 03 2013 Chris Feist <cfeist@redhat.com> - 0.9.77-1
- Fixed managing/unmanaging groups/clones/masters of resources
- Fixed issue when using --group when creating a resource

* Thu Aug 29 2013 Chris Feist <cfeist@redhat.com> - 0.9.76-1
- Renamed resource group remove/delete to ungroup
- Fixed moving resource masters
- Allow cloing/mastering last resource in a group

* Tue Aug 27 2013 Chris Feist <cfeist@redhat.com> - 0.9.75-1
- Removing a resource that is part of a resource set is now allowed
- When you try to remove a group from a master that has more than one
  resource you now recieve a helpful error
- Unclone works on clones where constraints have been added
- Removing a group with constraints now works properly
- Master/Slave groups now have constraints properly removed before being
  deleted

* Mon Aug 26 2013 Chris Feist <cfeist@redhat.com> - 0.9.74-1
- pcs cluster edit should now work properly
- Allow removal of group and resources inside group with
  pcs resource delete <group name>

* Tue Aug 20 2013 Chris Feist <cfeist@redhat.com> - 0.9.73-1
- Cluster name is now viewable on RHEL 6
- Cluster.conf is now removed on destroy
- Misc man page & usage updates
- When removing the last resource from a group, remove any constraints still
  remaining on group

* Mon Aug 19 2013 Chris Feist <cfeist@redhat.com> - 0.9.72-1
- Allow ban and clear of masters

* Thu Aug 15 2013 Chris Feist <cfeist@redhat.com> - 0.9.71-1
- Don't print pcsd status for RHEL6

* Thu Aug 15 2013 Chris Feist <cfeist@redhat.com> - 0.9.70-1
- Pulled in old fixes for RHEL6 that missed upstream
- Require ccs during install

* Tue Aug 13 2013 Chris Feist <cfeist@redhat.com> - 0.9.68-1
- Fix fencing for RHEL6

* Tue Aug 13 2013 Chris Feist <cfeist@redhat.com> - 0.9.67-2
- Minor man page fixes

* Tue Aug 13 2013 Chris Feist <cfeist@redhat.com> - 0.9.66-1
- Resynched to upstream sources

* Tue Aug 13 2013 Chris Feist <cfeist@redhat.com> - 0.9.65-1
- Resynched to upstream sources

* Tue Aug 13 2013 Chris Feist <cfeist@redhat.com> - 0.9.64-1
- Resynched to upstream sources

* Wed Aug 07 2013 Chris Feist <cfeist@redhat.com> - 0.9.62-1
- Resynched to upstream sources

* Mon Jul 29 2013 Chris Feist <cfeist@redhat.com> - 0.9.60-1
- Resynched to upstream sources
- Added pcsd wizards

* Thu Jul 25 2013 Chris Feist <cfeist@redhat.com> - 0.9.59-1
- Resynched to upstream sources

* Tue Jan 29 2013 Chris Feist <cfeist@redhat.com> - 0.9.26-11
- Fixed missing master/slave resources in 'pcs config'
- Resolves: rhbz#bz903712

* Tue Jan 22 2013 Chris Feist <cfeist@redhat.com> - 0.9.26-10
- Removed one extra place where pcs incorrectly deleted resources from the lrm
- Resolves: rhbz#893221

* Tue Jan 15 2013 Chris Feist <cfeist@redhat.com> - 0.9.26-9
- pcs now allows assigning constraints to group/clone/multistate resources
- pcs no longer deletes resources from the lrm during resource removal
- Resolves: rhbz#894174 rhbz#893221

* Mon Dec 17 2012 Chris Feist <cfeist@redhat.com> - 0.9.26-8
- Fixed issue with error when listing resource providers and standards
- Resolves: rhbz#bz887870

* Tue Dec 04 2012 Chris Feist <cfeist@redhat.com> - 0.9.26-7
- Fixed minor issue with pcs resource move/unmove display
- Resolves: rhbz#878681

* Tue Dec 04 2012 Chris Feist <cfeist@redhat.com> - 0.9.26-6
- Added additional specific steps for configuring pcs on Red Hat Enterprise
  Linux 6
- Resolves: rhbz#878682 

* Wed Nov 14 2012 Chris Feist <cfeist@redhat.com> - 0.9.26-3
- Added in missing pcs resource move/unmove functionality
- Resolves: rhbz#878681

* Tue Sep 25 2012 Chris Feist <cfeist@redhat.com> - 0.9.26-2
- Updates to fix issues with RHEL6 and pcs/corosync/pacemaker

* Tue Sep 25 2012 Chris Feist <cfeist@redhat.com> - 0.9.26-1
- Resync to latest version of pcs

* Mon Sep 24 2012 Chris Feist <cfeist@redhat.com> - 0.9.25-1
- Resync to latest version of pcs

* Thu Sep 20 2012 Chris Feist <cfeist@redhat.com> - 0.9.24-1
- Resync to latest version of pcs

* Thu Sep 20 2012 Chris Feist <cfeist@redhat.com> - 0.9.23-1
- Resync to latest version of pcs

* Wed Sep 12 2012 Chris Feist <cfeist@redhat.com> - 0.9.22-1
- Resync to latest version of pcs

* Thu Sep 06 2012 Chris Feist <cfeist@redhat.com> - 0.9.19-1
- Resync to latest version of pcs

* Tue Aug 07 2012 Chris Feist <cfeist@redhat.com> - 0.9.12-1
- Resync to latest version of pcs

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

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
