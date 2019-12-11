import os
import sys

sys.path.append(os.path.abspath("./ext"))

extensions = ['setupdocx.sphinx.ext.literalincludewrap']

master_doc = 'index'