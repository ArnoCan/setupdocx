
.. _HOWTO_MAN:

Create MAN
----------

The creation of the multiple man pages.

The precautions are same as the PDF type with additional restrictions.
A significant difference to all other formats is the lack of image and hyperlink support.
Thus these are dropped by the builder, but should be appropriate in the aspect of
page layout and text content.
Another aspect are tables, which have to be formatted fitting to a standard console window which
does not support horizontal scrolling.

The created output are multiple files formatted and named as standard MAN pages.
For the special configuration of the builder refer to the file *conf.py*.

The following call uses default values for the configuration contained within 
the document source directory.

   .. parsed-literal::
   
      python setup.py --doctype=man build_docx

The use of a specific configuration outside the source directory of the documentation: 

   .. parsed-literal::
   
      python setup.py \\  
         build_docx \\ 
            --docname=rtd-man \\
            --conf-dir=conf_docs/sphinx/rtd_man/ \\
            --clean


See also :ref:`man <CONFIG_TEMPLATE_SPHINX_MAN>`.

