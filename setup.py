# -*- coding: utf-8 -*-
"""Distribute 'setupdocx', the missing documentation commands
for *setup.py*.

The commands of the package *setupdocx* itself are 
defined as custom classes to be used before it's 
installation.

The file *setup.py* itself serves as an example for 
custom classes. The application should normally use
the created entry points instead.

Adds commands:

    build_docx: 
        Creates Sphinx based documentation including 
        inline API documentation. 
        Optional embeded javadoc-style API reference by epydoc.

        Default builder:

            sphinx - sphinx-apidoc + sphinx-build

        Supported doc types are:
           
            # primary formats:
            html, singlehtml, pdf, epub, man,
            
            # secondary formats:
            dirhtml, 
            latex, latexpdf, latexpdfja, 
            devhelp, htmlhelp, qthelp,

    build_apidoc: 
        Creates API documentation from the inline comments of the source code.

        Default builder:

            sphinx-apidoc

        Supported doc types are:
           
            rst

    build_apiref: 
        Creates Epydoc based documentation of javadoc-style.

        Default builder:

            epydoc

        Supported doc types are:
           
            # primary formats:
            html, pdf,
            
            # secondary formats:
            pdflatex, latexpdf, auto,
            latex, tex, dvi, ps  

    dist_docx: 
       Creates distribution packages for offline documents. 
       
       Supported archive types are:
       
           bzip2, lzma, tar, targz, tgz, zip,
           gzip
           
       Supported package types are:
       
           rpm, deb, pkg, apk, pacman

    install_docx:
       Install a local copy of the previously build documents in
       accordance to PEP-370. Calls 'create_sphinx.sh' and 'epydoc'.

Supports *setuplib* family commands:
    testx:
        Regression tests.

Additional local options:
   --sdk:
       Requires sphinx, epydoc, and dot-graphics.

   --no-install-requires: 
       Suppresses installation dependency checks,
       requires appropriate PYTHONPATH.

   --offline: 
       Sets online dependencies to offline, or ignores online
       dependencies.

   --help-setupdocx: 
       Displays this help.

"""
from __future__ import absolute_import
from __future__ import print_function

import os
import sys
import re

import setuptools


try:
    #
    # optional remote debug only
    #
    from rdbg import start        # load a slim bootstrap module
    start.start_remote_debug()    # check whether '--rdbg' option is present, if so accomplish bootstrap
except:
    pass


import yapyutils.help
import yapyutils.files.utilities

#
# setup extension modules
#
import setupdocx

# documents
from setupdocx.build_docx import BuildDocX
from setupdocx.dist_docx import DistDocX
from setupdocx.install_docx import InstallDocX
from setupdocx.build_apiref import BuildApirefX
from setupdocx.build_apidoc import BuildApidocX

# unittests
from setuptestx.testx import TestX


__author__ = 'Arno-Can Uestuensoez'
__author_email__ = 'acue_sf2@sourceforge.net'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2015-2019 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__uuid__ = "1ba7bffb-c00b-4691-a3e9-e392f968e437"

__vers__ = [0, 1, 21, ]
__version__ = "%02d.%02d.%03d" % (__vers__[0], __vers__[1], __vers__[2],)
__release__ = "%d.%d.%d" % (__vers__[0], __vers__[1], __vers__[2],) + '-rc0'
__status__ = 'beta'


__sdk = False
"""Set by the option "--sdk". Controls the installation environment."""
if '--sdk' in sys.argv:
    __sdk = True
    sys.argv.remove('--sdk')


# required for various interfaces, thus just do it
_mypath = os.path.dirname(os.path.abspath(__file__))
"""Path of this file."""
sys.path.insert(0, os.path.abspath(_mypath))


#-------------------------------------------------------
#
# Package parameters for setuptools - see also setup.cfg
#
#-------------------------------------------------------

_name = 'setupdocx'
"""package name"""

__pkgname__ = "setupdocx"
"""package name"""

_version = "%d.%d.%d" % (__vers__[0], __vers__[1], __vers__[2],)
"""assembled version string"""

_author = __author__
"""author of the package"""

_author_email = __author_email__
"""author's email """

_license = __license__
"""license"""

#_packages = setuptools.find_packages('setupdocx')
_packages = [
    'setupdocx',
    ]
"""Python packages to be installed."""

#_packages = setuptools.find_packages('setupdocx')
_packages = [
    'setupdocx',
    ]
"""Python packages to be installed."""

_scripts = [
]
"""Scripts to be installed."""

_package_data = {
    'setupdocx': [
        'README.md', 'ArtisticLicense20.html', 'licenses-amendments.txt',
    ],
}
"""Provided data of the package."""

_url = 'https://sourceforge.net/projects/setupdocx/'
"""URL of this package"""

# _download_url="https://github.com/ArnoCan/setupdocx/"
_download_url = "https://sourceforge.net/projects/setupdocx/files/"


_install_requires = [
    'setuptestx',
    ]
"""prerequired non-standard packages"""


_description = (
    "Support of documentation commands and extensions for setuptools / distutils."
)

_README = os.path.join(os.path.dirname(__file__), 'README.md')
_long_description = '\n' + open(_README).read() + '\n'
"""detailed description of this package"""

_profiling_components = _mypath + os.sep + 'bin' + os.sep + '*.py ' + _mypath + os.sep + __pkgname__ + os.sep + '*.py'
"""Components to be used for the creation of profiling information for Epydoc."""

