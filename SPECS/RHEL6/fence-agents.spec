###############################################################################
###############################################################################
##
##  Copyright (C) 2004-2011 Red Hat, Inc.  All rights reserved.
##
##  This copyrighted material is made available to anyone wishing to use,
##  modify, copy, or redistribute it subject to the terms and conditions
##  of the GNU General Public License v.2.
##
###############################################################################
###############################################################################

# keep around ready for later user
## global alphatag git0a6184070

Name: fence-agents
Summary: Fence Agents for Red Hat Cluster
Version: 4.0.15
Release: 12%{?alphatag:.%{alphatag}}%{?dist}
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
URL: http://sources.redhat.com/cluster/wiki/
Source0: https://fedorahosted.org/releases/f/e/fence-agents/%{name}-%{version}.tar.bz2

Patch0: 0001-revert.patch
Patch1: 0002-revert.patch
Patch2: 0003-revert.patch
Patch3: 0004-revert.patch
Patch4: 0005-revert.patch
Patch5: 0006-revert.patch
Patch6: 0007-revert.patch
Patch7: 0008-revert.patch
Patch8: 0009-revert.patch
Patch9: 0010-revert.patch
Patch10: 0011-revert.patch
Patch11: 0012-revert.patch
Patch12: 0013-revert.patch
Patch13: 0014-revert.patch
Patch14: 0015-revert.patch
Patch15: 0016-revert.patch
Patch16: 0017-revert.patch
Patch17: 0018-revert.patch
Patch18: 0019-revert.patch
Patch19: 0020-revert.patch
Patch20: 0021-revert.patch
Patch21: 0022-revert.patch
Patch22: 0023-revert.patch
Patch23: 0024-revert.patch
Patch24: bz1094515-fence_kdump-monitor.patch
Patch25: bz1094515-2-fence_kdump-monitor.patch
Patch26: bz1094515-3-fence_kdump-monitor.patch
Patch27: bz1094515-4-fence_kdump-monitor.patch
Patch28: bz1049805-rebase_ipmi_unset_cipher.patch
Patch29: bz1049805-rebase_bladecenter.patch
Patch30: bz1049805-rebase_remove_python_scsi.patch
Patch31: bz1049805-rebase_tls.patch
Patch32: bz1118008-1-fence_mpath_metadata.patch
Patch33: bz1118008-2-fence_mpath_metadata.patch
Patch34: bz1254046-fence_ipmilan-option_i.patch
Patch35: bz1254700-fence_ipmilan-timeout.patch
Patch36: bz1256902-fence_ilo-tls_negotiation.patch
Patch37: bz1247062-fence_rsa-login.patch
Patch38: bz1254183-1-fence_mpath-reboot_problem.patch
Patch39: bz1254183-2-fence_mpath-reboot_problem.patch
Patch40: bz1274432-brocade.patch 
Patch41: bz1273632-fence_ipmilan-power_wait_revert.patch
Patch42: bz1259254-fence_apc-support_for_v6.patch
Patch43: bz1266600-fence_ipmilan-add_diag.patch
Patch44: bz1183829-fencing-add_list-status.patch
Patch45: bz1183829-2-fencing-add_list-status.patch
Patch46: bz1266600-2-fence_ipmilan-add_diag.patch

ExclusiveArch: i686 x86_64

# shipped agents
%global supportedagents apc apc_snmp bladecenter brocade cisco_mds cisco_ucs drac drac5 eaton_snmp emerson eps hpblade kdump ibmblade ifmib ilo ilo_moonshot ilo_mp ilo_ssh intelmodular ipdu ipmilan manual mpath rhevm rsb scsi wti vmware_soap
%global deprecated rsa sanbox2
%global testagents virsh vmware
%global requiresthirdparty egenera

## Runtime deps
Requires: sg3_utils telnet openssh-clients
Requires: pexpect net-snmp-utils
Requires: perl-Net-Telnet python-pycurl pyOpenSSL
Requires: python-suds gnutls-utils

# This is required by fence_virsh. Per discussion on fedora-devel
# switching from package to file based require.
Requires: /usr/bin/virsh

# This is required by fence_ipmilan. it appears that the packages
# have changed Requires around. Make sure to get the right one.
Requires: /usr/bin/ipmitool

## Setup/build bits

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

# Build dependencies
BuildRequires: perl python
BuildRequires: glibc-devel
BuildRequires: nss-devel nspr-devel
BuildRequires: libxslt pexpect
BuildRequires: python-pycurl
BuildRequires: python-suds
BuildRequires: automake autoconf pkgconfig libtool
BuildRequires: net-snmp-utils perl-Net-Telnet
BuildRequires: device-mapper-multipath

