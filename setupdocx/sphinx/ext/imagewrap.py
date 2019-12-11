# -*- coding: utf-8 -*-
"""Wrapper extension for the directive *image* / *Image* and *figure/Figure*.
In order to avoid copy-of-code or mix-in, the instance is processed by functions.
"""

import os
import re
import copy

from docutils.parsers.rst import directives
from docutils.parsers.rst.directives import images

import setupdocx


__author__ = 'Arno-Can Uestuensoez'
__author_email__ = 'acue_sf2@sourceforge.net'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2019 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__uuid__ = "45167c30-3261-4a38-9de4-d7151348ba48"


URI_PATTERN = re.compile(r'^\w+://')
#: helper for path normalization


class ImageWrapError(setupdocx.SetupDocXError): # pylint: disable=too-few-public-methods
    """Image wrapper failed."""
    pass


class FigureWrapError(ImageWrapError): # pylint: disable=too-few-public-methods
    """Figure wrapper failed."""
    pass


_UP = '..' + os.sep
def align_paths_to_top(path, base, rel, depth):
    """Aligns the provided image/figure relative paths. Checks first
    the existence of the path, if not exists adds the upward relative
    path as offset and checks the existence again. In case of a match
    the image path is replace by the existent, else kept unchanged.
    Ignores absolute paths.

    Args:
        path:
            Path to be aligned. Only non-absolute paths are processed.

        base:
            Base for relative input. Either absolute or relative to
            current position.

        rel:
            Relative paths as side-branch of the search.

        depth:
            Maximum number of upward directory nodes to be searched.

    Returns:
        Resolved path, either absolute or relative.

    Raises:

    """
    if (
            not URI_PATTERN.match(path)
            and path and not os.path.isabs(path)
            and not os.path.exists(base + rel + path)
            and os.path.exists(base + path)
        ):
        return _UP * depth + path
    return path


def cb_align_values_image(argument):
    """Imported callback, see:

    * docutils.parsers.rst.directives
    * docutils.parsers.rst.directives.images.Image.align_values

    """
    return directives.choice(argument, images.Image.align_values)


