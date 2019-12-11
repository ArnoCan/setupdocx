
.. _HOWTO_INSTALDOC:


Install the Document
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
         from setupdocx.install_docx import InstallDocX

   Add a custom class:

      .. code-block:: python
         :linenos: 

         class install_docx(BuildDocX):
             """Defines additional text processing.
             """
             
             def __init__(self, *args, **kargs):
                 BuildDocX.__init__(self, *args, **kargs)
                 self.name = 'setupdocx'
         
   Integrate into distutils [distutils]_:

      .. code-block:: python
         :linenos: 

         setup(
             cmdclass={
                 'install_docx': install_docx,
             },
   

#. **Call the 'setup.py'**

   Install the document:
   
      .. parsed-literal::
   
         python setup.py install_docx --name-in=<your-docname>

   The document is installed by default in the directory:

      .. parsed-literal::
   
         doc/<docname>


#. **Read the Document**

   In case of the document type *html* this contains by default the main page:
   
      .. parsed-literal::
   
         doc/<docname>/index.html


See also :ref:`setupdocxEXAMPLES`.