%prep
%setup -q -n %{name}-%{version}

%patch0 -p1 -b .revert01
%patch1 -p1 -b .revert02
%patch2 -p1 -b .revert03
%patch3 -p1 -b .revert04
%patch4 -p1 -b .revert05
%patch5 -p1 -b .revert06
%patch6 -p1 -b .revert07
%patch7 -p1 -b .revert08
%patch8 -p1 -b .revert09
%patch9 -p1 -b .revert10
%patch10 -p1 -b .revert11
%patch11 -p1 -b .revert12
%patch12 -p1 -b .revert13
%patch13 -p1 -b .revert14
%patch14 -p1 -b .revert15
%patch15 -p1 -b .revert16
%patch16 -p1 -b .revert17
%patch17 -p1 -b .revert18
%patch18 -p1 -b .revert19
%patch19 -p1 -b .revert20
%patch20 -p1 -b .revert21
%patch21 -p1 -b .revert22
%patch22 -p1 -b .revert23
%patch23 -p1 -b .revert24
%patch24 -p1 -b .bz1094515
%patch25 -p1 -b .bz1094515.2
%patch26 -p1 -b .bz1094515.3
%patch27 -p1 -b .bz1094515.4
%patch28 -p1 -b .bz1049805.1
%patch29 -p1 -b .bz1049805.2
%patch30 -p1 -b .bz1049805.3
%patch31 -p1 -b .bz1049805.4
%patch32 -p1 -b .bz1118008.1
%patch33 -p1 -b .bz1118008.2
%patch34 -p1 -b .bz1254046
%patch35 -p1 -b .bz1254700
%patch36 -p1 -b .bz1256902
%patch37 -p1 -b .bz1247062
%patch38 -p1 -b .bz1254183.1
%patch39 -p1 -b .bz1254183.2
%patch40 -p1 -b .bz1274432
%patch41 -p1 -b .bz1273632
%patch42 -p1 -b .bz1259254
%patch43 -p1 -b .bz1266600
%patch44 -p1 -b .bz1183829
%patch45 -p1 -b .bz1183829.2
%patch46 -p1 -b .bz1266600.2

%build
./autogen.sh
%{configure} \
	--with-agents='%{supportedagents} %{deprecated} %{testagents} %{requiresthirdparty}'

