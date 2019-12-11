
.. _CONFIG_TEMPLATE_SPHINX_AGOGO:

*****
agogo
*****

.. raw:: html

    <style>
      html, body{
         height: 100%;
      }
      .document{
         height: 100%;
      }

    </style>



The *agogo* provides a standard style contained in *sphinx*.

.. only:: singlehtml

   .. container:: figabstract
   
      .. figurewrap:: _static/agogo.png
         :width-latex: 400
         :width: 600
         :target-html: _static/agogo.png
         :align: center
         
      Figure: Theme 'agogo'


.. only:: not singlehtml

   .. figurewrap:: _static/agogo.png
      :width-latex: 400
      :width: 600
      :target-html: _static/agogo.png
      :align: center
      
      Figure: Theme 'agogo'

**configuration**
   
   The current example implementation contains the files
   within the default path: 

      .. parsed-literal::
         
         setupddocx/configurations/sphinx/agogo
   
      .. raw:: html
      
         <div class="indextab">
         <div class="nonbreakheadtab">
         <div class="autocoltab">
   
      +----------------------------+-----------------------------------------+
      | file                       | remark                                  |
      +============================+=========================================+
      | docsrc/conf.py             | adds configuration variables            |
      +----------------------------+-----------------------------------------+
      | docsrc/epydoc.conf         | standard config for epydoc, the entries |
      +----------------------------+-----------------------------------------+
      |                            | target and css must be deativated       |
      +----------------------------+-----------------------------------------+
      | docsrc/_static/custom.css  | sets some custom colors and sizes       |
      +----------------------------+-----------------------------------------+
      | docsrc/_static/epydoc.css  | standard stylesheet config for epydoc   |
      +----------------------------+-----------------------------------------+
      | docsrc/_static/favicon.ico | provides a demo favicon, requires *ICO* |
      +----------------------------+-----------------------------------------+
      | docsrc/_static/logo.png    | provides a demo logo, requires *PNG*    |
      +----------------------------+-----------------------------------------+
   
      .. raw:: html
      
         </div>
         </div>
         </div>

**call**
   
   The call creates a html document within the local directory *doc*
   
      .. parsed-literal::

         python setup.py  \\
            build_docx \\
               --conf-dir=setupdocx/configurations/sphinx/agogo/ \\
            install_docx \\
               --dist-dir doc

         # cut-and-paste for execution
         # for readability split acros multiple lines

   The same call with detailed command line parameters:
   
      .. parsed-literal::

         python setup.py  \\
            build_docx \\
               --doctype=html \\
               --docname=agogo \\
               --conf-dir=setupdocx/confonfigurations/sphinx/agogo/
            install_docx \\
               --dist-dir doc \\
               --docname=agogo

         # cut-and-paste for execution
         # for readability split acros multiple lines

