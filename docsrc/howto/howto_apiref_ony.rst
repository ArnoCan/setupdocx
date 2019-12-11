
.. _HOWTO_APIREF_ONLY:

Create API Reference only
-------------------------

The creation of the API reference only is provided by the extra command *build_apiref*.
The command still calls in the wrapper *call_apiref.sh*.

The following call uses default values for the configuration contained within 
the document source directory.

   .. parsed-literal::
   
      python setup.py build_apiref

The use of a specific configuration outside the source directory of the documentation: 

   .. parsed-literal::
   
      python setup.py \\  
         build_apiref \\ 
            --doctype=html \\
            --docname=rtd-apiref \\
            --conf-dir=conf_docs/sphinx/rtd_apiref/ \\
            --clean
