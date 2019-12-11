
.. _CONFIG_TEMPLATE_SPHINX_MAN:

***
man
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
   
      .. figurewrap:: _static/man.png
         :width-latex: 400
         :width: 600
         :target-html: _static/man.png
         :align: center
         
      Figure: Theme 'man'


.. only:: not singlehtml

   .. figurewrap:: _static/man.png
      :width-latex: 400
      :width: 600
      :target-html: _static/man.png
      :align: center
      
      Figure: Theme 'man'

**configuration**
   
   The current example implementation contains the files
   within the default path:

      .. parsed-literal::
         
         setupddocx/configurations/sphinx/man
   
      .. raw:: html
      
         <div class="indextab">
         <div class="nonbreakheadtab">
         <div class="autocoltab">
   
      +--------------------------------------------------+-----------------------------------------+
      | file                                             | remark                                  |
      +==================================================+=========================================+
      | docsrc/conf.py                                   | adds configuration variables            |
      +--------------------------------------------------+-----------------------------------------+
      | docsrc/_static/custom.css                        | sets some custom colors and sizes       |
      +--------------------------------------------------+-----------------------------------------+
      | docsrc/_static/favicon.ico                       | provides a demo favicon, requires *ICO* |
      +--------------------------------------------------+-----------------------------------------+
      | docsrc/_static/logo.png                          | provides a demo logo, requires *PNG*    |
      +--------------------------------------------------+-----------------------------------------+
   
      .. raw:: html
      
         </div>
         </div>
         </div>

**call**
   
   The call creates a one or more man pages in the *docname* subdirectory within 
   the local directory *doc*
   
      .. parsed-literal::
      
         python setup.py  -q  \\
            build_docx  \\
               --conf-dir setupdocx/configurations/man/ \\
               --docname setupdocx-man \\ 
            install_docx \\
               --dist-dir doc \\
               --docname=setupdocx-man

         # cut-and-paste for execution
         # for readability split acros multiple lines
