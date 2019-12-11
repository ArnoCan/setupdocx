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
__copyright__ = "Copyright (C) 2010-2019 Arno-Can Uestuensoez" \
                " @Ingenieurbuero Arno-Can Uestuensoez"
__version__ = '0.1.36'
__uuid__ = "45167c30-3261-4a38-9de4-d7151348ba48"

__docformat__ = "restructuredtext en"


# authoring support
# 
todo_include_todos = False



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


#
# required minimal sphinx version
#
# needs_sphinx = '1.0'


#
# required extensions
#
extensions = []
if LooseVersion(sphinx.__version__) < LooseVersion('1.4'):
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
#        'javasphinx',
        'matplotlib.sphinxext.only_directives',
        'matplotlib.sphinxext.plot_directive',
        'sphinx.ext.autodoc',
        'sphinx.ext.doctest',
        'sphinx.ext.githubpages',
        'sphinx.ext.inheritance_diagram',
        'sphinx.ext.todo',
    ]
)  #: provided by present conf.py @UndefinedVariable

extensions.extend(  # @UndefinedVariable
    [
        'setupdocx.sphinx.ext.imagewrap.',
    ]
)  #: provided by setupdocx


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
#        *** html ***         #
#                             #
###############################


#
# theme name
#
html_theme = 'agogo'


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


#
# html options
#
html_theme_options = {

    # bodyfont (CSS font family): Font for normal text.

    # headerfont (CSS font family): Font for headings.
    
    # pagewidth (CSS length): Width of the page content, default 70em.
    "pagewidth": "90%",
    
    # documentwidth (CSS length): Width of the document (without sidebar), default 50em.
    "documentwidth": "70%",
    
    # sidebarwidth (CSS length): Width of the sidebar, default 20em.
    "sidebarwidth": "360",
    
    # bgcolor (CSS color): Background color.
    
    # headerbg (CSS value for “background”): background for the header area, default a grayish gradient.
    
    # footerbg (CSS value for “background”): background for the footer area, default a light gray gradient.
    
    # linkcolor (CSS color): Body link color.
    
    # headercolor1, headercolor2 (CSS color): colors for <h1> and <h2> headings.
    
    # headerlinkcolor (CSS color): Color for the backreference link in headings.
    
    # textalign (CSS text-align value): Text alignment for the body, default is justify.

}


def setup(app):
    app.add_stylesheet('custom.css')

    if os.environ['DOCX_APIREF'] == '1':
        # create API reference, activates 'quick navigation' menu entry
        app.add_config_value('apiref', '1', True)

    else:
        app.add_config_value('apiref', '0', True)
