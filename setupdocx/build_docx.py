#-*- coding: utf-8 -*-
"""Creates extended documentation based on configuration templates. 
Supports optional extraction of inline documentation and creation
of additional structured Javadoc style API reference from
inline documentation.

Supports abstract configuration templates for various document builders
e.g. *Sphinx*, *MkDocs*, *Epydoc*, *TexInfo*, *Docbook*, *Perldoc*,
and *txt2tags*.
Could be easily extended by custom wrappers.

Is foreseen as the common abstract build API for the template based 
creation of local and online documentation.
"""
from __future__ import absolute_import
from __future__ import print_function

import sys
import os
import re
import time
import gzip
import shutil

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


class SetuplibBuildDocXError(setupdocx.SetupDocXError):
    """Generic command error.
    """
    pass


class SetuplibBuildDocXConfError(SetuplibBuildDocXError):
    """Error reading configuration.
    """
    pass


class SetuplibBuildDocXSetupError(SetuplibBuildDocXError):
    """Error reading setup.
    """
    pass


class BuildDocX(distutils.cmd.Command):
    """Create compound documents."""

    description = 'Create compound documentation with optional API documentation and refrences.'
    user_options = [
        ('apiref',                None, "Calls the script 'call_apiref.sh', creates the API reference and "
                                        "integrates into sphinx, else sphinx only."
                                        " default: None"),
        ('break-on-err',          None, "Sets the environment variable 'DOCX_BREAKONERR' for the called "
                                        "wrapper script. Breaks after the first error state from the "
                                        "called builder. "
                                        "Default: 'off'"),
        ('builder=',              None, "The builder to be used for the processing of the document. "
                                        "See '--help-builder'. "
                                        "Default: 'sphinx'"),
        ('builder-path=',         None, "The directory path of the builder. "
                                        "Default: '<SETUPDOCX-PYTHONPATH>/setupdocx/builder/'"),
        ('build-dir=',            None, "The name of the build directory. "
                                        "Default: 'build/'"),
        ('build-reldir=',         None, "The name of the relative build subdirectory."
                                        " Default: 'apidoc/<builder>/'"),
        ('cap=',                  None, "The initial default values, for an example see the builder "
                                        "capabilities."
                                        "One or more values separated by comma ','."
                                        "No search operation, the name bust be an existing file path name."
                                        "This is an expert and developer option, which should not be used "
                                        "regularly."
                                        "Default: 'setupdocx/builder/<builder>/capabilities'"),
        ('clean',                 None, "Removes the cached previous build. "
                                        "The default directory is '<build-dir>/apidoc'."
                                        "Default: False"),
        ('clean-all',             None, "Removes the complete build directory before calling the wrapper. "
                                        "The default directory is '<build-dir>'."
                                        "Default: False"),
        ('config-path=',          None, "Directory containing configuration files. "
                                        "See '--list-templates-std' and '--list-templates'. "
                                        "Default: 'config/<builder>/:<docsource>/config/<builder>/'. "),
        ('copyright=',            None, "A copyright text to be used literally. "
                                        "Default: (C) <year> <author>. "),
        ('debug',                 'd',  "Raises degree of debug traces of current context. Supports "
                                        "repetition. "
                                        "Each raises the command verbosity level of the context by one."),
        ('docname=',              None, "The document output name. "
                                        "Default: attribute of derived class self.name"),
        ('docsource=',            None, "The name of the document source directory. "
                                        "Default: docsrc/"),
        ('doctemplate=',          None, "The document template directory relative to '--config-path'. "
                                        "See '--list-templates-std' and '--list-templates'. "
                                        "Default: default/html"),
        ('doctype=',              None, "The document type to create. "
                                        "See '--help-doctypes' for common types, "
                                        "for present types see '--list-templates-std' and "
                                        "'--list-templates'. "
                                        "Default: 'html', "),
        ('executable=',           None, "The executable called by the wrapper. "
                                        "Supports relative and absolute file path names. "
                                        "Default: 'sphinx-build'"),
        ('executableopts=',       None, "Additional options to be passed to the executable. "
                                        "Default: ''"),
        ('executableopts-reset',  None, "Initialize empty options for the called executable. "
                                        "Default: False"),
        ('help-doctypes',         None, "List of available document formats."),
        ('indexsrc=',             None, "The source file to be copied as 'index.rst'. "
                                        "Default: 'index.rst'"),
        ('list-templates-std',    None, "List provided configuration templates."),
        ('list-templates=',       None, "Lists the configuration templates with filter parameter, see "
                                        "manuals. "
                                        "Default: same as list-templates-std"),
        ('name=',                 None, "The name of the package. "
                                        "Default: attribute of derived class self.name"),
        ('noexec=',               'n',  "Print the call of the selected level only, do not execute. "
                                        "The value is an integer, decremented by each level until '0',"
                                        "which is the level to be printed."),
        ('quiet',                 'q',  "Quiet the current context, resets verbosity of applied context "
                                        "to '0'. "
                                        "Default: off"),
        ('rawdoc',                'r',  "Use the generated documents by 'apidoc' only."),
        ('srcdir=',               None, "Source directory."),
        ('set-release=',          None, "The release of the package."
                                        "Default: distribution.metadata.version"),
        ('set-version=',          None, "The version of the package. "
                                        "Default: distribution.metadata.version"),
        ('status=',               None, "The status in accordance to the trove classifiers. "
                                        "Default: '' - empty"),
        ('wrapper=',              None, "The wrapper called by the builder. "
                                        "Supports pure file names only. "
                                        "Default: 'call_doc.sh'"),
        ('wrapperopts=',          None, "Additional options to be passed to the called wrapper. "
                                        "Default: ''"),
        ('wrapperopts-reset',     None, "Drop generated options for the wrapper, does not effect "
                                        "environment. "
                                        "Default: False"),
        ('verbose',               'v',  "Raises verbosity of current context. Supports repetition. "
                                        "Each raises the command verbosity level of the context by one."),

        
###############################
###############################

#FIXME: clear this
        ('apidoc',             None, "Calls the script 'call_apidoc.sh', creates the API documentation and "
                                     "integrates into sphinx, else sphinx-build only."
                                     " default: None"),
        ('builder=',           None, "Builder to be used for the document processing. "
                                     "Default: 'sphinx' dependent of the doctype resulting in pure "
                                     "'sphinx-build' for inherent document types, or "
                                     "'sphinx-build' + 'make' for external types "
                                     "defined by '--doctype' e.g. such as 'html' or 'epub'. "
                                     "For called code-analysis tools see '--builder-apidoc' and "
                                     "'--builder-apiref'."
                                     "See '--help-builder' for a list of available builders."),
        ('build-apidoc=',      None, "the name of the called script for the creation of the API documentation,"
                                     " default: '<conf-dir>/call_apidoc.sh'"),
        ('build-apiref=',      None, "the name of the called script for the creation of the API reference,"
                                     " default: '<conf-dir>/call_apiref.sh'"),
        ('build-doc=',         None, "the name of the called script for the sphinx document creation,"
                                     " default: '<conf-dir>/call_doc.sh'"),
    ]

    #: The provided capabilities of the builder and it's components.
    capabilities = yapyutils.config.capabilities.Capability(
        #
        # the hardcoded final defaults
        #
        {
            "components": {
                "default":          "sphinx",  # adjusted in dependence of the 'doctype'
                "sphinx":           "sphinx",  # adjusted in dependence of the 'doctype'
                "apiref":           "epydoc",
                "epydoc":           "epydoc",
                "apidoc":           "sphinx-apidoc",
            },
            "sphinx": {
                "doctypes": [
                    "epub",           # epub
                    "html",           # simple HTML with defaults for sphinx and epydoc
                    "man",            # man page
                    "mangz",          # compressed man page
                    "pdf",            # one PDF file
            
                    "latex",          # latex
                    "latexpdf",       # pdf by latex
                    "latexpdfja",     # pdf by platex/dvipdfmx
            
                    "singlehtml",     # one HTML file
            
                    "devhelp",        # HTML-Help
                    "htmlhelp",       # HTML-Help
                    "qthelp",         # HTML-Help
        
                    # TODO:
                    # "dirhtml",        # one HTML file
                    # "json",           #  JSON
                    # "xml",            #  JSON
                ]
            },
            "epydoc": {
                "doctypes": [
                    "html",           # simple HTML with defaults for sphinx and epydoc
                ],
            },
            "apiref": {               #:  supported document types with integrated API reference - apiref = 1
                "doctypes": [
                    "html",           # simple HTML with defaults for sphinx and epydoc
                ],
            },
            "defaults": {             # DEFAULTS:
                'apidoc': False,          # False
                'apiref': False,          # False
                'build_apidoc': None,     # search(<conf-dir>, <configdir>, <docsrc>/conf)/call_apidoc.sh
                'build_apiref': None,     # search(<conf-dir>, <configdir>, <docsrc>/conf)/call_apiref.sh
                'build_dir': 'build/',    # build/
                'build_doc': None,        # search(<conf-dir>, <configdir>, <docsrc>/conf)/call_doc.sh
                'build_reldir': 'apidoc/sphinx/', # apidoc/sphinx/
                'clean': None,            # False
                'config_path':  None,     # config/:<docsource>/config/
                'copyright': None,        # default
                'docname': None,          # attribute of derived class, see self.name
                'docsource': 'docsrc/',   # docsrc/
                'doctemplate': None,      # default
                'doctype': None,          # html
                'indexsrc': 'index.rst',  # 'index.rst'
                'name': None,             # attribute of derived class, see self.name
                'release': None,          # <year>.<month>.<day>
                'srcdir': None,           # list/tuple(<name>/,)
                'version': None,          # 
            }
        }
    )

    def initialize_options(self):
        self.debug = None
        self.noexec = None
        self.quiet = None
        self.verbose = None
        self.break_on_err = None

        self.apidoc = None
        self.apiref = None
        self.build_apidoc = None
        self.build_apiref = None
        self.build_dir = None
        self.build_doc = None
        self.build_reldir = None
        self.builder = None
        self.builder_path = None
        self.cap = None
        self.clean = None
        self.clean_all = None
        self.config_path = None
        self.copyright = None
        self.docname = None
        self.docsource = None
        self.doctemplate = None
        self.doctype = None
        self.executable = None
        self.executableopts = None
        self.executableopts_reset = None
        self.gendoc = None
        self.help_doctypes = None
        self.indexsrc = None
        self.list_templates = None
        self.list_templates_std = None
        self.name = None
        self.set_release = None
        self.set_version = None
        self.status = None
        self.srcdir = None
        self.wrapper = None
        self.wrapperopts = None
        self.wrapperopts_reset = None

        self.debug_apidoc = None
        self.debug_apiref = None
        self.verbose_apidoc = None
        self.verbose_apiref = None
        self.verbose_ext = None

    def set_config_data(self, cap=None):
        """Initializes the hard-coded static values first, than
        reads the configuration file - if present - and superposes
        present values. 
        
        The configuration file is expected to be located within 
        the builder directory.

        Args:
            cap:
                A single or a comma separated list of capabilities files
                to be superposed sequentially.

        Returns:
            The updated value of 'self.capabilities'.

        Raises:
            SetuplibBuildDocXSetupError
            
            pass-through
        
        """
        if cap == None:
            if self.debug > 1:
                sys.stderr.write(
                    "# DBG: Superpose capabilities from:\n  builder = %s\n  path = %s\n  app  = %s\n" % (
                        str(self.builder),
                        str(self.builder_path),
                        str('sphinx'),
                        )
                    )

            self.capabilities.addfile(
                self.builder,
                path=(self.builder_path,),
                app='sphinx',
            )

        else:
            for c in cap.split(','):
                if os.path.exists(c):
                    if self.debug > 1:
                        sys.stderr.write(
                            "# DBG: Superpose capabilities from: %s\n" %(
                                str(c),
                                )
                            )
                        
                    self.capabilities.addfile(c,)

                else:
                    raise SetuplibBuildDocXSetupError(
                        "Capabilities not found:\n--cap = %s\nerr:    %s" %(
                            str(cap),
                            str(c),
                        )
                    )
        
    def finalize_options(self):

        # scan for any context-help request
        _help_request = setuplib.check_for_context_help(self)
        if _help_request:
            print(_help_request)
            sys.exit(0)

        # quick-and-dirty hack to resolve the inconsistency of
        # global and local verbose values of distutils
        try:
            # The context option is actually not set by the framework,
            # instead the global option is reset and intialized to
            # the number of occurances and passes to the initialization
            # of the memeber 'self.verbose'.
            # Thus the poll fails, while the value is already set via the framework.
            # See code distutils.dist.Distribution.
            # Anyhow...keeping it as a reminder.
            _v_opts = self.distribution.get_option_dict('build_docx')['verbose'][1]
            if _v_opts:
                self.verbose += 1
        except:
            # fallback to the slightly erroneous behavior when the interface 
            # of distutils changes
            pass


        # global and local verbose values of distutils
        try:
            # See verbose for description of the global option quiet.
            # See code distutils.dist.Distribution.
            _q_opts = self.distribution.get_option_dict('build_docx')['quiet'][1]
            if _q_opts:
                self.quiet += 1
        except:
            # fallback to the slightly erroneous behavior when the interface 
            # of distutils changes
            if self.quiet == None:
                self.quiet = 0
            pass


        # debug
        if self.debug == None:
            self.debug = 0

        if self.verbose_ext == None:
            self.verbose_ext = 0

        # wrapper specific settings
        if self.debug_apidoc == None:
            self.debug_apidoc = 0
        if self.verbose_apidoc == None:
            self.verbose_apidoc = 0

        if self.debug_apiref == None:
            self.debug_apiref = 0
        if self.verbose_apiref == None:
            self.verbose_apiref = 0

        #
        # exit the wrapper
        #
        if self.break_on_err == None:
            self.break_on_err = 0


        #
        # name of current package - serves as default for package subdiretory etc.
        #
        if self.name == None:
            self.name = self.distribution.metadata.name


        #
        # current builder
        #
        if self.builder == None:
            self.builder = 'sphinx'


        #
        # user has provided setup directory for builder - so load first new defaults
        #
        if self.builder_path != None:
            if not os.path.isdir(self.builder_path):
                raise SetuplibBuildDocXSetupError('Missing --builder-path=' + str(self.builder_path))
            self.builder_path = os.path.normpath(self.builder_path) + os.sep

        else:
            self.builder_path = os.path.dirname(__file__) + os.sep + 'builder' + os.sep


        #
        # default setup values for capabilities 
        #
        self.set_config_data(self.cap)


        #
        # validate consistency of current builder and defaults
        #
        if self.builder != self.capabilities['builder']['name']:
            raise SetuplibBuildDocXSetupError(
                'Inconsistent builder:\nbuilder:  %s\ndefaults: %s\n\nCheck:     %s' %(
                    str(self.builder),
                    str(self.capabilities['builder']['name']),
                    str(self.builder_path + self.builder)
                )
            )


        #
        # configuration template
        #
        if self.doctemplate == None:
            self.doctemplate = self.capabilities[self.builder]['defaults']['doctemplate']
        if self.doctemplate == None:
            self.doctype = "default"


        #
        # user provided configuration directory
        #
        if self.config_path == None:
            self.config_path = self.capabilities[self.builder]['defaults']['config_path']

        if not self.config_path:
            # empty - for whatever reason
            self.config_path = 'config' + os.sep + self.builder
            self.config_path += os.pathsep + os.path.dirname(__file__) + os.sep + 'config' + os.sep + self.builder

        else:
            self.config_path = os.path.normpath(self.config_path) + os.sep
        
        if not self.config_path:
            raise SetuplibBuildDocXConfError(
                'Missing template path "--config-path=%s"' % (str(self.config_path),))
        else:
            _oneok = False
            _onedirok = False
            for f in self.config_path.split(os.pathsep):
                if os.path.isdir(f):
                    _onedirok = True
                    fp = f + os.sep + self.doctemplate
                    if os.path.isdir(fp):
                        self.config_path = f
                        _oneok = True
            if not _oneok:
                if not _onedirok:
                    raise SetuplibBuildDocXConfError(
                        'Missing configuration template directory, got "--config-path=%s"' %( 
                            str(self.config_path)
                        )
                    )
                else:
                    raise SetuplibBuildDocXConfError(
                        '\n\nCannot find configuration template:\n' 
                        '   template name:  %s\n' 
                        '   search path:    %s\n' 
                        '\n' 
                        'Check options "--list-templates-std / --list-templates"\n' %( 
                            str(self.doctemplate),
                            str(self.config_path),
                        )
                    )


        #
        # set source directory of document
        #
        if self.docsource == None:
            self.docsource = self.capabilities[self.builder]['defaults']['docsource']
            if self.docsource == None:
                self.docsource = 'docsrc'
        if self.docsource:
            # set directory for pre-edited document components
            if not os.path.exists(self.docsource):
                raise SetuplibBuildDocXError("missing docsrc:" + str(self.docsource))
        else:
            # uses raw output of the called builder - default sphinx-apidoc - only
            pass  # a reminder...


        #
        # show templates
        #
        if self.list_templates_std != None:
            setupdocx.conf_list(depth=20)  # maximum depth of subdirectory scan
            sys.exit(0)


        #
        # show templates with filters
        #
        if self.list_templates != None:
            _kargs = {}
            _args = ''

