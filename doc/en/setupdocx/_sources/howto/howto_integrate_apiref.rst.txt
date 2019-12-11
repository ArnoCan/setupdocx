
.. _HOWTO_APIREF_INTEGRATE:

Integrated API Reference
------------------------

The documentation with integrated API reference is activated by the optional flag "*--apiref*".
This enables the call of the default wrapper *call_apiref.sh*, 
which calls in the current implementation *epydoc*.
The following call uses default values for the configuration contained within 
the document source directory.

   .. parsed-literal::
   
      python setup.py build_docx --apiref


The use of a specific configuration outside the source directory of the documentation: 


   .. parsed-literal::

      python setup.py \\  
         build_docx \\ 
            --apiref \\
            --doctype=html \\
            --docname=rtd-apiref \\
            --conf-dir=conf_docs/sphinx/rtd_apiref/ \\
            --clean


