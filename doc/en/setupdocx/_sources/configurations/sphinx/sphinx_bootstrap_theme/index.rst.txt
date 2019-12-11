
.. _CONFIG_TEMPLATE_SPHINX_BOOTSTRAP:

**********************************
Bootstrap - sphinx_bootstrap_theme
**********************************

.. raw:: html

    <style>
      html, body{
         height: 100%;
      }
      .document{
         height: 100%;
      }

    </style>



The *sphinx_bootstrap_theme* provides a local them for *ReadTheDocs* style.

.. only:: singlehtml

   .. container:: figabstract
   
      .. figurewrap:: _static/bootstrap.png
         :width-latex: 400
         :width: 600
         :target-html: _static/bootstrap.png
         :align: center
         
      Figure: Theme 'bootstrap'


.. only:: not singlehtml

   .. figurewrap:: _static/bootstrap.png
      :width-latex: 400
      :width: 600
      :target-html: _static/bootstrap.png
      :align: center
      
      Figure: Theme 'bootstrap'

The *bootstrap* theme supports pull-down menus.

.. only:: singlehtml

   .. container:: figabstract
   
      .. figurewrap:: _static/bootstrap_menu.png
         :width-latex: 400
         :width: 600
         :target-html: _static/bootstrap_menu.png
         :align: center
         
      Figure: Theme 'bootstrap' with open menu


.. only:: not singlehtml

   .. figurewrap:: _static/bootstrap_menu.png
      :width-latex: 400
      :width: 600
      :target-html: _static/bootstrap_menu.png
      :align: center
      
      Figure: Theme 'bootstrap' open menu

**configuration**
   
   The current example implementation contains the files
   within the default path:
      
      .. parsed-literal::
         
         setupddocx/configurations/sphinx/sphinx_bootstrap_theme
   
      .. raw:: html
      
         <div class="indextab">
         <div class="nonbreakheadtab">
         <div class="autocoltab">
   
      +--------------------------------+-----------------------------------------+
      | file                           | remark                                  |
      +================================+=========================================+
      | docsrc/conf.py                 | adds configuration variables            |
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
      
         python setup.py  -q  \\
            build_docx  \\
               --apiref  \\
               --conf-dir setupdocx/configurations/sphinx_bootstrap_theme/ \\
               --indexsrc=docsrc/index_rtd.rst \\
               --docname setupdocx-bootstrap \\ 
            install_docx \\
               --dist-dir doc \\
               --docname=setupdocx-bootstrap

         # cut-and-paste for execution
         # for readability split acros multiple lines

         