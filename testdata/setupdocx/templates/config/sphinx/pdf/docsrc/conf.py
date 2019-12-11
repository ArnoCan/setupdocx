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
__copyright__ = "Copyright (C) 2016 Arno-Can Uestuensoez" \
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
# if LooseVersion(sphinx.__version__) < LooseVersion('1.4'):
#     extensions.extend(  # @UndefinedVariable
#         [
#             'sphinx.ext.pngmath.',
#         ]
#     )  #: provided by present conf.py @UndefinedVariable
# else:
#     extensions.extend(  # @UndefinedVariable
#         [
#             'sphinx.ext.imgmath.',
#         ]
#     )  #: provided by present conf.py @UndefinedVariable

extensions.extend(  # @UndefinedVariable
    [
        # 'javasphinx',
#         'matplotlib.sphinxext.only_directives',
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
#        *** html ***         #
#                             #
###############################


# #
# # theme name
# #
# html_theme = 'pdf'                                              
# 
# 
# #
# # logo and favicon
# #
# html_logo = "_static/logo.png"
# html_favicon = "_static/favicon.ico"  # 64x64 - 4bit/16    
# 
# 
# #
# # search paths - relative to the build directory + target directory
# #
# html_static_path = ['_static']
# html_tepmplate_path = ['_templates']
# html_theme_path = ['_themes']



###############################
#                             #
#       *** LaTeX ***         #
#                             #
###############################

with open('conf.tex', 'r+') as f:
    PREAMBLE = f.read();

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',
    
    # Additional stuff for the LaTeX preamble.
    # 'preamble': '',
    # 'preamble': '\setcounter{tocdepth}{4}'
    'preamble': PREAMBLE

}


# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    (
        'index',                                         # source start file,
        'setupdocx.tex',                                 # target name, 
        u'Setup Commands for Documentation',             # title, 
        u'Arno-Can Uestuensoez',                         # author, 
        'manual'                                         # documentclass [howto/manual]
    ),
    (
        'pdf_faq',                                       # source start file,
        'faq.tex',                                       # target name, 
        u'FAQ - Setup Commands for Documentation',       # title, 
        u'Arno-Can Uestuensoez',                         # author, 
        'manual'                                         # documentclass [howto/manual]
    ),
    (
        'pdf_howto',                                     # source start file,
        'howto.tex',                                     # target name, 
        u'HowTo - Setup Commands for Documentation',     # title, 
        u'Arno-Can Uestuensoez',                         # author, 
        'manual'                                         # documentclass [howto/manual]
    ),
]


# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None
latex_logo = '_static/logo.png'

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
latex_domain_indices = True


def setup(app):
    app.add_stylesheet('custom.css')
    
    if os.environ['DOCX_APIREF'] == '1':
        # create API reference, activates 'quick navigation' menu entry
        app.add_config_value('apiref', '1', 'env')

    else:
        app.add_config_value('apiref', '0', 'env')

#     if html_theme != os.environ['DOCX_DOCTYPE']:
#         raise Exception(
#             'This configuration is prepared for the theme "epub" only, got "%s"' % (
#                 str(os.environ['DOCX_DOCTYPE']))
#             )

    