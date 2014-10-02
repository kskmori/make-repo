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
Version: 3.1.5
Release: 35%{?alphatag:.%{alphatag}}%{?dist}
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
URL: http://sources.redhat.com/cluster/wiki/
Source0: https://fedorahosted.org/releases/f/e/fence-agents/%{name}-%{version}.tar.bz2

Patch0: bz698365-add_rha_name_and_rha_description_tag_to_relaxng_xsl.patch
Patch1: bz461948-1-fence_kdump_new_fence_agent.patch
Patch2: bz461948-2-build_update_configure_ac_to_include_fence_kdump.patch
Patch3: bz461948-3-build_update_configure_ac_add_extra_checks_for_fence_kdump.patch
Patch4: bz461948-4-fence_kdump_fix_compiler_warnings.patch
Patch5: bz461948-5-fence_kdump_fix_more_compiler_warnings.patch
Patch6: bz461948-6-fence_kdump_drop_unused_protocol_definition.patch
Patch7: bz461948-7-fence_kdump_increase_default_timeout.patch
# Patch8 is disabled on purpose. Patch7 (in git) introduced binary files
# and 8 removes them, but git show SHA1 does not include binary output
# making 8 an empty patch that will fail to apply
# for consistency with git history the patch is here but not applied
Patch8: bz461948-8-fence_kdump_drop_binaries.patch
Patch9: bz461948-9-fence_kdump_fix_logging.patch
Patch10: bz461948-10-fence_kdump_restore_original_default_timeout.patch
Patch11: bz461948-11-fence_kdump_fix_metadata.patch
Patch12: bz718924-drac5_firmware_does_not_close_ssh_session.patch
Patch13: bz731166-fence_rhevm_change_UP_status_to_up_state_as_the_REST.patch
Patch14: bz731166-2-fence_rhevm_REST_API_URL_updated.patch
Patch15: bz732372-fence_ipmilan_exposes_user_password.patch
Patch16: bz726571-fence_ipmilan_should_honor_L_option.patch
Patch17: bz734429-fence_kdump-fix-potential-null-dereference.patch
Patch18: bz739384-fence_scsi-fix_simultaneous_unfence_operations.patch
Patch19: bz741339-fence_scsi-remove_unlink_of_fence_scsi_dev_file.patch
Patch20: bz740484-1-fence_ipmilan-parsing_args_for_passwd_script.patch
Patch21: bz742003-1-fence_rsb-rewrite_fence_agent.patch
Patch22: bz769681-1-fence_rhevm-incorrect_status.patch
Patch23: bz771211-1-fence_vmware_soap-Support-for-alias-names-as-ports.patch
Patch24: bz771936-1-fence_ipmilan-Possible-buffer-overflow.patch
Patch25: bz772597-1-fence_vmware_soap-Support-for-100-VM-in-VMWare.patch
Patch26: bz787706-fence_ipmilan_does_not_respect_power_wait.patch
Patch27: bz785091-Missing_password_is_not_reported_properly.patch
Patch28: bz714841-1-fence_agent_metadata.patch
Patch29: bz714841-2-fence_agent_metadata.patch
Patch30: bz714841-3-fence_agent_metadata.patch
Patch31: bz804169-using_delay_option_can_ends_with_timeout.patch
Patch32: bz804169-2-using_delay_option_can_ends_with_timeout.patch
Patch33: bz806883-attribute_unique_should_be_set_to_0.patch
Patch34: bz806897-fence_ipmilan-return_code_can_be_invalid.patch
Patch35: bz806912-fence_ipmilan_typo.patch
Patch36: bz804805-fence_node_fences_instead_of_unfencing.patch
Patch37: bz752449-1-fence_eaton_snmp_fix_default_power_wait_option_value.patch
Patch38: bz752449-2-fence_eaton_snmp_add_tested_models.patch
Patch39: bz825667-fence_scsi_add_metadata_action_to_man_page.patch
Patch40: bz822507-fix_unique_attributes.patch
Patch41: bz842314-eol_detection.patch
Patch42: bz818337-1-fence_hpblade.patch
Patch43: bz818337-2-fix_distman.patch
Patch44: bz740869-1-fence_ipdu.patch
Patch45: bz740869-2-fence_ipdu.patch
Patch46: bz800650-1-fence_symlink.patch
Patch47: bz800650-2-fence_symlink.patch
Patch48: bz769798-fence_vmware_soap-Faster_fencing.patch
Patch49: bz863568-fence_rhevm_new_api_rhevm.patch
Patch50: bz837174-add_action_metadata_to_rest_of_agents.patch
Patch51: bz863568-2-fence_rhevm_new_api_rhevm.patch
Patch52: bz837174-fence_scsi_allow_action_metadata_stdin.patch
Patch53: bz905478-fence_drac5-regression.patch
Patch54: bz902404-fence_vmware_soap-traceback_when_hostname_cannot_be_resolved.patch
Patch55: bz872308-fix_manual_page_for_ilo3_ilo4.patch
Patch56: bz896603-fence_cisco_ucs-respect_delay.patch
Patch57: bz887349-fence_scsi-add_unfence_to_man_page.patch
Patch58: bz912773-fence_scsi-delay.patch
Patch59: bz886614-fence_apc-firmware5-1.patch
Patch60: bz886614-fence_apc-firmware5-2.patch
Patch61: bz978326-fence_cisco_ucs-cannot_resolve_hostname.patch
Patch62: bz978325-fence_cisco_ucs-incorrect_timeout_used.patch
Patch63: bz917675-1-remove_static_metadata.patch
Patch64: bz917675-2-remove_static_metadata.patch
Patch65: bz959490-password_validation.patch
Patch66: bz870269-fence_ilo4.patch
Patch67: bz981086-fence_ipmilan-lanplus.patch
Patch68: bz912773-2-delay_into_manual_page.patch
Patch69: bz994186-error_in_xml.patch
Patch70: bz886614-2-improve_detection_eol.patch
Patch71: bz978325-fence_cisco_ucs-login_timeout.patch
Patch72: bz997416-fence_bladecenter-login.patch
Patch73: bz1014000-fence_vmware_soap-suds.patch

