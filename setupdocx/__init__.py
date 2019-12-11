# -*- coding: utf-8 -*-
"""Library for the creation of documentation.
Supports he management of multiple builders, output formats, and
templates.

Contains components for the creation of API documentation, API references in Javadoc style,
variable composition of document variants, packaging, and installation. 
"""
from __future__ import absolute_import
from __future__ import print_function

import os
import sys

import fnmatch
import re
import tempfile
import shutil

import json

__author__ = 'Arno-Can Uestuensoez'
__author_email__ = 'acue_sf2@sourceforge.net'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2015-2019 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__uuid__ = "45167c30-3261-4a38-9de4-d7151348ba48"

__version__ = "01.01.002"


# subsystem test and trace flags
_debug = 0
_verbose = 0

# helper
_head_printed = False


class SetupDocXError(Exception):
    """setupdocx error."""
    pass


separators = ['/', '\\\\', '.', ',', ';', ':', '|', '-', '_', ]
def conf_list(baselist=None, **kargs):
    """Lists current available configuration templates.
     
    Args:
        baselist:
            List of base directories to scan::

                baselist := <base-directory> [, <baselist>]
             
             
            Supports groups and nested subgroups of templates.
            Expects the following subdirectory structure::
 
                <base-directory>
                └── <builder>
                    ├── <conf-template-name>
                    │   ├── <doctype>
                    │   
                    ├── <conf-template-name>
                    │   ├── <doctype>
                    │   
                    ├── <conf-template-group-name>
                    │   ├── <conf-template-name>
                    │   │   ├── <doctype>
                    │   
                    ├── <conf-template-group-name>
                    │   ├── <conf-template-group-name>
                    │   │   ├── <conf-template-name>
                    │   │   │   ├── <doctype>
                    │   
                    ├── ...
 
 
            The default themes as provided by *setupdocx* are::
 
                setupdocx/config/
                ├── epydoc
                │   ├── embedded
                │   │   └── sphinx
                │   │       ├── rtd
                │   │       │   └── html
                │   │       │       └── iframe
                │   │       └── white-green
                │   │           └── html
                │   │               └── iframe
                │   └── standalone
                │       └── html
                ├── mkdocs
                │   ├── default
                │   │   └── html
                │   └── rtd
                │       └── html
                ├── pandoc
                └── sphinx
                    ├── agogo
                    │   └── html
                    ├── alabaster
                    │   └── html
                    ├── bizstyle
                    │   └── html
                    ├── bootstrap
                    │   └── html
                    ├── default
                    │   └── html
                    ├── guzzle
                    │   └── html
                    ├── nature
                    │   └── html
                    ├── rtd
                    │   ├── devhelp
                    │   ├── epub
                    │   ├── html
                    │   ├── htmlhelp
                    │   ├── man
                    │   ├── pdf
                    │   └── singlehtml
                    ├── rtd-github
                    │   └── html
                    ├── rtd-readthedocs
                    │   └── html
                    ├── sphinxdoc
                    └── traditional
                        └── html


        kargs:
            depth:
                The depth of subdirectories within the configuration directories::

                    depth := int >=0

                    default := 1

            display:
                Type of display for configuration names::
 
                    display := (
                          None      # name only
                        | std       #   alias for None
                        | standard  #   alias for None
                        | full      # as provided by baselist, either absolute or relative path
                        | abs       # absolute path
                        | rel       # relative path
                    )

                    default := None

            filter:
                Python-Regular expression as filter. The provided filter is used literally as
                a regular expression which is compiled and used for 're.search()' operations.
                For example::

                    filter=agogo,alabaster
                    filter=a.*
                    filter=(rtd)
                    filter=pdf
                    filter=html,epub

                    default := None  # non-filtered

            separator:
                The type of the separator::

                    separator := (
                        <table-index>
                        | <char-string>
                    )
                    table-index := [0-8]  # index into predefined 'separators'
                                          #  0: slash '/'
                                          #  1: back-slash '\\\\' 
                                          #  2: dot '.' 
                                          #  3: comma ',' 
                                          #  4: semicolon ';' 
                                          #  5: colon ':' 
                                          #  6: pipe '|' 
                                          #  7: hyphen '-' 
                                          #  8: underscore '_' 
                    
                    char-string := .*     # any string of 1 or more characters
                                          # the control character semicolon as 
                                          # load character needs to be masked
                                          # as a character class:
                                          #   [;] 

                    default := 0

            _dev_debug:
                Developer feature.
                
                Debug the list call only. This enables the isolated display of the
                tree resolution.
            
    Returns:
        None
         
    Raises:
        SetupDocXError
        
        pass-through
    """
    global _head_printed

    _display = kargs.get('display', None)
    _filter = kargs.get('filter', None)
    _sep = kargs.get('separator', 0)
    _all = kargs.get('all', False)

    _depth = int(kargs.get('depth', 1))
    if _depth == 0:
        _depth = 1

    __debug = int(kargs.get('_dev_debug', 0))
    _s = set(kargs)
    if _s & set(('all', 'display', 'filter', 'depth', 'separator', '_dev_debug')) != _s:
        raise SetupDocXError(
            "Unknown option(s): %s" % ( str(_s))
            )

    # mask suboption separator semicolon ';'
    if type(_sep) is not int:
        _sep = re.sub(r'(.*?)[\[];[\]]', r'\1;', _sep)

    if 'help' in (_display, _depth, _filter, _sep,):
        help(conf_list)
        sys.exit(0)

    if baselist == None:
        baselist = (os.path.dirname(__file__) + os.sep + 'config',)

    if _filter:
        _filter_re = re.compile(_filter)
    else:
        _filter_re =  None

    def _get_common_top(a, b):
        """Gets the first shared common top node of both paths.
        
        Args:
            a:
                Path a.

            b:
                Path a.

        Returns:
            If exists the common shared node::

                return := (<top-node>, #droppeda, #droppedb)

                top-node:  common hsared top-node
                #droppeda: the dropped number of sub-depth for a
                #droppedb: the dropped number of sub-depth for b

            else 'None'.
            
        Raises:
            pass-through

        """
        _a = a.split(os.sep)
        _b = b.split(os.sep)

        _la = len(_a)
        _lb = len(_b)

        _i = None
                
        if _la > _lb:
            for _bi in range(_lb):
                if _a[_bi] == _b[_bi]:
                    continue

                if _bi == _lb:
                    # no match
                    return None
                
                return (os.sep.join(_a[:_bi]), _la - _bi, _lb -_bi)

        else: # _la <= _lb
            for _ai in range(_la):
                if _a[_ai] == _b[_ai]:
                    continue
                
                if _ai == _la:
                    # no match
                    return None

                return (os.sep.join(_a[:_ai]), _la - _ai, _lb - _ai)

    def _sublist(theme):
        """
        Args:
            theme:
                The path to the theme.
            
        Returns:
            Printout.

        Raises:
            SetupDocXError
        
        """
        global _head_printed
        
        try:
            _s = separators[int(_sep)]
        except IndexError:
            raise SetupDocXError(
                "Unknown separator - index out of range: " + str(_sep)
                )
        except ValueError:
            _s = _sep

        _offset = os.path.normpath(_base) + os.sep  # just for safety - no performance issue here...
        b = os.path.normpath(theme) + os.sep

        _depth_cur = 0
        _depth_stack = [0]
        _lastdepth_path = [b,] 
        _head_printed = False
        _cache = []
        
        for dirpath, dirnames, filenames in os.walk(b):  # @UnusedVariable
            _dirpath = dirpath + os.sep

            if _debug > 3 or __debug > 2:
                #
                # some extensive structure traces
                #
                if _lastdepth_path[-1] != _dirpath:
                    if _dirpath.startswith(_lastdepth_path[-1]):
                        print("DBG:"
                              + "DOWN:" 
                              + str(_depth_cur) 
                              + " " + str(_depth_stack) 
                              + " dirpath = " + str(_dirpath))
                    else:
                        if _lastdepth_path[-1].startswith(_dirpath):
                            print("DBG:"
                                  + "UPWA:" 
                                  + str(_depth_cur) 
                                  + " " + str(_depth_stack) 
                                  + " dirpath = " + str(_dirpath))
                        else:
                            print("DBG:"
                                  + "CHNG:" 
                                  + str(_depth_cur) 
                                  + " " + str(_depth_stack) 
                                  + " lastpath = " + str(_lastdepth_path[-1]))
                            print("DBG:"
                                  + "CHNG:" 
                                  + str(_depth_cur) 
                                  + " " + str(_depth_stack) 
                                  + " dirpath =  " + str(_dirpath))
     
                else:
                    print("DBG:"
                          + "KEEP:" 
                          + str(_depth_cur) 
                          + " " + str(_depth_stack) 
                          + " dirpath = " + str(_dirpath))


            # shortcut for simple builder listing
            if _depth == 1:
                _print_head(_base)
                for d in sorted(dirnames):
                    print("     %s" % (str(d) ))
                return


            #
            # do the counters first for nested jumps and scattered structures
            #
            if _lastdepth_path[-1] != _dirpath:

                if _dirpath.startswith(_lastdepth_path[-1]):
                    # walks down the tree - one step
                    _depth_cur += 1  # does it stepwise
                    _depth_stack.append(_depth_cur)
                    _lastdepth_path.append(_dirpath)

                else:
                    if _lastdepth_path[-1].startswith(_dirpath + os.sep):
                        # walks up the tree - {1..n}-steps
                        _shared, _last, _cur = _get_common_top(_lastdepth_path[-1], _dirpath)
                        del(_depth_stack[_last - _cur:])
                        del(_lastdepth_path[_last - _cur:])
                        _depth_cur = _depth_stack[-1]

                    else:
                        #
                        # no direct parent - could be sidewalk between 1..n levels
                        #
                        
                        # find nearest shared top
                        _res = _get_common_top(_lastdepth_path[-1], _dirpath)
                        if _res:
                            _shared, _last, _cur = _res 

                            if _last > _cur:
                                # sidewalk with jump-up
                                del(_depth_stack[_cur - _last - 1:])
                                del(_lastdepth_path[_cur - _last - 1:])
                                
                                _x = re.sub(_shared + os.sep, '', _dirpath)
                                _x = _x.split(os.sep)[:-1]

                                _p = _shared
                                _d = _depth_stack[-1]
                                for _px in _x:
                                    _p += os.sep + _px + os.sep
                                    _lastdepth_path.append(_p)
                                    
                                    _d += 1
                                    _depth_stack.append(_d)

                                _depth_cur = _depth_stack[-1]
    
                            elif _last < _cur:
                                # sidewalk with jump-down
                                _x = re.sub(_shared + os.sep, '', _dirpath)
                                _x = _x.split(os.sep)[:-1]

                                _p = _shared
                                _d = _depth_stack[-1]
                                for _px in _x:
                                    _p += os.sep + _px
                                    _lastdepth_path.append(_p)
                                    
                                    _d += 1
                                    _depth_stack.append(_d)

                                _depth_cur = _depth_stack[-1]

                            elif _last == _cur:
                                # sidewalk at same depth again, happens for non-docsrc
                                _lastdepth_path[-1] = _dirpath
    
                            if _depth_cur == 1:
                                _head_printed = False


            if 'docsrc' in dirnames:

                if not _head_printed:
                    for c in sorted(_cache):
                        print("     %s" % (str(c),) )
                    _cache = []

                    _print_head(dirpath)
                    _head_printed = True

                dirnames.pop(dirnames.index('docsrc'))

                if _filter_re and not _filter_re.search(_dirpath):
                    continue

                if _depth_cur > _depth + 1:
                    continue

                if _display == 'abs':
                    # absolute path
                    d = os.path.abspath(dirpath)
                elif _display == 'rel':
                    # relative path
                    d = re.sub(_offset + r'[^' + os.sep+ ']*' + os.sep, '', dirpath)
                    d = re.sub(os.sep, _s, d)
                elif _display == 'full':
                    # as provided by baselist, either absolute or relative path
                    d = dirpath
                    d = re.sub(os.sep, _s, d)
                else:
                    # None:     name only
                    # std:      alias for None
                    # standard: alias for None
                    d = re.sub(_offset + r'[^' + os.sep+ ']*' + os.sep, '', dirpath)
                    ty = re.sub(_offset + r'.*' + os.sep, '', dirpath)
                    d = re.sub(os.sep + ty, '', d)

                    d = re.sub(os.sep, _s, d)
                    _cache.append("     %-40s - %s" % (str(d), str(ty)))
                    continue

                _cache.append("     %s" % (str(d),))
                
            else:
                if _all and not _head_printed:
                    _print_head(dirpath)
                    _head_printed = True

        if _cache:
            # print the remainings from last loop
            for c in sorted(_cache):
                print("     %s" % (str(c),) )

        print()

    def _print_head(y):
        """Print header for each builder.
        """
        global _head_printed
        if _head_printed:
            return

        _head_printed = True

        _builder = re.sub(_base, '', y)
        _builder = re.sub(r'[/\\\\]*([^/\\\\]*)[/\\\\].*$', r'\1', _builder)

        # for standard templates print the python module path too
        _stdconf = re.sub(r'.*[/\\\\](setupdocx[/\\\\].*)$', r'\1', _base)
        if _stdconf:
            _stdconf = re.sub(r'[/\\\\]', r'.', _stdconf)
            print("\navailable builder templates for: %s - %s.%s" % (
                _builder, _stdconf, _builder))
        else:
            print("\navailable builder templates for: %s" % (_builder))
        
        if _display in ('', 'std', 'standard', None):
            pass
        elif _display in ('abs',):
            pass
        elif _display in ('rel',):
            print(" - base-path: %s\n" % (str(os.path.normpath(_base + os.sep + _builder) + os.sep)))
        else:
            print(" - base-path: %s\n" % (str(os.path.normpath(_base + os.sep + _builder))))

    for _base in sorted(baselist):
        _sublist(_base)


