
.. _CALL_SPHINXAPIDOC:


call_sphinxapidoc.sh
====================

The *call_apidoc.sh* implements a wrapper for the generation of the API documentation.
The curent defaul call is:

   .. parsed-literal::
   
      sphinx-apidoc

The expected output is the raw output from the tool *sphinx-apidoc*,
which is prepared to be postprocess by adding additional files and modification
of the main configuration file *conf.py*.
The finished input source directory is finally processed by *sphinx*.


.. _CALL_SPHINXAPIDOC_SOURCE:

.. only:: builder_html

   Source
   ------

.. literalincludewrap:: _static/call_apidoc.sh
   :language: bash
   :linenos:

.. only:: builder_html

   Download
   --------
   
   `call_apidoc.sh <_static/call_apidoc.sh>`_

