#-*- coding: utf-8 -*-
"""installs created documetation
"""
from __future__ import absolute_import
from __future__ import print_function

import os
import sys
import shutil
import re

import distutils.cmd

import setupdocx
import setuplib

import yapyutils.files.utilities as utilities 
import yapyutils.files.finder as finder 
import yapyutils.config.capabilities


__author__ = 'Arno-Can Uestuensoez'
__author_email__ = 'acue_sf2@sourceforge.net'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2019 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__uuid__ = "1ba7bffb-c00b-4691-a3e9-e392f968e437"


class SetupDocXInstallError(setupdocx.SetupDocXError):
    pass


class InstallDocX(distutils.cmd.Command):
    """Compile and install documentation."""

    description = 'Install documentation locally from build directory.'
    user_options = [
        ('build-dir=',      None, "installation source, "
                                  "default 'build', "
                                  "resulting in the created document 'build/doc/<docname>'"),
        ('clean',           None, "removes the previous document, be careful with this and check the target twice,"
                                  "no additional confirmation is requested, default: False"),
        ('debug',           None, "debug flag"),
        ('docname=',        None, "document name, could be different from '--name' "
                                  "used as the input and the output name of the document, "
                                  "default: 'self.name'"),
        ('doctype=',        None, "document type to install, default 'html' only"),
        ('force',           None, "Force to processing by deactivating non-essential checks, "
                                  "suppresses validation, "
                                  "default: False"),
        ('forcedir',        None, "Force to pack directories, in case of single document types "
                                  "such as PDF too. Else the types PDF, and EPUB are compressed "
                                  "without the containing directory. The name of single-file documents is "
                                  "changed when archive name, version, etc. are provided. "
                                  "Default: False"),
        ('name=',           None, "package name, changes 'self.name', "
                                  "default: 'self.name'"),
        ('no-exec',        'n',   "print only, do not execute"),
        ('target-dir=',     None, "installation target directory, PEP-370, user data directory, "
                                  "default '/user/data/' + 'doc/en/html/man3'"),
        ('verbose',         None, "verbose flag"),
    ]

    #: The provided capabilities of the builder and it's components.
    capabilities = yapyutils.config.capabilities.Capability(
        {
            "components": {
                "default":          "sphinx-apidoc",  # adjusted in dependence of the 'doctype'
                "sphinx":           "sphinx-apidoc",  # extract rst for sphinx-build
                "sphinx-apidoc":    "sphinx-apidoc",  # extract rst for sphinx-build
            },
            "sphinx-apidoc": {
                "metatypes": [
                    "rst",                            # reStructuredText
                ],
                "doctypes": [
                    "html",                           # reStructuredText
                ]
            },
            "defaults": {                             # DEFAULTS: updated by capabilities.json
                "builder":          "default",        # False
                "builder_path":     None,             # search(<conf-dir>, <configdir>, <docsrc>/conf)/call_apidoc.sh
                "build_dir":        "build/",         # build/
                "build_reldir":     "sphinx/apidoc/", # apidoc/sphinx/
                "clean":            None,             # False
                "config_path":      None,             # <docsource>/conf/
                "docname":          None,             # attribute of derived class, see self.name
                "docsource":        "docsrc/",        # docsrc/
                "doctype":          None,             # html
                "indexsrc":         "index.rst",      # 'index.rst'
                "name":             None,             # attribute of derived class, see self.name
                "release":          None,             # 
                "srcdir":           None,             # list/tuple(<name>/,)
                "template":         "",               # default template, default:=alabaster
                "version":          None,             # 
            }
        }
    )

    doctypes_supported = (
        "html",  # simple HTML with defaults for sphinx and epydoc
        "singlehtml", 
        "epub", 
        "pdf", 
        "latexpdf", 
        "latexpdfja",
        "man",
        "mangz",

        # "devhelp",
        # "htmlhelp",
        # "qthelp",
    )

    doctypes_suffix = {
        "epub" : '.epub', 
        "pdf": '.pdf', 
        "latexpdf": '.pdf', 
        "latexpdfja": '.pdf',
        "mangz": '.gz',
    }

    # Sets default values for call options
    # Foreseen to be set by the derived class
    # in 'setup.py'.
    docx_defaults = {             # DEFAULTS:
        'apidoc': False,          # False
        'apiref': False,          # False
        'build_apidoc': None,     # search(<conf-dir>, <configdir>, <docsrc>/conf)/call_apidoc.sh
        'build_apiref': None,     # search(<conf-dir>, <configdir>, <docsrc>/conf)/call_apiref.sh
        'build_doc': None,        # search(<conf-dir>, <configdir>, <docsrc>/conf)/call_doc.sh
        'build_dir': 'build/',    # build/
        'build_reldir': 'apidoc/sphinx/', # apidoc/sphinx/
        'clean': None,            # False
        'conf_dir':  None,        # <docsource>/conf/
        'docname': None,          # attribute of derived class, see self.name
        'docsource': 'docsrc/',   # docsrc/
        'doctype': None,          # html
        'indexsrc': 'index.rst',  # 'index.rst'
        'name': None,             # attribute of derived class, see self.name
        'release': None,          # <year>.<month>.<day>
        'srcdir': None,           # list/tuple(<name>/,)
        'version': None,          # 
    }  #: default values for command line parameters


    def initialize_options(self):
        self.build_dir = None
        self.clean = None
        self.debug = None
        self.docname = None
        self.doctype = None
        self.force = None
        self.forcedir = None
        self.name = None
        self.no_exec = None
        self.target_dir = None
    
    def finalize_options(self):
        # quick-and-dirty hack to resolve the inconsistency of
        # global and local verbose values of distutils
        try:
            _v_opts = self.distribution.get_option_dict('dist_docx')['verbose'][1]
            if _v_opts:
                self.verbose += 1
        except:
            # fallback to the slightly erroneous behavior when the interface 
            # of distutils changes
            pass

        if self.forcedir == None:
            self.forcedir = False
        else:
            self.forcedir = True

        if self.force == None:
            self.force = False
        else:
            self.force = True

        if self.no_exec != None:
            self.no_exec = True

        if self.clean == None:
            self.clean = False
        else:
            self.clean = True

        if self.name == None:
            self.name = self.distribution.metadata.name

        if self.docname == None:
            self.docname = self.docx_defaults.get('docname')
            if self.docname == None:
                self.docname = self.name

