
.. _HOWTO_SINGLEHTML:

Create Single HTML
------------------


The creation of the single HTML format - with one page - is basically comparable to the
single document formats such as PDF.
A accompanying directory is still required for images and style sheets, the
content is actually contained within one page only.

The precautions are similar to the PDF and EPUB types.
This comprises the preference of anchor based links instead of file name based links.
The other special requirement is the layout of the pages.
The expected devices of book readers provide frequently smaller screen sizes, thus the image sizes
should be adapte to the output target type.
See also the contained *Sphinx* extension :ref:`sphinx.ext.imagewrap <setupdocxSphinxExtImagewrap>`.
The special requirements of this format could be easily packaged into configuration template.

The following call uses default values for the configuration contained within 
the document source directory.

   .. parsed-literal::
   
      python setup.py --doctype=singlehtml build_docx

The use of a specific configuration outside the source directory of the documentation: 

   .. parsed-literal::
   
      python setup.py \\  
         build_docx \\ 
            --docname=rtd-singlehtml \\
            --conf-dir=conf_docs/sphinx/rtd_singlehtml/ \\
            --clean


See also :ref:`singlehtml <CONFIG_TEMPLATE_SPHINX_SINGLEHTML>`.

