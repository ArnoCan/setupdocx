# -*- coding: utf-8 -*-
"""Custom configuration of *conf.py*.
to be appended to the file:
    ::

        ${BUILDDIR}/sphinx/apidoc/conf.py

"""

import sys
import os
import sphinx

from distutils.version import LooseVersion


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2010-2016 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.36'
__uuid__ = "45167c30-3261-4a38-9de4-d7151348ba48"

__docformat__ = "restructuredtext en"


#
# add path for temporary tools required for this configuration
#
sys.path.insert(0, os.path.abspath(os.path.dirname(os.getcwd())))
sys.path.insert(0, os.path.abspath(os.getcwd()))


#
# global metadata
#
project = 'setupdocx'
copyright = __copyright__
license = __license__
version = __version__
uuid = __uuid__


# authoring support
#
todo_include_todos = False

#
# required minimal sphinx version
#
# needs_sphinx = '1.0'


#
# running on read-the-docs
#
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'


#
# required extensions
#
extensions = []
if on_rtd:
    extensions.extend(  # @UndefinedVariable
        [
            'sphinx.ext.mathjax.',
        ]
    )  #: provided by present conf.py @UndefinedVariable
elif LooseVersion(sphinx.__version__) < LooseVersion('1.4'):
    extensions.extend(  # @UndefinedVariable
        [
            'sphinx.ext.pngmath.',
        ]
    )  #: provided by present conf.py @UndefinedVariable
else:
    extensions.extend(  # @UndefinedVariable
        [
            'sphinx.ext.imgmath.',
        ]
    )  #: provided by present conf.py @UndefinedVariable

extensions.extend(  # @UndefinedVariable
    [
        # 'javasphinx',
        'matplotlib.sphinxext.only_directives',
        'matplotlib.sphinxext.plot_directive',
        'sphinx.ext.autodoc',
        'sphinx.ext.doctest',
        'sphinx.ext.githubpages',
        'sphinx.ext.inheritance_diagram',
        'sphinx.ext.todo',
        'sphinx.ext.ifconfig',
    ]
)  #: provided by present conf.py @UndefinedVariable


extensions.extend(  # @UndefinedVariable
    [
        'setupdocx.sphinx.ext.imagewrap',
    ]
)  #: provided by present conf.py @UndefinedVariable

#
# master document of toctree
#
master_doc = 'index'

#
# source_suffix = ['.rst', '.md']
#
source_suffix = '.rst'

#
# language for generated text by sphinx
#
# language = None

#
# patterns to ignore - relative to source directory
# (affects also html_static_path and html_extra_path)
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# style for syntax highlighting
pygments_style = 'sphinx'


###############################
#                             #
#      *** general ***        #
#                             #
###############################

project = 'setupdocx'
copyright = '2019, Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez'


###############################
#                             #
#        *** html ***         #
#                             #
###############################


#
# theme name
#
html_theme = 'default_white_with_green'


#
# logo and favicon
#
html_logo = "_static/logo.png"
html_favicon = "_static/favicon.ico"  # 64x64 - 4bit/16    


#
# search paths - relative to the build directory + target directory
#
html_static_path = ['_static']
html_theme_path = ['_themes']
html_tepmplate_path = ['_templates']


#
# custom sidebar templates
#


#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
#
#   html_sidebars = {
#      default: ``['localtoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html']``
#   }
#
# html_sidebars = {}
html_sidebars = {
   'default': ['shortcuts.html', 'localtoc.html', 'application.html', 'searchbox.html'],
   'index': ['quickref.html', 'localtoc.html', 'application.html', 'searchbox.html'],
   'install': ['localtoc.html', 'application.html', 'searchbox.html'],
   'setuplib_cli': ['shortcuts.html', 'localtoc.html', 'application.html', 'searchbox.html'],
   'setup_platforms_build_target': ['localtoc.html', 'shortcuts.html', 'application.html', 'searchbox.html'],
   'references': ['localtoc.html', 'searchbox.html'],

   'howto/*':['quickref.html', 'localtoc.html', 'application.html', 'searchbox.html'],
   'index_toc':['quickref.html', 'globaltoc.html', 'application.html', 'searchbox.html'],
   'index_apiref_white_green':['quickref.html', 'globaltoc.html', 'application.html',  'searchbox.html'],

   '*': ['quickref.html', 'localtoc.html', 'application.html', 'searchbox.html'],
   '*/*': ['quickref2.html', 'localtoc.html', 'application2.html', 'searchbox.html'],
}


#
# html options
#
html_theme_options = {
    # "rightsidebar": "true",
    # "relbarbgcolor": "black",
    "externalrefs": "true",
    "sidebarwidth": "360",
    "stickysidebar": "true",
    # "collapsiblesidebar": "true",
    # "footerbgcolor": "",
    "footerbgcolor": "#ccccae",
    # "footertextcolor": "",
    "footertextcolor": "black",
    # "sidebarbgcolor": "",
    "sidebarbgcolor": "white",
    # "sidebarbtncolor": "",
    "sidebarbtncolor": "#666633",
    # "sidebartextcolor": "",
    "sidebartextcolor": "black",
    # "sidebarlinkcolor": "",
    "sidebarlinkcolor": "black",
    # "relbarbgcolor": "",
    "relbarbgcolor": "#83836f",
    # "relbartextcolor": "",
    # "relbarlinkcolor": "",
    # "bgcolor": "",
    # "textcolor": "",
    # "linkcolor": "",
    # "visitedlinkcolor": "",
    # "headbgcolor": "",
    "headbgcolor": "white",
    # "headtextcolor": "",
    # "headlinkcolor": "",
    # "codebgcolor": "",
    "codebgcolor": "#999966",
    # "codetextcolor": "",
    # "bodyfont": "",
    # "headfont": "",


    #
    # additional parameters for themes
    #
      
    # static initialization of the path to the main page of 
    #the api-specification, e.g.
    #    epydoc/index.html
    # 
    "cockpit": "index_part_cockpit.html",
    "cockpittitle": "apidoc",

    "apiref": "index_apiref_white_green.html",
    "apititle": "apiref",

    "faq": "faq/index.html",
    "faqtitle": "faq",

    "howto": "howto/index.html",
    "howtotitle": "Howto",

    "shortcuts": "index_toc.html#documentation",
    "shortcuttitle": "Shortcuts",

    "quickstart": "quickstart.html",
    "quickstarttitle": "Quick Start",
}



def setup(app):
    app.add_stylesheet('custom.css')

    if os.environ['DOCX_APIREF'] == '1':
        # create API reference, activates 'quick navigation' menu entry
        app.add_config_value('apiref', '1', 'env')

    else:
        app.add_config_value('apiref', '0', 'env')

