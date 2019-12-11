
.. _CALL_SPHINXBUILD:

call_sphinx.sh
==============

The *call_doc.sh* implements a wrapper for the generation of the API documentation.
The curent defaul call is:

   .. parsed-literal::

      sphinx

The expected input is the raw output from the tool *sphinx-apidoc*.
The processing first prepares the input by adding additional files and modification
of the main configuration file *conf.py*.
The finished input source directory is finally processed by *sphinx*.


.. _CALL_SPHINX_SOURCE:

.. only:: builder_html

   Source
   ------

.. literalincludewrap:: _static/call_doc.sh
   :language: bash
   :linenos:


.. only:: builder_html

   Download
   --------
   
   `call_doc.sh <_static/call_doc.sh>`_