CFLAGS="$(echo '%{optflags}')" make %{_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

## tree fix up
# fix libfence permissions
chmod 0755 %{buildroot}%{_datadir}/fence/*.py
# remove docs
rm -rf %{buildroot}/usr/share/doc/fence-agents
# compatibility symlink bladecenter_snmp to ibmblade
ln -sf %{_sbindir}/fence_ibmblade %{buildroot}/%{_sbindir}/fence_bladecenter_snmp
ln -sf %{_mandir}/man8/fence_ibmblade.8.gz %{buildroot}/%{_mandir}/man8/fence_bladecenter_snmp.8.gz

%clean
rm -rf %{buildroot}

%post
ccs_update_schema > /dev/null 2>&1 ||:

%description
Red Hat Fence Agents is a collection of scripts to handle remote
power management for several devices.

%files 
%defattr(-,root,root,-)
%doc doc/COPYING.* doc/COPYRIGHT doc/README.licence
%{_sbindir}/fence*
%{_datadir}/fence
%{_datadir}/cluster
%{_mandir}/man8/fence*

%changelog
* Wed Dec 16 2015 Marek Grac <mgrac@redhat.com> - 4.0.15-12
- fence_ipmilan: Add 'diag' action
  Resolves: rhbz#1266600

* Mon Dec 14 2015 Marek Grac <mgrac@redhat.com> - 4.0.15-11
- fence_ipmilan: Revert power_wait values
  Resolves: rhbz#1273632
- fence_apc: Support for firmware 6.x
  Resolves: rhbz#1259254
- fence_ipmilan: Add 'diag' action
  Resolves: rhbz#1266600
- fencing: Add '-list-status' action
  Resolves: rhbz#1183829

* Mon Nov 02 2015 Marek Grac <mgrac@redhat.com> - 4.0.15-10
- fence_brocade: Regression in get_power_status
  Resolves: rhbz#1274432

* Thu Aug 27 2015 Marek Grac <mgrac@redhat.com> - 4.0.15-9
- fence_ipmilan no longer understands -i
  Resolves: rhbz#1254046
- fence_ipmilan no longer understands 'timeout'
  Resolves: rhbz#1254700
- fence_ilo: Improve negotiation of TLS protocol
  Resolves: rhbz#1256902
- fence_rsa: Login process over telnet is not working
  Resolves: rhbz#1247062
- fence_mpath: lose scsi keys after restart
  Resolves: rhbz#1254183

* Thu Mar 26 2015 Marek Grac <mgrac@redhat.com> - 4.0.15-8
- fix fence2rng to handle quotes
  Resolves: rhbz#1118008

* Tue Mar 24 2015 Marek Grac <mgrac@redhat.com> - 4.0.15-7
- fence_scsi: remove new pythonic version
- fence_ipmilan: unset default cipher
- fence_ilo2: add options --tls1.0
- fence_bladecenter: fix login process
  Resolves: rhbz#1049805

* Mon Mar 02 2015 Marek Grac <mgrac@redhat.com> - 4.0.15-6
- fence_kdump: Fix problems found by Coverity
  Resolves: rhbz#1094515

* Thu Feb 26 2015 Marek Grac <mgrac@redhat.com> - 4.0.15-5
- fence_ilo_ssh: New fence agent
  Resolves: rhbz#1111482
- fence_kdump: Update metadata for 'monitor'
  Resolves: rhbz#1094515

* Wed Feb 25 2015 Marek Grac <mgrac@redhat.com> - 4.0.15-4
- fence_ilo_moonshot: New fence agent for HP Moonshot
  Resolves: rhbz#1099551
- fence_mpath: New fence agent for multipath devices
  Resolves: rhbz#1118008

* Wed Feb 25 2015 Marek Grac <mgrac@redhat.com> - 4.0.15-3
- fence_kdump: Doesn't support 'monitor'
  Resolves: rhbz#1094515

* Thu Feb 19 2015 Marek Grac <mgrac@redhat.com> - 4.0.15-2
- rebase of fence agents with reverts for backward compatibility
  Resolves: rhbz#1049805

* Wed Feb 18 2015 Marek Grac <mgrac@redhat.com> - 4.0.15-1
- rebase of fence agents with reverts for backward compatibility
  Resolves: rhbz#1049805

* Thu Jul 10 2014 Marek Grac <mgrac@redhat.com> - 3.0.15-48
- fencing: fix issue with "io_fencing" in metadata
  Resolves: rhbz#1114559

* Wed Jul 02 2014 Marek Grac <mgrac@redhat.com> - 3.0.15-47
- fence_brocade: add support for list to allow monitor
  Resolves: rhbz#1114528

* Tue Jul 01 2014 Marek Grac <mgrac@redhat.com> - 3.0.15-44
- fence_brocade: fix default action
  Resolves: rhbz#1114559
- fence_brocade: add support for list to allow monitor
  Resolves: rhbz#1114528

* Thu Jun 26 2014 Marek Grac <mgrac@redhat.com> - 3.0.15-43
- fix quoes in fence_ilo
  Resolves: rhbz#990537
- fix delay support for agents without off/reboot
  Resolves: rhbz#641632

* Mon Jun 23 2014 Marek Grac <mgrac@redhat.com> - 3.0.15-42
- fence_scsi_check can do hard reboot now
  Resolves: rhbz#1050022

* Fri Jun 20 2014 Marek Grac <mgrac@redhat.com> - 3.0.15-41
- fence_brocade ported to fencing library
  Resolves: rhbz#641632 rhbz#642232 rhbz#841556
- fence_rsb fails to power devices on with certain firmwares
  Resolves: rhbz#1110428

* Wed Jun 18 2014 Marek Grac <mgrac@redhat.com> - 3.0.15-40
- fencing: Add option --ssh-options
  Resolves: rhbz#1069618
- fence_vmware_soap: python exception when user does not have privileges
  Resolves: rhbz#1018263
- fence_wti: Add support for delay
  Resolves: rhbz#1079291
- fence_ilo: Unable to enter password with "
  Resolves: rhbz#990537
- fencing: Fence agent uses key authentication when it should use password
  Resolves: rhbz#1048842

* Fri Mar 14 2014 Marek Grac <mgrac@redhat.com> - 3.0.15-39
- fencing: fix exception when identity file is used
  Resolves: rhbz#1075683

* Fri Jan 24 2014 Marek Grac <mgrac@redhat.com> - 3.0.15-38
- fence_vmware_soap: Add delay option
  Resolves: rhbz#1051159

* Mon Oct 07 2013 Marek Grac <mgrac@redhat.com> - 3.0.15-35
- fence_vmware_soap: Fix symlink vulnerability caused by python-suds temp directory
  Resolves: rhbz#1014000

* Thu Aug 29 2013 Marek Grac <mgrac@redhat.com> - 3.0.15-34
- fence_cisco_ucs: Respect login timeout
  Resolves: rhbz#978325
- fence_bladecenter: Telnet login failure
  Resolves: rhbz#997416

* Mon Aug 12 2013 Marek Grac <mgrac@redhat.com> - 3.0.15-33
- fence_scsi: Fix error in XML metadata
  Resolves: rhbz#994186
- fence_scsi: Add documention of "delay" into manual pages
  Resolves: rhbz#912773
- fencing: Improve detection of EOL during login
  Resolves: rhbz#886614

* Thu Jul 18 2013 Marek Grac <mgrac@redhat.com> - 3.0.15-31
- improve description of lanplus parameter in fence ipmilan agent
  Resolves: rhbz#981086

* Mon Jul 15 2013 Marek Grac <mgrac@redhat.com> - 3.0.15-30
- add symlink for HP iLO4
  Resolves: rhbz#870269

* Fri Jun 28 2013 Marek Grac <mgrac@redhat.com> - 3.0.15-29
- remove static parts from cluster schema templates
  Resolves: rhbz#917675
- fence_cisco_ucs: agent did not respect login_timeout
  Resolves: rhbz#978325
- fence_cisco_ucs: agent fail with traceback when hostname cannot be resolved
  Resolves: rhbz#978326
- fencing: Validation if password/password_script or identity file is used was not processed
  Resolves: rhbz#959490
- fence_scsi: support unfence action in pacemaker cluster
  Resolves: rhbz#978328

* Thu Jun 27 2013 Marek Grac <mgrac@redhat.com> - 3.0.15-28
- fence_scsi: Add delay option
  Resolves: rhbz#912773
- fence_apc: Add support for firmware 5.x
  Resolves: rhbz#886614

* Wed Jun 26 2013 Marek Grac <mgrac@redhat.com> - 3.0.15-27
- fence_ipmilan: Fix manual page to mention HP iLO3, iLO4
  Resolves: rhbz#872308
- fence_cisco_ucs: Respect "delay" option
  Resolves: rhbz#896603
- fence_scsi: Add "unfence" operation to manual page
  Resolves: rhbz#887349

* Wed Feb 06 2013 Marek Grac <mgrac@redhat.com> - 3.0.15-26
- fence_drac5: fix regression caused by missing detection of EOL
  Resolves: rhbz#905478
- fence_vmware_soap: fix traceback when hostname cannot be resolved
  Resolves: rhbz#902404

* Thu Dec 20 2012 Ryan O'Hara <rohara@redhat.com> - 3.0.15-25
- fence_scsi: allow action=metadata via STDIN
  Resolves: rhbz#837174

* Tue Oct 09 2012 Marek Grac <mgrac@redhat.com> - 3.0.15-24
- fence_ipdu, fence_hpblade: fix building process

* Tue Oct 09 2012 Marek Grac <mgrac@redhat.com> - 3.0.15-23
- fence_rhevm: fix typo in RE
  Resolves: rhbz#863568

* Mon Oct 08 2012 Marek Grac <mgrac@redhat.com> - 3.0.15-22
- fencing: add action=metadata to the rest of the fence agents
  Resolves: rhbz#837174

* Mon Oct 08 2012 Marek Grac <mgrac@redhat.com> - 3.0.15-21
- fence_vmware_soap: Faster fencing and fix issue with VM without valid UUID
  Resolves: rhbz#769798
- fence_rhevm: Support new RHEV-M API
  Resolves: rhbz#863568

* Thu Oct 04 2012 Marek Grac <mgrac@redhat.com> - 3.0.15-20
- fence_ipdu: New fence agent for IBM iPDU
  Resolves: rhbz#740869
- fence_hpblade: New fence agent for HP blades
  Resolves: rhbz#818337
- Add fence symlinks for most used fence agents
  Resolves: rhbz#800650
- Fix unique attributes in XML output
  Resolves: rhbz#822507
- Automatic detection of EOL in telnet sessions
  Resolves: rhbz#823430

* Mon Sep 17 2012 Ryan O'Hara <rohara@redhat.com> - 3.1.5-19
- fence_scsi: add metadata action to man page
  Resolves: rhbz#825667

* Wed Aug 15 2012 Fabio M. Di Nitto <fdinitto@redhat.com> -  3.1.5-18
- fence_eaton_snmp: add agent to supported matrix
  Resolves: rhbz#752449

* Thu Apr 12 2012 Marek Grac <mgrac@redhat.com> - 3.1.5-17
- fence_brocade: does not accept "action" option from STDIN
  Resolves: rhbz#804805

* Mon Apr  2 2012 Marek Grac <mgrac@redhat.com> - 3.1.5-16
- fence agents: attribute unique in XML metadata should be set 0
  Resolves: rhbz#806883
- fence_ipmilan: Typo
  Resolves: rhbz#806912
- fence_ipmilan: Return code can be invalid with -M cycle
  Resolves: rhbz#806897

* Mon Mar 26 2012 Marek Grac <mgrac@redhat.com> - 3.1.5-15
- fence agents: Using "delay" option can ends with timeout (ipmilan part)
  Resolves: rhbz#804169

* Fri Mar 23 2012 Lon Hohberger <lhh@redhat.com> - 3.1.5-14
- fence agents: Using "delay" option can ends with timeout
  Resolves: rhbz#804169

* Tue Feb 21 2012 Marek Grac <mgrac@redhat.com> - 3.1.5-12
- fence_ipmilan: doesn't respect power_wait option for power off
  Resolves: rhbz#787706
- fencing: Missing password is not reported properly
  Resolves: rhbz#785091
- fencing: fence_<agent> metadata behaviour and docs 
  Resolves: rhbz#714841

* Sat Feb 18 2012 Marek Grac <mgrac@redhat.com> - 3.1.5-11
- fence_ipmilan: Parsing args for password script
  Resolves: rhbz#740484
- fence_rsb: Porting RSB fence agent to fencing library (ssh support added)
  Resolves: rhbz#742003
- fence_rhevm: Incorrect power status detection
  Resolves: rhbz#769681
- fence_vmware_soap: Support for alias names as ports
  Resolves: rhbz#771211
- fence_ipmilan: Possible buffer overflow
  Resolves: rhbz#771936
- fence_vmware_soap: Support for more than 100 virtual machines
  Resolves: rhbz#772597

* Wed Feb 8 2012 Ryan O'Hara <rohara@redhat.com - 3.1.5-11
- fence_scsi: remove unlink of fence_scsi.dev file during unfence
  Resolves: rhbz#741339

* Tue Sep 20 2011 Marek Grac <mgrac@redhat.com> - 3.1.5-10
- fence_kdump: Newly detected Coverity defect (null dereference)
  Resolves: rhbz#734429
- fence_scsi: fix scsi unfencing to allow simultaneous unfences
  Resolves: rhbz#738384

* Thu Sep 15 2011 Marek Grac <mgrac@redhat.com> - 3.1.5-9
- fence_ipmilan exposes user password on verbose mod
  Resolves: rhbz#732372
- fence_ipmilan should honor ipmilan's -L option (privileges)
  Resolves: rhbz#726571

* Mon Aug 29 2011 Marek Grac <mgrac@redhat.com> - 3.1.5-8
- fence-rhevm needs update path to REST API
  Resolves: rhbz#731166

* Mon Aug 22 2011 Marek Grac <mgrac@redhat.com> - 3.1.5-7
- fence_rhevm needs to change "UP" status to "up" state 
    as the REST-API has changed
  Resolves: rhbz#731166

* Mon Aug 15 2011 Marek Grac <mgrac@redhat.com> - 3.1.5-6
- drac5 firmware does not clear ssh session on exit
  Resolves: rhbz#718924

* Wed Aug  3 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.1.5-5
- Add fence_kdump and fence_kdump_send
  Resolves: rhbz#461948

* Mon Aug  1 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.1.5-4
- Update patch from correct git branch for rhbz#698365
  Related: rhbz#698365

* Tue Jul 26 2011 Lon Hohberger <lhh@redhat.com> - 3.1.5-3
- Enable fence_vmware_soap in spec file
  Resolves: rhbz#624673

* Fri Jul 22 2011 Lon Hohberger <lhh@redhat.com> - 3.1.5-2
- Add rha:name and rha:description tag to RelaxNG XSL
  Resolves: rhbz#698365

* Mon Jul 11 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.1.5-1
- Rebase package on top of new upstream
  * ship xsl and rng files required to build relaxng schema
- spec file update:
  add %post to generate new relaxng schema
  Resolves: rhbz#707123
- Add Requires: pyOpenSSL for fence_ilo
  Resolves: rhbz#718207
- Fix fence_drac5 list operation with Dell DRAC CMC
  (imported directly from new upstream)
  Resolves: rhbz#718196
- fence_bladecenter --missing_as_off reboot action fails on missing blade
  (imported directly from new upstream)
  Resolves: rhbz#708052

* Tue Jun  7 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.1.4-1
- Rebase package on top of new upstream
- spec file update:
  * update spec file copyright date
  * update upstream URL
  * drop all patches
  * update list of fence_agents (ibmblade listed twice, bladecenter_snmp deprecated)
  * drop libxml2-devel libvirt-devel clusterlib-devel corosynclib-devel and
    openaislib-devel from BuildRequires
  * make ready to enable fence_vmware_soap
  * update and clean configure and build section.
  * create bladecenter_snmp compat symlink at rpm install time
  * update file list to include scsi_check script
  Resolves: rhbz#707123
- Integrate watchdog with cluster to reboot nodes when scsi fencing has occurred
  (imported directly from new upstream)
  Resolves: rhbz#673575
- fence_ipmilan returns incorrect status on monitor op if chassis is powered off
  (imported directly from new upstream)
  Resolves: rhbz#693428
- fence_rsa: fix AttributeError: 'NoneType' object has no attribute 'group'
  (imported directly from new upstream)
  Resolves: rhbz#678019

* Wed Apr 06 2011 Lon Hohberger <lhh@redhat.com> - Version: 3.0.12-23
- fence_ipmilan: Correct return code for diag operation
  (fence_ipmilan_correct_return_code_for_diag_operation.patch)
  Resolves: rhbz#655764

* Fri Mar 25 2011 Marek Grac <mgrac@redhat.com> - 3.0.12-22
- fence_cisco_ucs: Add support for sub-organizations
  (fence_cisco_ucs-Support-for-sub-organization.patch)
  (fence_cisco_ucs-Fix-for-support-for-sub-organization.patch)
  Resolves: rhbz#678904

* Mon Mar 21 2011 Marek Grac <mgrac@redhat.com> - 3.0.12-21
- fence_rhevm: Update URL for RHEV-M REST API
  (fence_rhevm-Update-URL-to-RHEV-M-REST-API.patch)
  Resolves: rhbz#681674

* Fri Mar 18 2011 Marek Grac <mgrac@redhat.com> - 3.0.12-20
- fencing: Accept other values for yes (on, true)
  (fence-agents-Accept-other-values-for-true.patch)
  Resolves: rhbz#679502

* Wed Mar 16 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-18
- fence_wti: Unable to parse output when split into several screens
  (fence_wti_unable_to_parse_output_when_split_into_several_screens_part1.patch)
  (fence_wti_unable_to_parse_output_when_split_into_several_screens_part2.patch)
  Resolves: rhbz#678522

* Wed Mar 16 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-17
- Allow fence_scsi to use any valid hexadecimal key
  (fence_scsi_allow_use_of_any_valid_hexadecimal_key.patch)
- fence_scsi: grep for keys should be case insensitive
  (fence_scsi_grep_for_keys_should_be_case_insensitive.patch)
  Resolves: rhbz#653504

* Wed Mar  9 2011 Marcus Barrow <mbarrow@redhat.com> - 3.0.12-16
- update RHEVM running status.
  (fence_rhevm_change_running_status.patch)
  Resolves: rhbz#681669

* Mon Mar  7 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-15
- Ship fence_cisco_ucs again
  (spec file change only)
  Resolves: rhbz#682715

* Fri Feb 25 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-14
- Ship fence_brocade again
  (spec file change only)
  Resolves: rhbz#680170

* Thu Feb  3 2011 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-13
- fence_scsi: need stricter regular expression when looking for specific keys
  (fence_scsi_fix_regular_expression_for_grep.patch)
  Resolves: rhbz#670910
- fence_scsi: unfencing fails when device reports "unit attention"
  (fence_scsi_always_do_sg_turs_before_registration.patch)
  (fence_scsi_always_do_sg_turs_on_dm_mp_devices.patch)
  Resolves: rhbz#640343
- fence_scsi: verify that actions were successful
  (fence_scsi_verify_that_on_off_actions_succeed.patch)
  Resolves: rhbz#644385
- fence_scsi: identify dm-multipath devices correctly
  (fence_scsi_identify_dm_multipath_devices_correctly.patch)
  Resolves: rhbz#644389
- fence_scsi: properly log errors for all commands
  (fence_scsi_properly_log_errors_for_all_commands.patch)
  Resolves: rhbz#672597

* Thu Jan 20 2011 Marek Grac <mgrac@redhat.com> - 3.0.12-12
- Add "diag" option to fence_ipmilan to support ipmi chassis power diag option
  (fence_ipmilan-Add-diag-option-to-support-ipmitoo.patch)
  Resolves: rhbz#655764
- Fix manual page to describe usage of fence_ipmi with ilo3 
  (fence_ipmilan-Fix-manual-page-to-describe-usage-wit.patch)
  Resolves: rhbz#648892
- Metadata (man pages) generation does not take different sorts of action
  (library-Metadata-are-not-correct-if-agent-does-not.patch)
  Resolves: rhbz#623266

* Mon Oct 25 2010 Marek Grac <mgrac@redhat.com> - 3.0.12-11
- fence_drac5: make "port" a synonym of "module_name" for drac5
  (fence_drac5-make-port-a-synonym-of-module_name-for-d.patch)
  Resolves: rhbz#619096
- fencing: Not all parameters appear in metadata
  (fencing-Not-all-parameters-appear-in-metadata-1-2.patch)
  (fencing-Not-all-parameters-appear-in-metadata-2-2.patch)
  Resolves: rhbz#618703
- fence_egenera: Missing -u / user in manual page
  (fence_egenera-Missing-u-user-in-manual-page.patch)
  Resolves: rhbz#635824
- fence_cisco_ucs: New fence agent for Cisco UCS
  (fence_cisco_ucs-New-fence-agent-for-Cisco-UCS.patch)
  Resolves: rhbz#580492
- fencing: Method to cause one node to delay fencing
  (fencing-Method-to-cause-one-node-to-delay-fencing.patch)
  (fencing-Method-to-cause-one-node-to-delay-fencing-2.patch)
  (fencing-Method-to-cause-one-node-to-delay-fencing-dr.patch)
  (fencing-Method-to-cause-one-node-to-delay-fencing-ip.patch)
  Resolves: rhbz#614046

* Thu Oct 14 2010 Marek Grac <mgrac@redhat.com> - 3.0.12-10
- Support for ilo3 devices using fence_ipmilan
  (fence-agents-Add-power_wait-to-fence_ipmilan.patch)
  Resolves: rhbz#642671

* Wed Oct 13 2010 Marek Grac <mgrac@redhat.com> - 3.0.12-9
- Provide fence-rhev agent that uses the RHEV REST API
  (fence_rhevm.patch)
  Resolves: rhbz#595383

* Tue Aug 10 2010 Lon Hohberger <lhh@redhat.com> - Version: 3.0.12-8
- Fix syntax error in code that opens logfile.
  (fix_syntax_error_in_code_that_opens_logfile.patch)
  Resolves: rhbz#608887

* Wed Jul 21 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-7
- fence_rsb: Raise exceptions not strings with python 2.6
  (fence_rsb_raise_exceptions.patch)
  Resolves: rhbz#612941
- fence_ilo: will throw exception if user does not have power priviledges
  (fence_ilo_will_throw_exception_if_user_has_no_power_privs.patch)
  Resolves: rhbz#615255
- fence agents support clean up:
  drop support for baytech, brocade, mcdata, rackswitch and bullpap
  deprecate rsa and sanbox2
  rename ibmblade to bladecenter_snmp and add compatibility symlink
  (fence_rename_ibmblade_to_bladecenter_snmp_part1.patch)
  (fence_rename_ibmblade_to_bladecenter_snmp_part2.patch)
  Resolves: rhbz#616559
- spec file changelog cleanup for older releases
- rename Patch0 to be consistent with the others

* Mon Jun 28 2010 Lon Hohberger <lhh@redhat.com> - 3.0.12-6
- Don't truncate fence_scsi log files
  (fence_scsi_do_not_truncate_log_file.patch)
  Resolves: rhbz#608887

* Wed Jun 23 2010 Marek Grac <mgrac@redhat.com> - 3.0.12-4
- fence_apc fails for some port numbers
  (fence_apc_fails_for_some_port_numbers.patch)
- Resolves: rhbz#606297

* Fri Jun 18 2010 Marek Grac <mgrac@redhat.com> - 3.0.12-3
- Add support for non-default TCP ports for WTI fence agent
  (add_ipport_to_wti.patch)
- Resolves: rhbz#579059

* Wed May 19 2010 Lon Hohberger <lhh@redhat.com> - 3.0.12-2
- Add direct support for WTI VMR
  (add_direct_support_for_wti_vmr.patch)
  Resolves: rhbz#578617
- Fix changelog for 3.0.12-1 release (add missing bugzilla entries)

* Mon May 10 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.12-1
- Rebase on top of new upstream bug fix only release:
  * drop all bug fix patches.
  * Addresses the follwing issues:
    from 3.0.11 release:
  Resolves: rhbz#583019, rhbz#583017, rhbz#583948, rhbz#584003
  * Rebase:
  Resolves: rhbz#582351
- Stop build on ppc and ppc64.
  Resolves: rhbz#590985
- Update list of supported agents.

* Wed Apr  7 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.9-3
- Remove 'ipport' option from WTI fence agent
  (remove_ipport_option_from_wti_fence_agent.patch)
  Resolves: rhbz#579059

* Tue Mar 23 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.9-2
- Add workaround to broken snmp return codes
  (workaround_broken_snmp_return_codes.patch)
  Resolves: rhbz#574027

* Tue Mar  2 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.9-1
- new upstream release:
  Resolves: rhbz#557349, rhbz#564471
- spec file update:
  * update spec file copyright date
  * use bz2 tarball
  * bump minimum requirements for corosync/openais
  * fence-agents should not Requires fence-virt directly
  * stop shipping fence_xvmd

* Thu Feb 25 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.7-4
- Resolves: rhbz#568002
- Do not build fence-agents on s390 and s390x.

* Mon Feb  8 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.7-3
- Fix build of several agents (fix-build-with-man-page.patch)
- Resolves: rhbz#562806

* Thu Jan 14 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.7-2
- Stop shipping unsupported agents
- Add patch to fix man page shipping (man-page-cleanup.patch)

* Tue Jan 12 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.7-1
- New upstream release

* Mon Dec  7 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.6-2
- Use the correct tarball from upstream

* Mon Dec  7 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.6-1
- New upstream release (drop fence_head.diff)
- spec file updates:
  * use new Source0 url
  * use file based Requires for ipmitools (rhbz: 545237)

* Fri Dec  4 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.5-2.git0a6184070
- Drop fence_xvm from upstream (fence_head.diff)
- spec file updates:
  * Drop unrequired comments
  * Readd alpha tag and clean it's usage around
  * Requires: fence-virt in sufficient version to provide fence_xvm

* Fri Nov 20 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.5-1
- New upstream release

* Tue Oct 27 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.4-3
- Switch to file based Requires for virsh

* Tue Oct 27 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.4-2
- Fix Requires: on libvirt/libvirt-client

* Wed Oct 21 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.4-1
- New upstream release
- BuildRequire libxslt and pexpect for automatic man page generation

* Wed Sep 23 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.3-1
- New upstream release

* Mon Aug 24 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.2-2
- Fix changelog.

* Mon Aug 24 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.2-1
- New upstream release
- spec file updates:
  * remove dust from runtime dependencies

* Thu Aug 20 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.1-1
- New upstream release

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul  8 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-14
- New upstream release
- spec file updates:
  * Update copyright header
  * final release.. undefine alphatag
  * BuildRequires and Requires corosync/openais 1.0.0-1 final.

* Thu Jul  2 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-13.rc4
- New upstream release.
- spec file updates:
  * BuildRequires / Requires: latest corosync and openais
  * Drop --enable_virt. Now default upstream

* Sat Jun 20 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-12.rc3
- New upstream release.
- spec file updates:
  * BuildRequires / Requires: latest corosync and openais

* Wed Jun 10 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-11.rc2
- New upstream release + git94df30ca63e49afb1e8aeede65df8a3e5bcd0970
- spec file updates:
  * BuildRequires / Requires: latest corosync and openais
  * Build fence_xvm unconditionally now that libvirt is everywhere
  * Drop telnet_ssl wrapper in favour of nss version

* Tue Mar 24 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-10.rc1
- New upstream release.
- Cleanup BuildRequires to avoid to pull in tons of stuff when it's not
  required.
- Update BuildRoot usage to preferred versions/names.
- Stop shipping powermib. Those are not required for operations anymore.

* Thu Mar 12 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-9.beta1
- Fix arch check for virt support.
- Drop unrequired BuildRequires.
- Drop unrequired Requires: on perl.

* Mon Mar  9 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-8.beta1
- New upstream release.
- Update corosync/openais BuildRequires and Requires.

* Fri Mar  6 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-7.alpha7
- New upstream release.
- Drop fence_scsi init stuff that's not required anylonger.

* Tue Mar  3 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-6.alpha6
- New upstream release.

* Tue Feb 24 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-5.alpha5
- Fix directory ownership.

* Tue Feb 24 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-4.alpha5
- Drop Conflicts with cman.

* Mon Feb 23 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-3.alpha5
- New upstream release. Also address comments from first package review.

* Thu Feb 19 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-2.alpha4
- Add comments on how to build this package.
- Update build depends on new corosynclib and openaislib.

* Thu Feb  5 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-1.alpha4
- New upstream release.
- Fix datadir/fence directory ownership.
- Update BuildRequires: to reflect changes in corosync/openais/cluster
  library split.

* Tue Jan 27 2009 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.0.0-1.alpha3
- Initial packaging
