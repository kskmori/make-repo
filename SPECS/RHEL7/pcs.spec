Name: pcs		
Version: 0.9.143
Release: 15%{?dist}
License: GPLv2
URL: http://github.com/feist/pcs
Group: System Environment/Base
#BuildArch: x86_64
BuildRequires: python2-devel
Summary: Pacemaker Configuration System	
Source0: https://tojeline.fedorapeople.org/pkgs/pcs/pcs-withgems-%{version}.tar.gz
Source1: HAM-logo.png
Patch0: bz1122818-01-fix-resource-relocation-of-globally-unique-clones.patch
Patch1: bz1158577-01-improve-logging-in-pcsd.patch
Patch2: bz1189857-01-fix-Add-Resource-form-in-web-UI.patch
Patch3: bz1235022-01-add-nagios-support-to-pcs-resource-list-and-web-UI.patch
Patch4: bz1122818-02-fix-resource-relocate-for-remote-nodes.patch
Patch5: bz1253491-01-fix-pcs-pcsd-path-detection.patch
Patch6: bz1253294-01-fixed-command-injection-vulnerability.patch
Patch7: bz1258619-01-fix-ruby-traceback-on-pcsd-startup.patch
Patch8: bz1158577-02-fix-certificates-syncing.patch
Patch9: bz1189857-02-fix-tree-view-of-resources-in-web-UI.patch
Patch10: bz1158566-01-fix-dashboard-in-web-UI.patch
Patch11: bz1189857-03-web-UI-prevents-running-update-multiple-times-at-onc.patch
Patch12: bz1189857-04-fix-constraints-removing-in-web-UI.patch
Patch13: bz1158571-01-web-UI-mark-unsaved-permissions-forms.patch
Patch14: bz1189857-05-remove-removing-constriants-from-client-side-javascr.patch
Patch15: bz1235022-02-fix-crash-when-missing-nagios-metadata.patch
Patch16: bz1158571-02-check-and-refresh-user-auth-info-upon-each-request.patch
Patch17: bz1257369-01-always-print-output-of-crm_resource-cleanup.patch
Patch18: bz1158566-02-fix-loading-cluster-status-for-web-UI.patch
Patch19: bz1158569-01-fixed-a-typo-in-an-error-message.patch
Patch20: bz1158571-03-fix-checking-user-s-group-membership.patch
Patch21: bz1188361-01-Make-port-parameter-of-fence-agents-optional.patch
Patch22: bz1158569-02-fix-authentication-in-web-UI.patch
Patch23: bz1158566-03-web-UI-multiple-fixes-in-the-dashboard.patch
Patch24: bz1198640-01-web-UI-allows-spaces-in-optional-arguments-when-crea.patch
Patch25: bz1189857-06-web-UI-fixes-in-nodes-resources-fence-devices.patch
Patch26: bz1245264-01-Added-more-detailed-warnings-for-pcs-stonith-confirm.patch
Patch27: bz1189857-07-web-UI-fixes.patch
Patch28: bz1265425-01-Fix-for-crm_node-l-output-change.patch
Patch29: bz1268801-Fixed-issue-with-resource-manage-not-removing-meta-a.patch
Patch30: bz1268801-Fixes-for-managing-special-cases-of-unmanaged-resour.patch
Patch31: bz1268801-Fixes-for-managing-special-cases-of-unmanaged-resour-2.patch
Patch32: bz1272412-01-fix-setting-cluster-properties-in-web-UI.patch

BuildRequires: ruby >= 2.0.0 ruby-devel rubygems pam-devel git
BuildRequires: systemd-units rubygem-bundler
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Requires: pacemaker-cli corosync ruby >= 2.0.0 pacemaker python-clufter
Requires: psmisc initscripts openssl

Provides: bundled(rubygem-backports) = 3.6.4
Provides: bundled(rubygem-eventmachine) = 1.0.7
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
%autosetup -p1 -S git

cp -f %SOURCE1 pcsd/public/images

%build

%install
rm -rf $RPM_BUILD_ROOT
pwd
make install DESTDIR=$RPM_BUILD_ROOT PYTHON_SITELIB=%{python_sitelib}
make install_pcsd DESTDIR=$RPM_BUILD_ROOT PYTHON_SITELIB=%{python_sitelib} hdrdir="%{_includedir}" rubyhdrdir="%{_includedir}" includedir="%{_includedir}"
chmod 755 $RPM_BUILD_ROOT/%{python_sitelib}/pcs/pcs.py

