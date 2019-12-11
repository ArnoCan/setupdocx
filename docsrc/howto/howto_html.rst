
.. _HOWTO_HTML:

Create HTML
-----------

The creation of the HTML format - with multiple pages - is the standard case.
This is also the most robust and simple type for the production.

In case of the forseen production of multiple document formats still some precautions for the
additional formats shoudl be introduced.
This comprises the preference of anchor based links instead of file name based links.
The other special requirement is the layout of the pages.
The expected devices of book readers provide frequently smaller screen sizes, thus the image sizes
should be adapte to the output target type.
See also the contained *Sphinx* extension :ref:`sphinx.ext.imagewrap <setupdocxSphinxExtImagewrap>`.
The special requirements of this format could be easily packaged into configuration template.

The following call uses default values for the configuration contained within 
the document source directory.

   .. parsed-literal::
   
      python setup.py --doctype=html build_docx

In this case the default configuration is for *HTML* thus the short call could be used.

   .. parsed-literal::
   
      python setup.py build_docx

The use of a specific configuration outside the source directory of the documentation: 

   .. parsed-literal::
   
      python setup.py \\  
         build_docx \\ 
            --docname=rtd-html \\
            --conf-dir=conf_docs/sphinx/rtd_html/ \\
            --clean


See also :ref:`html <CONFIG_TEMPLATE_SPHINX_HTML>`.