_doc_subpath = 'en' + os.path.sep + 'html' + os.path.sep + 'man7'
"""Relative path under the documents directory."""

if __sdk:  # pragma: no cover
    try:
        import sphinx_rtd_theme  # @UnusedImport
    except:
        sys.stderr.write(
            "WARNING: Cannot import package 'sphinx_rtd_theme', cannot create local 'ReadTheDocs' style.")

    _install_requires.extend(
        [
            'setuptestx',
            'pythonids',
            'sphinx >= 1.6',
            'epydoc >= 3.0',
        ]
    )

    _packages = _packages_sdk

_test_suite = "tests.CallCase"

__no_install_requires = False
if '--no-install-requires' in sys.argv:
    __no_install_requires = True
    sys.argv.remove('--no-install-requires')

__offline = False
if '--offline' in sys.argv:
    __offline = True
    __no_install_requires = True
    sys.argv.remove('--offline')

# Help on addons.
if '--help-setupdocx' in sys.argv:
    yapyutils.help.usage('setup')
    sys.exit(0)

if __no_install_requires:
    print("#")
    print("# Changed to offline mode, ignore install dependencies completely.")
    print("# Requires appropriate PYTHONPATH.")
    print("# Ignored dependencies are:")
    print("#")
    for ir in _install_requires:
        print("#   " + str(ir))
    print("#")
    _install_requires = []


class build_docx(BuildDocX):
    """For test and debug of setupdocx itself.
    Applicable for custom classes.
    
    Use the entry points for standard application. 
    """
    
    def __init__(self, *args, **kargs):
        #
        # attribute examples
        #
        # self.name = _name
        # self.copyright = __copyright__
        # self.status = __status__
        # self.release = __release__
        #
        BuildDocX.__init__(self, *args, **kargs)


class install_docx(InstallDocX):
    """For test and debug of setupdocx itself.
    Applicable for custom classes.
    
    Use the entry points for standard application. 
    """

    def __init__(self, *args, **kargs):
        #
        # attribute examples
        #
        # self.name = _name
        # self.copyright = __copyright__
        # self.status = __status__
        # self.release = __release__
        #
        InstallDocX.__init__(self, *args, **kargs)


class dist_docx(DistDocX):
    """For test and debug of setupdocx itself.
    Applicable for custom classes.
    
    Use the entry points for standard application. 
    """

    def __init__(self, *args, **kargs):
        #
        # attribute examples
        #
        # self.name = _name
        # self.copyright = __copyright__
        # self.status = __status__
        # self.release = __release__
        #
        DistDocX.__init__(self, *args, **kargs)


class build_apidoc(BuildApidocX):
    """For test and debug of setupdocx itself.
    Applicable for custom classes.
    
    Use the entry points for standard application. 
    """

    def __init__(self, *args, **kargs):
        #
        # attribute examples
        #
        # self.name = _name
        # self.copyright = __copyright__
        # self.status = __status__
        # self.release = __release__
        #
        BuildApidocX.__init__(self, *args, **kargs)


class build_apiref(BuildApirefX):
    """For test and debug of setupdocx itself.
    Applicable for custom classes.
    
    Use the entry points for standard application. 
    """

    def __init__(self, *args, **kargs):
        #
        # attribute examples
        #
        # self.name = _name
        # self.copyright = __copyright__
        # self.status = __status__
        # self.release = __release__
        #
        BuildApirefX.__init__(self, *args, **kargs)


class testx(TestX):
    """For test and debug of setupdocx itself.
    Applicable for custom classes.
    
    Use the entry points for standard application. 
    """

    def __init__(self, *args, **kargs):
        #
        # attribute examples
        #
        # self.name = _name
        # self.copyright = __copyright__
        # self.status = __status__
        # self.release = __release__
        #
        TestX.__init__(self, *args, **kargs)


#
# see setup.py for remaining parameters
#
setuptools.setup(
    author=_author,
    author_email=_author_email,
    cmdclass={
        'build_apidoc': build_apidoc,  # for bootstrap of setuplib - not required for applications
        'build_apiref': build_apiref,  # for bootstrap of setuplib - not required for applications
        'build_docx':   build_docx,    # for bootstrap of setuplib - not required for applications
        'install_docx': install_docx,  # for bootstrap of setuplib - not required for applications
        'dist_docx':    dist_docx,     # for bootstrap of setuplib - not required for applications
        'testx':        testx,         # for bootstrap of setuplib - not required for applications
    },
    description=_description,
    download_url=_download_url,
    entry_points={
        'distutils.commands': [
            'build_apidoc = setupdocx.build_apidoc:BuildApidocX',
            'build_apiref = setupdocx.build_apiref:BuildApirefX',
            'build_docx = setupdocx.build_docx:BuildDocX',
            'install_docx = setupdocx.install_docx:InstallDocX',
            'dist_docx = setupdocx.dist_docx:DistDocX',
        ]
    },
    install_requires=_install_requires,
    license=_license,
    long_description=_long_description,
    name=_name,
    package_data=_package_data,
    packages=_packages,
    scripts=_scripts,
    url=_url,
    version=_version,
    zip_safe=False,
)

if '--help' in sys.argv:
    print()
    print("Help on provided package extensions by " + str(_name))
    print("   --help-" + str(_name))
    print()

sys.exit(0)