#     _sep = kargs.get('separator', 0)
#     _sep = re.sub(r'(.*?)[\\\\]{0,1}(?<=[\\\\]);', r'\1;', _sep)

            # mask the suboption separator 
#            for ai in re.split(r'(?<![\\\\]);', self.list_templates):
            for ai in re.split(r'(?<![\[]);(?![\]])', self.list_templates):
                if ai:
                    try:
                        _k, _v = ai.split('=')
                        if _k == 'baselist':
                            _v = _v.split(os.pathsep)
                        _kargs[_k] = _v
                    except ValueError:
                        _args += ',' + ai

            if _args.endswith(',help'):
                _h = """
Supports the keyword arguments of 'setupdocx.conf_list'.

The keyword parameter 'filter' could be replaced by a comma separated
list of arguments to be assembled into a filter rule.

*args=<list-of-OR-parts-python-re-expression>*
  Example::

    input:
       args := 'agogo,alabas.*'

    rule:
       args-rule := '(agogo|alabas.*)'

*filter=<python-re-expression>*

    input:
       filter := 'filter=(agogo|alabas.*)'

    rule:
       args-rule := '(agogo|alabas.*)'
 
The keyword parameter 'filter' provides for a wider range of rule syntaxes, 
while the 'args' list offers simplicity for casual calls.

The call without parameters is the same as the option '--list-templates-std'. 
The 'setupdocx.conf_list' parameters provided for the user interface are:

    setupdocx.conf_list
    ===================

    """
                # help(setupdocx.conf_list)
                print(_h + setupdocx.conf_list.__doc__)
                sys.exit(0)
                
            _filters = None
            if _args:
                _filters = [x for x in _args.split(',') if x]

                if len(_filters) > 1:
                    _filter = '(' + '|'.join(_filters) + ')'
                else:
                    _filter = _filters[0]

            if 'filter' in _kargs:
                if _filters:
                    raise SetuplibBuildDocXError(
                        "Filters could be provided either by args as a comma separated list "
                        "of partial 're' rules internallz converted to a single rule, "
                        "or by the 'filters=' option as a single final Python-regular "
                        "expression. The resulting rule is compiled by 're.compile()'. "
                        "Got:\n"
                        "   args:    %s\n"
                        "   filters: %s\n" % (
                            str(_filters),
                            str(_kargs['filter']),
                            )
                        )

