#-*- coding: utf-8 -*-
"""Creates extended API reference by *epydoc*.
"""
from __future__ import absolute_import
from __future__ import print_function

import sys
import os
import re
import shutil
import time
import json

import distutils.cmd
import setupdocx
import setuplib

import yapyutils.files.utilities as utilities 
import yapyutils.files.finder as finder 
import yapyutils.config.capabilities
import yapyutils.releases

__author__ = 'Arno-Can Uestuensoez'
__author_email__ = 'acue_sf2@sourceforge.net'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2019 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__uuid__ = "45167c30-3261-4a38-9de4-d7151348ba48"


class SetuplibBuildApirefXError(setupdocx.SetupDocXError):
    pass


class BuildApirefX(distutils.cmd.Command):
    """Create API reference."""

    description = 'Create API reference.'
    user_options = [
        ('build-apiref=',   None, "the name of the called script for the creation of the API reference,"
                                  " default: <conf-dir>/call_apiref.sh"),
        ('build-dir=',      None, "the name of the build directory,"
                                  " default: build/"),
        ('clean',           None, "removes the cached previous build, "
                                  "default: False"),
        ('conf-dir=',       None, "directory containing the configuration files, "
                                  "default: <docsource>/conf/"),
        ('debug',           'd',   "raises level of debug traces of current context, supports repetition, "
                                   "each raises the debug level of the context by one"),
        ('docname=',        None, "document output name, default: attribute of derived class self.name"),
        ('docsource=',      None, "the name of the document source directory, default: docsrc/"),
        ('doctype=',        None, "document type to create, default: 'html'"),
        ('help-doctypes',   None,  "List available document formats"),
        ('name=',           None, "the name of the package, default: metadata"),
        ('no-exec',        'n',   "print only, do not execute"),
        ('no-exec-max',    'N',   "print only the complete call stack, do not execute"),
        ('rawdoc',         'r',   "Uses the generated documents by 'apiref' only, currently the only option."),
        ('release=',        None, "The release of the package"),
        ('srcdir=',         None,  "Source directory"),
        ('verbose',         'v',   "raises verbosity of current context, supports repetition, "
                                   "each raises the command verbosity level of the context "),
        ('verbose-ext=',   'x',   "verbose for external tools, integer value, higher values raise the level"),
        ('version=',        None, "The version of the package, "
                                  "default: attribute of derived class self.distribution.metadata.version"),
    ]

    #: The provided capabilities of the builder and it's components.
    capabilities = yapyutils.config.capabilities.Capability(
        {
            "components": {
                "default":          "epydoc",
                "epydoc":           "epydoc",
            },
            "epydoc": {
                "doctypes": [
                    # primary format types
                    "html",           # HTML: --html
                    "pdf",            # PDF:  --pdf
            
                    # secondary format types
                    "auto",           # PDF:  --pdf --pdfdriver=auto
                    "pdflatex",       # PDF:  --pdf --pdfdriver=pdflatex
                    "latexpdf",       # PDF:  --pdf --pdfdriver=latex
                    "latex",          # PDF:  --latex
                    "tex",            # TeX:  --tex
                    "text",           # text: --text
                    "dvi",            # DVI:  --dvi
                    "ps",             # PS:   --ps
                ]
            },
            "defaults": {             # DEFAULTS:
                'build_apiref': None, # search(<conf-dir>, <configdir>, <docsrc>/conf)/call_apiref.sh
                'build_dir': None,    # build/
                'clean': None,        # False
                'conf_dir':  None,    # <docsource>/conf/
                'docname': None,      # from metadata
                'docsource': None,    # docsrc/
                'doctype': None,      # html
                'name': None,         # from metadata
                'release': None,      # <year>.<month>.<day>
                'srcdir': None,       # list/tuple(<name>/,)
                'version': None,      # 
            }
        }
    )

    def initialize_options(self):
        self.build_apiref = None
        self.build_dir = None
        self.clean = None
        self.conf_dir = None
        self.debug = None
        self.docname = None
        self.docsource = None
        self.doctype = None
        self.help_doctypes = None
        self.name = None
        self.no_exec = None
        self.no_exec_max = None
        self.rawdoc = None
        self.release = None
        self.srcdir = None
        self.verbose_ext = ''
        self.version = None
        
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
        
        if self.help_doctypes != None:
            print("Known document types:")
            for dt in  sorted(self.doctypes_supported):
                print("  --doctype=%s" % (dt))
            sys.exit(0)

        if self.docsource == None:
            self.docsource = self.docx_defaults.get('docsource')
            if self.docsource == None:
                self.docsource = 'docsrc'
        if self.docsource and not os.path.exists(self.docsource):
            raise SetuplibBuildApirefXError("missing docsrc:" + str(self.docsource))
        
        if self.conf_dir == None:
            self.conf_dir = self.docx_defaults.get('conf_dir')
            if not self.conf_dir:
                self.conf_dir = self.docsource + os.sep + 'conf'
        if not os.path.exists(self.conf_dir):
            raise SetuplibBuildApirefXError("missing confdir:" + str(self.conf_dir))

        if self.build_dir == None:
            self.build_dir = self.docx_defaults.get('conf_dir')
            if not self.build_dir:
                self.build_dir = 'build'

        # location of shared call scripts
        self.searchpath = (
            self.conf_dir, 
            self.docsource + os.sep + 'conf',
            os.path.dirname(__file__),
            )

        if self.build_apiref == None:
            # default API reference creator
            self.build_apiref = self.docx_defaults.get('build_apiref')
            if not self.build_apiref:
                self.build_apiref = os.sep.join(finder.get_filelocation(
                    'call_apiref.sh', 
                     self.searchpath)
                ) 

        if self.clean == None:
            self.clean = self.docx_defaults.get('clean')
            if self.clean == None:
                self.clean = '0'
            else:
                self.clean = '1'
        else:
            self.clean = '1'

        if self.rawdoc == None:
            self.rawdoc = ''
        else:
            self.rawdoc = str(self.rawdoc)

        if self.docname == None:
            self.docname = self.docx_defaults.get('docname')
            if self.docname == None:
                self.docname = self.name

        if self.doctype == None:
            self.doctype = self.docx_defaults.get('doctype')
        if self.doctype == None:
            self.doctype = "html"
        else:
            if self.doctype not in self.doctypes_supported:
                raise SetuplibBuildApirefXError("doctype = " + str(self.doctype) + " - supported: " + str(self.doctypes_supported))

        if self.srcdir == None:
            self.srcdir = self.docx_defaults.get('srcdir')
            if self.srcdir == None:
                self.srcdir = self.name
            else:
                if type(self.srcdir) is not (list, tuple,):
                    self.srcdir = ';'.join(self.srcdir)

        if self.no_exec_max != None:
            self.no_exec_max = '1'
        else:
            self.no_exec_max = ''

        if self.no_exec != None:
            self.no_exec = True

        self.verbose0 = self.verbose 

        if self.debug == None:
            self.debug = ''
        else:
            self.debug = self.debug 

        if self.version == None:
            try:
                self.version = self.distribution.metadata.version
            except:
                sys.stderr.write(
                    "WARNING: Cannot readout the version, requires either call option '--version', "
                    "or stored configuration data.\n"
                    )
        else:
            self.version = yapyutils.releases.get_version_complete(self.set_version)

        if self.release == None:
            self.release = time.strftime("%Y.%m.%d", time.gmtime())

    def join_sphinx_mod_epydoc(self, dirpath):
        """Integrates links for *sphinx* into the the sidebar of 
        the output of *epydoc*.

        Adds the following entries before the "Table of Contents" to 
        the *sphinx* document:
        
        * Home
        * Top

        .. note::
        
           This method is subject to be changed.
           Current version is hardcoded, see documents.
           Following releases will add customization.
        
        Args:
            dirpath:
                Directory path to the file 'index.html'.

        Returns:
            None

        Raises:
            None
                
        """

        pt = '<a target="moduleFrame" href="toc-everything.html">Everything</a>'
        rp  = r'<a href="../index.html" target="_top">Home</a>'
        rp += r' - '
        rp += r'<a href="./index.html" target="_top">Top</a>'
        rp += r' - '
        rp += pt
    
        fn = dirpath + '/apiref/toc.html'
        setupdocx.sed(fn, pt, rp, re.MULTILINE)  # @UndefinedVariable

        pt = '[@]local-manuals'
        rp  = r'[<a href="../index.html#table-of-contents" target="_top">@local-manuals</a>'
        for flst in os.walk(dirpath + '/apiref/'):
            for fn in flst[2]:
                if fn[-5:] == '.html':
                    setupdocx.sed(flst[0]+os.path.sep+fn, pt, rp, re.MULTILINE)  # @UndefinedVariable
        
        pt = '[&][#]64[;]local-manuals'
        rp  = r'@[<a href="../index.html#table-of-contents" target="_top">local-manuals</a>]'
        for flst in os.walk(dirpath + '/apiref/'):
            for fn in flst[2]:
                if fn[-5:] == '.html':
                    setupdocx.sed(flst[0]+os.path.sep+fn, pt, rp, re.MULTILINE)  # @UndefinedVariable

    def run(self):
        """Creates documents.
        
        Calls first the *bash* script 'create_sphinx.sh', than
        executes *epydoc* when *--epydoc* is set.
        
        The *epydoc* integration also 
         
        
        """

        command_apiref = []
        if self.build_apiref:
            command_apiref.append(self.build_apiref + ";")
        elif self.verbose > 1:
            raise SetuplibBuildApirefXError("requires build-apiref") 

         

        #
        # set parameter via environ
        #
        os.environ['DOCX_BUILDDIR'] = self.build_dir
        os.environ['DOCX_CLEAN'] = self.clean
        os.environ['DOCX_CONFDIR'] = self.conf_dir
        os.environ['DOCX_DEBUG'] = str(self.debug)
        os.environ['DOCX_DOCNAME'] = self.docname
        os.environ['DOCX_DOCSRC'] = self.docsource
        os.environ['DOCX_DOCTYPE'] = self.doctype 
        os.environ['DOCX_LIB'] = os.path.abspath(os.path.dirname(__file__))
        os.environ['DOCX_NAME'] = self.name
        os.environ['DOCX_NOEXEC'] = self.no_exec_max
        os.environ['DOCX_RAWDOC'] = self.rawdoc
        os.environ['DOCX_SRCDIR'] = self.srcdir
        os.environ['DOCX_VERBOSE'] = str(self.verbose0)
        os.environ['DOCX_VERBOSEX'] = str(self.verbose_ext)
        

        os.environ['DOCX_VERSION'] = self.version
        if self.release:
            os.environ['DOCX_RELEASE'] = self.release

        _bdir = self.build_dir + os.sep + 'apiref' + os.sep + 'epydoc'
        try:
            os.makedirs(_bdir)
        except:
            pass
        _fpath = _bdir + os.sep + 'setenv.sh'
        with open(_fpath, 'w') as _f:
            _f.writelines(
                (
                    'DOCX_BUILDDIR="' + os.environ['DOCX_BUILDDIR']  + '"; export DOCX_BUILDDIR;'  + os.linesep,
                    'DOCX_CLEAN="'    + os.environ['DOCX_CLEAN']     + '"; export DOCX_CLEAN'      + os.linesep,
                    'DOCX_CONFDIR="'  + os.environ['DOCX_CONFDIR']   + '"; export DOCX_CONFDIR'    + os.linesep,
                    'DOCX_DEBUG="'    + os.environ['DOCX_DEBUG']     + '"; export DOCX_DEBUG'      + os.linesep,
                    'DOCX_DOCNAME="'  + os.environ['DOCX_DOCNAME']   + '"; export DOCX_DOCNAME'    + os.linesep,
                    'DOCX_DOCSRC="'   + os.environ['DOCX_DOCSRC']    + '"; export DOCX_DOCSRC'     + os.linesep,
                    'DOCX_DOCTYPE="'  + os.environ['DOCX_DOCTYPE']   + '"; export DOCX_DOCTYPE'    + os.linesep,
                    'DOCX_LIB="'      + os.environ['DOCX_LIB']       + '"; export DOCX_LIB'        + os.linesep,
                    'DOCX_NAME="'     + os.environ['DOCX_NAME']      + '"; export DOCX_NAME'       + os.linesep,
                    'DOCX_NOEXEC="'   + os.environ['DOCX_NOEXEC']    + '"; export DOCX_NOEXEC'     + os.linesep,
                    'DOCX_RAWDOC="'   + os.environ['DOCX_RAWDOC']    + '"; export DOCX_RAWDOC'     + os.linesep,
                    'DOCX_RELEASE="'  + os.environ['DOCX_RELEASE']   + '"; export DOCX_RELEASE'    + os.linesep,
                    'DOCX_SRCDIR="'   + os.environ['DOCX_SRCDIR']    + '"; export DOCX_SRCDIR'     + os.linesep,
                    'DOCX_VERBOSE="'  + os.environ['DOCX_VERBOSE']   + '"; export DOCX_VERBOSE'    + os.linesep,
                    'DOCX_VERBOSEX="' + os.environ['DOCX_VERBOSEX']  + '"; export DOCX_VERBOSEX'   + os.linesep,
                    'DOCX_VERSION="'  + os.environ['DOCX_VERSION']   + '"; export DOCX_VERSION'    + os.linesep,
                )
            )

        _fpath = _bdir + os.sep + 'setenv.bat'
        with open(_fpath, 'w') as _f:
            _f.writelines(
                (
                    'set DOCX_BUILDDIR="' + os.environ['DOCX_BUILDDIR']  + '"' + os.linesep,
                    'set DOCX_CLEAN="'    + os.environ['DOCX_CLEAN']     + '"' + os.linesep,
                    'set DOCX_CONFDIR="'  + os.environ['DOCX_CONFDIR']   + '"' + os.linesep,
                    'set DOCX_DEBUG="'    + os.environ['DOCX_DEBUG']     + '"' + os.linesep,
                    'set DOCX_DOCNAME="'  + os.environ['DOCX_DOCNAME']   + '"' + os.linesep,
                    'set DOCX_DOCSRC="'   + os.environ['DOCX_DOCSRC']    + '"' + os.linesep,
                    'set DOCX_DOCTYPE="'  + os.environ['DOCX_DOCTYPE']   + '"' + os.linesep,
                    'set DOCX_LIB="'      + os.environ['DOCX_LIB']       + '"' + os.linesep,
                    'set DOCX_NAME="'     + os.environ['DOCX_NAME']      + '"' + os.linesep,
                    'set DOCX_NOEXEC="'   + os.environ['DOCX_NOEXEC']    + '"' + os.linesep,
                    'set DOCX_RAWDOC="'   + os.environ['DOCX_RAWDOC']    + '"' + os.linesep,
                    'set DOCX_SRCDIR="'   + os.environ['DOCX_SRCDIR']    + '"' + os.linesep,
                    'set DOCX_VERBOSE="'  + os.environ['DOCX_VERBOSE']   + '"' + os.linesep,
                    'set DOCX_VERBOSEX="' + os.environ['DOCX_VERBOSEX']  + '"' + os.linesep,
                    'set DOCX_VERSION="'  + os.environ['DOCX_VERSION']   + '"' + os.linesep,
                    'set DOCX_RELEASE="'  + os.environ['DOCX_RELEASE']   + '"' + os.linesep,
                    )
                )
            
        if self.no_exec or self.no_exec_max or self.verbose > 1:
            print()
            print("Environ:")
            print("   DOCX_BUILDDIR = " + str(self.build_dir))
            print("   DOCX_CLEAN    = " + str(self.clean))
            print("   DOCX_CONFDIR  = " + str(self.conf_dir))
            print("   DOCX_DEBUG    = " + str(self.debug))
            print("   DOCX_DOCNAME  = " + str(self.docname))
            print("   DOCX_DOCSRC   = " + str(self.docsource))
            print("   DOCX_DOCTYPE  = " + str(self.doctype))
            print("   DOCX_LIB      = " + str(os.environ['DOCX_LIB']))
            print("   DOCX_NAME     = " + str(self.name))
            print("   DOCX_NOEXEC   = " + str(self.no_exec_max))
            print("   DOCX_RAWDOC   = " + str(self.rawdoc))
            print("   DOCX_RELEASE  = " + str(self.release))
            print("   DOCX_SRCDIR   = " + str(self.srcdir))
            print("   DOCX_VERBOSE  = " + str(self.verbose0))
            print("   DOCX_VERBOSEX = " + str(self.verbose_ext))
            print("   DOCX_VERSION  = " + str(self.version))
            print()
            print("Scripts: ")
            print("   build_apiref  = " + str(self.build_apiref))
            print()
            print("Call: ")

            print("   " + ' '.join(command_apiref))

            print()

            if self.no_exec:
                sys.exit(0)


        # common build locations
        dst0 = os.path.normpath(self.build_dir + "/doc/" + str(self.docname))

        if self.verbose:
            print()
            print("Call: " + str(' '.join(command_apiref)))
        exit_code = os.system(' '.join(command_apiref)) # create apidoc
        if self.verbose:
            print()
            print("Finished: %s => exit=%s\n\n" % (str(' '.join(command_apiref)), str(exit_code)))

#TODO:
#         # set cross-links
#         if self.build_apidoc and self.build_doc:
#             self.join_sphinx_mod_epydoc(dst0)

