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
Version: 4.0.11
Release: 27%{?alphatag:.%{alphatag}}%{?dist}.5
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
URL: http://sourceware.org/cluster/wiki/
Source0: https://fedorahosted.org/releases/f/e/fence-agents/%{name}-%{version}.tar.xz
Patch0: bz1072564-1-add_ssl_secure_and_ssl_insecure.patch
Patch1: bz1072564-2-add_ssl_secure_and_ssl_insecure.patch
Patch2: backward-rename_fence_scsi_check_to_pl.patch
Patch3: bz1121122-1-fence_ilo_ssh.patch
Patch4: bz1140921-1-fence_zvm.patch
Patch5: bz1111597-1-fence_rsb.patch
Patch6: bz1148762-1-fence_wti_eol.patch
Patch7: bz1153059-1-fence_vmware_soap-fail_usage.patch
Patch8: bz1111599-1-fence_cisco_and_soap_logout.patch
Patch9: bz1162092-1-fix_ssl_secure.patch
Patch10: bz1140921-2-fence_zvm.patch
Patch11: bz1140921-3-fence_zvm.patch
Patch12: bz1121122-2-broken_syslog.patch
Patch13: bz1121122-3-eol_changed.patch
Patch14: bz1121122-3.5-delay_test.patch
Patch15: bz1121122-4-symlink_ilo34_ssh.patch
Patch16: bz1121122-5-symlink_ilo34_ssh.patch
Patch17: bz1173178-1-rewrite_fence_zvmip.patch
Patch18: tests-01.patch
Patch19: tests-02.patch
Patch20: bz1199970-fence_ilo_support_tls10.patch
Patch21: bz1203877-fence_ipmilan-default_cipher.patch
Patch22: bz1214359-1-fence_compute.patch
Patch23: bz1214359-2-fence_compute.patch
Patch24: bz1214359-3-fence_compute.patch
Patch25: bz1214359-4-fence_compute.patch
Patch26: test-01-fix_xml_metadata.patch
Patch27: bz1213571-fence_scsi-add_monitor.patch
Patch28: bz1214919-fence_scsi-already_on.patch
Patch29: bz1145769-fence_rhevm-cookies_auth.patch
Patch30: bz1165591-fence_cisco_ucs-https.patch
Patch31: bz1196068-fence_kdump-add_monitor.patch
Patch32: bz1196068-2-fence_kdump-add_monitor.patch
Patch33: bz1196068-3-fence_kdump-add_monitor.patch
Patch34: bz1196068-4-fence_kdump-add_monitor.patch
Patch35: bz1207982-fence2rng-quotes.patch
Patch36: bz1171732-1-fence_emerson.patch
Patch37: bz1171732-2-fence_emerson.patch
Patch38: bz1171732-3-fence_emerson.patch
Patch39: bz1188750-0-fence_zvmip-improve_usage_of_resources.patch
Patch40: bz1188750-fence_zvmip-improve_usage_of_resources.patch
Patch41: bz1214359-5-fence_compute.patch
Patch42: bz1214359-6-fence_compute.patch
Patch43: bz1216997-support_for_hp_superdome.patch
Patch44: bz1102727-fence_mpath.patch
Patch45: bz1102727-2-duplicate_getopt.patch
Patch46: bz1214359-7-fence_compute_xml_test.patch
Patch47: bz1214522-port_as_ip.patch
Patch48: bz1102727-2-fence_mpath.patch
Patch49: bz1243485-1-fence_scsi-force-on.patch
Patch50: bz1243485-2-fence_scsi-monitor.patch
Patch51: bz1250586-list_status.patch
Patch52: bz1214522-2-port_as_ip.patch
Patch53: bz1214522-3-port_as_ip.patch
Patch54: bz1185329-fence_rsa.patch
Patch55: bz1251491-none_as_state.patch
Patch56: bz1214522-4-port_as_ip.patch
Patch57: bz1214522-5-port_as_ip.patch
Patch58: bz1102727-3-fence_mpath.patch
Patch59: bz1250586-2-list_status.patch
Patch60: bz1243485-3-fence_scsi_check.patch
Patch61: bz1241648-fence_ipmilan_password_verbose.patch
Patch62: bz1257137-1-fence_ipmilan_regression.patch
Patch63: bz1257137-2-fence_ipmilan_regression.patch
Patch64: bz1256908-fence_ilo-tls_negotiation.patch
Patch65: bz1259319-fence_apc_v6.patch
Patch66: bz1257137-3-fence_ipmilan_regression.patch
Patch67: bz1274432-fence_brocade-fix_incorrect_return.patch
Patch68: bz1265426-1-fence_scsi_hard.patch
Patch69: bz1265426-2-fence_scsi_hard.patch
Patch70: bz1265426-3-fence_scsi_hard.patch
Patch71: bz1265426-4-fence_scsi_hard.patch
Patch72: bz1299577-fence_compute.patch
Patch73: bz1303698-fence_cisco_ucs-Obtain-status-of-device-from-differe.patch
Patch74: bz1303698-2-fence_cisco_ucs-Add-missing-as-off.patch
Patch75: bz1303698-3-fence_cisco_ucs-Update-XML-metadata.patch
Patch76: bz1303698-4-fence_cisco_ucs-Update-XML-metadata.patch

