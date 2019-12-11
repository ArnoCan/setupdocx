
********************
Test Include Wrapper
********************

Simple
======

simple include by

::

   .. include:: _static/included.sh


resulting in

"""

.. include:: _static/included.sh

"""

wrapped include by

::

   .. literalincludewrap:: _static/included.sh
      :language: bash
      :linenos:


resulting in

"""

.. literalincludewrap:: _static/included.sh
   :language: bash
   :linenos:

"""
         

Nested
======
         
nested include by

::

   .. include:: a/b/included.rst


resulting in

"""

.. include:: a/b/included.rst

"""
