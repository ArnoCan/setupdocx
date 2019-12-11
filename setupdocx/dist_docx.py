#-*- coding: utf-8 -*-
"""creates a document-package for the distribution of the package documentation
"""
from __future__ import absolute_import
from __future__ import print_function

import os
import sys
import shutil
import time
import zipfile
import tarfile
import gzip

import distutils.cmd
import setupdocx
import setuplib

import yapyutils.files.utilities as utilities 
import yapyutils.files.finder as finder 
import yapyutils.config.capabilities

#
# the setupdocx is at the lowest architecture level, 
# thus should require as few prerequisites as possible,
# ...so doing it manually where required...
#
# lzma is available beginning with Python-3.3 - others than CPython to be checked
#
try:
    import pythonids
    if pythonids.PYVxyz >= pythonids.PYV33:
        isPYV33plus = True
    else:
        isPYV33plus = False

except:
    if sys.version >= '3.3':
        isPYV33plus = True
    else:
        isPYV33plus = False


__author__ = 'Arno-Can Uestuensoez'
__author_email__ = 'acue_sf2@sourceforge.net'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2019 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__uuid__ = "45167c30-3261-4a38-9de4-d7151348ba48"


class SetuplibDistDocXError(setupdocx.SetupDocXError):
    pass


class DistDocX(distutils.cmd.Command):
    """Create a document distribution package."""

    description = 'Compile documentation into a distribution package.'
    user_options = [
        ('append',          None, "append files to existing archive, default: create new,"
                                  "can be used to add new unpack-dir"),
        ('build-dir=',      None, "document source location, default 'build/', "
                                  "reads the prepared documents from <build-dir>/doc/<document-name>"),
        ('clean',           None, "removes the previous document, be careful with this and check the target twice,"
                                  "no additional confirmation is requested, default: False"),
        ('date',            None, "adds the build date to the archive name, default '<year>.<month>.<day>'"),
        ('debug',           None, "debug flag for 'build_docx'"),
        ('dist-dir=',       None, "archive location for creation, default 'dist/'"),
        ('doctype=',        None, "document type to pack, default: 'html', "
                                  "see '--help-doctypes'"),
        ('extra-suffixes=', None, "comma separated list of extra suffixes, "
                                  "single file-documents are validated by suffixes, e.g. '.pdf' or '.epub', "
                                  "non-digit suffixes for man pages require extra suffixes, see manuals"
                                  "default: ''"),
        ('force',           None, "Force to processing by deactivating non-essential checks, "
                                  "suppresses validation, "
                                  "default: False"),
        ('forcedir',        None, "Force to pack directories, in case of single document types "
                                  "such as PDF too. Else the types PDF, and EPUB are compressed "
                                  "without the containing directory. The name of single-file documents is "
                                  "changed when archive name, version, etc. are provided. "
                                  "Default: False"),
        ('formats=',        None, "comma separated list of types of the created packages, default: 'zip', "
                                  "see '--help-formats'"),
        ('help-doctypes',   None,  "List available document formats."),
        ('help-formats',    None,  "List available distribution formats."),
        ('name=',           None, "changes package name 'self.name', "
                                  "see also '--name-in' and '--name-out'"),
        ('name-in=',        None, "input package name, default 'self.name'"),
        ('name-out=',       None, "output package name, default 'self.name'"),
        ('no-exec',        'n',   "print only, do not execute"),
        ('plat-name=',      None, "platform name to add to name, default: ''"),
        ('quiet',           'q',  "quiet of current context, resets verbosity of applied context to '0',"
                                  " default: off"),
        ('set-release=',    None, "The release of the package"),
        ('set-version',     None, "sets version of created archive, default: ''"),
        ('verbose',         'v',  "raises verbosity of current context, supports repetition, "
                                  "each raises the command verbosity level of the context by one "),
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

    doctypes_supported = (
        "html",  # simple HTML with defaults for sphinx and epydoc
        "singlehtml", 
        "epub", 
        "pdf", 
        "latexpdf", 
        "latexpdfja",
        "man",
        "mangz",
        "devhelp",
        "htmlhelp",
        "qthelp",
    )

    doctypes_suffix = {
        "epub" : '.epub', 
        "pdf": '.pdf', 
        "latexpdf": '.pdf', 
        "latexpdfja": '.pdf',
        "mangz": '.gz',
    }
    
    formats_supported = (
        "bzip2",
        "gz",
        "lzma",
        "tar",
        "targz",
        "tgz",
        "xz",
        "zip",
    )

    formats_suffix = {
        "bz2": "bz2",
        "gz": "gz",
        "bzip2": "bz2",
        "lzma": "lzma",
        "tar": "tar",
        "targz": "tar.gz",
        "tgz": "tgz",
        "xz": "xz",
        "zip": "zip",
    }

    def initialize_options(self):
        self.append = None
        self.build_dir = None
        self.clean = None
        self.date = None
        self.debug = None
        self.dist_dir = None
        self.doctype = None
        self.extra_suffixes = None
        self.force = None
        self.forcedir = None
        self.formats = None
        self.help_doctypes = None
        self.help_formats = None
        self.name_in = None
        self.name_out = None
        self.no_exec = None
        self.plat_name = None
        self.set_version = None
        self.set_release = None
        self.version = None

    def finalize_options(self):

        # quick-and-dirty hack to resolve the inconsistency of
        # global and local verbose values of distutils
        try:
            _v_opts = self.distribution.get_option_dict('dist_docx')['verbose'][1]
            if _v_opts:
                self.verbose += 1
        except:
            # fallback to the slightly erroneous behavior when the interface 
            # of distutils changes
            pass

        if self.clean == None:
            self.clean = False
        else:
            self.clean = True

        if self.name_in == None:
            self.name_in = self.name
        if self.name_out == None:
            self.name_out = self.name
        
        self.unpackdir = self.name_out + os.sep

        if self.force == None:
            self.force = False
        else:
            self.force = True

        if self.dist_dir == None:
            self.dist_dir = "dist" + os.sep

        if self.build_dir == None:
            self.build_dir = "build" + os.sep

        if self.doctype == None:
            self.doctype = "html"
        else:
            if self.doctype not in self.doctypes_supported:
                raise SetuplibDistDocXError(
                    "doctype = " + str(self.doctype) + " - supported: " + str(self.doctypes_supported))

        if self.extra_suffixes == None:
            self.extra_suffixes = tuple()
        else:
            # have to trust - no criteria
            self.extra_suffixes = self.extra_suffixes.split(',')

        if self.formats == None:
            self.formats = ("zip",)
        else:
            self.formats = self.formats.split(',')
            for f in self.formats:
                if f not in self.formats_supported:
                    raise SetuplibDistDocXError(
                        "format = " + str(f) + " - supported: " + str(self.formats_supported))


        self.pkgname = self.name_out + "-doc-" + self.doctype

        if self.no_exec != None:
            self.no_exec = True
        else:
            self.no_exec = False

        if self.set_version != None:
            self.pkgname += "-" + str(self.distribution.metadata.version)

        if self.set_release != None:
            # either alternative to version or add-on, e.g. 'alpha'
            self.pkgname += "-" + str(self.set_release)

        if self.date != None:
            # platform
            self.pkgname += str(time.strftime("-%Y.%m.%d", time.gmtime()))

        if self.plat_name != None:
            # platform
            self.pkgname += "-" + str(self.plat_name)

        if self.append != None:
            self.append = True

        if self.help_doctypes != None:
            print("Known document types:")
            for dt in  sorted(self.doctypes_supported):
                print("  --doctype=%s" % (dt))
            sys.exit(0)
            
        if self.help_formats != None:
            print("Known archive types:")
            for dt in  sorted(self.formats_supported):
                print("  --type=%-10s  # suffix: %s" % (dt, self.formats_suffix[dt]))
            sys.exit(0)

        if self.forcedir == None:
            self.forcedir = False
        else:
            if 'gz' in self.formats:
                raise SetuplibDistDocXError(
                    """
  'gzip' is supported for one single file document only
  you selected '--forcedir' for gzip: 

    formats = %s
"""
                    % (str(self.formats))
                    )
        if 'mangz' == self.doctype and 'gz' in self.formats:
            raise SetuplibDistDocXError(
                    """\n  The document type 'mangz' is already a compressed gzip format."""
                    )


    def run(self):
        """Assembles the distribution packages from the build directory.
        """
        _in = os.path.normpath(self.build_dir + os.sep + "doc" + os.sep + self.name_in)
        if not os.path.exists(_in):
            raise SetuplibDistDocXError("Requires pre-built documents:" + str(_in))

        if self.verbose > 1:
            print("package from:     " + _in)
        _in = os.path.abspath(_in)

        _out = os.path.normpath(self.dist_dir + os.sep + self.pkgname)
        _suffixes = ', '.join([self.formats_suffix[x] for x in self.formats])
        if self.verbose > 1:
            print("package to:       %s.%s" % (_out, str(_suffixes)))
        _out = os.path.abspath(_out)

        if self.verbose > 1:
            print("package unpack:   " + self.unpackdir)
            print()
        
        if self.no_exec:
            if not os.path.exists(self.dist_dir):
                print("mkdir: " + self.dist_dir)

            print("create: %s: %s" %(_out, _suffixes))

        else:
            if not os.path.exists(self.build_dir):
                os.makedirs(self.build_dir)
            _tmpdir = self.build_dir + os.sep + 'docxdist'
            if not os.path.exists(_tmpdir):
                os.makedirs(_tmpdir)
            
            if not os.path.exists(self.dist_dir):
                os.makedirs(self.dist_dir)

            _oldpwd = os.curdir 

            if self.append:
                _mode = 'a'
            else:
                _mode = 'w' 

            
#             if (
#                     self.unpackdir 
#                     and self.unpackdir == os.path.dirname(_in)
#                 ):
#                 #
#                 # an unpack directory is provided, 
#                 #
#                 os.chdir(os.path.dirname(os.path.normpath(_in)))
#                 _relpackdir =  os.path.basename(os.path.normpath(_in))
# 
#             elif (
#                 
#                 #FIXME:
#                     self.unpackdir
#                     and self.unpackdir == os.path.basename(_in) 
#                     and os.path.exists(_in) 
#                     and  os.path.isfile(_in)
#                 ):
#                 #
#                 # an unpack file name is provided,  
#                 #
#                 os.chdir(os.path.dirname(os.path.normpath(_in)))
#                 _relpackdir =  os.path.basename(os.path.normpath(_in))
# 
#             else:
            os.chdir(_tmpdir)
            
            if self.clean:
                if self.verbose > 2:
                    print('shutil.rmtree(%s, True)' % (self.unpackdir))
                shutil.rmtree(self.unpackdir, True)
            
            if self.verbose > 2:
                print('shutil.copytree(%s, %s)' % (
                    str(_in), str(self.unpackdir + os.sep)))
            shutil.copytree(_in, self.unpackdir + os.sep)
            

            #
            # documents consisting of multiple files
            #
            if self.doctype in ('html', 'singlehtml', 'htmlhelp', 'qthelp',):
                # pack directories
                _relpackdir =  os.path.normpath(self.unpackdir)
                _packsource = (_relpackdir,)
                if self.verbose > 3:
                    print('pack: %s' % (str(_relpackdir)))

            #
            # documents packs containing multiple autonomous files
            #
            elif self.doctype in ('man', 'mangz',):
                # pack directories
                _relpackdir =  os.path.normpath(self.unpackdir)
                if self.doctype in ('man',):
                    self.extra_suffixes = self.extra_suffixes + (
                        '.1', '.2', '.3', '.4', '.5', '.6', '.7', '.8', '.9', '.0', )
                if self.forcedir:
                    # pack directories
                    _packsource = (_relpackdir,)

                else:
                    # pack single file(s)
                    os.chdir(_relpackdir)
                    _packsource = []
                    for _f in os.listdir('.'):
                        _s = os.path.splitext(_f)[1]
                        if (
                                not self.force 
                                and _s not in self.extra_suffixes
                                and _s != self.doctypes_suffix.get(self.doctype, False)
                            ):
                            raise SetuplibDistDocXError(
                                    """incompatible suffix type,
   expect doctype:     %s
   got file:           %s
   see pack directory: %s
   see options:        '--extra-suffixes' and '--force'""" %(
                                    str(self.doctype), str(os.path.basename(_f)),
                                    _relpackdir,
                                    ))
                        _packsource.append(_f)

            #
            # documents consisting of one file 
            #
            elif self.doctype in ('latexpdf', 'latexpdfja', 'pdf', 'epub',):
                _relpackdir =  os.path.normpath(self.unpackdir)
                if self.forcedir:
                    # pack directories
                    _packsource = (_relpackdir,)

                else:
                    # pack single file(s)
                    os.chdir(_relpackdir)
                    _packsource = []
                    _s = os.path.splitext(_f)[1]
                    
                    for _f in os.listdir('.'):
                        if (
                                not self.force 
                                and _s not in self.extra_suffixes
                                and _s != self.doctypes_suffix.get(self.doctype, False)
                            ):
                            raise SetuplibDistDocXError(
                                '''
incompatible suffix type,
    expect doctype:     %s
    got file:           %s
    see pack directory: %s
''' %(
                                    str(self.doctype), str(os.path.basename(_f)),
                                    _relpackdir))
                        _packsource.append(_f)

                if self.verbose > 3:
                    print('pack: %s' % (str(_relpackdir)))

                if self.verbose > 2:
                    print('shutil.copy(%s, %s)' % (
                        str(_in(), str(self.unpackdir + os.sep))))

            
            # os.mkdir(self.build_dir + os.sep + self.unpackdir)

            for f in self.formats:
                _outn = os.path.basename(_out)
                if f in ('bzip2', 'bz2'):
                    if self.verbose > 1:
                        print("create bzip2: " + str(_outn + '.bz2'))
                    with tarfile.open(_out + '.bz2', _mode + ":bz2") as tar:
                        for name in _packsource:
                            tar.add(name)
    
                elif f == 'tar':
                    if self.verbose > 1:
                        print("create tar: " + str(_outn + '.tar'))
                    with tarfile.open(_out + '.tar', _mode) as tar:
                        for name in _packsource:
                            tar.add(name)
        
                elif f == 'targz':
                    if self.verbose > 1:
                        print("create tar.gz: " + str(_outn + '.tar.gz'))
                    with tarfile.open(_out + '.tar.gz', _mode + ":gz") as tar:
                        for name in _packsource:
                            tar.add(name)
        
                elif f == 'tgz':
                    if self.verbose > 1:
                        print("create tgz: " + str(_outn + '.tgz'))
                    with tarfile.open(_out + '.tgz', _mode + ":gz") as tar:
                        for name in _packsource:
                            tar.add(name)
                
                elif f == 'zip':
                    if self.verbose > 1:
                        print("create zip: " + str(_outn + '.zip'))
                    with zipfile.ZipFile(_out + '.zip', _mode) as myzip:
                        for _ps in _packsource:
                            if self.doctype in ('latexpdf', 'latexpdfja', 'pdf', 'epub', 'man',  'mangz',):
                                myzip.write(_ps)
    
                            else:
                                for root, dirs, files in os.walk(_ps):
                                    for f in files:
                                        myzip.write(root + os.sep + f)
    
                elif f == 'lzma':
                    if self.verbose > 1:
                        print("create lzma: " + str(_outn + '.lzma'))
                    if isPYV33plus:
                        with tarfile.open(_out + '.xz', _mode + ":xz") as tar:
                            for name in _packsource:
                                tar.add(name)
        
                    else:
                        os.chdir(_oldpwd)
                        raise SetuplibDistDocXError("Requires Python >= 3.3")
    
                elif f == 'xz':
                    if self.verbose > 1:
                        print("create xz: " + str(_outn + '.xz'))
                    if isPYV33plus:
                        with tarfile.open(_out + '.xz', _mode + ":xz") as tar:
                            for name in _packsource:
                                tar.add(name)
        
                    else:
                        os.chdir(_oldpwd)
                        raise SetuplibDistDocXError("Requires Python >= 3.3")
    
                elif f == 'gz' > 1:
                    if self.verbose:
                        print("create gz: " + str(_outn + '.gz'))
                    for name in _packsource:
                        with open(name, 'rb') as f_in, gzip.open(name + '.gz', 'wb') as f_out:
                            shutil.copyfileobj(f_in, f_out)
                            os.unlink(name)
    
                else:
                    if not self.force:
                        raise SetuplibDistDocXError("Unknown format:" + str(f))
    
            os.chdir(_oldpwd)
