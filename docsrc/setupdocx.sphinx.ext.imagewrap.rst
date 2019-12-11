.. _setupdocxSphinxExtImagewrap:

.. raw:: html

   <div class="shortcuttab">
   <div class="nonbreakheadtab">
   <div class="autocoltab">

.. index::
   single: sphinx.ext.imagewrap;
   single: imagewrap;
   
sphinx.ext.imagewrap
====================

The Sphinx extension *setupdocx.sphinx.ext.imagewrap* handles required different sizes for multiple
builders.
This includes in particular *epub*, *html*, and *pdf*(*pdflatex*).
This includes a simple syntax extension for multiple variants.
The extension is inspired by the article "Using Sphinx to Write Technical Books"
and the contained example "*Autoimage*" see [DrPedroKroger]_.

The *imagewrap* covers all possible parameters in order to simply
wrap the *image* directive, without the introduction of extra features.
The original directive

   .. parsed-literal::

      .. image:: gnu.png
         (options)

is extended by inheritance of the class *Image* to:

   .. parsed-literal::

      .. imagewrap:: gnu.png
         (options)

Where the parameters are processed and passed to the class *Image*.
For example:

   .. parsed-literal::

      .. imagewrap:: _static/gnu.png  
         width-html: 400px         # for HTML
         width-latexpdf: 250px     # for latexpdf == PDF
         width-epub: 150px         # for epub
         width-epub2: 150px        # for epub
         width-mobi: 150px         # for mobi
         width: 200px              # for all non-specified

         scale-html': directives.percentage,
         scale-latex': directives.percentage,
         scale-epub': directives.percentage,
         scale-epub2': directives.percentage,
         scale-mobi': directives.percentage,
         scale': directives.percentage,
         
         height-html': directives.length_or_unitless,
         height-latex': directives.length_or_unitless,
         height-epub': directives.length_or_unitless,
         height-epub2': directives.length_or_unitless,
         height-mobi': directives.length_or_unitless,
         height': directives.length_or_unitless,




Module
------
.. automodule:: setupdocx.sphinx.ext.imagewrap

Functions
---------

cb_align_values_image
^^^^^^^^^^^^^^^^^^^^^
.. autofunction:: setupdocx.sphinx.ext.imagewrap.cb_align_values_image

align_paths_to_top
^^^^^^^^^^^^^^^^^^
.. autofunction:: setupdocx.sphinx.ext.imagewrap.align_paths_to_top

setup
^^^^^
.. autofunction:: setupdocx.sphinx.ext.imagewrap.setup


ImageExt
--------
.. autoclass:: setupdocx.sphinx.ext.imagewrap.ImageExt


.. _SPEC_ImageWrap_option_spec:

option_spec
^^^^^^^^^^^
The member *option_spec* defines the known parameters.

   .. parsed-literal::

       option_spec = {
           'scale-html': directives.percentage,
           'scale-latex': directives.percentage,
           'scale-epub': directives.percentage,
           'scale-epub2': directives.percentage,
           'scale-mobi': directives.percentage,
           'scale': directives.percentage,
           
           'height-html': directives.length_or_unitless,
           'height-latex': directives.length_or_unitless,
           'height-epub': directives.length_or_unitless,
           'height-epub2': directives.length_or_unitless,
           'height-mobi': directives.length_or_unitless,
           'height': directives.length_or_unitless,
   
           'width-html': directives.length_or_percentage_or_unitless,
           'width-latex': directives.length_or_percentage_or_unitless,
           'width-epub': directives.length_or_percentage_or_unitless,
           'width-epub2': directives.length_or_percentage_or_unitless,
           'width-mobi': directives.length_or_percentage_or_unitless,
           'width': directives.length_or_percentage_or_unitless,
       
           'align': None,
   
       }  #: wrap all image parameters


.. _SPEC_ImageWrap_run:

align_paths_to_top
^^^^^^^^^^^^^^^^^^
.. automethod:: ImageExt.align_paths_to_top

extract_own_options
^^^^^^^^^^^^^^^^^^^
.. automethod:: ImageExt.extract_own_options

set_own_options
^^^^^^^^^^^^^^^
.. automethod:: ImageExt.set_own_options

run
^^^
.. automethod:: ImageExt.run

.. _setupdocxSphinxExtFigurewrap:

FigureExt
---------
.. autoclass:: setupdocx.sphinx.ext.imagewrap.FigureExt



.. _SPEC_FigureWrap_option_spec:

option_spec
^^^^^^^^^^^
The member *option_spec* defines the known parameters.

   .. parsed-literal::

       option_spec = {
           'scale-html': directives.percentage,
           'scale-latex': directives.percentage,
           'scale-epub': directives.percentage,
           'scale-epub2': directives.percentage,
           'scale-mobi': directives.percentage,
           'scale': directives.percentage,
           
           'height-html': directives.length_or_unitless,
           'height-latex': directives.length_or_unitless,
           'height-epub': directives.length_or_unitless,
           'height-epub2': directives.length_or_unitless,
           'height-mobi': directives.length_or_unitless,
           'height': directives.length_or_unitless,
   
           'width-html': directives.length_or_percentage_or_unitless,
           'width-latex': directives.length_or_percentage_or_unitless,
           'width-epub': directives.length_or_percentage_or_unitless,
           'width-epub2': directives.length_or_percentage_or_unitless,
           'width-mobi': directives.length_or_percentage_or_unitless,
           'width': directives.length_or_percentage_or_unitless,
       
           'align': None,
   
       }  #: wrap all image parameters

.. _SPEC_FigureWrap_run:


align_figure
^^^^^^^^^^^^
.. automethod:: FigureExt.align_figure

extract_own_options
^^^^^^^^^^^^^^^^^^^
.. automethod:: FigureExt.extract_own_options

setoptions_figure
^^^^^^^^^^^^^^^^^
.. automethod:: FigureExt.setoptions_figure

run
^^^
.. automethod:: FigureExt.run

Exceptions
----------

.. autoexception:: ImageWrapError
.. autoexception:: FigureWrapError

.. raw:: html

   </div>
   </div>
   </div>