#         if self.docname == None:
#             self.docname = self.name

        if self.doctype == None:
            self.doctype = "html"
        else:
            if self.doctype not in self.doctypes_supported:
                raise SetupDocXInstallError(
                    "doctype = " + str(self.doctype) + " - supported: " + str(self.doctypes_supported))

        if self.build_dir == None:
            self.build_dir = os.path.normpath("build/doc/"+str(self.docname))

        if self.target_dir == None:
            if self.doctype in ('man', 'mangz',):
                self.target_dir = "man/"
            
            else:
                self.target_dir = "doc/en/"

            if sys.platform in ('win32'):
                self.target_dir = os.path.normpath(
                    os.path.expandvars("%APPDATA%/Python/" + self.target_dir))
            else:
                self.target_dir = os.path.normpath(
                    os.path.expanduser("~/.local/" + self.target_dir))
        else:
            self.target_dir = os.path.normpath(self.target_dir) 


    def run(self):
        """Installs created document from *build* directory to target directory.
        """
        if self.no_exec:
            if self.clean and os.path.exists(self.target_dir):
                print("shutil.rmtree(%s)" % (str(self.target_dir)))
            print(
                "shutil.copytree(%s, %s)" %(str(self.build_dir), str(self.target_dir)))
            
        else:

            #
            # common single-file documents: pdf, epub
            #
            if self.doctype in ('pdf', 'epub',):
                if self.forcedir:
                    _t = self.target_dir + os.sep + str(self.docname)
                    if self.clean and os.path.exists(_t):
                        shutil.rmtree(_t)
                    shutil.copytree(self.build_dir, _t)

                else:
                    if not os.path.exists(self.target_dir):
                        os.makedirs(self.target_dir)
                    
                    for f in os.listdir(self.build_dir):
                        shutil.copy(self.build_dir + os.sep + f, self.target_dir)

            #
            # man pages: man, man.gz
            #
            elif self.doctype in ('man', 'mangz',):
                if self.forcedir:
                    _t = self.target_dir + os.sep + str(self.docname)
                    if self.clean and os.path.exists(_t):
                        shutil.rmtree(_t)
                    shutil.copytree(self.build_dir, _t)
                else:
                    for f in os.listdir(self.build_dir):
                        _src = self.build_dir + os.sep + f
                        # transform flat files into man structure
                        
                        if self.doctype == 'man':
                            _sec = re.sub(r'^.*[.]', '', f)
                        elif self.doctype == 'mangz':
                            _sec = re.split(r'^(.*[.])([^.]+)(.gz)$', f)[2]

                        _secpath = self.target_dir + os.sep + 'man' + str(_sec)
                        if not os.path.exists(_secpath):
                            os.makedirs(_secpath)
                        shutil.copy(_src, _secpath)

            #
            # directory based documents: html, singlehtml, helpdev, helpqt, ... 
            #
            else:
                _t = self.target_dir + os.sep + str(self.docname)
                if self.clean and os.path.exists(_t):
                    shutil.rmtree(_t)
                shutil.copytree(self.build_dir, _t)

                print("# "+str(self.build_dir))
                print("#   from        : "+str(self.build_dir))
                print("#   to          : "+str(_t))
                print("#   display with: firefox -P preview.simple " + str(_t) + "/index.html")
                return
            
        print("# "+str(self.build_dir))
        print("#   from        : "+str(self.build_dir))
        print("#   to          : "+str(self.target_dir))

