
.. _HOWTO_PACKAGEDOC:


Package the Document
--------------------

Sphinx
^^^^^^

#. **Write the 'setup.py'**

   Write a setup with imported *setupdocx* classes,
   for a complete example refer to :ref:`SETUPPYSRC`.

      .. code-block:: python
         :linenos: 

         #
         # setup extension modules
         #
         from setupdocx import usage, sed
         
         # documents
         from setupdocx.dist_docx import DistDocX

   Add a custom class:

      .. code-block:: python
         :linenos: 

         class dist_docx(DistDocX):
             """Defines additional text processing.
             """
             
             def __init__(self, *args, **kargs):
                 DistDocX.__init__(self, *args, **kargs)
                 self.name = 'setupdocx'
         
   Integrate into distutils [distutils]_:

      .. code-block:: python
         :linenos: 

         setup(
             cmdclass={
                 'dist_docx': dist_docx,
             },
   

#. **Call the 'setup.py'**

   Package the document into a file archive:
   
      .. parsed-literal::
   
         python setup.py dist_docx --name-in=<your-docname>

   The package is created by default in the standard distribution directory
   of the current project. The default type is *zip*:

      .. parsed-literal::
   
         dist/<docname>-<release>.zip



See also :ref:`setupdocxEXAMPLES`.


Epydoc
^^^^^^
available soon

