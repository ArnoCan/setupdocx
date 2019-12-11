
.. _HOWTO_CREATEDOC:

Create the Document
-------------------

Sphinx
^^^^^^
#. **Define the Document Structure**

   Define the document structure based on *toctree*,
   see [sphinxdoc]_ and [restdir]_.

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
         from setupdocx.build_docx import BuildDocX

   Add a custom class:

      .. code-block:: python
         :linenos: 

         class build_docx(BuildDocX):
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
                 'build_docx': build_docx,
             },
   
#. **Create the Configuration**

   Create a configuration directory, e.g. by copying and adapting one of the provided templates.
   The provided templates should work out of the box on a production platform 
   based on *Linux* - they did at the time of writing.
   Refer to the sections for a pre-view.

   * Standard Themes:
   
     These are contained in the standard *Sphinx* installation.   

      * :ref:`CONFIG_TEMPLATE_SPHINX_AGOGO`
      * :ref:`CONFIG_TEMPLATE_SPHINX_BIZSTYLE`
      * :ref:`CONFIG_TEMPLATE_SPHINX_DEFAULT2`
      * :ref:`CONFIG_TEMPLATE_SPHINX_DEFAULT3`
      * :ref:`CONFIG_TEMPLATE_SPHINX_NATURE`
      * :ref:`CONFIG_TEMPLATE_SPHINX_SPHINXDOC`
      * :ref:`CONFIG_TEMPLATE_SPHINX_TRADITIONAL`
      
   * Special Themes:   

     These are opensource and has to be installed, e.g. via *PyPI*, or
     *github*.   

      * :ref:`CONFIG_TEMPLATE_SPHINX_ALABASTER`
      * :ref:`CONFIG_TEMPLATE_SPHINX_GUZZLE`
      * :ref:`CONFIG_TEMPLATE_SPHINX_RTD`
      * :ref:`CONFIG_TEMPLATE_SPHINX_BOOTSTRAP`

   * Custom Themes:
     These are modified by local changes. The current demos are based
     on standard themes.   

      * :ref:`CONFIG_TEMPLATE_SPHINX_DEFAULT_EXTENDED`
      * :ref:`CONFIG_TEMPLATE_SPHINX_EPUB`
      * :ref:`CONFIG_TEMPLATE_SPHINX_PDF`
      

#. **Call the 'setup.py'**

   Create teh document:
   
      .. parsed-literal::
   
         python setup.py build_docx --conf-dir=/your/configuration/path/

   The document is created by default in the directory:

      .. parsed-literal::
   
         build/doc/<docname>


#. **Read the Document**

   In case of the document type *html* this contains by default the main page:
   
      .. parsed-literal::
   
         build/doc/<docname>/index.html
   


See also :ref:`setupdocxEXAMPLES`.



Epydoc
^^^^^^
available soon