class ImageExt(object):
    """Wraps the class *Image*. Passes builder specific values.
    For the image parameters refer to [restdir]_.

    .. note::

        When multiple builder are called, requires to run with
        the cache erase option. ::

                sphinx-build -E ..,

    The wrapper is designed to be implemented as a mixin only.
    """

    #: provided additional options
    option_spec_image = {
        'scale-html': directives.percentage,
        'scale-singlehtml': directives.percentage,
        'scale-latex': directives.percentage,
        'scale-epub': directives.percentage,
        'scale-epub2': directives.percentage,
        'scale-mobi': directives.percentage,

        'height-html': directives.length_or_percentage_or_unitless,
        'height-singlehtml': directives.length_or_percentage_or_unitless,
        'height-latex': directives.length_or_percentage_or_unitless,
        'height-epub': directives.length_or_percentage_or_unitless,
        'height-epub2': directives.length_or_percentage_or_unitless,
        'height-mobi': directives.length_or_percentage_or_unitless,

        'width-html': directives.length_or_percentage_or_unitless,
        'width-singlehtml': directives.length_or_percentage_or_unitless,
        'width-latex': directives.length_or_percentage_or_unitless,
        'width-epub': directives.length_or_percentage_or_unitless,
        'width-epub2': directives.length_or_percentage_or_unitless,
        'width-mobi': directives.length_or_percentage_or_unitless,

        'target-html': directives.uri,
        'target-singlehtml': directives.uri,
        'target-latex': directives.uri,
        'target-epub': directives.uri,
        'target-epub2': directives.uri,
        'target-mobi': directives.uri,

        'align': cb_align_values_image,

    }  #: wrap all image parameters

    #: complete options
    option_spec = copy.copy(option_spec_image)

    def __init__(self, *args, **kargs):
        super(ImageExt, self).__init__(*args, **kargs)

        self._env = None
        self._builder = None
        self.own_opts = {}

    def align_paths_to_top(self, res):
        """Aligns the provided image/figure relative paths. Checks first
        the existence of the path, if not exists adds the upward relative
        path as offset and checks the existence again. In case of a match
        the image path is replace by the existent, else kept unchanged.
        Ignores items with absolute paths.

        Aligns::
            source-path

            target-html
            target

        REMARK: Had to reengineer a bit of redundant attributes - so eventually some
        additional fixes may be required in future. 

        Args:
            res:
                result from call of 'images.Image.run()'.

        Returns:
            None, updates 'res'.

        Raises:
            pass-through

        """
        env = self.state.document.settings.env #pylint: disable=E1101

        _base = env.srcdir + os.sep
        _rel = os.path.dirname(env.docname) + os.sep
        _depth = len(_rel.split(os.sep)) - 1

        _opts = self.own_opts

        # normalize the source link - for target links
        res[0]['uri'] = align_paths_to_top(self.arguments[0], _base, _rel, _depth) #pylint: disable=E1101

        #
        #TODO: final validation required for portability
        #
        # normalize additional attributes - suppress a bunch of fake-warnings
        #
        # satisfies the ImageCollector in the final step, which uses the uri of the image child. 
        self.arguments[0] = res[0]['uri'] #pylint: disable=E1101

        try:
            res[0].children[0]['targethtml'] = res[0]['uri']
        except: 
            pass

        try:
            res[0].children[0]['uri'] = res[0]['uri'] 
        except: 
            pass

        # seems to be analsed once before reaching this point: res[0].children[0]rawsource = ...

        # normalize the reference target
        # want the priority hierarchy, thus prefetch all known
        _f0 = None
        for k in _opts:
            # should be one only for currenty builder
            if k.startswith('target-') and k in self.option_spec_image.keys():
                _f0 = _opts.get(k)

        # an optional generic - e.g. as default for under-construction
        _f1 = _opts.get('target')

        if _f0 and not os.path.isabs(_f0):
            res[0]['refuri'] = align_paths_to_top(_f0, _base, _rel, _depth)

        elif _f1 and not os.path.isabs(_f1):
            res[0]['refuri'] = align_paths_to_top(_f1, _base, _rel, _depth)

        # do not need it, but keep it as reminder
        #else:
        #    res[0]['refuri'] = align_paths_to_top(self.arguments[0], _base, _rel, _depth)

    def extract_own_options(self):
        """Process the parameters, and maps the values to the parent class *Image*.
        The values are provided by the member *self.options*. ::

                scale-{html, singlehtml, latex, epub, epub2, mobi,}
                height-{html, singlehtml, latex, epub, epub2, mobi,}
                width-{html, singlehtml, latex, epub, epub2, mobi,}
                align-{html, singlehtml, latex, epub, epub2, mobi,}
                target-{html, singlehtml, latex, epub, epub2, mobi,}

        Defaults values are::

                scale
                height
                width
                align
                target

        Fetches the known-and-present special options only from 'self.options'.
        These are stored in 'self.own_opts', the original default values remain
        untouched.

        """
        builder = self._builder
        opts = self.options #pylint: disable=E1101
        _opts = self.own_opts

        if opts is None:
            return opts

        # set the specifics for the builder, or keep the generic
        try:
            _opts['width-' + builder] = opts.pop('width-' + builder)
        except KeyError:
            pass

        try:
            _opts['height-' + builder] = opts.pop('height-' + builder)
        except KeyError:
            pass

        try:
            _opts['scale-' + builder] = opts.pop('scale-' + builder)
        except KeyError:
            pass

        try:
            _opts['target-' + builder] = opts.pop('target-' + builder)
        except KeyError:
            pass

        # now remove unused special options
        _for_del = []
        for k in opts.keys():
            _k = re.sub(r'.*-([^-]+)$', r'\1', k)
            if _k in self.option_spec_image.keys():
                _for_del.append(k)

        for k in _for_del:
            opts.pop(k)

        return _opts

    def set_own_options(self, res):
        """Updates the options of the result with the own extention-options.

        ::

                scale-{html, latex, epub, mobi,}   => scale
                height-{html, latex, epub, mobi,}  => height
                width-{html, latex, epub, mobi,}   => width
                align-{html, latex, epub, mobi,}   => align
                target-{html, latex, epub, mobi,}  => target

        Args:
            res:
                result from call of 'images.Image.run()'.

        Returns:
            None, updates 'res'.

        Raises:
            pass-through

        """
        if self.own_opts is None:
            # nothing to do
            return

        # align contained source paths such as uri and target
        self.align_paths_to_top(res)

        # non-path option mappings
        _width = self.own_opts.get('width-' + self._builder)
        _height = self.own_opts.get('height-' + self._builder)
        _scale = self.own_opts.get('scale-' + self._builder)

        if _width:
            res[0]['width'] = _width

        if _height:
            res[0]['height'] = _height

        if _scale:
            res[0]['scale'] = _scale

    def run(self):
        """Process the parameters by *self.setoptions*, and calls
        the run method of the parent class *Image*. Inherits
        the option_spec from *docutils.parsers.rst.directives.images.Image*.
        Adds the following parameters. ::

                scale-{html, latex, epub, mobi,}
                height-{html, latex, epub, mobi,}
                width-{html, latex, epub, mobi,}
                align-{html, latex, epub, mobi,}
                target-{html, latex, epub, mobi,}

        """
        # fetch builder
        self._env = self.state.document.settings.env #pylint: disable=E1101
        self._builder = self._env.app.builder.name

        # initialize the wrapper extensions
        # pop-out additional options
        self.extract_own_options()

        # process original base class
        res = super(ImageExt, self).run() #pylint: disable=E1101

        # sets the extension options
        self.set_own_options(res)

        return res


