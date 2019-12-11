
.. _CONFIG_TEMPLATE_SPHINX_BIZSTYLE:

********
bizstyle
********

.. raw:: html

    <style>
      html, body{
         height: 100%;
      }
      .document{
         height: 100%;
      }

    </style>



The *bizstyle* provides a standard style contained in *sphinx*.

.. only:: singlehtml

   .. container:: figabstract
   
      .. figurewrap:: _static/bizstyle.png
         :width-latex: 400
         :width: 600
         :target-html: _static/bizstyle.png
         :align: center
         
      Figure: Theme 'bizstyle'


.. only:: not singlehtml

   .. figurewrap:: _static/bizstyle.png
      :width-latex: 400
      :width: 600
      :target-html: _static/bizstyle.png
      :align: center
      
      Figure: Theme 'bizstyle'

**configuration**
   
   The current example implementation contains the files
   within the default path:

      .. parsed-literal::
         
         setupddocx/configurations/sphinx/bizstyle
   
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
               --conf-dir=setupdocx/configurations/sphinx/bizstyle/ \\
            install_docx \\
               --dist-dir doc

         # cut-and-paste for execution
         # for readability split acros multiple lines

   The same call with detailed command line parameters:
   
      .. parsed-literal::

         python setup.py  \\
            build_docx \\
               --doctype=html \\
               --docname=bizstyle \\
               --conf-dir=setupdocx/confonfigurations/sphinx/bizstyle/
            install_docx \\
               --dist-dir doc \\
               --docname=bizstyle

         # cut-and-paste for execution
         # for readability split acros multiple lines
