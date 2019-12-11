# -*- coding: utf-8 -*-
# The license for the configuration files 'conf.py' - only is MIT
#  
# Copyright 2019 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software
# and associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute,
# sublicense, and/or sell copies of the Software, and to permit persons to whom the Software
# is furnished to do so, subject to the following conditions:
# 
#     The above copyright notice and this permission notice shall be included in all
#     copies or substantial portions of the Software.
# 
#     THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
#     INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
#     PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
#     HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
#     OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
#     SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
#
"""Custom configuration of *conf.py*.
to be appended to the file:
    ::

        ${BUILDDIR}/sphinx/apidoc/conf.py

"""

import sys
import os
import sphinx

from distutils.version import LooseVersion
import guzzle_sphinx_theme


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
##else:
##    extensions.extend(  # @UndefinedVariable
##        [
##            'sphinx.ext.imgmath.',
##        ]
##    )  #: provided by present conf.py @UndefinedVariable

extensions.extend(  # @UndefinedVariable
    [
#        'javasphinx',
##        'matplotlib.sphinxext.only_directives',
##        'matplotlib.sphinxext.plot_directive',
        'sphinx.ext.autodoc',
        'sphinx.ext.doctest',
        'sphinx.ext.githubpages',
        'sphinx.ext.inheritance_diagram',
        'sphinx.ext.todo',
    ]
)  #: provided by present conf.py @UndefinedVariable

extensions.extend(  # @UndefinedVariable
    [
        'setupdocx.sphinx.ext.imagewrap',
        'setupdocx.sphinx.ext.literalincludewrap',
    ]
)  #: provided by setupdocx


# Register the theme as an extension to generate a sitemap.xml
extensions.append("guzzle_sphinx_theme")

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
html_theme = 'guzzle_sphinx_theme'


#
# logo and favicon
#
html_logo = "_static/logo.png"
html_favicon = "_static/favicon.ico"  # 64x64 - 4bit/16    


#
# search paths - relative to the build directory + target directory
#
html_static_path = ['_static']
# html_theme_path = ['_themes']
html_theme_path = guzzle_sphinx_theme.html_theme_path()
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
# Guzzle theme options (see theme.conf for more information)
html_theme_options = {
    # Set the name of the project to appear in the sidebar
    "project_nav_name": "setupdocx",
    
    # Set to an html template to load custom HTML for the homepage
    # index_template =
    
    # Set the name of the project to appear in the left sidebar.
    # project_nav_name =
    
    # Path to a touch icon
    # touch_icon =
    
    # Set this value to enable Disqus comments
    # disqus_comments_shortname =
    
    # Set to enable google analytics
    # google_analytics_account =
    
    # Specify a base_url used to generate sitemap.xml links. If not specified, then
    # no sitemap will be built.
    # base_url =
    
    # Allow a separate homepage from the "master_doc"
    # homepage =
    
    # Allow the project link to be overwritten to a custom URL.
    # projectlink =
    
    # The maximum depth of the global TOC; set it to -1 to allow unlimited depth
    # globaltoc_depth = 2
    
    # If true, TOC entries that are not ancestors of the current page are collapsed
    # globaltoc_collapse = true
    
    # If true, the global TOC tree will also contain hidden entries
    # globaltoc_includehidden = true    
}




def setup(app):
    app.add_stylesheet('custom.css')