class FigureExt(ImageExt):
    """Wraps the class *Figure*. Passes builder specific values.
    For the figure parameters refer to [restdir]_.

    .. note::

        When multiple builder are called, requires to run with
        the cache erase option. ::

            sphinx-build -E ..,

    The permitted values of some parameters are slightly different from
    the parent image classes [restdir]_. This is taken into account.

    For the complete parameter description refer to [restdir]_, here a copy
    of the different semantics of "*width*" and "*figwidth*".
    This option [figwidth] does not scale the included image;
    use the "width" image option for that. ::

        +---------------------------+
        |        figure             |
        |                           |
        |<------ figwidth --------->|
        |                           |
        |  +---------------------+  |
        |  |     image           |  |
        |  |                     |  |
        |  |<--- width --------->|  |
        |  +---------------------+  |
        |                           |
        |The figure's caption should|
        |wrap at this width.        |
        +---------------------------+

    The wrapper is designed to be implemented as a mixin only.

    """
    option_spec_figure = {
        'figwidth-html': directives.length_or_percentage_or_unitless,
        'figwidth-singlehtml': directives.length_or_percentage_or_unitless,
        'figwidth-latex': directives.length_or_percentage_or_unitless,
        'figwidth-epub': directives.length_or_percentage_or_unitless,
        'figwidth-epub2': directives.length_or_percentage_or_unitless,
        'figwidth-mobi': directives.length_or_percentage_or_unitless,

        'figclass-html': directives.length_or_unitless,
        'figclass-singlehtml': directives.length_or_unitless,
        'figclass-latex': directives.length_or_unitless,
        'figclass-epub': directives.length_or_unitless,
        'figclass-epub2': directives.length_or_unitless,
        'figclass-mobi': directives.length_or_unitless,

    }  #: wrap all image parameters

    option_spec = copy.copy(option_spec_figure)
    option_spec.update(ImageExt.option_spec_image)

    def __init__(self, *args, **kargs):
        super(FigureExt, self).__init__(*args, **kargs)

        self.own_opts = {}

    def extract_own_options(self):
        """Process the parameters, and maps the values to the parent class *Figure*.
        The values are provided by the member *self.options*. ::

            figwidth-{html, latex, epub, mobi,}
            figclass-{html, latex, epub, mobi,}

        Fetches the known-and-present special options only from 'self.options'.
        These are stored in 'self.own_opts', the original default values remain
        untouched.

        """
        env = self.state.document.settings.env #pylint: disable=E1101
        builder = env.app.builder.name
        opts = self.options #pylint: disable=E1101
        _opts = self.own_opts

        if opts is None:
            return _opts

        # set the specifics for the builder, or keep the generic
        try:
            _opts['figwidth'] = opts.pop('figwidth-' + builder)
        except KeyError:
            pass

        return _opts

    def align_figure(self, argument): #pylint:  disable=R0201
        return directives.choice(argument, images.Figure.align_h_values)

    def setoptions_figure(self, inst): #pylint:  disable=R0201
        """Process the parameters, and maps the values to the parent class *Figure*.
        The values are provided by the member *self.options*. ::

            figwidth-{html, latex, epub, mobi,}
            figclass-{html, latex, epub, mobi,}

        """
        env = inst.state.document.settings.env
        builder = env.app.builder.name
        opts = inst.options

        if opts is None:
            return opts

        _x = opts.get('figwidth-' + builder, None)
        if _x != None:
            opts['figwidth'] = _x

        _x = opts.get('figclass-' + builder, None)
        if _x != None:
            opts['figclass'] = _x

        return opts

    def run(self):
        """Process the parameters by *self.setoptions*, and calls
        the run method of the parent class *Figure*. Inherits
        the option_spec from *docutils.parsers.rst.directives.images.Figure*.
        Adds the following parameters. ::

            figwidth-{html, latex, epub, mobi,}
            figclass-{html, latex, epub, mobi,}

        """
        # initialize the wrapper extensions
        # pop-out additional options
        self.extract_own_options()

        # process original base class
        res = super(FigureExt, self).run()

        # align contained source paths
        self.align_paths_to_top(res)

        return res


def setup(app):
    """Initialize the extension."""

    #
    # extended image wrapper
    #
    class ImageWrap(ImageExt, images.Image): #pylint:  disable=C0111
        pass

    for name, value in images.Image.option_spec.items():
        ImageWrap.option_spec[name] = value

    for name, value in ImageExt.option_spec.items():
        ImageWrap.option_spec[name] = value

    app.add_directive('imagewrap', ImageWrap)

    #
    # extended figure wrapper
    #
    class FigureWrap(FigureExt, images.Figure): #pylint:  disable=C0111
        pass

    for name, value in images.Image.option_spec.items():
        FigureWrap.option_spec[name] = value

    for name, value in FigureExt.option_spec.items():
        FigureWrap.option_spec[name] = value

    app.add_directive('figurewrap', FigureWrap)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
