
.. _HOWTO_EPUB:

Create EPUB
-----------

The creation of the EPUB format requires some precaution inparticular related to references.
The prefered type of links for internal references should be set by named references as anchors
instead of filenames.
The other special requirement is the layout of the pages.
The expected devices of book readers provide frequently smaller screen sizes, thus the image sizes
should be adapte to the output target type.
See also the contained *Sphinx* extension :ref:`sphinx.ext.imagewrap <setupdocxSphinxExtImagewrap>`.
The special requirements of this format could be easily packaged into configuration template.

The following call uses default values for the configuration contained within 
the document source directory.

   .. parsed-literal::
   
      python setup.py --doctype=epub build_docx

The use of a specific configuration outside the source directory of the documentation: 

   .. parsed-literal::
   
      python setup.py \\  
         build_docx \\ 
            --doctype=epub \\
            --docname=rtd-epub \\
            --conf-dir=conf_docs/sphinx/rtd_epub/ \\
            --clean


See also :ref:`epub <CONFIG_TEMPLATE_SPHINX_EPUB>`.

