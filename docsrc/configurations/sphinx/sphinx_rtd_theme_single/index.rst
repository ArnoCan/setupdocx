
.. _CONFIG_TEMPLATE_SPHINX_SINGLEHTML:

***************************************
Read The Docs - sphinx_rtd_theme_single
***************************************

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
The *singlehtml* variant is adapted for correct table of contents. 


.. only:: singlehtml

   .. container:: figabstract
   
      .. figurewrap:: _static/rtd_singlehtml.png
         :width-latex: 400
         :width: 600
         :target-html: _static/rtd_singlehtml.png
         :align: center
         
      Figure: Theme 'sphinx_rtd_theme' - singlehtml


.. only:: not singlehtml

   .. figurewrap:: _static/rtd_singlehtml.png
      :width-latex: 400
      :width: 600
      :target-html: _static/rtd_singlehtml.png
      :align: center
      
      Figure: Theme 'sphinx_rtd_theme' - singlehtml

**configuration**
   
   The current example implementation contains the files
   within the default path:

      .. parsed-literal::
         
         setupddocx/configurations/sphinx/sphinx_rtd_theme_single
   
      .. raw:: html
      
         <div class="indextab">
         <div class="nonbreakheadtab">
         <div class="autocoltab">
   
      +--------------------------------+-----------------------------------------+
      | file                           | remark                                  |
      +================================+=========================================+
      | docsrc/conf.py                 | adds configuration variables            |
      +--------------------------------+-----------------------------------------+
      | docsrc/index.rst               | addapts landing page for TOC            |
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
               --doctype=htmlsingle  \\
               --conf-dir=setupdocx/configurations/sphinx_rtd_theme_single/ \\
               --docname=setupdocx-rtd-single \\ 
            install_docx \\
               --dist-dir=doc \\
               --docname=setupdocx-rtd-single

         # cut-and-paste for execution
         # for readability split acros multiple lines

