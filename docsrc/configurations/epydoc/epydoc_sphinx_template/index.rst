
.. _CONFIG_TEMPLATE_EPYDOC_ATTACH_SPHINX_TEMPLATE:

***************************
Attached by Sphinx Template
***************************

.. raw:: html

    <style>
      html, body{
         height: 100%;
      }
      .document{
         height: 100%;
      }

    </style>



The *epydoc_sphinx_template* provides a configuration for the command *build_docx*
to embed the API reference.
This includes the sidebar entries "Shortcuts" and "Application".
The selection of the API reference is presented as the link "apiref" within the sidebar.
The landing page of the link contains the *IFrame* as a container here for the *Epydoc*
document.
The path and the title could be configured via "*conf.py*".

.. only:: singlehtml

   .. container:: figabstract
   
      .. figurewrap:: _static/sphinx_template_select.png
         :width-latex: 400
         :width: 600
         :target-html: _static/sphinx_template_select.png
         :align: center
         
      Figure: Theme 'epydoc_embed'


.. only:: not singlehtml

   .. figurewrap:: _static/sphinx_template_select.png
      :width-latex: 400
      :width: 600
      :target-html: _static/sphinx_template_select.png
      :align: center
      
      Figure: Theme 'epydoc_embed'

Resulting in the display:


.. only:: singlehtml

   .. container:: figabstract
   
      .. figurewrap:: _static/sphinx_template_iframe.png
         :width-latex: 400
         :width: 600
         :target-html: _static/sphinx_template_iframe.png
         :align: center
         
      Figure: Theme 'epydoc_embed'


.. only:: not singlehtml

   .. figurewrap:: _static/sphinx_template_iframe.png
      :width-latex: 400
      :width: 600
      :target-html: _static/sphinx_template_iframe.png
      :align: center
      
      Figure: Theme 'epydoc_embed'


The full-screen mode.

.. only:: singlehtml

   .. container:: figabstract
   
      .. figurewrap:: _static/epydoc_full.png
         :width-latex: 400
         :width: 600
         :target-html: _static/epydoc_full.png
         :align: center
         
      Figure: Theme 'epydoc_embed'


.. only:: not singlehtml

   .. figurewrap:: _static/epydoc_full.png
      :width-latex: 400
      :width: 600
      :target-html: _static/epydoc_full.png
      :align: center
      
      Figure: Theme 'epydoc_embed'

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
      | docsrc/epydoc.css          | standard stylesheet config for epydoc   |
      +----------------------------+-----------------------------------------+
      | docsrc/_static/custom.css  | sets some custom colors and sizes       |
      +----------------------------+-----------------------------------------+
      | docsrc/_static/favicon.ico | provides a demo favicon, requires *ICO* |
      +----------------------------+-----------------------------------------+
      | docsrc/_static/logo.png    | provides a demo logo, requires *PNG*    |
      +----------------------------+-----------------------------------------+
      | docsrc/_themes             | the theme                               |
      +----------------------------+-----------------------------------------+
   
      .. raw:: html
      
         </div>
         </div>
         </div>

**call**
   
   The call creates a html document within the local directory *doc*
   
      .. parsed-literal::

         python setup.py  \\
            build_docx  \\
               --conf-dir=setupdocx/configurations/epydoc/default_white_with_green_iframe/  \\
               --apiref  \\
            install_docx  \\
               --dist-dir doc  \\

         # cut-and-paste for execution
         # for readability split acros multiple lines

   The same call with detailed command line parameters:
   
      .. parsed-literal::

         python setup.py  \\
            build_docx  \\
               --doctype=html  \\
               --docname=white_with_green_iframe  \\
               --conf-dir=setupdocx/configurations/epydoc/default_white_with_green_iframe/  \\
               --apiref  \\
            install_docx  \\
               --dist-dir doc  \\
               --docname=white_with_green_iframe

         # cut-and-paste for execution
         # for readability split acros multiple lines

