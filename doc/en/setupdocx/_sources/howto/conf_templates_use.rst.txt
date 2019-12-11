
.. _HOWTO_USECONFTEMPLATES:

Use Configuration Templates
---------------------------

Sphinx
^^^^^^
#. **Select a Configuration Template**

   Create your own from ground up, or select a provided theme
   and the appropriate configuration template.
   The following templates for *Sphinx* are contained in *setupdocx*.
        
   * Standard Themes:
   
     These are contained in the standard *Sphinx* installation.   

      * :ref:`CONFIG_TEMPLATE_SPHINX_AGOGO`
      * :ref:`CONFIG_TEMPLATE_SPHINX_BIZSTYLE`
      * :ref:`CONFIG_TEMPLATE_SPHINX_DEFAULT2`
      * :ref:`CONFIG_TEMPLATE_SPHINX_DEFAULT3`
      * :ref:`CONFIG_TEMPLATE_SPHINX_NATURE`
      * :ref:`CONFIG_TEMPLATE_SPHINX_SPHINXDOC`
      * :ref:`CONFIG_TEMPLATE_SPHINX_TRADITIONAL`
      
   * Special Themes:   

     These are opensource and has to be installed, e.g. via *PyPI*, or
     *github*.   

      * :ref:`CONFIG_TEMPLATE_SPHINX_ALABASTER`
      * :ref:`CONFIG_TEMPLATE_SPHINX_GUZZLE`
      * :ref:`CONFIG_TEMPLATE_SPHINX_RTD`
      * :ref:`CONFIG_TEMPLATE_SPHINX_BOOTSTRAP`

   * Custom Themes:
     These are modified by local changes. The current demos are based
     on standard themes.   

      * :ref:`CONFIG_TEMPLATE_SPHINX_DEFAULT_EXTENDED`
      * :ref:`epub <CONFIG_TEMPLATE_SPHINX_EPUB>`
      * :ref:`CONFIG_TEMPLATE_SPHINX_PDF`


#. **Define the Document Structure**

   Define the appropriate document structure based on *toctree*,
   see [sphinxdoc]_ and [restdir]_.
   Be aware, that document formats based on a single file behave differently than multi-file
   formats, though they obviously concatenate instead of linking by references.
   Thus the the different output formats require frequently configurations  
   which contain the appropriate *index.rst* and more when required.
   See the contained subdirectory *docsrc* of the configuration, 
   for the document creation including the *setup.py* refer to :ref:`HOWTO_CREATEDOC`.

#. **Copy the Configuration Template**

   Copy the template directory in order to adapt your files, the structure, 
   and the style.
   The directory is the later parameter :ref:`--confdir <setupdocxbuild_OPTIONS_config_path>`
   of the call:
   
      .. parsed-literal::
      
         python setup.py build_docx :ref:`--confdir= <setupdocxbuild_OPTIONS_config_path>` <config-path>

