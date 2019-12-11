
**********************
Upper-Searched Include
**********************

the following file is searched in the upper tree given by

::

   .. literalincludewrap:: _static/included.sh
      :language: bash
      :linenos:

which matches

::

  literalincludewrap/a/b/../../_static/included.sh
                         A
                         |
                        <= start search here
  actual match:
    
    literalincludewrap/_static/included.sh
  
and included as

"""

.. literalincludewrap:: _static/included.sh
   :language: bash
   :linenos:
         
"""