# Temporary fix for ruby-2.0.0 and rpam
#cp $RPM_BUILD_ROOT/usr/lib/pcsd/gemhome/gems/rpam-ruby19-1.2.1/ext/Rpam/rpam_ext.so $RPM_BUILD_ROOT/usr/lib/pcsd/gemhome/gems/rpam-ruby19-1.2.1/lib

%post
%systemd_post pcsd.service

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
/usr/lib/systemd/system/pcsd.service
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
* Wed Oct 21 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.143-15
- Fixed setting cluster properties in web UI
- Resolves: rhbz#1272412

* Wed Oct 07 2015 Chris Feist <cfeist@redhat.com> - 0.9.143-14
- Fixed remaining issues when managing resources/groups/etc. that were
  previously unmanaged
- Resolves: rhbz#1268801

* Tue Oct 06 2015 Chris Feist <cfeist@redhat.com> - 0.9.143-12
- Fixed issue managing resources that were clones and had the unmanaged
  meta attribute set under the clone/master
- Resolves: rhbz#1268801

* Wed Sep 23 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.143-11
- Fix for crm_node -l output change
- Resolves: rhbz#1265425

* Tue Sep 22 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.143-10
- Web UI fixes
- Added more detailed warnings for 'pcs stonith confirm'
- Resolves: rhbz#1189857 rhbz#1245264

* Wed Sep 16 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.143-9
- Multiple fixes in web UI (dashboard, nodes, resources, fence devices)
- Fixed an authentication issue in web UI
- Port parameter of fence agents is now considered optional
- Resolves: rhbz#1158566 rhbz#1188361 rhbz#1189857

* Tue Sep 08 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.143-8
- Fixes in loading cluster status for web UI
- Fixed checking user/group membership
- Fixed a typo in an error message
- Resolves: #rhbz1158566 #rhbz1158569 #rhbz1158571

* Mon Sep 07 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.143-7
- Multiple fixes in web UI
- Fixed crash on missing nagios agents metadata
- Check user/group membership on each request
- Print output of crm_resource in pcs resource cleanup
- Resolves: #rhbz1158571 #rhbz1189857 #rhbz1235022 #rhbz1257369

* Tue Sep 01 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.143-6
- Added missing dependency on openssl
- Resolves: #rhbz1158577

* Tue Sep 01 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.143-5
- Fixed pcsd certificates synchronization
- Multiple fixes in web UI
- Resolves: #rhbz1158566 #rhbz1158577 #rhbz1189857

* Mon Aug 31 2015 Chris Feist <cfeist@redhat.com> - 0.9.143-4
- Fixed issue causing traceback on pcsd stop
- Resolves: #rhbz#1258619

* Wed Aug 26 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.143-3
- Fixed relocation of remote nodes to their optimal node
- Fixed pcs/pcsd path detection
- Fixed command injection vulnerability
- Resolves: #rhbz1122818 #rhbz1253294 #rhbz1253491

* Fri Aug 14 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.143-2
- Fixed relocation of unique clone resources to their optimal node
- Improved logging of node to node communication
- Fixed 'Add resource' form in web UI
- Fixed support for nagios agents
- Resolves: rhbz#1122818 rhbz#1158577 rhbz#1189857 rhbz#1235022

* Mon Aug 10 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.143-1
- Added support for setting permissions for users and groups to clusters managed by web UI
- Resources are now displayed in a tree (clone, master/slave, group, primitive) in web UI
- Renamed 'pcs resource relocate clean' command to 'pcs resource relocate clear'
- Improved logging of config files synchronization
- Various fixes in Resources tab in web UI
- Added missing dependecy on initscripts to the spec file
- Fixed traceback when running 'pcs resource enable clvmd --wait'
- Resolves: rhbz#1122818 rhbz#1158571 rhbz#1158577 rhbz#1182119 rhbz#1189857 rhbz#1198640 rhbz#1219574 rhbz#1243579 rhbz#1247818 rhbz#1250720

* Fri Jul 10 2015 Chris Feist <cfeist@redhat.com> - 0.9.142-2
- Cleaned up tarball

