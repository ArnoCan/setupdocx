
.. _HOWTO_APIDOC_ONLY:

API Documentation only
----------------------

The creation of a final document for the genrated API documentation only is enabled by the two flags
*--apidoc* and *--rawdoc*.
The flag *--apidoc* enables the call of the default wrapper *call_apidoc.sh*,
which calls in the current implementation *sphinx-apidoc*.
The flag *--rawdoc* supresses the further configuration of the contents of the build directory
by the configuration templates.

The following call uses default values for the configuration contained within 
the document source directory.

   .. parsed-literal::
   
      python setup.py build_docx --apidoc --rawdoc

The use of a specific configuration outside the source directory of the documentation: 

   .. parsed-literal::
   
      python setup.py \\  
         build_docx \\ 
            --apidoc \\
            --rawdoc \\
            --doctype=html \\
            --docname=rtd-apidoc \\
            --conf-dir=conf_docs/sphinx/rtd_apidoc/ \\
            --clean