%if 0%{?rhel}
%global supportedagents apc apc_snmp bladecenter brocade cisco_mds cisco_ucs compute drac5 eaton_snmp emerson eps hpblade ibmblade ifmib ilo ilo_moonshot ilo_mp ilo_ssh intelmodular ipdu ipmilan mpath kdump rhevm rsa rsb scsi vmware_soap wti
%global allfenceagents fence-agents-apc fence-agents-apc-snmp fence-agents-bladecenter fence-agents-brocade fence-agents-cisco-mds fence-agents-cisco-ucs fence-agents-compute fence-agents-drac5 fence-agents-eaton-snmp fence-agents-emerson fence-agents-eps fence-agents-hpblade fence-agents-ibmblade fence-agents-ifmib fence-agents-ilo2 fence-agents-ilo-moonshot fence-agents-ilo-mp fence-agents-ilo-ssh fence-agents-intelmodular fence-agents-ipdu fence-agents-ipmilan fence-agents-mpath fence-agents-kdump fence-agents-rhevm fence-agents-rsa fence-agents-rsb fence-agents-scsi fence-agents-vmware-soap fence-agents-wti
%ifarch s390x
%global testagents virsh zvm
%else
%global testagents virsh
%endif
%endif

## Setup/build bits

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

# Build dependencies
BuildRequires: glibc-devel
BuildRequires: gnutls-utils
BuildRequires: libxslt
BuildRequires: python pexpect python-pycurl python-suds python-requests
BuildRequires: net-snmp-utils
BuildRequires: autoconf automake libtool

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1 -b .bz1072564-1
%patch1 -p1 -b .bz1072564-2
%patch2 -p1 -b .backward-fence_scsi_check_rename
%patch3 -p1 -b .bz1121122-1
%patch4 -p1 -b .bz1140921-1
%patch5 -p1 -b .bz1111597-1
%patch6 -p1 -b .bz1148762-1
%patch7 -p1 -b .bz1153059-1
%patch8 -p1 -b .bz1111599-1
%patch9 -p1 -b .bz1162092-1
%patch10 -p1 -b .bz1140921-2
%patch11 -p1 -b .bz1140921-3
%patch12 -p1 -b .bz1121122-2
%patch13 -p1 -b .bz1121122-3
%patch14 -p1 -b .bz1121122-3.5
%patch15 -p1 -b .bz1121122-4
%patch16 -p1 -b .bz1121122-5
%patch17 -p1 -b .bz1173178-1
%patch18 -p1 -b .tests-01
%patch19 -p1 -b .tests-02
%patch20 -p1 -b .bz1199970-1
%patch21 -p1 -b .bz1203877-1
%patch22 -p1 -b .bz1214359-1
%patch23 -p1 -b .bz1214359-2
%patch24 -p1 -b .bz1214359-3
%patch25 -p1 -b .bz1214359-4
%patch26 -p1 -b .test-01-fix_xml_metadata.patch
%patch27 -p1 -b .bz1213571
%patch28 -p1 -b .bz1214919
%patch29 -p1 -b .bz1145769
%patch30 -p1 -b .bz1165591
%patch31 -p1 -b .bz1196068
%patch32 -p1 -b .bz1196068-2
%patch33 -p1 -b .bz1196068-3
%patch34 -p1 -b .bz1196068-4
%patch35 -p1 -b .bz1207982
%patch36 -p1 -b .bz1171732.1
%patch37 -p1 -b .bz1171732.2
%patch38 -p1 -b .bz1171732.3
%patch39 -p1 -b .bz1188750.0
%patch40 -p1 -b .bz1188750
%patch41 -p1 -b .bz1214359-5
%patch42 -p1 -b .bz1214359-6
%patch43 -p1 -b .bz1216997
%patch44 -p1 -b .bz1102727
%patch45 -p1 -b .bz1102727-2
%patch46 -p1 -b .bz1214359-7
%patch47 -p1 -b .bz1214522
%patch48 -p1 -b .bz1102727-2
%patch49 -p1 -b .bz1243485-1
%patch50 -p1 -b .bz1243485-2
%patch51 -p1 -b .bz1250586
%patch52 -p1 -b .bz1214522-2
%patch53 -p1 -b .bz1214522-3
%patch54 -p1 -b .bz1185329
%patch55 -p1 -b .bz1251491
%patch56 -p1 -b .bz1214522-4
%patch57 -p1 -b .bz1214522-5
%patch58 -p1 -b .bz1102727-3
%patch59 -p1 -b .bz1250586-2
%patch60 -p1 -b .bz1243485-3
%patch61 -p1 -b .bz1241648
%patch62 -p1 -b .bz1257137-1
%patch63 -p1 -b .bz1257137-2
%patch64 -p1 -b .bz1256908
%patch65 -p1 -b .bz1259319
%patch66 -p1 -b .bz1257137-3
%patch67 -p1 -b .bz1274432-1
%patch68 -p1 -b .bz1265426-1
%patch69 -p1 -b .bz1265426-2
%patch70 -p1 -b .bz1265426-3
%patch71 -p1 -b .bz1265426-4
%patch72 -p1 -b .bz1299577
%patch73 -p1 -b .bz1303698
%patch74 -p1 -b .bz1303698-2
%patch75 -p1 -b	.bz1303698-3
%patch76 -p1 -b	.bz1303698-4

