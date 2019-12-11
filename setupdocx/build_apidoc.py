#-*- coding: utf-8 -*-
"""Extract inline API documentation for the compilation with *build_docx*.
Optionally generate API only documentation by easy application of various 
standard and custom templates. 
"""
from __future__ import absolute_import
from __future__ import print_function

import sys
import os
import time
import shutil
import json
import re

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


class SetuplibBuildApidocError(setupdocx.SetupDocXError):
    """Error on build apidoc.
    """
    pass


class SetuplibBuildApidocSetupError(SetuplibBuildApidocError):
    """Erroneous builder tool setup.
    """
    pass


class SetuplibBuildApidocConfError(SetuplibBuildApidocError):
    """Erroneous configuration of templates/styles for the builder .
    """
    pass


class BuildApidocX(distutils.cmd.Command):
    """Create API inline documentation by usage of the defined builder."""

    description = 'Create API inline documentation.'
    user_options = [
        ('builder=',              None, "The builder to be used for the processing of the inline documentation. "
                                        "See '--help-builder'. "
                                        "Default: 'sphinx'"),
        ('builder-path=',         None, "The directory path of the builder. "
                                        "Default: '<SETUPDOCX-PYTHONPATH>/setupdocx/builder/'"),
        ('build-dir=',            None, "The name of the build directory. "
                                        "Default: 'build/'"),
        ('build-reldir=',         None, "The name of the relative build subdirectory."
                                        " Default: '<builder>/apidoc/'"),
        ('clean',                 None, "Removes the cached previous build. Default: False"),
        ('clean-all',             None, "Removes the complete build directory before calling the wrapper. "
                                        "Default: '<build-dir>/apidoc'."),
        ('config-path=',          None, "The directory path containing the assigned configurations. "
                                        "See '--list-templates-std' and '--list-templates'. "
                                        "Default: 'config/<builder>/:<docsource>/config/<builder>/'. "),
        ('debug',                 'd',  "Raises degree of debug traces of current context. Supports repetition. "
                                        "Each raises the command verbosity level of the context by one."),
        ('docname=',              None, "The document output name. "
                                        "Default: attribute of derived class self.name"),
        ('docsource=',            None, "The name of the document source directory. "
                                        "Default: 'docsrc/'"),
        ('doctemplate=',          None, "The design template to be used. A valid entry within '<config-path>/'. "
                                        "Default: 'alabaster'."),
        ('doctype=',              None, "The final document type to create. this requires '--gendoc' for activation."
                                        "See '--list-doctypes'. "
                                        "Default: 'html', "),
        ('executable=',           None, "The executable called by the wrapper. "
                                        "Supports relative and absolute file path names. "
                                        "Default: 'sphinx-apidoc'"),
        ('executableopts=',       None, "Additional options to be passed to the executable. "
                                        "Default: ''"),
        ('executableopts-reset',  None, "Initialize empty options for the called executable. "
                                        "Default: 'False'"),
        ('gendoc',                'r',  "Create complete API document. The default is to create the 'rst' files only. "
                                        "Default: off"),
        ('indexsrc=',             None, "The source file to be copied as 'index.rst'. "
                                        "Default: 'index.rst'"),
        ('list-doctypes',         None, "List of available types of document formats."),
        ('list-metatypes',        None, "List of available types of meta formats."),
        ('list-templates-std',    None, "List provided configuration templates."),
        ('list-templates=',       None, "Lists the configuration templates with filter parameter, see manuals. "
                                        "Online help is evailable by the parameter 'list-templates=help'. "
                                        "Default: same as '--list-templates-std'"),
        ('metatype=',             None, "The meta document type to create to be added to the document sources. "
                                        "See '--list-metatypes'. "
                                        "Default: 'rst', "),
        ('name=',                 None, "The name of the package. "
                                        "Default: attribute of derived class 'self.name'"),
        ('noexec=',               None, "Print the call of the selected level only, do not execute. "
                                        "The value is an integer, decremented by each level until '0', "                                        "which is the level to be printed. "
                                        "The option is different from he global '--dry-run' options, as it "
                                        "has to handle multiple call levels of subprocesses."),
        ('quiet',                 'q',  "Quiet the current context, resets verbosity of applied context to '0'. "
                                        "This is the enforced global option, which is the negative option "
                                        "of '--verbose'. "
                                        "Default: off"),
        ('raw',                   None, "If present uses the raw document output from the API generation, "
                                        "else copies from configuration template. "
                                        "Default: off"),
        ('srcdir=',               None, "Source directory."),
        ('set-release=',          None, "The release of the package."),
        ('set-version=',          None, "The version of the package. "
                                        "Default: attribute of derived class self.distribution.metadata.version"),
        ('wrapper=',              None, "The wrapper called by the builder. "
                                        "Supports pure file names only. "
                                        "Default: 'call_apidoc.sh'"),
        ('wrapperopts=',          None, "Additional options to be passed to the called wrapper. "
                                        "Default: ''"),
        ('wrapperopts-reset',     None, "Drop generated options for the wrapper, does not effect environment. "
                                        "Default: 'False'"),
        ('verbose',               'v',  "Raises verbosity of current context. Supports repetition. "
                                        "Each raises the command verbosity level of the context by one. "
                                        "The value is defined by the global option defined in "
                                        "'Distribution'. "
                                        "Refer to the manuals for the special behaviour when used as "
                                        "either a global option(start 'verbose=1'), "
                                        "or as a command context option(start 'verbose=0'). "
                                        "Default:=1."),
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

    def initialize_options(self):
        """API of 'distutils'.
        
        REMARK: verbose and debug are encapsulated/hidden by distutils.
        """
        self.verbose = None
        self.debug = None
        self.quiet = None

        self.build_dir = None
        self.build_reldir = None
        self.builder = None
        self.builder_path = None
        self.clean = None
        self.clean_all = None
        self.config_path = None
        self.docname = None
        self.docsource = None
        self.doctemplate = None
        self.doctype = None
        self.executable = None
        self.executableopts = None
        self.executableopts_reset = None
        self.gendoc = None
        self.indexsrc = None
        self.list_doctypes = None
        self.list_metatypes = None
        self.list_templates = None
        self.list_templates_std = None
        self.metatype = None
        self.name = None
        self.noexec = None
        self.raw = None
        self.set_release = None
        self.set_version = None
        self.srcdir = None
        self.wrapper = None
        self.wrapperopts = None
        self.wrapperopts_reset = None

    def set_builder_data(self, fpname):
        """Initializes the hard-coded static values first, than
        reads the configuration file - if present - and superposes
        present values. 
        
        The configuration file is expected to be located within 
        the builder directory.
        
        Args:
            fpname:
                The file or directory path name of the setup.
                File path names are treated literally, while
                directory names are scanned for::

                    capabilities.<ext>
                    
                    ext := (json)
                    # Current version supports JSON only.
                
        Returns:
            Loaded configutation 'capabilities'.

        Raises:
            SetuplibBuildApidocSetupError
            
            pass-through
            
        """
        if fpname and os.path.isfile(fpname):
            # file path name is provided
            
            if os.path.splitext(fpname)[1] != 'json':
                raise SetuplibBuildApidocSetupError(
                    "Current version supports JSON only, got: " 
                    + str(os.path.splitext(fpname))
                    )
            
            with open(fpname) as data_file:  # load data
                self.capabilities = json.load(data_file)
        
        elif fpname and os.path.isdir(fpname):
            # director path is provided
            
            _f = fpname + os.sep + 'capabilities.json'
            if not os.path.isfile(_f):
                raise SetuplibBuildApidocSetupError(
                    "Missing setup file: " 
                    + str(_f)
                    )
            
            with open(_f) as data_file:  # load data
                self.capabilities.data = json.load(data_file)
        
        else:
            raise SetuplibBuildApidocSetupError(
                "Setup of builder requires either a file or a directory: " 
                + str(fpname)
                )


    def finalize_options(self):
        """API of 'distutils'.

        Args:
            none
                
        Returns:
            none

        Raises:
            SetuplibBuildApidocSetupError

            SetuplibBuildApidocError

            pass-through
        """

        # scan for any context-help request - despite the following prepared more detailed
        if not (
                self.list_templates and self.list_templates.endswith('help')
            ): 
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


        # raw
        if self.raw == None:
            self.raw = 0
        else:
            self.raw = 1

        #
        # current builder
        #
        if self.builder == None:
            self.builder = 'sphinx'

        attr_searchpath=(self.builder, 'apidoc',)

        #
        # user has provided setup directory for builder - so load first new defaults
        #
        if self.builder_path != None:
            if not os.path.isdir(self.builder_path):
                raise SetuplibBuildApidocSetupError('Missing --builder-path=' + str(self.builder_path))
            self.builder_path = os.path.normpath(self.builder_path) + os.sep
            self.set_builder_data(self.builder_path + self.builder)

        else:
            self.builder_path = os.path.dirname(__file__) + os.sep + 'builder' + os.sep
            self.set_builder_data(self.builder_path + self.builder)


        #
        # validate consistency of current builder and defaults
        #
        if self.builder != self.capabilities('builder', 'name'):
            raise SetuplibBuildApidocSetupError(
                'Inconsistent builder:\nbuilder:  %s\ndefaults: %s\n\nCheck:     %s' %(
                    str(self.builder),
                    str(self.capabilities('builder', 'name')),
                    str(self.builder_path + self.builder)
                )
            )


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
            raise SetuplibBuildApidocConfError(
                'Missing template path "--config-path=%s"' % (str(self.config_path),))
        else:
            _oneok = False
            _onedirok = False
            for f in self.config_path.split(os.pathsep):
                if os.path.isdir(f):
                    _onedirok = True
                    if self.doctemplate:
                        fp = f + os.sep + self.doctemplate
                    else:
                        fp = f + os.sep
                    if os.path.isdir(fp):
                        self.config_path = f
                        _oneok = True
            if not _oneok:
                if not _onedirok:
                    raise SetuplibBuildApidocConfError(
                        'Missing configuration template directory, got "--config-path=%s"' %( 
                            str(self.config_path)
                        )
                    )
                else:
                    raise SetuplibBuildApidocConfError(
                        '\n\nCannot find configuration template:\n' 
                        '   template name:  %s\n' 
                        '   search path:    %s\n' 
                        '\n' 
                        'Check options "--list-templates-std / --list-templates"\n' %( 
                            str(self.doctemplate),
                            str(self.config_path),
                        )
                    )
#         if self.config_path == None:
#             self.config_path = self.capabilities(
#                     'defaults', 'config_path',
#                     searchpath=attr_searchpath
#                 )
#             if self.config_path == None:
#                 self.config_path = 'config' + os.sep + self.builder
#                 self.config_path += os.pathsep + os.path.dirname(__file__) + os.sep + 'config' + os.sep + self.builder
# 
#         elif not self.config_path:
#             raise SetuplibBuildApidocConfError(
#                 'Missing --config-path=' + str(self.config_path))
#         else:
#             if not os.path.isdir(self.config_path):
#                 raise SetuplibBuildApidocConfError(
#                     'Requires directory, got --config-path=' + str(self.config_path))


        #
        # set source directory of document
        #
        if self.docsource == None:
            self.docsource = self.capabilities(
                'defaults', 'docsource', searchpath=attr_searchpath)
            if self.docsource == None:
                self.docsource = 'docsrc'
        if self.docsource:
            # set directory for pre-edited document components
            if not os.path.exists(self.docsource):
                raise SetuplibBuildApidocError("missing docsrc:" + str(self.docsource))
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
                    raise SetuplibBuildApidocError(
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
                
            #
            # show templates
            #
            if _kargs.get('depth') == None:
                setupdocx.conf_list(depth=2, **_kargs)  # show a bit more than top-level - for new users
                sys.exit(0)

#             elif str(_kargs.get('depth')) == '0':
#                 _kargs.pop('depth')

            setupdocx.conf_list(**_kargs)
            sys.exit(0)

#         #
#         # show templates with filters
#         #
#         if self.list_templates != None:
#             _kargs = {}
#             _args = ''
# 
# #     _sep = kargs.get('separator', 0)
# #     _sep = re.sub(r'(.*?)[\\\\]{0,1}(?<=[\\\\]);', r'\1;', _sep)
# 
#             # mask the suboption separator 
# #            for ai in re.split(r'(?<![\\\\]);', self.list_templates):
#             for ai in re.split(r'(?<![\[]);(?![\]])', self.list_templates):
#                 if ai:
#                     try:
#                         _k, _v = ai.split('=')
#                         if _k == 'baselist':
#                             _v = _v.split(os.pathsep)
#                         _kargs[_k] = _v
#                     except ValueError:
#                         # sort out some options without value
#                         if ai == 'all':
#                             # list empty builder too
#                             _kargs['all'] = True
#                         
#                         # add arguments
#                         else:
#                             _args += ',' + ai
# 
#             if _args.endswith(',help'):
#                 _h = """
# Supports the keyword arguments of 'setupdocx.conf_list'.
# 
# The keyword parameter 'filter' could be replaced by a comma separated
# list of arguments to be assembled into a filter rule.
# 
# *args=<list-of-OR-parts-python-re-expression>*
#   Example::
# 
#     input:
#        args := 'agogo,alabas.*'
# 
#     rule:
#        args-rule := '(agogo|alabas.*)'
# 
# *filter=<python-re-expression>*
# 
#     input:
#        filter := 'filter=(agogo|alabas.*)'
# 
#     rule:
#        args-rule := '(agogo|alabas.*)'
#  
# The keyword parameter 'filter' provides for a wider range of rule syntaxes, 
# while the 'args' list offers simplicity for casual calls.
# 
# The call without parameters is the same as the option '--list-templates-std'. 
# The 'setupdocx.conf_list' parameters provided for the user interface are:
# 
#     setupdocx.conf_list
#     ===================
# 
#     """
#                 # help(setupdocx.conf_list)
#                 print(_h + setupdocx.conf_list.__doc__)
#                 sys.exit(0)
#                 
#             _filters = None
#             if _args:
#                 _filters = [x for x in _args.split(',') if x]
#                 if len(_filters) > 1:
#                     _filter = '(' + '|'.join(_filters) + ')'
#                 else:
#                     _filter = _filters[0]
# 
#             if 'filter' in _kargs:
#                 if _filters:
#                     raise SetuplibBuildApidocError(
#                         "Filters could be provided either by args as a comma separated list "
#                         "of partial 're' rules internallz converted to a single rule, "
#                         "or by the 'filters=' option as a single final Python-regular "
#                         "expression. The resulting rule is compiled by 're.compile()'. "
#                         "Got:\n"
#                         "   args:    %s\n"
#                         "   filters: %s\n" % (
#                             str(_filters),
#                             str(_kargs['filter']),
#                             )
#                         )
#             elif _filters:
#                 _kargs['filter'] = _filter
# 
# #                _filter_re = re.compile(_kargs['filter'])
# 
# #             if not _filters:
# #                 _filter_re =  None
#                 
#             setupdocx.conf_list([self.config_path], **_kargs)
#             sys.exit(0)


        #
        # show doctypes
        #
        if self.list_doctypes != None:
            print(
                "Known document types for API only documentation. These are activated by '--gendoc':"
                )
            print()

            _dtypes = list(self.capabilities('doctypes', searchpath=attr_searchpath))[:]
            for _dt in _dtypes:
                print("  {dtype:<20} --doctype={dtype}".format(dtype=str(_dt)))
            print()
            print(
                "Note: For metaformats refer to '--list-metatypes'."
                )
            print()
                
            sys.exit(0)


        #
        # show metatypes
        #
        if self.list_metatypes != None:
            print("Known meta types for documents:")
            print()
            _mtypes = list(self.capabilities('metatypes', searchpath=attr_searchpath))[:]
            for _mt in _mtypes:
                print("  {mtype:<20} --metatype={mtype}".format(mtype=str(_mt)))
            print()
            print(
                "Note: For docformats of API only documentation refer to '--list-doctypes'."
                )
            print()
                
            sys.exit(0)


        #
        # common top of build directory for output
        #
        if self.build_dir == None:
            self.build_dir = self.capabilities('defaults', 'build_dir', searchpath=attr_searchpath)
            if not self.build_dir:
                self.build_dir = 'build'


        #
        # subdirectory of build for output
        #
        if self.build_reldir == None:
            self.build_reldir = self.capabilities('defaults', 'build_reldir', searchpath=attr_searchpath)
            if not self.build_reldir:
                self.build_reldir = 'sphinx/apidoc/'

        # the complete path for the assembled document sources to be processed 
        self.build_doc_path = os.path.normpath(self.build_dir + os.sep + self.build_reldir)


        #
        # clean-all - removes complete build subdirectory
        #
        if self.clean_all == None:
            # self.clean_all = self.capabilities.data[self.builder]['apidoc']['defaults']['clean-all']
            self.clean_all = self.capabilities('defaults', 'clean_all', searchpath=attr_searchpath)
            if not self.clean_all:
                self.clean_all =  0
            else:
                self.clean_all = 1
        else:
            self.clean_all = True

        #
        # clean - removes pre-artifacts
        #
        if self.clean == None:
            self.clean = self.capabilities('defaults', 'clean', searchpath=attr_searchpath)
            if not self.clean:
                self.clean = 0
            else:
                self.clean = 1
        else:
            self.clean = 1


        #
        # raw output from the executed tool only, e.g. sphinx-apidoc
        #
        if self.gendoc == None:
            self.gendoc = 0
        else:
            self.gendoc = 1


        #
        # name - from metadata
        #
        if self.name == None:
            self.name = self.distribution.metadata.name


        #
        # document name - default from metadata
        #
        if self.docname == None:
            self.docname = self.capabilities('defaults', 'docname', searchpath=attr_searchpath)
            if self.docname == None:
                self.docname = self.name


        #
        # document template to be used
        #
        if self.doctemplate == None:
            self.doctemplate = self.capabilities('defaults', 'template', searchpath=attr_searchpath)
        if not self.doctemplate:
            # final default
            self.doctemplate = ''  # default:=alabaster


        #
        # document type to be created
        #
        if self.doctype == None:
            self.doctype = self.capabilities('defaults', 'doctype', searchpath=attr_searchpath)
        if not self.doctype:
            # final default
            self.doctype = 'html'
        # some alias
        if self.doctype == 'pdf':
            self.doctype = 'latexpdf'

        #
        # custom index file appropriate to the doctype option,
        # in case of e.g. 'builder=sphinx' => 'indexsrc=rst' 
        #
        if self.indexsrc == None:
            self.indexsrc = self.capabilities('defaults', 'indexsrc', searchpath=attr_searchpath)
            if self.indexsrc == None:
                self.indexsrc = ''


        #
        # directory containing the source code
        #
        if self.srcdir == None:
            self.srcdir = self.capabilities('defaults', 'srcdir', searchpath=attr_searchpath)
            if self.srcdir == None:
                self.srcdir = self.name
            else:
                if type(self.srcdir) is (list, tuple,):
                    self.srcdir = ';'.join(self.srcdir)


        #
        # do not execute - just display call
        # effects top-level only
        #
        if self.noexec != None:
            self.noexec = int(self.noexec)
        else:
            self.noexec = 0

        if self.verbose == None:
            self.verbose0 = 0
        else:
            self.verbose0 = self.verbose 

        if self.debug == None:
            self.debug0 = 0
        else:
            self.debug0 = self.debug 



        #
        # executable - default is sphinx-apidoc
        #
        if self.executable == None:
            self.executable = self.capabilities('defaults', 'executable', searchpath=attr_searchpath)
            if self.executable == None:
                self.executable = 'sphinx-apidoc'
            elif self.executable == '':
                raise SetuplibBuildApidocSetupError(
                    "Requires executable: --executable"
                    )

        #
        # executableopts_reset - reset options before adding new options
        #
        if self.executableopts_reset == None:
            self.executableopts_reset = self.capabilities(
                'defaults', 'executableopts_reset', searchpath=attr_searchpath)
            if not self.executableopts_reset:
                self.executableopts_reset = 0
            elif self.executableopts_reset:
                self.executableopts_reset = 1


        #
        # executableopts - additional options to be passed to executable
        #
        if not self.executableopts:
            self.executableopts = self.capabilities(
                'defaults', 'executableopts', searchpath=attr_searchpath)
            if self.executableopts == None:
                self.executableopts = ''


        #
        # wrapper - default is call_apidoc.sh
        #
        if self.wrapper == None:
            self.wrapper = self.capabilities(
                'defaults', 'wrapper', searchpath=attr_searchpath)
            if self.wrapper == None:
                self.wrapper = 'call_apidoc.sh'
            elif self.wrapper == '':
                raise SetuplibBuildApidocSetupError(
                    "Requires wrapper: --wrapper"
                    )


        #
        # wrapperopts - additional options to be passed to wrapper
        #
        if self.wrapperopts_reset == None:
            self.wrapperopts_reset = self.capabilities(
                'defaults', 'wrapperopts_reset', searchpath=attr_searchpath)
            if not self.wrapperopts_reset:
                self.wrapperopts_reset = 0
            else:
                self.wrapperopts_reset = 1

        if self.wrapperopts_reset:
            self.wrapperopts = '1' 
        else:
            #
            # wrapperopts - additional options to be passed to executable
            #
            if self.wrapperopts == None:
                self.wrapperopts = self.capabilities(
                    'defaults', 'wrapperopts', searchpath=attr_searchpath)
                if self.wrapperopts == None:
                    self.wrapperopts = ''


        #
        # set version of document
        #
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


        #
        # set release of document
        #
        if self.set_release == None:
            try:
                if self.release == None:
                    self.release = ''
            except:
                self.release = self.version
        else:
            self.release = self.set_release 


        self.builddate = time.strftime("%Y.%m.%d-%H:%M", time.gmtime())
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

    def run(self):
        """Creates documents.
        Calls the defined and activated wrapper scripts.
        The call flow could be customized by various 
        interfaces. ::
        
                I.      self.set_environment()    # could be superposed by derived class
                II.     self.call_prologue()       # could be superposed by derived class 
                III.    subprocesses:
                    1.    builder_path.sh          # could be arbitrary custom call wrapper
                    2.    build_docx.sh            # could be arbitrary custom call wrapper
                    3.    build_apiref.sh          # could be arbitrary custom call wrapper
                IV.     self.call_epilogue()       # could be superposed by derived class

        """
        #
        # clean
        #
        if self.clean_all:
            # clean the complete build directory
            if self.verbose > 2:
                print('shutil.rmtree(%s, True)' % (self.build_dir))
            shutil.rmtree(self.build_dir, True)

        elif self.clean:
            # clean build directory of apidoc - build/<builder>/apidoc
            if self.verbose > 2:
                print('shutil.rmtree(%s, True)' % (self.build_doc_path))
            shutil.rmtree(self.build_doc_path, True)


        # create when missing
        if not os.path.exists(self.build_doc_path):
            os.makedirs(self.build_doc_path)
        elif not os.path.isdir(self.build_doc_path):
            raise SetuplibBuildApidocError(
                "File present with target dirname: "
                + str(self.build_doc_path)
                )


        #
        # call string of apidoc wrapper for subprocess
        #
        command_apidoc = []
        if self.builder_path:
            command_apidoc.append(self.builder_path + self.builder + os.sep + self.wrapper)
        elif self.verbose > 1:
            command_apidoc.append(self.wrapper)
            sys.stdout.write("skip : builder_path\n")

        command_apidoc.append(self.wrapperopts)
        
        if self.noexec == 1  or self.verbose > 1 or self.debug:
            print()
            print("build_apidoc:Capabilities: ")
            print("   capabilities  = " 
                  + str(self.builder_path + self.builder + os.sep + 'capabilities.json'))
             
            print()
            print("build_apidoc:Scripts: ")
            print("   builder_path  = " + str(self.builder_path))

            print()
            print("build_apidoc:Calls: ")
            print("   " + ' '.join(command_apidoc))
                 
            print()
            print("build_apidoc:Configuration path: ")
            print("   config_path   = " + str(os.path.abspath(self.config_path)))

            print()
 
            if self.noexec > 0:
                sys.exit(0)


        #
        # decrement counter for passing to the next level
        #
        if self.noexec > 0:
            self.noexec -= 1

        self.call_prologue()

        if self.verbose or self.debug:
            print("build_apidoc:Calling wrapper " + str(' '.join(command_apidoc)))
            print()
        exit_code = os.system(' '.join(command_apidoc)) # create apidoc
        if self.verbose or self.debug:
            print()
            print("Finished: %s => exit=%s\n\n" % (
                str(' '.join(command_apidoc)), str(exit_code)))
            print()

        self.call_epilogue()

    def set_environment(self):
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
        os.environ['DOCX_AUTHOR'] = self.author
        os.environ['DOCX_BUILDDIR'] = self.build_dir
        os.environ['DOCX_BUILDER'] = self.builder
        os.environ['DOCX_BUILDRELDIR'] = self.build_reldir
        os.environ['DOCX_CLEAN'] = str(self.clean)
        os.environ['DOCX_CONFIGPATH'] = self.config_path
        os.environ['DOCX_COPYRIGHT'] = self.copyright
        os.environ['DOCX_DEBUG'] = str(self.debug0)
        os.environ['DOCX_DOCNAME'] = self.docname
        os.environ['DOCX_DOCSRC'] = self.docsource
        os.environ['DOCX_DOCTEMPLATE'] = self.doctemplate
        os.environ['DOCX_DOCTYPE'] = self.doctype 
        os.environ['DOCX_EMBED'] = '1' 
        os.environ['DOCX_EXEC'] = str(self.executable)
        os.environ['DOCX_EXECOPTS'] = str(self.executableopts)
        os.environ['DOCX_EXECOPTS_RESET'] = str(self.executableopts_reset)
        os.environ['DOCX_GENDOC'] = str(self.gendoc)
        os.environ['DOCX_INDEXSRC'] = self.indexsrc
        os.environ['DOCX_LIB'] = os.path.abspath(os.path.dirname(__file__))
        os.environ['DOCX_LICENSE'] = self.license
        os.environ['DOCX_MISSION'] = self.description
        os.environ['DOCX_NAME'] = self.name
        os.environ['DOCX_NOEXEC'] = str(self.noexec)
        os.environ['DOCX_QUIET'] = str(self.quiet)
        os.environ['DOCX_RAWDOC'] = str(self.raw)
        os.environ['DOCX_SRCDIR'] = self.srcdir
        os.environ['DOCX_STATUS'] = self.status
        os.environ['DOCX_VERBOSE'] = str(self.verbose0)
        os.environ['DOCX_WRAPPER'] = str(self.wrapper)
        os.environ['DOCX_WRAPPEROPTS'] = str(self.wrapperopts)
        os.environ['DOCX_WRAPPEROPTS_RESET'] = str(self.wrapperopts_reset)

        os.environ['DOCX_VERSION'] = self.version
        if self.set_release:
            os.environ['DOCX_RELEASE'] = self.release
        else:
            os.environ['DOCX_RELEASE'] = self.version


        if self.noexec or self.verbose > 1 or self.debug > 0:
            print()
            print("build_apidoc:Call environment parameters:")
            print("   DOCX_AUTHOR             = " + str(os.environ['DOCX_AUTHOR']))
            print("   DOCX_BUILDDIR           = " + str(self.build_dir))
            print("   DOCX_BUILDER            = " + str(self.builder))
            print("   DOCX_BUILDRELDIR        = " + str(self.build_reldir))
            print("   DOCX_CLEAN              = " + str(self.clean))
            print("   DOCX_CONFIGPATH         = " + str(self.config_path))
            print("   DOCX_COPYRIGHT          = " + str(self.copyright))
            print("   DOCX_DEBUG              = " + str(self.debug0))
            print("   DOCX_DOCNAME            = " + str(self.docname))
            print("   DOCX_DOCSRC             = " + str(self.docsource))
            print("   DOCX_DOCTEMPLATE        = " + str(self.doctemplate))
            print("   DOCX_DOCTYPE            = " + str(self.doctype))
            print("   DOCX_EMBED              = " + str(os.environ['DOCX_EMBED']))
            print("   DOCX_EXEC               = " + str(self.executable))
            print("   DOCX_EXECOPTS           = " + str(self.executableopts))
            print("   DOCX_EXECOPTS_RESET     = " + str(self.executableopts_reset))
            print("   DOCX_GENDOC             = " + str(self.gendoc))
            print("   DOCX_INDEXSRC           = " + str(self.indexsrc))
            print("   DOCX_LIB                = " + str(os.environ['DOCX_LIB']))
            print("   DOCX_LICENSE            = " + str(os.environ['DOCX_LICENSE']))
            print("   DOCX_MISSION            = " + str(os.environ['DOCX_MISSION']))
            print("   DOCX_NAME               = " + str(self.name))
            print("   DOCX_NOEXEC             = " + str(self.noexec))
            print("   DOCX_QUIET              = " + str(self.quiet))
            print("   DOCX_RAWDOC             = " + str(self.raw))
            print("   DOCX_RELEASE            = " + str(self.release))
            print("   DOCX_SRCDIR             = " + str(self.srcdir))
            print("   DOCX_STATUS             = " + str(os.environ['DOCX_STATUS']))
            print("   DOCX_VERBOSE            = " + str(self.verbose0))
            print("   DOCX_VERSION            = " + str(self.version))
            print("   DOCX_WRAPPER            = " + str(self.wrapper))
            print("   DOCX_WRAPPEROPTS        = " + str(self.wrapperopts))
            print("   DOCX_WRAPPEROPTS_RESET  = " + str(self.wrapperopts_reset))
            print()
            
    def write_environment_setter(self):
        """Writes the environment previously set by 'self.set_environment'
        into shell scripts to be optionally sourced when the wrapper is
        manually called from the command line.
        
        ATTENTION: 'self.set_environment' must be called before.
        
        """
        try:
            os.makedirs(self.build_doc_path)
        except:
            pass
        _fpath = self.build_doc_path + os.sep + 'setenv.sh'
        with open(_fpath, 'w') as _f:
            _f.writelines(
                (
                    'DOCX_AUTHOR="'             + os.environ['DOCX_AUTHOR']              + '"; export DOCX_AUTHOR;'             + os.linesep,
                    'DOCX_BUILDDIR="'           + os.environ['DOCX_BUILDDIR']            + '"; export DOCX_BUILDDIR;'           + os.linesep,
                    'DOCX_BUILDER="'            + os.environ['DOCX_BUILDER']             + '"; export DOCX_BUILDER;'            + os.linesep,
                    'DOCX_BUILDRELDIR="'        + os.environ['DOCX_BUILDRELDIR']         + '"; export DOCX_BUILDRELDIR;'        + os.linesep,
                    'DOCX_CLEAN="'              + os.environ['DOCX_CLEAN']               + '"; export DOCX_CLEAN'               + os.linesep,
                    'DOCX_CONFIGPATH="'         + os.environ['DOCX_CONFIGPATH']          + '"; export DOCX_CONFIGPATH'          + os.linesep,
                    'DOCX_COPYRIGHT="'          + os.environ['DOCX_COPYRIGHT']           + '"; export DOCX_COPYRIGHT;'          + os.linesep,
                    'DOCX_DEBUG="'              + os.environ['DOCX_DEBUG']               + '"; export DOCX_DEBUG'               + os.linesep,
                    'DOCX_DOCNAME="'            + os.environ['DOCX_DOCNAME']             + '"; export DOCX_DOCNAME'             + os.linesep,
                    'DOCX_DOCSRC="'             + os.environ['DOCX_DOCSRC']              + '"; export DOCX_DOCSRC'              + os.linesep,
                    'DOCX_DOCTEMPLATE="'        + os.environ['DOCX_DOCTEMPLATE']         + '"; export DOCX_DOCTEMPLATE;'        + os.linesep,
                    'DOCX_DOCTYPE="'            + os.environ['DOCX_DOCTYPE']             + '"; export DOCX_DOCTYPE'             + os.linesep,
                    'DOCX_EMBED="'              + os.environ['DOCX_EMBED']               + '"; export DOCX_EMBED'               + os.linesep,
                    'DOCX_EXEC="'               + os.environ['DOCX_EXEC']                + '"; export DOCX_EXEC'                + os.linesep,
                    'DOCX_EXECOPTS="'           + os.environ['DOCX_EXECOPTS']            + '"; export DOCX_EXECOPTS'            + os.linesep,
                    'DOCX_EXECOPTS_RESET="'     + os.environ['DOCX_EXECOPTS_RESET']      + '"; export DOCX_EXECOPTS_RESET'      + os.linesep,
                    'DOCX_GENDOC="'             + os.environ['DOCX_GENDOC']              + '"; export DOCX_GENDOC'              + os.linesep,
                    'DOCX_INDEXSRC="'           + os.environ['DOCX_INDEXSRC']            + '"; export DOCX_INDEXSRC'            + os.linesep,
                    'DOCX_LIB="'                + os.environ['DOCX_LIB']                 + '"; export DOCX_LIB'                 + os.linesep,
                    'DOCX_LICENSE="'            + os.environ['DOCX_LICENSE']             + '"; export DOCX_LICENSE;'            + os.linesep,
                    'DOCX_MISSION="'            + os.environ['DOCX_MISSION']             + '"; export DOCX_MISSION;'            + os.linesep,
                    'DOCX_NAME="'               + os.environ['DOCX_NAME']                + '"; export DOCX_NAME'                + os.linesep,
                    'DOCX_NOEXEC="'             + os.environ['DOCX_NOEXEC']              + '"; export DOCX_NOEXEC'              + os.linesep,
                    'DOCX_QUIET="'              + os.environ['DOCX_QUIET']               + '"; export DOCX_QUIET'               + os.linesep,
                    'DOCX_RAWDOC="'             + os.environ['DOCX_RAWDOC']              + '"; export DOCX_RAWDOC'              + os.linesep,
                    'DOCX_RELEASE="'            + os.environ['DOCX_RELEASE']             + '"; export DOCX_RELEASE'             + os.linesep,
                    'DOCX_SRCDIR="'             + os.environ['DOCX_SRCDIR']              + '"; export DOCX_SRCDIR'              + os.linesep,
                    'DOCX_STATUS="'             + os.environ['DOCX_STATUS']              + '"; export DOCX_STATUS;'             + os.linesep,
                    'DOCX_VERBOSE="'            + os.environ['DOCX_VERBOSE']             + '"; export DOCX_VERBOSE'             + os.linesep,
                    'DOCX_VERSION="'            + os.environ['DOCX_VERSION']             + '"; export DOCX_VERSION'             + os.linesep,
                    'DOCX_WRAPPER="'            + os.environ['DOCX_WRAPPER']             + '"; export DOCX_WRAPPER'             + os.linesep,
                    'DOCX_WRAPPEROPTS="'        + os.environ['DOCX_WRAPPEROPTS']         + '"; export DOCX_WRAPPEROPTS'         + os.linesep,
                    'DOCX_WRAPPEROPTS_RESET="'  + os.environ['DOCX_WRAPPEROPTS_RESET']   + '"; export DOCX_WRAPPEROPTS_RESET'   + os.linesep,
                )
            )

        _fpath = self.build_doc_path + os.sep + 'setenv.bat'
        with open(_fpath, 'w') as _f:
            _f.writelines(
                (
                    'set DOCX_AUTHOR="'            + os.environ['DOCX_AUTHOR']            + '"' + os.linesep,
                    'set DOCX_BUILDDIR="'          + os.environ['DOCX_BUILDDIR']          + '"' + os.linesep,
                    'set DOCX_BUILDER="'           + os.environ['DOCX_BUILDER']           + '"' + os.linesep,
                    'set DOCX_BUILDRELDIR="'       + os.environ['DOCX_BUILDRELDIR']       + '"' + os.linesep,
                    'set DOCX_CLEAN="'             + os.environ['DOCX_CLEAN']             + '"' + os.linesep,
                    'set DOCX_CONFIGPATH="'        + os.environ['DOCX_CONFIGPATH']        + '"' + os.linesep,
                    'set DOCX_COPYRIGHT="'         + os.environ['DOCX_COPYRIGHT']         + '"' + os.linesep,
                    'set DOCX_DEBUG="'             + os.environ['DOCX_DEBUG']             + '"' + os.linesep,
                    'set DOCX_DOCNAME="'           + os.environ['DOCX_DOCNAME']           + '"' + os.linesep,
                    'set DOCX_DOCSRC="'            + os.environ['DOCX_DOCSRC']            + '"' + os.linesep,
                    'set DOCX_DOCTEMPLATE="'       + os.environ['DOCX_DOCTEMPLATE']       + '"' + os.linesep,
                    'set DOCX_DOCTYPE="'           + os.environ['DOCX_DOCTYPE']           + '"' + os.linesep,
                    'set DOCX_EMBED="'             + os.environ['DOCX_EMBED']             + '"' + os.linesep,
                    'set DOCX_EXEC="'              + os.environ['DOCX_EXEC']              + '"' + os.linesep,
                    'set DOCX_EXECOPTS="'          + os.environ['DOCX_EXECOPTS']          + '"' + os.linesep,
                    'set DOCX_EXECOPTS_RESET="'    + os.environ['DOCX_EXECOPTS_RESET']    + '"' + os.linesep,
                    'set DOCX_GENDOC="'            + os.environ['DOCX_GENDOC']            + '"' + os.linesep,
                    'set DOCX_INDEXSRC="'          + os.environ['DOCX_INDEXSRC']          + '"' + os.linesep,
                    'set DOCX_LIB="'               + os.environ['DOCX_LIB']               + '"' + os.linesep,
                    'set DOCX_LICENSE="'           + os.environ['DOCX_LICENSE']           + '"' + os.linesep,
                    'set DOCX_MISSION="'           + os.environ['DOCX_MISSION']           + '"' + os.linesep,
                    'set DOCX_NAME="'              + os.environ['DOCX_NAME']              + '"' + os.linesep,
                    'set DOCX_NOEXEC="'            + os.environ['DOCX_NOEXEC']            + '"' + os.linesep,
                    'set DOCX_QUIET="'             + os.environ['DOCX_QUIET']             + '"' + os.linesep,
                    'set DOCX_RAWDOC="'            + os.environ['DOCX_RAWDOC']            + '"' + os.linesep,
                    'set DOCX_RELEASE="'           + os.environ['DOCX_RELEASE']           + '"' + os.linesep,
                    'set DOCX_SRCDIR="'            + os.environ['DOCX_SRCDIR']            + '"' + os.linesep,
                    'set DOCX_STATUS="'            + os.environ['DOCX_STATUS']            + '"' + os.linesep,
                    'set DOCX_VERBOSE="'           + os.environ['DOCX_VERBOSE']           + '"' + os.linesep,
                    'set DOCX_VERSION="'           + os.environ['DOCX_VERSION']           + '"' + os.linesep,
                    'set DOCX_WRAPPER="'           + os.environ['DOCX_WRAPPER']           + '"' + os.linesep,
                    'set DOCX_WRAPPEROPTS="'       + os.environ['DOCX_WRAPPEROPTS']       + '"' + os.linesep,
                    'set DOCX_WRAPPEROPTS_RESET="' + os.environ['DOCX_WRAPPEROPTS_RESET'] + '"' + os.linesep,
                    )
                )

    def call_prologue(self):
        """Executed before the call of the wrapper. 
        
        The default version supports *Sphinx* and writes the project 
        data into the file '<build-dir>/<build-reldir>/project.rst'.
        Replace this method in the derived class as required. 
        """
        #
        # set environment for wrapper
        #
        self.set_environment()

        if self.gendoc:        
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
            
            #
            # write environment data scripts command line application.
            #
            self.write_environment_setter()
            
    
    def call_epilogue(self):
        """Executed after the call of the wrapper. 
        """
        pass