#. **Adapt the Configuration Template**

   The configuration template contains the required configuration data for the selected
   tools as well as for the independent autonomous representaion of the document, e.g.
   static data such as images and style sheets. 
   The default is the *Sphinx* toolset [sphinxdoc]_.
   
   The configuration of sphinx provided by *conf.py* permits for multiple sections of
   different so called builders. 
   This is e.g. *html* *epub*, *latex* for *PDF*, or *man* for manpages.
   Anyhow, due to additional restrictions, e.g. such as no image capabilities of man pages,
   or the different behaviour of single and multi page documents related in particular to the
   directives *include*, and *toc*, or references, it is advisable to distinguish each 
   created document type by a separate set of configuration in it's own directory.
   The directory contains the view parts as well as frequently required content patches.
   The most commonly required patch is here the main file *index.rst*, as well as 
   the appropriate *custom.css*.
   Subdirectories such as customized *_themes* and *_templates* are supported too.
   
   The *setupdocx* in addition supports some sphinx extensions, in particular for the simplified
   size-adaptation of images including figures :ref:`setupdocxSphinxExtImagewrap` to the
   various output formats.  

   The architecture of the *setupdocx* is based on multiple layers. 
   The integration modules for *setup.py* support additional commands [distutils]_,
   while the actual used toolset is wrapped within a slim adaptation layer of scripts
   based on a command line interface.
   The provided default wrapper scripts are generic and may fit to all standard requirements.
   These are located within the installation directory of *setupdocx*.
   The search order for the actual executed script is
   
      #. confdir - :ref:`--confdir <setupdocxbuild_OPTIONS_config_path>`
      #. docsrc -  :ref:`--docsource <setupdocxbuild_OPTIONS_docsource>`
      #. setupdocx - the installation directory
   
   Anyhow, when required the scripts could be easily modified or completely replaced.
   Either by persistent  configuration, or call-by-call with teh parameters
   :ref:`--build-apidoc <setupdocxbuild_OPTIONS_build_apidoc>`,
   :ref:`--build-apiref <setupdocxbuild_OPTIONS_build_apiref>`,
   or
   :ref:`--build-doc <setupdocxbuild_OPTIONS_build_doc>`.
   alternatively by a specific naming scheme for the build tools, e.g.
   :ref:`--build-doc <setupdocxbuild_OPTIONS_build_doc>`.
   
   The provided interface is based on envirnment variables, see :ref:`setupdocx_ENV_call_environment`.
   The actual resulting environment parameters are displayed by the 
   option global option '--verbose', see also :ref:`DOCX_VERBOSE <setupdocx_ENV_DOCX_VERBOSE>`.  
   The current release contains *bash* scripts only, while additional based on *PowerShell*,
   and *Python* will follow soon. 

   The required directory structure of the configuration template directory is
   for example in case of *ReadTheDocs*:
   
      .. parsed-literal::
      
         <conf-template-name>
         └── docsrc
             ├── conf.py             # this file must be edited
             ├── index.rst           # this file must be edited
             └── _static
                 ├── custom.css
                 ├── favicon.ico     # this file must be edited
                 └── logo.png        # this file must be edited

   In case of included API reference, here based on *epydoc*:
   
      .. parsed-literal::
      
         <conf-template-name>
         └── docsrc
             ├── conf.py             # this file must be edited
             ├── index.rst           # this file must be edited
             └── _static
                 ├── custom.css
                 ├── epydoc.conf     # this file must be edited
                 ├── epydoc.css      # this file must be edited
                 ├── favicon.ico     # this file must be edited
                 └── logo.png        # this file must be edited

   The same with optional custom call-scripts. Due to the pure
   environment based interface you can use whantever implementation
   language you want, as long as it is capable to read environment 
   variables. 
   
      .. parsed-literal::
      
         <conf-template-name>
         ├── **call_apidoc.ps1**         # this is optional - implemented by 'PowerShell'
         ├── **call_apiref.lua**         # this is optional - implemented by 'Lua'
         ├── **call_doc.py**             # this is optional - implemented by 'Python'
         └── docsrc
             ├── conf.py             # this file must be edited
             ├── index.rst           # this file must be edited
             └── _static
                 ├── custom.css
                 ├── epydoc.conf     # this file must be edited
                 ├── epydoc.css      # this file must be edited
                 ├── favicon.ico     # this file must be edited
                 └── logo.png        # this file must be edited


   The complete content of the directory *docsrc* is copied into the directory.

      .. parsed-literal::

         :ref:`\<build-dir\> <setupdocxbuild_OPTIONS_build_dir>`/apidoc/sphinx

   The files superpose the generated output by *sphinx-apidoc* called 
   by first step of *call_apidoc.sh*.
   So check initially the created *index.rst* of *sphinx-apidoc*.
   The first step of the call of *call_apidoc.sh* could be suppressed
   by using an empty option :ref:`--build-apidoc <setupdocxbuild_OPTIONS_build_apidoc>`.

      .. parsed-literal::

         python setup.py build_docx :ref:`--build-apidoc='' <setupdocxbuild_OPTIONS_build_apidoc>`
   
   The other build steps could be deactivated the same way by 
   :ref:`--build-doc <setupdocxbuild_OPTIONS_build_doc>`,
   while the build step of    
   :ref:`--apiref <setupdocxbuild_OPTIONS_apiref>`
   is optional and deactivated by default anyway.
   
   The required minimum modifications mainly comprise the name of the project, 
   list of source directories, and eventually required extensions e.g.
   for *Sphinx*.
   The files are inline documented, though the modification should be easily done.
   
   See also :ref:`HOWTO_CREATECONFTEMPLATES`.

#. **Call 'setup.py'**

   Once the preparations are completed, the document should be created by the call:
   
      .. parsed-literal::
   
         python setup.py build_docx :ref:`--confdir=/your/configuration/path/ <setupdocxbuild_OPTIONS_config_path>`

   The document is created by default in the directory:

      .. parsed-literal::
   
         :ref:`\<build-dir\> <setupdocxbuild_OPTIONS_build_dir>`/doc/:ref:`\<docname\> <setupdocxbuild_OPTIONS_docname>`

   See also :ref:`HOWTO_CREATEDOC`, and :ref:`setupdocxEXAMPLES`.

#. **Read the Document**

   In case of the document type *html* this contains by default the main page:
   
      .. parsed-literal::
   
         :ref:`\<build-dir\> <setupdocxbuild_OPTIONS_build_dir>`/doc/:ref:`\<docname\> <setupdocxbuild_OPTIONS_docname>`/index.html

For further steps refer to :ref:`HOWTO_INSTALDOC`, and :ref:`HOWTO_PACKAGEDOC`.

Epydoc - Standalone
^^^^^^^^^^^^^^^^^^^
available soon

Epydoc Embedded into Sphinx
^^^^^^^^^^^^^^^^^^^^^^^^^^^
available soon

