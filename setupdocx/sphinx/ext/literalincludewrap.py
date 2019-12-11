# -*- coding: utf-8 -*-
"""Wrapper extension for the directive *literalinclude*.
Extends path by search.  
"""

import os

from sphinx.directives import code

from setupdocx import SetupDocXError

__author__ = 'Arno-Can Uestuensoez'
__author_email__ = 'acue_sf2@sourceforge.net'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2019 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__uuid__ = "45167c30-3261-4a38-9de4-d7151348ba48"


class LiteralIncludeWrapError(SetupDocXError):
    pass


_up = '..' + os.sep
def align_paths_to_top(inst):
    """Aligns the provided include relative paths. Checks first
    the existence of the path, if not exists adds the upward relative
    path as offset and checks the existence again. In case of a match 
    the path is replace by the existent, else kept unchanged.
    Ignores absolute paths. 
    """
    env = inst.state.document.settings.env

    _base = env.srcdir + os.sep
    _rel = os.path.dirname(env.docname) + os.sep
    _depth = len(_rel.split(os.sep)) - 1
    
    _f = inst.arguments[0]
    if _f and not os.path.isabs(_f):
        if not os.path.exists(_base + _rel + _f):
            if os.path.exists(_base + _f):
                inst.arguments[0] =  _up * _depth + _f


class LiteralIncludeWrap(code.LiteralInclude):
    """Wraps the class *Literalinclude*. Adjusts paths and passes to parent class.
    Thus allows position independed include paths.
    """
    def run(self):
        """Process the paths by *self.setoptions*, and calls 
        the run method of the parent class *LiteralInclude*. Inherits
        the option_spec from *sphinx.directives.code.LiteralInclude*.
        """
        align_paths_to_top(self)
        return super(LiteralIncludeWrap, self).run()


def setup(app):
    """Initialize the extension."""
    app.add_directive('literalincludewrap', LiteralIncludeWrap)

