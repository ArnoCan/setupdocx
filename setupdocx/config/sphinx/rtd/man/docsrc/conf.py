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


__author__ = 'Arno-Can Uestuensoez'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2016-2019 Arno-Can Uestuensoez" \
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
todo_include_todos = False


#
# required minimal sphinx version
#
# needs_sphinx = '1.0'


#
# required extensions
#
extensions = []
extensions.extend(  # @UndefinedVariable
    [
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
        'setupdocx.sphinx.ext.literalincludewrap',
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
#        *** man ***          #
#                             #
###############################


#
# theme name
#
html_theme = 'man'
 
 
# #
# # search paths - relative to the build directory + target directory
# #
# html_static_path = ['_static']
# html_tepmplate_path = ['_templates']
# html_theme_path = ['_themes']

# #
# # html options
# #
# html_theme_options = {}


# This value determines how to group the document tree into manual pages. 
# It must be a list of tuples (startdocname, name, description, authors, section), where the items are:
# 
#     startdocname: document name that is the “root” of the manual page. All documents referenced 
#                   by it in TOC trees will be included in the manual file too. (If you want one 
#                   master manual page, use your master_doc here.)
#     name:         name of the manual page. This should be a short string without spaces or 
#                   special characters. It is used to determine the file name as well as the
#                   name of the manual page (in the NAME section).
#     description:  description of the manual page. This is used in the NAME section.
#     authors:      A list of strings with authors, or a single string. Can be an empty
#                   string or list if you do not want to automatically generate an AUTHORS
#                   section in the manual page.
#     section:      The manual page section. Used for the output file name as well as in the 
#                   manual page header.

man_pages = [
    # shared
    ('setupdocx', 'SetupDocX', 'Document automation for Python2/3 setuptools', 'Arno-Can Uestuensoez', 3),
    ('setupdocx.sphinx.ext.imagewrap', 'ImageWrap', 'ImageWrap and FigureWap', 'Arno-Can Uestuensoez', 3),
    ('setupdocx.sphinx.ext.literalincludewrap', 'LiteralIncludeWrap', 'Path wrapper for literal includes', 'Arno-Can Uestuensoez', 3),
    ('setup_conf', 'setupdocx-config', 'configuration for CLI', 'Arno-Can Uestuensoez', 5),
    ('setup', 'setup.py', 'pattern for setup.py', 'Arno-Can Uestuensoez', 5),
#    ('setuplib_cli', 'setupdocx', 'document creation commands for setup.py', 'Arno-Can Uestuensoez', 1),
    

    ('setupdocx.build_docx', 'build_docx', 'setup.py extension for document creation', 'Arno-Can Uestuensoez', 1),
    ('setupdocx.build_apidoc', 'build_apidoc', 'setup.py extension for auto API extraction', 'Arno-Can Uestuensoez', 1),
    ('setupdocx.build_apiref', 'build_apiref', 'setup.py extension for API reference creation', 'Arno-Can Uestuensoez', 1),
    ('setupdocx.dist_docx', 'dist_docx', 'setup.py extension for document packaging', 'Arno-Can Uestuensoez', 1),
    ('setupdocx.install_docx', 'install_docx', 'setup.py extension for document installation', 'Arno-Can Uestuensoez', 1),

    ('call_doc', 'call_doc.sh', 'wrapper for document creation', 'Arno-Can Uestuensoez', 1),
    ('call_apidoc', 'call_apidoc.sh', 'wrapper for API generator', 'Arno-Can Uestuensoez', 1),
    ('call_apiref', 'call_apiref.sh', 'wrapper for API reference generator', 'Arno-Can Uestuensoez', 1),
    ('libbash', 'libbash.sh', 'library for bash based wrapper scripts', 'Arno-Can Uestuensoez', 3),

]


# man_show_urls
# 
#     If true, add URL addresses after links. Default is False.
# 
#     New in version 1.1.
man_show_urls = True


def setup(app):
    app.add_stylesheet('custom.css')
    
    try:
        if os.environ['DOCX_APIREF'] == '1':
            # create API reference, activates 'quick navigation' menu entry
            app.add_config_value('apiref', '1', 'env')
    
        else:
            app.add_config_value('apiref', '0', 'env')
    except:
        pass

    if html_theme != os.environ['DOCX_DOCTYPE']:
        raise Exception(
            'This configuration is prepared for the theme "%s" only, got "%s"' % (
                    html_theme,
                    str(os.environ['DOCX_DOCTYPE'])
                )
            )

    