%build
./autogen.sh
%{configure} --with-agents='%{supportedagents} %{testagents}'
CFLAGS="$(echo '%{optflags}')" make %{_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

## tree fix up
# fix libfence permissions
chmod 0755 %{buildroot}%{_datadir}/fence/*.py
# remove docs
rm -rf %{buildroot}/usr/share/doc/fence-agents

%clean
rm -rf %{buildroot}

%description
Red Hat Fence Agents is a collection of scripts to handle remote
power management for several devices.

%package common
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Common utilities for fence agents
Requires: python pexpect
%description common
Red Hat Fence Agents is a collection of scripts and libraries to handle remote power management for various devices.
%files common
%defattr(-,root,root,-)
%doc doc/COPYING.* doc/COPYRIGHT doc/README.licence
%{_datadir}/fence
%{_datadir}/cluster
%{_datadir}/fence/fencing.py
%{_datadir}/fence/fencing_snmp.py

%package all
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agents
Requires: %{allfenceagents}
%ifarch i686 x86_64
Requires: fence-virt
%endif
Provides: fence-agents = %{version}-%{release}
Obsoletes: fence-agents < 3.1.13
%description all
Red Hat Fence Agents is a collection of all supported fence agents.
%files all

%if 0%{?fedora}
%package alom
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for SUN ALOM
Requires: fence-agents-common >= %{version}-%{release}
Requires: telnet openssh-clients
Obsoletes: fence-agents
%description alom
Red Hat Fence Agents
%files alom
%defattr(-,root,root,-)
%{_sbindir}/fence_alom
%{_mandir}/man8/fence_alom.8*
%endif

%package apc
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for APC devices
Requires: fence-agents-common >= %{version}-%{release}
Requires: telnet openssh-clients
Obsoletes: fence-agents
%description apc
The fence-agents-apc package contains a fence agent for APC devices that are accessed via telnet or SSH. 
%files apc 
%defattr(-,root,root,-)
%{_sbindir}/fence_apc
%{_mandir}/man8/fence_apc.8*

%package apc-snmp
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for APC devices (SNMP)
Requires: fence-agents-common >= %{version}-%{release}
Requires: net-snmp-utils
Obsoletes: fence-agents
%description apc-snmp
The fence-agents-apc-snmp package contains a fence agent for APC devices that are accessed via the SNMP protocol. 
%files apc-snmp
%defattr(-,root,root,-)
%{_sbindir}/fence_apc_snmp
%{_mandir}/man8/fence_apc_snmp.8*

%package bladecenter
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for IBM BladeCenter 
Requires: fence-agents-common >= %{version}-%{release}
Requires: telnet openssh-clients
Obsoletes: fence-agents
%description bladecenter
The fence-agents-bladecenter package contains a fence agent for IBM BladeCenter devices that are accessed via telnet or SSH.
%files bladecenter
%defattr(-,root,root,-)
%{_sbindir}/fence_bladecenter
%{_mandir}/man8/fence_bladecenter.8*

%package brocade
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for HP Brocade
Requires: fence-agents-common >= %{version}-%{release}
Requires: telnet openssh-clients
Obsoletes: fence-agents
%description brocade
The fence-agents-brocade package contains a fence agent for HP Brocade devices that are accessed via telnet or SSH.
%files brocade
%defattr(-,root,root,-)
%{_sbindir}/fence_brocade
%{_mandir}/man8/fence_brocade.8*

%package cisco-mds
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for Cisco MDS 9000 series
Requires: fence-agents-common >= %{version}-%{release}
Requires: net-snmp-utils
Obsoletes: fence-agents
%description cisco-mds
The fence-agents-cisco-mds package contains a fence agent for Cisco MDS 9000 series devices that are accessed via the SNMP protocol.
%files cisco-mds
%defattr(-,root,root,-)
%{_sbindir}/fence_cisco_mds
%{_mandir}/man8/fence_cisco_mds.8*

%package cisco-ucs
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for Cisco UCS series
Requires: fence-agents-common >= %{version}-%{release}
Requires: pycurl
Obsoletes: fence-agents
%description cisco-ucs
The fence-agents-cisco-ucs package contains a fence agent for Cisco UCS series devices that are accessed via the SNMP protocol.
%files cisco-ucs
%defattr(-,root,root,-)
%{_sbindir}/fence_cisco_ucs
%{_mandir}/man8/fence_cisco_ucs.8*

%package compute
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for Nova compute nodes
Requires: fence-agents-common >= %{version}-%{release}
Requires: python-requests
Obsoletes: fence-agents
%description compute
The fence-agents-compute package contains a fence agent for Nova compute nodes.
%files compute
%defattr(-,root,root,-)
%{_sbindir}/fence_compute
%{_mandir}/man8/fence_compute.8*

%package drac5
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for Dell DRAC 5
Requires: fence-agents-common >= %{version}-%{release}
Requires: telnet openssh-clients
Obsoletes: fence-agents
%description drac5
The fence-agents-drac5 package contains a fence agent for Dell DRAC 5 series devices that are accessed via telnet or SSH.
%files drac5
%defattr(-,root,root,-)
%{_sbindir}/fence_drac5
%{_mandir}/man8/fence_drac5.8*

%package eaton-snmp
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for Eaton network power switches
Requires: fence-agents-common >= %{version}-%{release}
Requires: net-snmp-utils
Obsoletes: fence-agents
%description eaton-snmp
The fence-agents-eaton-snmp package contains a fence agent for Eaton network power switches that are accessed via the SNMP protocol.
%files eaton-snmp
%defattr(-,root,root,-)
%{_sbindir}/fence_eaton_snmp
%{_mandir}/man8/fence_eaton_snmp.8*

%package emerson
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for Emerson devices (SNMP)
Requires: fence-agents-common >= %{version}-%{release}
Obsoletes: fence-agents
%description emerson
The fence-agents-emerson package contains a fence agent for Emerson devices that are accessed via the SNMP protocol.
%files emerson
%defattr(-,root,root,-)
%{_sbindir}/fence_emerson
%{_mandir}/man8/fence_emerson.8*

%package eps
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for ePowerSwitch 8M+ power switches
Requires: fence-agents-common >= %{version}-%{release}
Obsoletes: fence-agents
%description eps
The fence-agents-eps package contains a fence agent for ePowerSwitch 8M+ power switches that are accessed via the HTTP(s) protocol.
%files eps
%defattr(-,root,root,-)
%{_sbindir}/fence_eps
%{_mandir}/man8/fence_eps.8*

%package hpblade
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for HP BladeSystem devices
Requires: fence-agents-common >= %{version}-%{release}
Requires: telnet openssh-clients
Obsoletes: fence-agents
%description hpblade
The fence-agents-hpblade package contains a fence agent for HP BladeSystem devices that are accessed via telnet or SSH.
%files hpblade
%defattr(-,root,root,-)
%{_sbindir}/fence_hpblade
%{_mandir}/man8/fence_hpblade.8*

%package ibmblade
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for IBM BladeCenter
Requires: fence-agents-common >= %{version}-%{release}
Requires: net-snmp-utils
Obsoletes: fence-agents
%description ibmblade
The fence-agents-ibmblade package contains a fence agent for IBM BladeCenter devices that are accessed via the SNMP protocol.
%files ibmblade
%defattr(-,root,root,-)
%{_sbindir}/fence_ibmblade
%{_mandir}/man8/fence_ibmblade.8*

%package ifmib
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for devices with IF-MIB interfaces
Requires: fence-agents-common >= %{version}-%{release}
Requires: net-snmp-utils
Obsoletes: fence-agents
%description ifmib
The fence-agents-ifmib package contains a fence agent for IF-MIB interfaces that are accessed via the SNMP protocol.
%files ifmib
%defattr(-,root,root,-)
%{_sbindir}/fence_ifmib
%{_mandir}/man8/fence_ifmib.8*

%package ilo2
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for HP iLO2 devices
Requires: fence-agents-common >= %{version}-%{release}
Requires: gnutls-utils
Obsoletes: fence-agents
%description ilo2
The fence-agents-ilo2 package contains a fence agent for HP iLO2 devices that are accessed via the HTTP(s) protocol.
%files ilo2
%defattr(-,root,root,-)
%{_sbindir}/fence_ilo
%{_sbindir}/fence_ilo2
%{_mandir}/man8/fence_ilo.8*
%{_mandir}/man8/fence_ilo2.8*

%package ilo-moonshot
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for HP iLO Moonshot devices
Requires: telnet openssh-clients
Requires: fence-agents-common >= %{version}-%{release}
Obsoletes: fence-agents
%description ilo-moonshot
The fence-agents-ilo-moonshot package contains a fence agent for HP iLO Moonshot devices that are accessed via telnet or SSH.
%files ilo-moonshot
%defattr(-,root,root,-)
%{_sbindir}/fence_ilo_moonshot
%{_mandir}/man8/fence_ilo_moonshot.8*

%package ilo-mp
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for HP iLO MP devices
Requires: fence-agents-common >= %{version}-%{release}
Requires: telnet openssh-clients
Obsoletes: fence-agents
%description ilo-mp
The fence-agents-ilo-mp package contains a fence agent for HP iLO MP devices that are accessed via telnet or SSH.
%files ilo-mp
%defattr(-,root,root,-)
%{_sbindir}/fence_ilo_mp
%{_mandir}/man8/fence_ilo_mp.8*

%package ilo-ssh
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for HP iLO devices via SSH
Requires: fence-agents-common >= %{version}-%{release}
Requires: telnet openssh-clients
Obsoletes: fence-agents
%description ilo-ssh
The fence-agents-ilo-ssh package contains a fence agent for HP iLO devices that are accessed via SSH.
%files ilo-ssh
%defattr(-,root,root,-)
%{_sbindir}/fence_ilo_ssh
%{_mandir}/man8/fence_ilo_ssh.8*
%{_sbindir}/fence_ilo3_ssh
%{_mandir}/man8/fence_ilo3_ssh.8*
%{_sbindir}/fence_ilo4_ssh
%{_mandir}/man8/fence_ilo4_ssh.8*

%package intelmodular
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for devices with Intel Modular interfaces
Requires: fence-agents-common >= %{version}-%{release}
Requires: net-snmp-utils
Obsoletes: fence-agents
%description intelmodular
The fence-agents-intelmodular package contains a fence agent for Intel Modular interfaces that are accessed via the SNMP protocol.
%files intelmodular
%defattr(-,root,root,-)
%{_sbindir}/fence_intelmodular
%{_mandir}/man8/fence_intelmodular.8*

%package ipdu
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for IBM iPDU network power switches
Requires: fence-agents-common >= %{version}-%{release}
Requires: net-snmp-utils
Obsoletes: fence-agents
%description ipdu
The fence-agents-ipdu package contains a fence agent for IBM iPDU network power switches that are accessed via the SNMP protocol.
%files ipdu
%defattr(-,root,root,-)
%{_sbindir}/fence_ipdu
%{_mandir}/man8/fence_ipdu.8*

%package ipmilan
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for devices with IPMI interface
Requires: fence-agents-common >= %{version}-%{release}
Requires: /usr/bin/ipmitool
Obsoletes: fence-agents
%description ipmilan
The fence-agents-ipmilan package contains a fence agent for devices with IPMI interface. 
%files ipmilan
%defattr(-,root,root,-)
%{_sbindir}/fence_ipmilan
%{_mandir}/man8/fence_ipmilan.8*
%{_sbindir}/fence_idrac
%{_mandir}/man8/fence_idrac.8*
%{_sbindir}/fence_ilo3
%{_mandir}/man8/fence_ilo3.8*
%{_sbindir}/fence_ilo4
%{_mandir}/man8/fence_ilo4.8*
%{_sbindir}/fence_imm
%{_mandir}/man8/fence_imm.8*

%package mpath
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for reservations over Device Mapper Multipath
Requires: fence-agents-common >= %{version}-%{release}
Requires: device-mapper-multipath
Obsoletes: fence-agents
%description mpath
The fence-agents-mpath package contains fence agent for SCSI persisent reservation over Device Mapper Multipath
%files mpath
%defattr(-,root,root,-)
%{_sbindir}/fence_mpath
%{_mandir}/man8/fence_mpath.8*

%package kdump
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for use with kdump crash recovery service
Requires: fence-agents-common >= %{version}-%{release}
Obsoletes: fence-agents
%description kdump
The fence-agents-kdump package contains a fence agent for use with kdump crash recovery service.
%files kdump
%defattr(-,root,root,-)
%{_sbindir}/fence_kdump
%{_libexecdir}/fence_kdump_send
%{_mandir}/man8/fence_kdump.8*
%{_mandir}/man8/fence_kdump_send.8*

%if 0%{?fedora}
%package ldom
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for Sun LDom virtual machines
Requires: fence-agents-common >= %{version}-%{release}
Requires: telnet openssh-clients
Obsoletes: fence-agents
%description ldom
The fence-agents-ldom package contains a fence agent for Sun LDom devices that are accessed via telnet or SSH.
%files ldom
%defattr(-,root,root,-)
%{_sbindir}/fence_ldom
%{_mandir}/man8/fence_ldom.8*
%endif

%if 0%{?fedora}
%package lpar
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for IBM LPAR
Requires: fence-agents-common >= %{version}-%{release}
Requires: telnet openssh-clients
Obsoletes: fence-agents
%description lpar
The fence-agents-lpar package contains a fence agent for IBM LPAR devices that are accessed via telnet or SSH.
%files lpar
%defattr(-,root,root,-)
%{_sbindir}/fence_lpar
%{_mandir}/man8/fence_lpar.8*
%endif

%package rhevm
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for RHEV-M
Requires: fence-agents-common >= %{version}-%{release}
Obsoletes: fence-agents
%description rhevm
The fence-agents-rhevm package contains a fence agent for RHEV-M via REST API
%files rhevm
%defattr(-,root,root,-)
%{_sbindir}/fence_rhevm
%{_mandir}/man8/fence_rhevm.8*

%package rsa
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for IBM RSA II
Requires: fence-agents-common >= %{version}-%{release}
Requires: telnet openssh-clients
Obsoletes: fence-agents
%description rsa
The fence-agents-rsa package contains a fence agent for IBM RSA II devices that are accessed via telnet or SSH.
%files rsa
%defattr(-,root,root,-)
%{_sbindir}/fence_rsa
%{_mandir}/man8/fence_rsa.8*

%package rsb
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for Fujitsu RSB
Requires: fence-agents-common >= %{version}-%{release}
Requires: telnet openssh-clients
Obsoletes: fence-agents
%description rsb
The fence-agents-rsb package contains a fence agent for Fujitsu RSB devices that are accessed via telnet or SSH.
%files rsb
%defattr(-,root,root,-)
%{_sbindir}/fence_rsb
%{_mandir}/man8/fence_rsb.8*

%if 0
%package sanbox2
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for QLogic SANBox2 FC switches
Requires: fence-agents-common >= %{version}-%{release}
Requires: telnet
Obsoletes: fence-agents
%description sanbox2
The fence-agents-sanbox2 package contains a fence agent for QLogic SANBox2 switches that are accessed via telnet.
%files sanbox2
%defattr(-,root,root,-)
%{_sbindir}/fence_sanbox2
%{_mandir}/man8/fence_sanbox2.8*
%endif

%package scsi
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for SCSI persisent reservations
Requires: sg3_utils fence-agents-common >= %{version}-%{release}
Obsoletes: fence-agents
%description scsi
The fence-agents-scsi package contains fence agent for SCSI persisent reservations
%files scsi
%defattr(-,root,root,-)
%{_sbindir}/fence_scsi
%{_datadir}/cluster/fence_scsi_check.pl
%{_datadir}/cluster/fence_scsi_check
%{_datadir}/cluster/fence_scsi_check_hardreboot
%{_mandir}/man8/fence_scsi.8*

%package virsh
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for virtual machines based on libvirt
Requires: fence-agents-common >= %{version}-%{release}
Requires: openssh-clients /usr/bin/virsh
Obsoletes: fence-agents
%description virsh
The fence-agents-virsh package contains a fence agent for virtual machines that are accessed via SSH.
%files virsh
%defattr(-,root,root,-)
%{_sbindir}/fence_virsh
%{_mandir}/man8/fence_virsh.8*

%package vmware-soap
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for VMWare with SOAP API v4.1+
Requires: fence-agents-common >= %{version}-%{release}
Requires: python-suds python-requests
Obsoletes: fence-agents
%description vmware-soap
The fence-agents-vmware-soap package contains a fence agent for VMWare with SOAP API v4.1+
%files vmware-soap
%defattr(-,root,root,-)
%{_sbindir}/fence_vmware_soap
%{_mandir}/man8/fence_vmware_soap.8*

%package wti
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for WTI Network power switches
Requires: fence-agents-common >= %{version}-%{release}
Requires: telnet openssh-clients
Obsoletes: fence-agents
%description wti
The fence-agents-wti package contains a fence agent for WTI network power switches that are accessed via telnet or SSH.
%files wti
%defattr(-,root,root,-)
%{_sbindir}/fence_wti
%{_mandir}/man8/fence_wti.8*

%ifarch s390x
%package zvm
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
Summary: Fence agent for z/VM hypervisors
Requires: fence-agents-common >= %{version}-%{release}
Requires: telnet openssh-clients
Obsoletes: fence-agents
%description zvm
The fence-agents-zvm package contains a fence agent for z/VM hypervisors
%files zvm
%defattr(-,root,root,-)
%{_sbindir}/fence_zvmip
%{_mandir}/man8/fence_zvmip.8*
%endif

%changelog
* Tue Feb 09 2016 Marek Grac <mgrac@redhat.com> - 4.0.11-27.5
- fence_cisco_ucs: Change endpoint for 'status' action
  Resolves: rhb#1303698

* Tue Feb 02 2016 Marek Grac <mgrac@redhat.com> - 4.0.11-27.4
- fence_cisco_ucs: Change endpoint for 'status' action
  Resolves: rhb#1303698

* Wed Jan 20 2016 Marek Grac <mgrac@redhat.com> - 4.0.11-30
- fence_compute: Replace with current implementation
  Resolves: rhbz#1299577

* Wed Dec 16 2015 Marek Grac <mgrac@redhat.com> - 4.0.11-27.2
- fence_scsi: Add fence_scsi_check_hardreboot
  Resolves: rhbz#bz1292071

* Mon Oct 26 2015 Marek Grac <mgrac@redhat.com> - 4.0.11-27
- fence_brocade: Fix return status in get_power_status
  Resolves: rhbz#1274431

* Thu Sep 17 2015 Marek Grac <mgrac@redhat.com> - 4.0.11-26
- fence_ipmilan: Fix -i attribute
  Resolves: rhbz#1257137

* Mon Sep 14 2015 Marek Grac <mgrac@redhat.com> - 4.0.11-25
- fence_apc: Support for v6.x
  Resolves: rhbz#1259319

* Wed Sep 02 2015 Marek Grac <mgrac@redhat.com> - 4.0.11-24
- fence_ipmilan: Add removed attributes -i & timeout
  Resolves: rhbz#1257137
- fence_ipmilan: Do not print password in verbose mode
  Resolves: rhbz#1241648
- fence_ilo: Negotiation of TLS1.0 is more automatic
  Resolves: rhbz#1256908

* Mon Aug 17 2015 Marek Grac <mgrac@redhat.com> - 4.0.11-23
- fence_scsi: Fix watchdog script broken by more strict 'monitor'
  Resolves: 1243485

* Wed Aug 12 2015 Marek Grac <mgrac@redhat.com> - 4.0.11-21
- fence_mpath: Fix unfencing after non-cluster reboot
  Resolves: 1102727
- manual pages now describe 'list-status' properly

* Tue Aug 11 2015 Marek Grac <mgrac@redhat.com> - 4.0.11-20
- fencing: Fix place where --plug + --port-as-ip are tested
  Resolves: rhbz#1214522

* Mon Aug 10 2015 Marek Grac <mgrac@redhat.com> - 4.0.11-19
- fencing: do not fail when state is None
  Resolves: rhbz#1251491

* Wed Aug 05 2015 Marek Grac <mgrac@redhat.com> - 4.0.11-18
- fence_rsa: Fix login issue
  Resolves: rhbz#1185329
- fencing: support for list-status
  Resolves: rhbz#1250586
- fencing: Fix support for --port-as-ip
  Resolves: rhbz#1214522

* Thu Jul 16 2015 Marek Grac <mgrac@redhat.com> - 4.0.11-17
- fence_scsi: Improve monitoring and add option to force ON
  Resolves: rhbz#1243485

* Mon Jun 29 2015 Marek Grac <mgrac@redhat.com> - 4.0.11-16
- fence_compute: Agent cleanup
  Resolves: rhbz#1214359
- fence_hpblade: Add support for HP Integrity Superdome
  Resolves: rhbz#1216997
- fence_zvmip: Add --missing-as-off and change monitor/status actions
  Resolves: rhbz#1188750
- fence_mpath: new fence agent
  Resolves: rhbz#1102727
- fencing: Option --port-as-ip
  Resolves: rhbz#1214522

* Mon Jun 22 2015 Marek Grac <mgrac@redhat.com> - 4.0.11-15
- fence_zvmip: Connection timeout issues
  Resolves: rhbz#1188750

* Thu Jun 18 2015 Marek Grac <mgrac@redhat.com> - 4.0.11-14
- fence_rhevm: Add authentication via cookies
  Resolves: rhbz#1145769
- fence_ilo_moonshot: New fence agent
  Resolves: rhbz#1152917
- fence_emerson: New fence agent
  Resolves: rhbz#1171732
- fence_rsa: New fence agent
  Resolves: rhbz#1185329

* Wed Jun 17 2015 Marek Grac <mgrac@redhat.com> - 4.0.11-13
- fence_scsi: Add monitor operation
  Resolves: rhbz#1213571
- fence_scsi: Force unfence if any of paths is off
  Resolves: rhbz#1214919
- fence_cisco_ucs: Fix https:// prefix with --ssl-(in)secure
  Resolves: rhbz#1165591
- fence_kdump: Add monitor operation
  Resolves: rhbz#1196068
- fence2rng: Fix problem with quotes
  Resolves: rhbz#1207982

* Mon Jun 08 2015 Marek Grac <mgrac@redhat.com> - 4.0.11-12
- New fence agent fence_compute
  Resolves: rhbz#1214359

* Wed Mar 25 2015 Marek Grac <mgrac@redhat.com> - 4.0.11-11
- fence_ipmilan: Unset default cipher
  Resolves: rhbz#1203877
- fence_ilo2: Add --tls1.0
  Resolves: rhbz#1199970
- update scripts so 'make check' is working again

* Mon Jan 05 2015 Marek Grac <mgrac@redhat.com> - 4.0.11-10
- fence_zvmip: Add fence_zvmip ported to fencing library
  Resolves: rhbz#1173178

* Mon Dec 01 2014 Marek Grac <mgrac@redhat.com> - 4.0.11-9
- fence_ilo_ssh: Fix EOL issue, syslog problem and add fence_ilo_[34]_ssh symlink
  Resolves: rhbz#1121122

* Wed Nov 12 2014 Marek Grac <mgrac@redhat.com> - 4.0.11-8
- fence_zvm: Add 'monitor' support for fence_zvmip
  Resolves: rhbz#1140921

* Mon Nov 10 2014 Marek Grac <mgrac@redhat.com> - 4.0.11-7
- HTTPS connection do not validate certificate (introduced with rebase)
  Resolves: rhbz#1162092

* Thu Oct 16 2014 Marek Grac <mgrac@redhat.com> - 4.0.11-6
- fence_cisco_ucs and fence_vmware_soap should logout even in case of failure
  Resolves: rhbz#1111599
- fence_vmware_soap: Fix issue with import of fail_usage
  Resolves: rhbz#1153059

* Thu Oct 02 2014 Marek Grac <mgrac@redhat.com> - 4.0.11-5
- fence_wti: Fix problem with EOL introduced by rebase
  Resolves: rhbz#1148762
- fence_rsb: Fix issue with new firmware 
  Resolves: rhbz#1111597

* Sat Sep 20 2014 Fabio M. Di Nitto <fdinitto@redhat.com> - 4.0.11-4
- add initial support for IBM z/VM
  Resolves: rhbz#1140921

* Mon Sep 15 2014 Marek Grac <mgrac@redhat.com> - 4.0.11-3
- temporary removes fence-agents-amt because amtterm is missing

* Wed Sep 03 2014 Marek Grac <mgrac@redhat.com> - 4.0.11-2
- add a fence agents for AMT and iLO-ssh
  Resolves: rhbz#1121122 rhbz#1107439

* Wed Sep 03 2014 Marek Grac <mgrac@redhat.com> - 4.0.11-1
- rebase of fence agents
  Resolves: rhbz#1120682
- INFO: fence_scsi_check.pl is now a python script

* Wed Mar 19 2014 Marek Grac <mgrac@redhat.com> - 4.0.2-21
- fencing: Add --ssl-secure and --ssl-insecure for fence_vmware_soap
  Resolves: rhbz#1072564

* Fri Mar 07 2014 Marek Grac <mgrac@redhat.com> - 4.0.2-20
- fencing: Add --ssl-secure and --ssl-insecure for fence_vmware_soap
  Resolves: rhbz#1072564

* Wed Mar 05 2014 Marek Grac <mgrac@redhat.com> - 4.0.2-19
- fencing: Add --ssl-secure and --ssl-insecure
  Resolves: rhbz#1072564

* Thu Feb 27 2014 Fabio M. Di Nitto <fdinitto@redhat.com> - 4.0.2-18
- fence_vmware_soap: fix short/long option parsing traceback
  Resolves: rhbz#1018780

* Wed Feb 26 2014 Fabio M. Di Nitto <fdinitto@redhat.com> - 4.0.2-17
- Fix fence-agents-* Requires on proper fence-agents-common and silence
  suds error
  Resolves: rhbz#1018780

* Thu Feb 20 2014 Fabio M. Di Nitto <fdinitto@redhat.com> - 4.0.2-16
- Allow ssl connections to disable TLS negotiation with "notls" option.
  Resolves: rhbz#990539

* Wed Feb 19 2014 Marek Grac <mgrac@redhat.com> - 4.0.2-15
- Fix dependencies issues

* Mon Feb 17 2014 Marek Grac <mgrac@redhat.com> - 4.0.2-14
- fence_vmware_soap: Fix unexpected exception
  Resolves: rhbz#1018780
- nss_wrapper was replaced by gnutls-cli
  Resolves: rhbz#990539

* Wed Jan 29 2014 Marek Grac <mgrac@redhat.com> - 4.0.2-13
- fencing: Do not use public key if identity file is not defined
  Resolves: rhbz#1048843
- fence_vmware_soap: Add support for --delay option
  Resolves: rhbz#1057299
- fence_wti: Add support for named groups (also for firmware 1.43)
  Resolves: rhbz#1022536

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 4.0.2-12
- Mass rebuild 2014-01-24

* Thu Jan 23 2014 Marek Grac <mgrac@redhat.com> - 4.0.2-11
- fencing: Ensure validity of XML metadata using Relax NG 
  Resolves: rhbz#1022529

* Thu Jan 23 2014 Marek Grac <mgrac@redhat.com> - 4.0.2-10
- fix default action for fabric fencing agents
  Resolves: rhbz#1021392
- modify key generation in fence_scsi to support pacemaker/corosync cluster
  Resolves: rhbz#994466

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 4.0.2-9
- Mass rebuild 2013-12-27

* Wed Nov 20 2013 Marek Grac <mgrac@redhat.com> - 4.0.2-8
- fence-agents-all now includes fence-virt which is not available everywhere
  Resolves: rhbz#1028940

* Tue Nov 12 2013 Marek Grac <mgrac@redhat.com> - 4.0.2-7
- fence-agents-all now includes fence-virt
  Resolves: rhbz#1028940

* Mon Nov 04 2013 Marek Grac <mgrac@redhat.com> - 4.0.2-6
- fencing: Ensure validity of XML metadata using Relax NG 
  Resolves: rhbz#1022529
- fencing: Fix invalid use of options[".."]
  Resolves: rhbz#1022533
- fence_brocade: Add fence agent
  Resolves: rhbz#1021392

* Mon Nov 04 2013 Marek Grac <mgrac@redhat.com> - 4.0.2-5
- fence_vmware_soap: Report if user privileges are not enough for given operation
  Resolves: rhbz#1018780
- fence_wti: Add support for named groups
  Resolves: rhbz#1022536
- fence_rsb: Update regular expression to match newer firmware version
  Resolves: rhbz#1022538

* Mon Nov 04 2013 Marek Grac <mgrac@redhat.com> - 4.0.2-4
- fence_vmware_soap: Disable cache in SUDS library to resolve SELinux problems
  Resolves: rhbz#1022528
- fencing: Add information that operation 'unfence' should be run automatically after start of the cluster
  Resolves: rhbz#1012994
- Aligned to upstream 4.0.4

* Mon Sep 02 2013 Marek Grac <mgrac@redhat.com> - 4.0.2-3
- fence_bladecenter: Fix telnet login failure
- fence_brocade: Rewrite to fencing library
- fencing_snmp: Fix 'KeyError --a'
- fence_scsi: Fix XML metadata
- fence_scsi: Add a documentation of "delay"
- fence_ilo2: Unable to login when password contains "

* Tue Jul 30 2013 Marek Grac <mgrac@redhat.com> - 4.0.2-2
- new upstream release

* Tue Jul 09 2013 Marek Grac <mgrac@redhat.com> - 4.0.1-1
- new upstream release

* Mon Jun 24 2013 Marek Grac <mgrac@redhat.com> - 4.0.0-5
- fence-agents-all should provide fence-agent for clean update path

* Wed Apr 03 2013 Marek Grac <mgrac@redhat.com> - 4.0.0-4
- minor changes in spec file

* Thu Mar 21 2013 Marek Grac <mgrac@redhat.com> - 4.0.0-3
- minor changes in spec file

* Mon Mar 18 2013 Marek Grac <mgrac@redhat.com> - 4.0.0-2
- minor changes in spec file

* Mon Mar 11 2013 Marek Grac <mgrac@redhat.com> - 4.0.0-1
- new upstream release
- introducing subpackages