* Thu Jul 09 2015 Chris Feist <cfeist@redhat.com> - 0.9.142-1
- Rebase to latest upstream sources
- Added ability to set hostname when using IP address to create a cluster
- Added ability to clear out tokens with pcs pcsd clear-auth
- Added ability to use nagios agents
- Fixed issue with orphaned resources causing GUI to fail to work properly
- More dashboard fixes
- Synchronize files between pcsd instances in a cluster to allow for HA pcsd
- ACL role fixes for pcs/pcsd
- Resolves: rhbz#118310 rhbz#1207805 rhbz#1235022 rhbz#1198222 rhbz#1158566 rhbz#1158577 rhbz#1166160

* Tue Jun 23 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.141-1
- Rebased to latest upstream packages
- Added a command to relocate resources to their preferred host
- Fixed the dashboard in web UI
- Configure corosync to log to a file
- Added warning when creating a duplicate resource operation
- Added support for debugging resource agents
- Do not automatically use --force when removing a resource using web UI
- Fixed pcsd communication when one of the nodes is not authenticated
- Updated ruby gems
- Spec file fixes
- Resolves: rhbz#1198265 rhbz#1122818 rhbz#1158566 rhbz#1163671 rhbz#1175400 rhbz#1185096 rhbz#1198274 rhbz#1213429 rhbz#1231987 rhbz#1232644 rhbz#1233574

* Wed Jun 03 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.140-1
- Rebased to latest upstream packages
- Added a note to man page and help poiting to cluster properties description
- Fixed parsing of the corosync.conf file
- Fixed diferences between the 'pcs cluster status' and 'pcs status cluster' commands as one is documented to be an alias of the other
- Do not remove constraints referencing a group when removing a resource from the group
- Added dashboard showing status of clusters to web UI
- Added node authentication dialog to web UI
- Added synchronization of web UI configuration files across cluster nodes
- Fixed node authentication when one of the nodes is unreachable
- Fixed an error message in the 'pcs config restore' command if a node is not authenticated
- Fixed parsing of 'pcs acl role create' command's parameters
- Properly overwrite a tokens file if its contents is unparsable
- The 'pcs config' command now displays resources defaults and operations defaults
- Show a useful error message when attempting to add a duplicate fence level in web UI
- Added the require-all parameter to ordering constraints listing
- Fixed VirtualDomain resource removal when there are constraints for the resource
- Added a warning when removing a cluster node may cause a loss of the quorum
- Fixed an error when uncloning a non-cloned resource
- Fixed an error when removing a resource from a cloned group
- Fixed waiting for resource commands to finish
- Fixed 'pcs cluster start' and similar commands when run under a non-root account
- Fixed parsing of 'pcs constraint order set' command's parameters
- Fixed an error when creating a resource with an id which already exists
- Improved man page and help for the 'pcs resource move' and 'pcs resource ban' commands
- Fixed an error when referencing a non-existing acl role in 'pcs acl' commands
- Fixed an error when adding an invalid stonith level
- Fixed constraints removal and node standby / unstandby using remote web UI
- Fixed formatting of resource / fence agent description
- Fence agent description now contains information about the agent
- The 'pcs status --full' command now displays node attributes and migration summary
- Clufter moved to a standalone package
- Fixed pcsd communication when one of the nodes is not authenticated
- Fixed a timeout value in the fence_xvm agent form
- Fixed the 'pcs resource enable' command when working with clones and multi-state resources
- Resolves: rhbz#1198265 rhbz#1121791 rhbz#1134426 rhbz#1158491 rhbz#1158537 rhbz#1158566 rhbz#1158569 rhbz#1158577 rhbz#1163682 rhbz#1165803 rhbz#1166160 rhbz#1170205 rhbz#1176687 rhbz#1182793 rhbz#1182986 rhbz#1183752 rhbz#1186692 rhbz#1187320 rhbz#1187571 rhbz#1188571 rhbz#1196412 rhbz#1197758 rhbz#1199073 rhbz#1201452 rhbz#1202457 rhbz#1204880 rhbz#1205653 rhbz#1206214 rhbz#1206219 rhbz#1206223 rhbz#1212904 rhbz#1213429 rhbz#1215198 rhbz#1218979

* Tue Jun 02 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.137-16
- Fixes cluster property name validation
- Resolves: rhbz#1218478

* Wed Apr 15 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.137-15
- Fixes issues with cookie signing in pcsd
- Resolves: rhbz#1211568

* Mon Mar 09 2015 Tomas Jelinek <tojeline@redhat.com> - 0.9.137-14
- Do not set two_nodes=1 in corosync.conf when auto_tie_breaker=1 is set
- Resolves: rhbz#1197770

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

