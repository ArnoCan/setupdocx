
.. _CONFIG_TEMPLATE_SPHINX_ALABASTER:

*********************
Alabaster - alabaster
*********************

.. raw:: html

    <style>
      html, body{
         height: 100%;
      }
      .document{
         height: 100%;
      }

    </style>



The *alabaster* provides a standard style contained in *sphinx*.

.. only:: singlehtml

   .. container:: figabstract
   
      .. figurewrap:: _static/alabaster.png
         :width-latex: 400
         :width: 600
         :target-html: _static/alabaster.png
         :align: center
         
      Figure: Theme 'alabaster'


.. only:: not singlehtml

   .. figurewrap:: _static/alabaster.png
      :width-latex: 400
      :width: 600
      :target-html: _static/alabaster.png
      :align: center
      
      Figure: Theme 'alabaster'

**configuration**
   
   The current example implementation contains the files
   within the default path:

      .. parsed-literal::
         
         setupddocx/configurations/sphinx/alabaster
   
      .. raw:: html
      
         <div class="indextab">
         <div class="nonbreakheadtab">
         <div class="autocoltab">
   
      +--------------------------------+-----------------------------------------+
      | file                           | remark                                  |
      +================================+=========================================+
      | docsrc/conf.py                 | adds configuration variables            |
      +--------------------------------+-----------------------------------------+
      | docsrc/index.rst               | adaptation of totree                    |
      +--------------------------------+-----------------------------------------+
      | docsrc/index_application.rst   | adaptation of totree                    |
      +--------------------------------+-----------------------------------------+
      | docsrc/index_documentation.rst | adaptation of totree                    |
      +--------------------------------+-----------------------------------------+
      | docsrc/index_starthere.rst     | adaptation of totree                    |
      +--------------------------------+-----------------------------------------+
      | docsrc/_static/custom.css      | sets some custom colors and sizes       |
      +--------------------------------+-----------------------------------------+
      | docsrc/_static/favicon.ico     | provides a demo favicon, requires *ICO* |
      +--------------------------------+-----------------------------------------+
      | docsrc/_static/logo.png        | provides a demo logo, requires *PNG*    |
      +--------------------------------+-----------------------------------------+
   
      .. raw:: html
      
         </div>
         </div>
         </div>

**call**
   
   The call creates a html document within the local directory *doc*
   
      .. parsed-literal::

         python setup.py  \\
            build_docx \\
               --conf-dir=setupdocx/configurations/sphinx/alabaster/ \\
            install_docx \\
               --dist-dir doc \\
               --docname=alabaster

         # cut-and-paste for execution
         # for readability split acros multiple lines

   The same call with detailed command line parameters:
   
      .. parsed-literal::

         python setup.py  \\
            build_docx \\
               --doctype=html \\
               --docname=alabaster \\
               --conf-dir=setupdocx/confonfigurations/sphinx/alabaster/
            install_docx \\
               --dist-dir doc \\
               --docname=alabaster

         # cut-and-paste for execution
         # for readability split acros multiple lines
