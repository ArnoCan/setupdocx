
.. _CONFIG_TEMPLATE_EPYDOC_EMBED_IFRAME:

*************************
Epydoc Embedded in IFrame
*************************

.. raw:: html

    <style>
      html, body{
         height: 100%;
      }
      .document{
         height: 100%;
      }

    </style>



The configuration template *epydoc_sphinx_iframe* provides a configuration for the 
commands *build_docx* and/or *build_apiref* for the document type *HTML*.
The result is an embedded *Epydoc* document within the directory within the *Sphinx* document.
The integration requires an additional page with an *IFrame* as the container for the
*EPydoc* document.

The provided example is based on the theme *sphinx_rtd_theme* for a local *ReadTheDocs*
document style creation.
The theme could be easily installed via *PyPI.org*.
   

.. only:: singlehtml

   .. container:: figabstract
   
      .. figurewrap:: _static/epydoc_sphinx_iframe.png
         :width-latex: 400
         :width: 600
         :target-html: _static/epydoc_sphinx_iframe.png
         :align: center
         
      Figure: Configuration 'epydoc_sphinx_iframe'


.. only:: not singlehtml

   .. figurewrap:: _static/epydoc_sphinx_iframe.png
      :width-latex: 400
      :width: 600
      :target-html: _static/epydoc_sphinx_iframe.png
      :align: center
      
      Figure: Configuration 'epydoc_sphinx_iframe'

The full-screen mode.
Due to ongoing groundwork on an enhanced documentation tool the integration of
*Epydoc* is currently kept on basic level, while the efforts are focused else.
Thus some legacy  options change to full-screen mode, which requires the back-button 
of the browser to return to the previous position.
The *Epydoc* option *Home* switches back to the top of the containing document.
This feature is not yet publicly available, but present on the public 
documents of the author.

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
   The integration is not fully automated.
   This is due to the intended support of arbitrary designs and themes.
   Thus the container page for the *Epydoc* integration has to be edited 
   by the author of the document.

   The following required steps of the creation, integration, packaging, and
   the continous local installation are fully automated.
   The commands could easily be used manually, or integrated into a CI/CD
   framework. 
   This requires just the copy of the patched files into the configuration 
   directory and the call of the command *build_docx* with the configuration
   parameter :ref:`--confdir <setupdocxbuild_OPTIONS_config_path>`. 
   
   The current example implementation contains the files required for the
   *ReadTheDocs* theme as well as for *Epydoc*.
   The configuration is part of the package and stored within the default path: 

      .. parsed-literal::
         
         setupddocx/configurations/epydoc/epydoc_sphinx_iframe
   
   The contained files are listed in the following table.
   These are copied by the standard mechanism into the documents build directory
   in order to replace present files.
   Thus the configuration could be kept outside the patched document without changing
   the documents default sources.
   
      .. raw:: html
      
         <div class="indextab">
         <div class="nonbreakheadtab">
         <div class="autocoltab">
   
      +-------------------------------------+------------------------------------------+
      | file                                | remark                                   |
      +=====================================+==========================================+
      | docsrc/index.rst                    | replaces *index.rst* of the document     |
      +-------------------------------------+------------------------------------------+
      | docsrc/index_part_apiref_scaled.rst | adds a page with the IFrame for *Epydoc* |
      +-------------------------------------+------------------------------------------+
      | docsrc/conf.py                      | adds configuration variables             |
      +-------------------------------------+------------------------------------------+
      | docsrc/epydoc.conf                  | standard config for epydoc, the entries  |
      +-------------------------------------+------------------------------------------+
      |                                     | target and css must be deactivated       |
      +-------------------------------------+------------------------------------------+
      | docsrc/epydoc.css                   | standard stylesheet config for epydoc    |
      +-------------------------------------+------------------------------------------+
      | docsrc/_static/custom.css           | sets some custom colors and sizes        |
      +-------------------------------------+------------------------------------------+
      | docsrc/_static/favicon.ico          | provides a demo favicon, requires *ICO*  |
      +-------------------------------------+------------------------------------------+
      | docsrc/_static/logo.png             | provides a demo logo, requires *PNG*     |
      +-------------------------------------+------------------------------------------+

      .. raw:: html
      
         </div>
         </div>
         </div>

**call**
   
   The call creates a html document within the local directory *doc*
   
      .. parsed-literal::

         python setup.py  \\
            build_docx \\
               --apiref \\
               --conf-dir=setupdocx/configurations/epydoc/epydoc_sphinx_iframe/ \\
            install_docx \\
               --dist-dir doc

         # copy-and-paste for execution
         # for readability split acros multiple lines

   The same call with detailed command line parameters:
   
      .. parsed-literal::

         python setup.py  \\
            build_docx \\
               --doctype=html \\
               --docname=sphinx_epydoc \\
               --conf-dir=setupdocx/configurations/epydoc/epydoc_sphinx_iframe/ \\
               --apiref \\
            install_docx \\
               --dist-dir doc \\
               --docname=sphinx_epydoc

         # copy-and-paste for execution
         # for readability split acros multiple lines

