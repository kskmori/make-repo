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
Version: 4.0.10
Release: 1%{?alphatag:.%{alphatag}}%{?dist}
License: GPLv2+ and LGPLv2+
Group: System Environment/Base
URL: http://sourceware.org/cluster/wiki/
Source0: fence-agents/%{name}-%{version}.tar.xz

%if 0%{?fedora}
%global supportedagents alom apc apc_snmp bladecenter brocade cisco_mds cisco_ucs drac5 eaton_snmp eps hpblade ibmblade ifmib ilo ilo_mp intelmodular ipdu ipmilan kdump ldom lpar rhevm rsa rsb scsi vmware_soap wti
%global testagents virsh
%global allfenceagents fence-agents-alom fence-agents-apc fence-agents-apc-snmp fence-agents-bladecenter fence-agents-brocade fence-agents-cisco-mds fence-agents-cisco-ucs fence-agents-drac5 fence-agents-eaton-snmp fence-agents-eps fence-agents-hpblade fence-agents-ibmblade fence-agents-ifmib fence-agents-ilo2 fence-agents-ilo-mp fence-agents-intelmodular fence-agents-ipdu fence-agents-ipmilan fence-agents-kdump fence-agents-ldom fence-agents-lpar fence-agents-rhevm fence-agents-rsa fence-agents-rsb fence-agents-scsi fence-agents-vmware-soap fence-agents-wti
%endif

%if 0%{?rhel}
%global supportedagents apc apc_snmp bladecenter brocade cisco_mds cisco_ucs drac5 eaton_snmp eps hpblade ibmblade ifmib ilo ilo_mp intelmodular ipdu ipmilan kdump rhevm rsb scsi vmware_soap wti
%global testagents virsh
%global allfenceagents fence-agents-apc fence-agents-apc-snmp fence-agents-bladecenter fence-agents-brocade fence-agents-cisco-mds fence-agents-cisco-ucs fence-agents-drac5 fence-agents-eaton-snmp fence-agents-eps fence-agents-hpblade fence-agents-ibmblade fence-agents-ifmib fence-agents-ilo2 fence-agents-ilo-mp fence-agents-intelmodular fence-agents-ipdu fence-agents-ipmilan fence-agents-kdump fence-agents-rhevm fence-agents-rsb fence-agents-scsi fence-agents-vmware-soap fence-agents-wti
%endif

## Setup/build bits

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

# Build dependencies
BuildRequires: perl 
BuildRequires: glibc-devel
BuildRequires: gnutls-utils
BuildRequires: libxslt
BuildRequires: python pexpect python-pycurl python-suds python-requests
BuildRequires: perl(Net::Telnet) net-snmp-utils
%if 0%{?fedora}
BuildRequires: perl(Pod::MinimumVersion)
%endif

%prep
%setup -q -n %{name}-%{version}

%build
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

%if 0%{?fedora}
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
%endif

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
Requires: perl sg3_utils
Obsoletes: fence-agents
%description scsi
The fence-agents-scsi package contains fence agent for SCSI persisent reservations
%files scsi
%defattr(-,root,root,-)
%{_sbindir}/fence_scsi
%{_sbindir}/fence_scsi_check
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

%changelog
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


