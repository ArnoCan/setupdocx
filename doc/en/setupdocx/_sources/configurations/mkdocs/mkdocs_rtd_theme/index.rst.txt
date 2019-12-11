
.. _CONFIG_TEMPLATE_MKDOCS_RTD:

********************************
Read The Docs - mkdocs_rtd_theme
********************************

.. raw:: html

    <style>
      html, body{
         height: 100%;
      }
      .document{
         height: 100%;
      }

    </style>



The *sphinx_rtd_theme* provides a local them for *ReadTheDocs* style.

**configuration**
   
   The current example implementation contains the files
   within the default path:

      .. parsed-literal::
         
         setupddocx/configurations/sphinx/sphinx_rtd_theme
   
      .. raw:: html
      
         <div class="indextab">
         <div class="nonbreakheadtab">
         <div class="autocoltab">
   
      +----------------+-----------------------------------------+
      | file           | remark                                  |
      +================+=========================================+
      | call_apidoc.sh | standard wrapper for sphinx-apidoc      |
      +----------------+-----------------------------------------+
      | call_apiref.sh | standard wrapper for epdoc              |
      +----------------+-----------------------------------------+
      | call_doc.sh    | standard wrapper for sphinx-build       |
      +----------------+-----------------------------------------+
      | conf.py        | adds configuration variables            |
      +----------------+-----------------------------------------+
      | custom.css     | sets some custom colors and sizes       |
      +----------------+-----------------------------------------+
      | epydoc.conf    | standard config for epydoc, the entries |
      +                +                                         +
      |                | target and css must be deativated       |
      +----------------+-----------------------------------------+
      | epydoc.css     | standard stylesheet config for epydoc   |
      +----------------+-----------------------------------------+
      | favicon.ico    | provides a demo favicon, requires *ICO* |
      +----------------+-----------------------------------------+
      | logo.png       | provides a demo logo, requires *PNG*    |
      +----------------+-----------------------------------------+
   
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
               --conf-dir setupdocx/configurations/sphinx_rtd_theme/ \\
               --indexsrc=docsrc/index_rtd.rst \\
               --docname setupdocx-rtd \\ 
            install_docx \\
               --dist-dir doc \\
               --docname=setupdocx-rtd

         # cut-and-paste for execution
         # for readability split acros multiple lines

         