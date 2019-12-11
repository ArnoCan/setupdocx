
.. _CONFIG_TEMPLATE_SPHINX_PDF:

***
pdf
***

.. raw:: html

    <style>
      html, body{
         height: 100%;
      }
      .document{
         height: 100%;
      }

    </style>




The *pdf* is provided by the builders *latexpdf* and *latexpdfja* which are based on
*latex*.

.. only:: singlehtml

   .. container:: figabstract
   
      .. figurewrap:: _static/pdf.png
         :width-latex: 400
         :width: 600
         :target-html: _static/pdf.png
         :align: center
         
      Figure: Theme 'pdf'


.. only:: not singlehtml

   .. figurewrap:: _static/pdf.png
      :width-latex: 400
      :width: 600
      :target-html: _static/pdf.png
      :align: center
      
      Figure: Theme 'pdf'

**configuration**
   
   The current example implementation contains the files
   within the default path:

      .. parsed-literal::
         
         setupddocx/configurations/sphinx/pdf
   
      .. raw:: html
      
         <div class="indextab">
         <div class="nonbreakheadtab">
         <div class="autocoltab">
   
      +--------------------------------+-----------------------------------------+
      | file                           | remark                                  |
      +================================+=========================================+
      | docsrc/conf.py                 | adds configuration variables            |
      +--------------------------------+-----------------------------------------+
      | docsrc/conf.tex                | adds configuration to the latex builder |
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
   
   The call creates a *PDF* document within the local directory *doc*
   
      .. parsed-literal::
      
         python setup.py  -q  \\
            build_docx  \\
               --conf-dir setupdocx/configurations/pdf/ \\
               --docname setupdocx-pdf \\ 
            install_docx \\
               --dist-dir doc \\
               --docname=setupdocx-pdf

         # cut-and-paste for execution
         # for readability split acros multiple lines
 