#                _filter_re = re.compile(_kargs['filter'])

#             if not _filters:
#                 _filter_re =  None
                
            setupdocx.conf_list(**_kargs)
            sys.exit(0)


        #
        # show doctypes
        #
        if self.help_doctypes != None:
            if self.apiref: 
                print("Known document types for integrated API reference:")
                
                #FIXME:
                for dt in  sorted(self.capabilities[self.apiref]['doctypes']):
                    print("  --doctype=%s" % (dt))
                print()
                print(
                    "Note: The integrated '--apiref' currently supports 'html' only."
                    )
                print()
            else:
                print("Known document types:")
                print()

                print("   Primary formats:")
                _dtypes = list(self.capabilities[self.builder]['doctypes'][:])
                if 'html' in _dtypes:
                    print("     --doctype=%s" % ('html'))
                    _dtypes.pop(_dtypes.index('html'))
                if 'singlehtml' in _dtypes:
                    print("     --doctype=%s" % ('singlehtml'))
                    _dtypes.pop(_dtypes.index('singlehtml'))
                if 'epub' in _dtypes:
                    print("     --doctype=%s" % ('epub'))
                    _dtypes.pop(_dtypes.index('epub'))
                if 'pdf' in _dtypes:
                    print("     --doctype=%s" % ('pdf'))
                    _dtypes.pop(_dtypes.index('pdf'))
                if 'man' in _dtypes:
                    print("     --doctype=%s" % ('man'))
                    _dtypes.pop(_dtypes.index('man'))
                print()
                    
                print("   Secondary formats:")
                for dt in  sorted(_dtypes):
                    print("     --doctype=%s" % (dt))
                print()

                print(
                    "Note: The integrated '--apiref' is supported for 'html' only."
                    )
                print()
                
            sys.exit(0)
        
