
.. _CONFIG_TEMPLATE_SPHINX_EPUB:

****
epub
****

.. raw:: html

    <style>
      html, body{
         height: 100%;
      }
      .document{
         height: 100%;
      }

    </style>



The *epub* provides a standard style contained in *sphinx*.

.. only:: singlehtml

   .. container:: figabstract
   
      .. figurewrap:: _static/epub.png
         :width-latex: 400
         :width: 600
         :target-html: _static/epub.png
         :align: center
         
      Figure: Theme 'epub'


.. only:: not singlehtml

   .. figurewrap:: _static/epub.png
      :width-latex: 400
      :width: 600
      :target-html: _static/epub.png
      :align: center
      
      Figure: Theme 'epub'

**configuration**
   
   The current example implementation contains the files
   within the default path:

      .. parsed-literal::
         
         setupddocx/configurations/sphinx/epub
   
      .. raw:: html
      
         <div class="indextab">
         <div class="nonbreakheadtab">
         <div class="autocoltab">
   
      +--------------------------------------------------+-----------------------------------------+
      | file                                             | remark                                  |
      +==================================================+=========================================+
      | docsrc/conf.py                                   | adds configuration variables            |
      +--------------------------------------------------+-----------------------------------------+
      | docsrc/index.rst                                 | adapted index                           |
      +--------------------------------------------------+-----------------------------------------+
      | docsrc/_static/custom.css                        | sets some custom colors and sizes       |
      +--------------------------------------------------+-----------------------------------------+
      | docsrc/_static/favicon.ico                       | provides a demo favicon, requires *ICO* |
      +--------------------------------------------------+-----------------------------------------+
      | docsrc/_static/logo.png                          | provides a demo logo, requires *PNG*    |
      +--------------------------------------------------+-----------------------------------------+
      | docsrc/_themes/epub_demo/theme.conf              | configuration of theme                  |
      +--------------------------------------------------+-----------------------------------------+
      | docsrc/_themes/epub_demo/_static/epub_acue.css_t | dapted style sheet                      |
      +--------------------------------------------------+-----------------------------------------+
   
      .. raw:: html
      
         </div>
         </div>
         </div>

**call**
   
   The call creates a *EPUB* document within the local directory *doc*
   
      .. parsed-literal::
      
         python setup.py  -q  \\
            build_docx  \\
               --conf-dir setupdocx/configurations/epub/ \\
               --docname setupdocx-epub \\ 
            install_docx \\
               --dist-dir doc \\
               --docname=setupdocx-epub

         # cut-and-paste for execution
         # for readability split acros multiple lines
