
.. _CONFIG_EPYDOC_STANDALONE:

*****************
Epydoc Standalone
*****************

.. raw:: html

    <style>
      html, body{
         height: 100%;
      }
      .document{
         height: 100%;
      }

    </style>



The *epydoc_standalone* provides a configuration for the command *build_apiref*.
The created result is pure *Epydoc* document.
This is currently reliable for *HTML*, even though other formats such as *PDF* are supported too.

.. only:: singlehtml

   .. container:: figabstract
   
      .. figurewrap:: _static/epydoc_standalone.png
         :width-latex: 400
         :width: 600
         :target-html: _static/epydoc_standalone.png
         :align: center
         
      Figure: Theme 'epydoc_standalone'


.. only:: not singlehtml

   .. figurewrap:: _static/epydoc_standalone.png
      :width-latex: 400
      :width: 600
      :target-html: _static/epydoc_standalone.png
      :align: center
      
      Figure: Theme 'epydoc_standalone'

**configuration**
   
   The current example implementation contains the files
   within the default path: 

      .. parsed-literal::
         
         setupddocx/configurations/epydoc/standalone
   
      .. raw:: html
      
         <div class="indextab">
         <div class="nonbreakheadtab">
         <div class="autocoltab">
   
      +---------------------------+-----------------------------------------------------------+
      | file                      | remark                                                    |
      +===========================+===========================================================+
      | docsrc/epydoc.conf        | standard config for epydoc, the entries                   |
      +---------------------------+-----------------------------------------------------------+
      |                           | target and css must be deativated for use by command line |
      +---------------------------+-----------------------------------------------------------+
      | docsrc/epydoc.css         | standard stylesheet config for epydoc                     |
      +---------------------------+-----------------------------------------------------------+
   
      .. raw:: html
      
         </div>
         </div>
         </div>

**call**
   
   The call creates a html document within the local directory *doc*.
   
      .. parsed-literal::

         python setup.py  \\
            build_apiref \\
               --conf-dir=setupdocx/configurations/epydoc/standalone/ \\
            install_docx \\
               --dist-dir doc

         # copy-and-paste for execution
         # for readability split acros multiple lines

   The same call with detailed command line parameters:
   
      .. parsed-literal::

         python setup.py  \\
            build_apiref \\
               --doctype=html \\
               --docname=standalone \\
               --conf-dir=setupdocx/configurations/epydoc/standalone/ \\
            install_docx \\
               --dist-dir doc \\
               --docname=standalone

         # copy-and-paste for execution
         # for readability split acros multiple lines

