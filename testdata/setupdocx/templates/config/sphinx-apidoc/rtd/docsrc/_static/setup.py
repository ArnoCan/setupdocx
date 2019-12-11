# -*- coding: utf-8 -*-
"""Distribute 'setupdocx', the missing commands for *setup.py*.

Use this file itself as an example.

Additional Args:
    build_docx: 
        Creates Sphinx based documentation with embeded javadoc-style
        API documentation by epydoc. Supported doc types are:
           
            html, singlehtml, dirhtml, epub,
            pdf, latex, latexpdf, latexpdfja, 
            man, 
            devhelp, htmlhelp, qthelp,

   dist_docx: 
       Creates distribution packages for offline documents. Supported
       archive types are:
       
           bzip2, lzma, tar, targz, tgz, zip
           

   install_docx: 
       Install a local copy of the previously build documents in
       accordance to PEP-370. Calls 'create_sphinx.sh' and 'epydoc'.

    build_apiref: 
        Creates Epydoc based documentation of javadoc-style.
        Supported doc types are:
           
            html, 
            pdf, latex, latexpdf, 

   testx: 
       Runs PyUnit tests by discovery of 'tests'.

Additional Options:
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

from setuptools import setup, find_packages  # basically forces CPython as prerequisite


try:
    #
    # optional remote debug only
    #
    from rdbg.start import start_remote_debug  # load a slim bootstrap module
    start_remote_debug()  # check whether '--rdbg' option is present, if so accomplish bootstrap
except:
    pass

#
# setup extension modules
#
from setupdocx import usage, sed

# documents
from setupdocx.build_docx import BuildDocX
from setupdocx.dist_docx import DistDocX
from setupdocx.install_docx import InstallDocX
from setupdocx.build_apiref import BuildApirefX

# unittests
from setuptestx.testx import TestX


__author__ = 'Arno-Can Uestuensoez'
__author_email__ = 'acue_sf2@sourceforge.net'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2015-2019 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__uuid__ = "1ba7bffb-c00b-4691-a3e9-e392f968e437"

__vers__ = [0, 1, 2, ]
__version__ = "%02d.%02d.%03d" % (__vers__[0], __vers__[1], __vers__[2],)


__sdk = False
"""Set by the option "--sdk". Controls the installation environment."""
if '--sdk' in sys.argv:
    __sdk = True
    sys.argv.remove('--sdk')


# required for various interfaces, thus just do it
_mypath = os.path.dirname(os.path.abspath(__file__))
"""Path of this file."""
sys.path.insert(0, os.path.abspath(_mypath))


#--------------------------------------
#
# Package parameters for setuptools
#
#--------------------------------------

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

_packages = find_packages(include=['setupdocx', 'setupdocx.*', 'setup'])
"""Python packages to be installed."""

_packages_sdk = find_packages(include=['setupdocx'])
"""Python packages to be installed."""

_scripts = [
    "bin/rtsetupdocx.py",
    "bin/rtsetupdocx",
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

_install_requires = []
"""prerequired non-standard packages"""


_description = (
    "The 'setupdocx', the missing commands for *setup.py*."
)

_README = os.path.join(os.path.dirname(__file__), 'README.md')
_long_description = open(_README).read() + 'nn'
"""detailed description of this package"""

_classifiers = [
    "Framework :: Setuptools Plugin",
    "Development Status :: 3 - Alpha",
    "Environment :: Console",
    "Environment :: MacOS X",
    "Environment :: Other Environment",
    "Environment :: Win32 (MS Windows)",
    "Environment :: X11 Applications",
    "Framework :: IPython",
    "Intended Audience :: Developers",
    "Intended Audience :: System Administrators",
    "License :: Free To Use But Restricted",
    "License :: OSI Approved :: Artistic License",
    "Natural Language :: English",
    "Operating System :: MacOS :: MacOS X",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: Other OS",
    "Operating System :: POSIX :: BSD :: FreeBSD",
    "Operating System :: POSIX :: BSD :: OpenBSD",
    "Operating System :: POSIX :: Linux",
    "Operating System :: POSIX :: Other",
    "Operating System :: POSIX :: SunOS/Solaris",
    "Operating System :: POSIX",
    "Operating System :: Unix",
    "Programming Language :: C",
    "Programming Language :: C++",
    "Programming Language :: Cython",
    "Programming Language :: Java",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: IronPython",
    "Programming Language :: Python :: Implementation :: Jython",
    "Programming Language :: Python :: Implementation :: PyPy",
    "Programming Language :: Python",
    "Programming Language :: Unix Shell",
    "Topic :: Home Automation",
    "Topic :: Internet",
    "Topic :: Scientific/Engineering :: Interface Engine/Protocol Translator",
    "Topic :: Scientific/Engineering",
    "Topic :: Security",
    "Topic :: Software Development :: Build Tools",
    "Topic :: Software Development :: Code Generators",
    "Topic :: Software Development :: Compilers",
    "Topic :: Software Development :: Debuggers",
    "Topic :: Software Development :: Embedded Systems",
    "Topic :: Software Development :: Interpreters",
    "Topic :: Software Development :: Libraries :: Application Frameworks",
    "Topic :: Software Development :: Libraries :: Java Libraries",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Software Development :: Libraries :: pygame",
    "Topic :: Software Development :: Libraries",
    "Topic :: Software Development :: Pre-processors",
    "Topic :: Software Development :: Testing",
    "Topic :: Software Development",
    "Topic :: System :: Distributed Computing",
    "Topic :: System :: Installation/Setup",
    "Topic :: System :: Logging",
    "Topic :: System :: Monitoring",
    "Topic :: System :: Networking",
    "Topic :: System :: Operating System",
    "Topic :: System :: Shells",
    "Topic :: System :: Software Distribution",
    "Topic :: System :: System Shells",
    "Topic :: System :: Systems Administration",
    "Topic :: Utilities",
]
"""the classification of this package"""

_epydoc_api_patchlist = [
    'shortcuts.html',
    'config.html',
    'os_categorization.html',
]
"""Patch list of Sphinx documents for the insertion of links to API documentation."""

_profiling_components = _mypath + os.sep + 'bin' + os.sep + '*.py ' + _mypath + os.sep + __pkgname__ + os.sep + '*.py'
"""Components to be used for the creation of profiling information for Epydoc."""

_doc_subpath = 'en' + os.path.sep + 'html' + os.path.sep + 'man7'
"""Relative path under the documents directory."""

if __sdk:  # pragma: no cover
    try:
        import sphinx_rtd_theme  # @UnusedImport
    except:
        sys.stderr.write("WARNING: Cannot import package 'sphinx_rtd_theme', cannot create local 'ReadTheDocs' style.")

    _install_requires.extend(
        [
            'pythonids',
            'sphinx >= 1.4',
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
    usage('setup')
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
    """Defines additional text processing.
    """
    
    def __init__(self, *args, **kargs):
        BuildDocX.__init__(self, *args, **kargs)
        self.name = 'setupdocx'

    def join_sphinx_mod_sphinx(self, dirpath):
        """Integrates links for *epydoc* into the the sidebar of the default style,
        and adds links to *sphinx* into the output of *epydoc*. This method needs to 
        be adapted to the actual used theme and templates by the application. Thus
        no generic method is supported, but a call interface. The call is activated
        when the option *--apiref* is set.  

        Adds the following entries before the "Table of Contents" to 
        the *sphinx* document:
        
        * API
          Before "Previous topic", "Next topic"

        .. note::
        
           This method is subject to be changed.
           Current version is hardcoded, see documents.
           Following releases will add customization.
        
        Args:
            **dirpath**:
                Directory path to the file 'index.html'.
        
        Returns;
            None

        Raises:
            None
                
        """
    
        if self.verbose > 0:
            print('\nStart post-create document patches\n')
        
        pt = re.compile(r'(<span class="codelink"><a href=".*?' + str(self.name) + '[^#]*?[#][^"]+">source[&]nbsp;code</a></span>)')

        def rpfunc(match):
            rp  = r'[<span class="codelink"><a href="../api.html#" target="_top">api</a></span>]&nbsp;'
            rp += match.group(1)
            return rp
        
        for flst in os.walk(dirpath + '/epydoc/'):
            for fn in flst[2]:
                if fn[-5:] == '.html':
                    if self.verbose > 0:
                        print("process: " + str(fn))
                    sed(flst[0]+os.path.sep+fn, pt, rpfunc)


class install_docx(InstallDocX):
    """Defines the package name.
    """

    def __init__(self, *args, **kargs):
        InstallDocX.__init__(self, *args, **kargs)
        self.name = 'setupdocx'


class dist_docx(DistDocX):
    """Defines the package name.
    """

    def __init__(self, *args, **kargs):
        DistDocX.__init__(self, *args, **kargs)
        self.name = 'setupdocx'


class build_apiref(BuildApirefX):
    """Defines the package name.
    """

    def __init__(self, *args, **kargs):
        BuildApirefX.__init__(self, *args, **kargs)
        self.name = 'setupdocx'


class testx(TestX):
    """Defines the package name.
    """

    def __init__(self, *args, **kargs):
        TestX.__init__(self, *args, **kargs)
        self.name = 'setuplib'


#
# see setup.py for remaining parameters
#
setup(
    author=_author,
    author_email=_author_email,
    classifiers=_classifiers,
    cmdclass={
        'build_apiref': build_apiref,
        'build_docx': build_docx,
        'install_docx': install_docx,
        'dist_docx': dist_docx,
        'testx': testx,
    },
    description=_description,
    download_url=_download_url,
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
    print("Help on usage extensions by " + str(_name))
    print("   --help-" + str(_name))
    print()

sys.exit(0)