ExclusiveArch: i686 x86_64

# shipped agents
%global supportedagents apc apc_snmp bladecenter brocade cisco_mds cisco_ucs drac drac5 eaton_snmp eps hpblade kdump ibmblade ifmib ilo ilo_mp intelmodular ipdu ipmilan manual rhevm rsb scsi wti vmware_soap
%global deprecated rsa sanbox2
%global testagents virsh vmware
%global requiresthirdparty egenera

## Runtime deps
Requires: sg3_utils telnet openssh-clients
Requires: pexpect net-snmp-utils
Requires: perl-Net-Telnet python-pycurl pyOpenSSL
Requires: python-suds

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

%prep
%setup -q -n %{name}-%{version}

%patch0 -p1 -b .bz698365.1
%patch1 -p1 -b .bz461948.1
%patch2 -p1 -b .bz461948.2
%patch3 -p1 -b .bz461948.3
%patch4 -p1 -b .bz461948.4
%patch5 -p1 -b .bz461948.5
%patch6 -p1 -b .bz461948.6
%patch7 -p1 -b .bz461948.7
#%patch8 -p1 -b .bz461948.8
# see above why patch8 is not applied!
%patch9 -p1 -b .bz461948.9
%patch10 -p1 -b .bz461948.10
%patch11 -p1 -b .bz461948.11
%patch12 -p1 -b .bzbz718924.1
%patch13 -p1 -b .bz731166.1
%patch14 -p1 -b .bz731166.2
%patch15 -p1 -b .bz732372.1
%patch16 -p1 -b .bz726571.1
%patch17 -p1 -b .bz734429.1
%patch18 -p1 -b .bz739384.1
%patch19 -p1 -b .bz741339-1
%patch20 -p1 -b .bz740484.1
%patch21 -p1 -b .bz742003.1
%patch22 -p1 -b .bz769681.1
%patch23 -p1 -b .bz771211.1
%patch24 -p1 -b .bz771936.1
%patch25 -p1 -b .bz772597.1
%patch26 -p1 -b .bz787706
%patch27 -p1 -b .bz785091
%patch28 -p1 -b .bz714841.1
%patch29 -p1 -b .bz714841.2
%patch30 -p1 -b .bz714841.3
%patch31 -p1 -b .bz804169.1
%patch32 -p1 -b .bz804619.2
%patch33 -p1 -b .bz806883.1
%patch34 -p1 -b .bz806897.1
%patch35 -p1 -b .bz806912.1
%patch36 -p1 -b .bz804805.1
%patch37 -p1 -b .bz752449.1
%patch38 -p1 -b .bz752449.2
%patch39 -p1 -b .bz825667.1
%patch40 -p1 -b .bz822507.1
%patch41 -p1 -b .bz842314.1
%patch42 -p1 -b .bz818337.1
%patch43 -p1 -b .bz818337.2
%patch44 -p1 -b .bz740869.1
%patch45 -p1 -b .bz740869.2
%patch46 -p1 -b .bz800650.1
%patch47 -p1 -b .bz800650.2
%patch48 -p1 -b .bz769798.1
%patch49 -p1 -b .bz863568.1
%patch50 -p1 -b .bz837174.1
%patch51 -p1 -b .bz863568.2
%patch52 -p1 -b .bz837174.2
%patch53 -p1 -b .bz905478.1
%patch54 -p1 -b .bz902404.1
%patch55 -p1 -b .bz872308.1
%patch56 -p1 -b .bz896603.1
%patch57 -p1 -b .bz887349.1
%patch58 -p1 -b .bz912773.1
%patch59 -p1 -b .bz886614.1
%patch60 -p1 -b .bz886614.2
%patch61 -p1 -b .bz978326.1
%patch62 -p1 -b .bz978325.1
%patch63 -p1 -b .bz917675.1
%patch64 -p1 -b .bz917675.2
%patch65 -p1 -b .bz959490.1
%patch66 -p1 -b .bz870269.1
%patch67 -p1 -b .bz981086.1
%patch68 -p1 -b .bz912773.2
%patch69 -p1 -b .bz994186.1
%patch70 -p1 -b .bz886614.2
%patch71 -p1 -b .bz978325.2
%patch72 -p1 -b .bz997416.1
%patch73 -p1 -b .bz1014000.1

%build
./autogen.sh
%{configure} \
	--with-agents='%{supportedagents} %{deprecated} %{testagents} %{requiresthirdparty}'

CFLAGS="$(echo '%{optflags}')" make %{_smp_mflags}

%install
rm -rf %{buildroot}
make -C fence/agents install DESTDIR=%{buildroot}

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

* Wed Jul 18 2013 Marek Grac <mgrac@redhat.com> - 3.0.15-31
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

* Mon Mar 20 2011 Marek Grac <mgrac@redhat.com> - 3.0.12-21
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