#         if self.docsource == None:
#             self.docsource = self.capabilities[self.builder]['defaults']['docsource']
#             if self.docsource == None:
#                 self.docsource = 'docsrc'
#         if self.docsource and not os.path.exists(self.docsource):
#             raise SetuplibBuildDocXError("missing docsrc:" + str(self.docsource))
        
#         if self.config_path == None:
#             self.config_path = self.capabilities[self.builder]['defaults']['config_path']
#             if not self.config_path:
#                 self.config_path = self.docsource + os.sep + 'conf'
#             self.config_path = os.path.abspath(os.path.normpath(self.config_path)) + os.sep
#         if not os.path.exists(self.config_path):
#             raise SetuplibBuildDocXError("missing confdir:" + str(self.config_path))

        if self.build_dir == None:
            self.build_dir = self.capabilities[self.builder]['defaults']['build_dir']
            if not self.build_dir:
                self.build_dir = 'build/'

        if self.build_reldir == None:
            self.build_reldir = self.capabilities[self.builder]['defaults']['build_reldir']
            if not self.build_reldir:
                self.build_reldir = 'apidoc/sphinx'

        # the complete path for the assembled document sources to be processed 
        self.build_doc_path = os.path.normpath(self.build_dir + os.sep + self.build_reldir)

        # create when missing
        if not os.path.exists(self.build_doc_path):
            os.makedirs(self.build_doc_path)
        elif not os.path.isdir(self.build_doc_path):
            raise SetuplibBuildDocXError(
                "File present with target dirname: "
                + str(self.build_doc_path)
                )


        if self.gendoc == None:
            self.gendoc = 0
        else:
            self.gendoc = 1


        # location of shared call scripts
        self.searchpath = (
            self.config_path, 
            self.docsource + os.sep + 'conf',
            os.path.dirname(__file__) + os.sep + 'builder' + os.sep + self.builder,
            os.path.dirname(__file__) + os.sep + 'builder' + os.sep + 'sphinx',
            os.path.dirname(__file__) + os.sep + 'builder' + os.sep + 'epydoc',
            os.path.dirname(__file__) + os.sep + 'builder' + os.sep + 'mkdocs',
            os.path.dirname(__file__) + os.sep + 'builder' + os.sep + 'pandoc',
            os.path.dirname(__file__),
            )

        if self.build_doc == None:
            # default document creator
            self.build_doc = self.capabilities['defaults']['build_doc']
            if not self.build_doc:
                self.build_doc = os.sep.join(finder.get_filelocation(
                    'call_doc.sh', self.searchpath))         
        if not self.build_doc or not os.path.exists(self.build_doc):
            raise setupdocx.SetupDocXError(
                "requires a build script, got: '%s'" % (str(self.build_doc)))

        if self.build_apidoc == None:
            # default API extractor
            self.build_apidoc = self.capabilities['defaults']['build_apidoc']
            if not self.build_apidoc:
                self.build_apidoc = os.sep.join(finder.get_filelocation(
                    'call_apidoc.sh', self.searchpath)) 

        if self.build_apiref == None:
            # default API reference creator
            self.build_apiref = self.capabilities['defaults']['build_apiref']
            if not self.build_apiref:
                self.build_apiref = os.sep.join(finder.get_filelocation(
                    'call_apiref.sh', self.searchpath)) 

        if self.apidoc == None:
            self.apidoc = self.capabilities['defaults']['apidoc']
        if self.apidoc == None:
            self.apidoc = ''
        elif self.apidoc == False:
            self.apidoc = ''
        else:
            self.apidoc = '1'

        if self.apiref == None:
            self.apiref = self.capabilities['defaults']['apiref']
        if self.apiref == None:
            self.apiref = ''
        elif self.apiref == False:
            self.apiref = ''
        else:
            self.apiref = '1'

        if self.clean == None:
            self.clean = self.capabilities[self.builder]['defaults']['clean'] 
            if self.clean == None:
                self.clean = '0'
            else:
                self.clean = '1'
        else:
            self.clean = '1'

