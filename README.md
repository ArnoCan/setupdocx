setupdocx
=========

The ‘setupdocx‘ provides a control layer for continuous documentation by the simplified creation, packaging, and installation of documentation.
The provided commands are distributed as entry points and optional base classes for further customization into *setup.py* - setuptools / distutils. 

The current release supports the following commands:

* **build_docx** - Enhanced documentation.

  Supports the first integration of *Epydoc* into *Sphinx* for combined *Javadoc* style 
  documentation of *Python* and *Java*.
  Manages arbitrary document templates for the supported builder,
  supports multiple builds with arbitrary document layouts, designs, and patched contents.

* **install_docx** - Installs local documentation.

  Installs documentation locally from build directory, see PEP-0370. 

* **dist_docx** - Documentation packaging. 

  Creates distribution packages for documentation.

* **build_apidoc** - Standalone Generator for API Documentation 

  Extracts the inline documentation only.
  Manages arbitrary document templates for the supported builder,
  supports multiple builds with arbitrary document layouts, designs, and patched contents.

* **build_apiref** - Standalone Generator for API Reference  

  Extracts the inline documentation as JavaDoc style API reference.
  Manages arbitrary document templates for the supported builder,
  supports multiple builds with arbitrary document layouts, designs, and patched contents.

For more extensions refer to the online documentation.

**Online documentation**:

* https://setupdocx.sourceforge.io/

**Runtime-Repository**:

* PyPI: https://pypi.org/project/setupdocx/

  Install: *pip install setupdocx*, see also section 'Install' of the online documentation.


**Downloads**:

* sourceforge.net: https://sourceforge.net/projects/setupdocx/files/

* bitbucket.org: https://bitbucket.org/acue/setupdocx

* github.com: https://github.com/ArnoCan/setupdocx/

* pypi.org: https://pypi.org/project/setupdocx/


Project Data
------------

* PROJECT: 'setupdocx'

* MISSION: Command extension of *setup.py* for multi-platform and documentation deployments.

* VERSION: 00.01

* RELEASE: 00.01.021

* STATUS: beta

* AUTHOR: Arno-Can Uestuensoez

* COPYRIGHT: Copyright (C) 2019 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez

* LICENSE: Artistic-License-2.0 + Forced-Fairplay-Constraints

Concepts and enumeration values are migrated from the 

* *UnifiedSessionsManager* (C) 2008 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez.  

Sphinx
------
Tested with Sphinx-1.7 on Python2.7.14, and Python3.6.5.

Runtime Environment
-------------------
For a comprehensive list refer to the documentation.

**Python Syntax Support**

*  Python2.7, and Python3

**Python Implementation Support**

*  CPython, IPython, IronPython, Jython, and PyPy

**OS on Server, Workstation, Laptops, Virtual Machines, and Containers**

* Linux: AlpineLinux, ArchLinux, CentOS, Debian, Fedora, Gentoo, OpenSUSE, Raspbian, RHEL, Slackware, SLES, Ubuntu, ...  

* BSD: DragonFlyBSD, FreeBSD, NetBSD, OpenBSD, GhostBSD, TrueOS, NomadBSD

* OS-X: Snow Leopard

* Windows: Win10, Win8.1, Win7, WinXP, Win2019, Win2016, Win2012, Win2008, Win2000

* WSL-1.0: Alpine, Debian, KaliLinux, openSUSE, SLES, Ubuntu

* Cygwin

* UNIX: Solaris10, Solaris11

* Minix: Minix3

* ReactOS

**Network and Security**

* Network Devices: OpenWRT

* Security: KaliLinux, pfSense

**OS on Embedded Devices**

* RaspberryPI: ArchLinux, CentOS, OpenBSD, OpenWRT, Raspbian

* ASUS-TinkerBoard: Armbian

Current Release
---------------

REMARK:
   Currently tested by application to the other projects of the author.
   So for now no package tests defined.

Major Changes:

* Initial version.

Issues:

* Current release supports *shell* only and is released for *bash*, so
  safe to use on *POSIX* platforms.
  So may should on *Windows-10* et.al. / *NT-10.0*, in any case in *WSL*.
  General support for *Windows* platforms is coming soon - so the full scale
  of platforms will be supported.

ToDo:

* make all templates completely generic for any package - some like 'man' contain hardcoded names for setupdocx
* Add optional gzip to man pages.
* Add rpm, deb, apk.

Known Issues:

* Not yet

