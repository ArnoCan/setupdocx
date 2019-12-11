
.. _HOWTO_APIDOCAND_DOC_ONLY:

Generated API Document
----------------------

The documentation with generated API documentation is activated by the optional flag "*--apidoc*".
This enables the call of the default wrapper *call_apidoc.sh*,
which calls in the current implementation *sphinx-apidoc*.
The main *index.rst* could be replaced by an optional configuration specific file form
the configuration template.
The following call uses default values for the configuration contained within 
the document source directory.

   .. parsed-literal::
   
      python setup.py build_docx --apidoc

The use of a specific configuration outside the source directory of the documentation: 

   .. parsed-literal::
   
      python setup.py \\  
         build_docx \\ 
            --apidoc \\
            --doctype=html \\
            --docname=rtd-apidoc \\
            --conf-dir=conf_docs/sphinx/rtd_apidoc/ \\
            --clean