#         if self.name == None:
#             self.name = self.distribution.metadata.name

        if self.docname == None:
            self.docname = self.capabilities[self.builder]['defaults']['docname']
            if self.docname == None:
                self.docname = self.name

        if self.doctype == None:
            self.doctype = self.capabilities[self.builder]['defaults']['doctype']

        self.mangz = False  # provides compression of man pages
        if self.doctype == None:
            self.doctype = "html"
        elif self.doctype == 'mangz':
            self.doctype = "man"
            self.mangz = True
        else:
            if self.doctype not in self.capabilities[self.builder]['doctypes']:
                raise SetuplibBuildDocXError(
                    "doctype = " + str(self.doctype) 
                    + " - supported: " + str(self.capabilities[self.builder]['doctypes']))

        if self.indexsrc == None:
            self.indexsrc = self.capabilities[self.builder]['defaults']['indexsrc']
            if self.indexsrc == None:
                self.indexsrc = ''

        if self.srcdir == None:
            self.srcdir = self.capabilities[self.builder]['defaults']['srcdir']
            if self.srcdir == None:
                self.srcdir = self.name
            else:
                if type(self.srcdir) is (list, tuple,):
                    self.srcdir = os.pathsep.join(self.srcdir)

        if self.noexec != None:
            self.noexec = True

        if self.verbose == None:
            self.verbose0 = ''
        else:
            self.verbose0 = self.verbose 
            

        if self.status == None:
            self.status = ''

        if self.set_version == None:
            try:
                self.version = self.distribution.metadata.version
            except:
                sys.stderr.write(
                    "WARNING: Cannot readout the version, requires either call option '--version', "
                    "or stored configuration data.\n"
                    )
        else:
            self.version = yapyutils.releases.get_version_complete(self.set_version)

        if self.set_release == None:
            try:
                if self.release == None:
                    self.release = ''
            except:
                self.release = self.version
        else:
            self.release = self.set_release 

        self.builddate = time.strftime("%Y.%m.%d-%H:%M", time.gmtime())

        if self.clean_all == None:
            self.clean_all = self.capabilities[self.builder]['defaults']['clean_all']
        else:
            self.clean_all = True

        self.author = self.distribution.metadata.author
        self.license = self.distribution.metadata.license
        self.description = self.distribution.metadata.description

        try:
            if self.copyright == None:
                self.copyright = "(C)%s %s" % (str(time.strftime("%Y", time.gmtime())), str(self.author)) 
        except:
            self.copyright = "(C)%s %s" % (str(time.strftime("%Y", time.gmtime())), str(self.author)) 

        try:
            if self.status == None:
                self.status = ''
            elif not self.status:
                self.status = "Unknown" 
                sys.stdout.write("Status is not set: Unknown\n")
        except:
            self.status = "Missing" 
            sys.stdout.write("Status is not defined: Missing\n")

        # the complete path for the final document
        self.build_out_path = os.path.normpath(self.build_dir + "/doc/" + str(self.docname))

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
        utilities.sed(fn, pt, rp, re.MULTILINE)  # @UndefinedVariable

        pt = '[@]local-manuals'
        rp  = r'[<a href="../index.html#table-of-contents" target="_top">@local-manuals</a>'
        for flst in os.walk(dirpath + '/apiref/'):
            for fn in flst[2]:
                if fn[-5:] == '.html':
                    utilities.sed(flst[0]+os.path.sep+fn, pt, rp, re.MULTILINE)  # @UndefinedVariable
        
        pt = '[&][#]64[;]local-manuals'
        rp  = r'@[<a href="../index.html#table-of-contents" target="_top">local-manuals</a>]'
        for flst in os.walk(dirpath + '/apiref/'):
            for fn in flst[2]:
                if fn[-5:] == '.html':
                    utilities.sed(flst[0]+os.path.sep+fn, pt, rp, re.MULTILINE)  # @UndefinedVariable

    def run(self):
        """Creates documents.
        Calls the defined and activated wrapper scripts.
        The call flow could be customized by various 
        interfaces. ::
        
                I.      self.call_environment()    # could be superposed by derived class
                II.     self.call_prologue()       # could be superposed by derived class 
                III.    subprocesses:
                    1.    build_apidoc.sh          # could be arbitrary custom call wrapper
                    2.    build_docx.sh            # could be arbitrary custom call wrapper
                    3.    build_apiref.sh          # could be arbitrary custom call wrapper
                IV.     self.call_epilogue()       # could be superposed by derived class

        """
        if self.clean_all:
            # clean build directories of apidoc + apiref
            if self.verbose > 2:
                print('shutil.rmtree(%s, True)' % (self.build_doc_path))
            shutil.rmtree(self.build_doc_path, True)
            _b = self.build_dir + os.sep + 'apiref'
            if self.verbose > 2:
                print('shutil.rmtree(%s, True)' % (self.build_doc_path))
            shutil.rmtree(self.build_doc_path, True)

        # call string of *sphinx* for subprocess
        command_apidoc = []
        if self.build_apidoc:
            command_apidoc.append(self.build_apidoc + ";")
        elif self.verbose > 1:
            sys.stdout.write("skip : build_apidoc\n")

        command_doc = []
        if self.build_doc:
            command_doc.append(self.build_doc + ";")
        elif self.verbose > 1:
            sys.stdout.write("skip : build_doc\n")

        command_apiref = []
        if self.build_apiref:
            command_apiref.append(self.build_apiref + ";")
        elif self.verbose > 1:
            sys.stdout.write("skip : build_apiref\n")


        if self.noexec or self.verbose > 1:
            print()
            print("Scripts: ")
            print("   build_apidoc  = " + str(self.build_apidoc))
            print("   build_apiref  = " + str(self.build_apiref))
            print("   build_doc     = " + str(self.build_doc))
            
            print()
            
            print("Calls: ")

            if self.apidoc and self.build_apidoc:
                print("   " + ' '.join(command_apidoc))
            else:
                print("   build_apidoc is deactivated")
                
            if self.apiref and self.build_apiref:
                print("   " + ' '.join(command_apiref))
            else:
                print("   build_apiref is deactivated")

            if self.build_doc:
                print("   " + ' '.join(command_doc))
            else:
                print("   build_doc is deactivated")


            print()

            if self.noexec:
                sys.exit(0)

        self.call_environment()
        self.call_prologue()

        if self.apidoc == '1':
            #
            # activate epydoc
            #

            if command_apidoc:
                if self.verbose:
                    print()
                    print("Call API wrapper: %s\n" % (str(' '.join(command_apidoc))))
                exit_code = os.system(' '.join(command_apidoc))
                if self.verbose:
                    print()
                    print("Called/Finished callDocSphinx.sh => exit="+str(exit_code))
                    print()

                if self.break_on_err > 0 and exit_code != 0:
                    sys.exit(exit_code)

        if command_doc:
            if self.verbose:
                print()
                print("Call DOC wrapper: %s\n" % str(' '.join(command_doc)))
            exit_code = os.system(' '.join(command_doc))
            if self.verbose:
                print()
                print("Called/Finished callDocSphinx.sh => exit="+str(exit_code))
                print()
            if self.break_on_err > 0 and exit_code != 0:
                sys.exit(exit_code)

            if self.mangz:
                for _mp in os.listdir(self.build_out_path):
                    _in = self.build_out_path + os.sep + _mp
                    _out = self.build_out_path + os.sep + _mp + '.gz'
                    with open(_in, 'rb') as f_in, gzip.open(_out, 'wb') as f_out:
                        shutil.copyfileobj(f_in, f_out)
                    os.unlink(_in)

        self.call_prologue()

        if self.apiref == '1':
            #
            # activate epydoc
            #
            
            if self.verbose:
                print()
                print("Call: " + str(' '.join(command_apiref)))
            exit_code = os.system(' '.join(command_apiref)) # create apidoc
            if self.verbose:
                print()
                print("Finished: %s => exit=%s\n\n" % (
                    str(' '.join(command_apiref)), str(exit_code)))
            if self.break_on_err > 0 and exit_code != 0:
                sys.exit(exit_code)

            # set cross-links
            if self. apiref and self.build_apiref and self.build_doc:
                self.join_sphinx_mod_epydoc(self.build_out_path)


    def call_environment(self):
        """Sets the specific environment variables for the subprocess.
        In addition writes source files of the environment for the 
        manual command line start.
        
        The defined variables represent the interface to the wrapper calls,
        so no modification of the provided environment is permitted. When
        additional information is required do not forget to call this method.  
        
        """
        #
        # set parameter via environ
        #
        os.environ['DOCX_APIDOC'] = str(self.apidoc)
        os.environ['DOCX_APIREF'] = str(self.apiref)
        os.environ['DOCX_AUTHOR'] = str(self.author)
        os.environ['DOCX_BREAKONERR'] = str(self.break_on_err)
        os.environ['DOCX_BUILDDIR'] = str(self.build_dir)
        os.environ['DOCX_BUILDER'] = str(self.builder)
        os.environ['DOCX_BUILDRELDIR'] = (self.build_reldir)
        os.environ['DOCX_CLEAN'] = (self.clean)
        os.environ['DOCX_CONFIGPATH'] = str(self.config_path)
        os.environ['DOCX_COPYRIGHT'] = str(self.copyright)
        os.environ['DOCX_DEBUG'] = str(self.debug)
        os.environ['DOCX_DEBUGAPIDOC'] = str(self.debug_apidoc)
        os.environ['DOCX_DEBUGAPIREL'] = str(self.debug_apiref)
        os.environ['DOCX_DOCNAME'] = str(self.docname)
        os.environ['DOCX_DOCSRC'] = str(self.docsource)
        os.environ['DOCX_DOCTEMPLATE'] = str(self.doctemplate) 
        os.environ['DOCX_DOCTYPE'] = str(self.doctype) 
        os.environ['DOCX_EMBED'] = '1' 
        os.environ['DOCX_GENDOC'] = str(self.gendoc)
        os.environ['DOCX_INDEXSRC'] = str(self.indexsrc)
        os.environ['DOCX_LIB'] = os.path.abspath(os.path.dirname(__file__))
        os.environ['DOCX_LICENSE'] = str(self.license)
        os.environ['DOCX_MISSION'] = str(self.description)
        os.environ['DOCX_NAME'] = str(self.name)
        os.environ['DOCX_NOEXEC'] = str(self.noexec)
        os.environ['DOCX_QUIET'] = str(self.quiet)
        os.environ['DOCX_SRCDIR'] = str(self.srcdir)
        os.environ['DOCX_STATUS'] = str(self.status)
        os.environ['DOCX_VERBOSE'] = str(self.verbose0)
        os.environ['DOCX_VERBOSEAPIDOC'] = str(self.verbose_apidoc)
        os.environ['DOCX_VERBOSEAPIREL'] = str(self.verbose_apiref)
        os.environ['DOCX_VERBOSEX'] = str(self.verbose_ext)

        os.environ['DOCX_VERSION'] = str(self.version)
        if self.set_release:
            os.environ['DOCX_RELEASE'] = str(self.release)
        else:
            os.environ['DOCX_RELEASE'] = str(self.version)

        try:
            os.makedirs(self.build_doc_path)
        except:
            pass
        _fpath = self.build_doc_path + os.sep + 'setenv.sh'
        with open(_fpath, 'w') as _f:
            _f.writelines(
                (
                    'DOCX_APIDOC="'        + os.environ['DOCX_APIDOC']        + '"; export DOCX_APIDOC;'       + os.linesep,
                    'DOCX_APIREF="'        + os.environ['DOCX_APIREF']        + '"; export DOCX_APIREF'        + os.linesep,
                    'DOCX_AUTHOR="'        + os.environ['DOCX_AUTHOR']        + '"; export DOCX_AUTHOR;'       + os.linesep,
                    'DOCX_BREAKONERR="'    + os.environ['DOCX_BREAKONERR']    + '"; export DOCX_BREAKONERR;'     + os.linesep,
                    'DOCX_BUILDDIR="'      + os.environ['DOCX_BUILDDIR']      + '"; export DOCX_BUILDDIR;'     + os.linesep,
                    'DOCX_BUILDER="'       + os.environ['DOCX_BUILDER']       + '"; export DOCX_BUILDER;'     + os.linesep,
                    'DOCX_BUILDRELDIR="'   + os.environ['DOCX_BUILDRELDIR']   + '"; export DOCX_BUILDRELDIR;'  + os.linesep,
                    'DOCX_CLEAN="'         + os.environ['DOCX_CLEAN']         + '"; export DOCX_CLEAN'         + os.linesep,
                    'DOCX_CONFIGPATH="'    + os.environ['DOCX_CONFIGPATH']    + '"; export DOCX_CONFIGPATH'    + os.linesep,
                    'DOCX_COPYRIGHT="'     + os.environ['DOCX_COPYRIGHT']     + '"; export DOCX_COPYRIGHT;'    + os.linesep,
                    'DOCX_DEBUGAPIDOC="'   + os.environ['DOCX_DEBUGAPIDOC']   + '"; export DOCX_DEBUGAPIDOC'   + os.linesep,
                    'DOCX_DEBUGAPIREL="'   + os.environ['DOCX_DEBUGAPIREL']   + '"; export DOCX_DEBUGAPIREL'   + os.linesep,
                    'DOCX_DOCNAME="'       + os.environ['DOCX_DOCNAME']       + '"; export DOCX_DOCNAME'       + os.linesep,
                    'DOCX_DOCSRC="'        + os.environ['DOCX_DOCSRC']        + '"; export DOCX_DOCSRC'        + os.linesep,
                    'DOCX_DOCTEMPLATE="'   + os.environ['DOCX_DOCTEMPLATE']   + '"; export DOCX_DOCTEMPLATE'   + os.linesep,
                    'DOCX_DOCTYPE="'       + os.environ['DOCX_DOCTYPE']       + '"; export DOCX_DOCTYPE'       + os.linesep,
                    'DOCX_EMBED="'         + os.environ['DOCX_EMBED']         + '"; export DOCX_EMBED'         + os.linesep,
                    'DOCX_GENDOC="'        + os.environ['DOCX_GENDOC']        + '"; export DOCX_GENDOC'        + os.linesep,
                    'DOCX_INDEXSRC="'      + os.environ['DOCX_INDEXSRC']      + '"; export DOCX_INDEXSRC'      + os.linesep,
                    'DOCX_LIB="'           + os.environ['DOCX_LIB']           + '"; export DOCX_LIB'           + os.linesep,
                    'DOCX_LICENSE="'       + os.environ['DOCX_LICENSE']       + '"; export DOCX_LICENSE;'      + os.linesep,
                    'DOCX_MISSION="'       + os.environ['DOCX_MISSION']       + '"; export DOCX_MISSION;'      + os.linesep,
                    'DOCX_NAME="'          + os.environ['DOCX_NAME']          + '"; export DOCX_NAME'          + os.linesep,
                    'DOCX_NOEXEC="'        + os.environ['DOCX_NOEXEC']        + '"; export DOCX_NOEXEC'        + os.linesep,
                    'DOCX_QUIET="'         + os.environ['DOCX_QUIET']         + '"; export DOCX_QUIET'         + os.linesep,
                    'DOCX_RELEASE="'       + os.environ['DOCX_RELEASE']       + '"; export DOCX_RELEASE'       + os.linesep,
                    'DOCX_SRCDIR="'        + os.environ['DOCX_SRCDIR']        + '"; export DOCX_SRCDIR'        + os.linesep,
                    'DOCX_STATUS="'        + os.environ['DOCX_STATUS']        + '"; export DOCX_STATUS;'       + os.linesep,
                    'DOCX_VERBOSE="'       + os.environ['DOCX_VERBOSE']       + '"; export DOCX_VERBOSE'       + os.linesep,
                    'DOCX_VERBOSEAPIDOC="' + os.environ['DOCX_VERBOSEAPIDOC'] + '"; export DOCX_VERBOSEAPIDOC' + os.linesep,
                    'DOCX_VERBOSEAPIREL="' + os.environ['DOCX_VERBOSEAPIREL'] + '"; export DOCX_VERBOSEAPIREL' + os.linesep,
                    'DOCX_VERBOSEX="'      + os.environ['DOCX_VERBOSEX']      + '"; export DOCX_VERBOSEX'      + os.linesep,
                    'DOCX_VERSION="'       + os.environ['DOCX_VERSION']       + '"; export DOCX_VERSION'       + os.linesep,
                )
            )

        _fpath = self.build_doc_path + os.sep + 'setenv.bat'
        with open(_fpath, 'w') as _f:
            _f.writelines(
                (
                    'set DOCX_APIDOC="'       + os.environ['DOCX_APIDOC']       + '"' + os.linesep,
                    'set DOCX_APIREF="'       + os.environ['DOCX_APIREF']       + '"' + os.linesep,
                    'set DOCX_AUTHOR="'       + os.environ['DOCX_AUTHOR']       + '"' + os.linesep,
                    'set DOCX_BREAKONERR="'   + os.environ['DOCX_BREAKONERR']   + '"' + os.linesep,
                    'set DOCX_BUILDDIR="'     + os.environ['DOCX_BUILDDIR']     + '"' + os.linesep,
                    'set DOCX_BUILDER="'      + os.environ['DOCX_BUILDER']      + '"' + os.linesep,
                    'set DOCX_BUILDRELDIR="'  + os.environ['DOCX_BUILDRELDIR']  + '"' + os.linesep,
                    'set DOCX_CLEAN="'        + os.environ['DOCX_CLEAN']        + '"' + os.linesep,
                    'set DOCX_CONFIGPATH="'   + os.environ['DOCX_CONFIGPATH']   + '"' + os.linesep,
                    'set DOCX_COPYRIGHT="'    + os.environ['DOCX_COPYRIGHT']    + '"' + os.linesep,
                    'set DOCX_DEBUGAPIDOC="'  + os.environ['DOCX_DEBUGAPIDOC']  + '"' + os.linesep,
                    'set DOCX_DEBUGAPIREL="'  + os.environ['DOCX_DEBUGAPIREL']  + '"' + os.linesep,
                    'set DOCX_DOCNAME="'      + os.environ['DOCX_DOCNAME']      + '"' + os.linesep,
                    'set DOCX_DOCSRC="'       + os.environ['DOCX_DOCSRC']       + '"' + os.linesep,
                    'set DOCX_DOCTEMPLATE="'  + os.environ['DOCX_DOCTEMPLATE']  + '"' + os.linesep,
                    'set DOCX_DOCTYPE="'      + os.environ['DOCX_DOCTYPE']      + '"' + os.linesep,
                    'set DOCX_EMBED="'        + os.environ['DOCX_EMBED']        + '"' + os.linesep,
                    'set DOCX_GENDOC="'       + os.environ['DOCX_GENDOC']       + '"' + os.linesep,
                    'set DOCX_INDEXSRC="'     + os.environ['DOCX_INDEXSRC']     + '"' + os.linesep,
                    'set DOCX_LIB="'          + os.environ['DOCX_LIB']          + '"' + os.linesep,
                    'set DOCX_LICENSE="'      + os.environ['DOCX_LICENSE']      + '"' + os.linesep,
                    'set DOCX_MISSION="'      + os.environ['DOCX_MISSION']      + '"' + os.linesep,
                    'set DOCX_NAME="'         + os.environ['DOCX_NAME']         + '"' + os.linesep,
                    'set DOCX_NOEXEC="'       + os.environ['DOCX_NOEXEC']       + '"' + os.linesep,
                    'set DOCX_RELEASE="'      + os.environ['DOCX_RELEASE']      + '"' + os.linesep,
                    'set DOCX_SRCDIR="'       + os.environ['DOCX_SRCDIR']       + '"' + os.linesep,
                    'set DOCX_STATUS="'       + os.environ['DOCX_STATUS']       + '"' + os.linesep,
                    'set DOCX_VERBOSE="'      + os.environ['DOCX_VERBOSE']      + '"' + os.linesep,
                    'set DOCX_VERBOSEAPIDOC="'+ os.environ['DOCX_VERBOSEAPIDOC']+ '"' + os.linesep,
                    'set DOCX_VERBOSEAPIREL="'+ os.environ['DOCX_VERBOSEAPIREL']+ '"' + os.linesep,
                    'set DOCX_VERBOSEX="'     + os.environ['DOCX_VERBOSEX']     + '"' + os.linesep,
                    'set DOCX_VERSION="'      + os.environ['DOCX_VERSION']      + '"' + os.linesep,
                    )
                )

        if self.noexec or self.verbose > 1:
            print()
            print("Environ:")
            print("   DOCX_APIDOC         = " + str(os.environ['DOCX_APIDOC']))
            print("   DOCX_APIREF         = " + str(self.apiref))
            print("   DOCX_AUTHOR         = " + str(os.environ['DOCX_AUTHOR']))
            print("   DOCX_BREAKONERR     = " + str(self.break_on_err))
            print("   DOCX_BUILDDIR       = " + str(self.build_dir))
            print("   DOCX_BUILDER        = " + str(self.builder))
            print("   DOCX_BUILDRELDIR    = " + str(self.build_reldir))
            print("   DOCX_CLEAN          = " + str(self.clean))
            print("   DOCX_CONFIGPATH     = " + str(self.config_path))
            print("   DOCX_COPYRIGHT      = " + str(self.copyright))
            print("   DOCX_DEBUGAPIDOC    = " + str(self.debug_apidoc))
            print("   DOCX_DEBUGAPIREF    = " + str(self.debug_apiref))
            print("   DOCX_DOCNAME        = " + str(self.docname))
            print("   DOCX_DOCSRC         = " + str(self.docsource))
            print("   DOCX_DOCTEMPLATE    = " + str(self.doctemplate))
            print("   DOCX_DOCTYPE        = " + str(self.doctype))
            print("   DOCX_EMBED          = " + str(os.environ['DOCX_EMBED']))
            print("   DOCX_GENDOC         = " + str(self.gendoc))
            print("   DOCX_INDEXSRC       = " + str(self.indexsrc))
            print("   DOCX_LIB            = " + str(os.environ['DOCX_LIB']))
            print("   DOCX_LICENSE        = " + str(os.environ['DOCX_LICENSE']))
            print("   DOCX_MISSION        = " + str(os.environ['DOCX_MISSION']))
            print("   DOCX_NAME           = " + str(self.name))
            print("   DOCX_NOEXEC         = " + str(self.noexec))
            print("   DOCX_QUIET          = " + str(self.quiet))
            print("   DOCX_RELEASE        = " + str(self.set_release))
            print("   DOCX_SRCDIR         = " + str(self.srcdir))
            print("   DOCX_STATUS         = " + str(os.environ['DOCX_STATUS']))
            print("   DOCX_VERBOSE        = " + str(self.verbose0))
            print("   DOCX_VERBOSEAPIDOC  = " + str(self.verbose_apidoc))
            print("   DOCX_VERBOSEAPIREF  = " + str(self.verbose_apiref))
            print("   DOCX_VERBOSEX       = " + str(self.verbose_ext))
            print("   DOCX_VERSION        = " + str(self.set_version))
    

    def call_prologue(self):
        """Executed before the call of the wrapper. 
        
        The default version supports *Sphinx* and writes the project 
        data into the file '<build-dir>/<build-reldir>/project.rst'.
        Replace this method in the derived class as required. 
        """
        
        #
        # write project data into 'project.rst'
        #
        _fpath = self.build_doc_path + os.sep + 'project.rst'
        with open(_fpath, 'w') as _f:
            _f.writelines(
                (
                    '**Product Data**' + os.linesep + os.linesep,
                    '* MISSION='       + self.description + os.linesep + os.linesep,
                    '* AUTHOR='        + self.author + os.linesep + os.linesep,
                    '* PROJECT='       + self.name + os.linesep + os.linesep,
                    '* COPYRIGHT='     + self.copyright + os.linesep + os.linesep,
                    '* LICENSE='       + self.license + os.linesep + os.linesep,
                    '* VERSION='       + self.version + os.linesep + os.linesep,
                    '* RELEASE='       + self.release + os.linesep + os.linesep,
                    '* STATUS='        + self.status + os.linesep + os.linesep,
                    '* BUILDDATE='     + self.builddate + os.linesep + os.linesep,
                    )
                )
            
    
    def call_epilogue(self):
        """Executed after the call of the wrapper. 
        """
        pass
