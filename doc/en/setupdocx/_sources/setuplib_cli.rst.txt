
.. _SETUPLIBCOMMANDSCLI:

**********************
Command Line Interface
**********************

The package *setupdocx* provides the following extensions for the standard 
command line interface of *setup.py* from the *setuptools* / *distutils*.
See :ref:`EXAMPLES <setupdocxEXAMPLES>` for required integration steps, 
check integration with:

   .. parsed-literal::

      :ref:`python setup.py --help-commands <setupdocxOPTIONS_help-commands>`

You should see the extra commands "*build_docx*", "*dist_docx*", and "*install_docx*".

* *setup.py* extension commands:

   .. raw:: html

      <style>
         div.tmptab table.docutils col {
            width: auto;
         }
         div.tmptab table td:nth-child(1) {
            width: 30ch;
         }
      </style>
   
      <div class="tmptab">
      <div class="overviewtab">
   
   +------------------------------------------------------+--------------------------------------------------------------------------------------------------+
   | :ref:`build_docx <setupdocxCOMMANDS_build_docx>`     | Generate API specification, and create documents. Optional combined with *apidoc*, and *apiref*. |
   +------------------------------------------------------+--------------------------------------------------------------------------------------------------+
   | :ref:`build_apidoc <setupdocxCOMMANDS_build_apidoc>` | Generate API specification only.                                                                 |
   +------------------------------------------------------+--------------------------------------------------------------------------------------------------+
   | :ref:`build_apiref <setupdocxCOMMANDS_build_apiref>` | Generate Javadoc style API specification.                                                        |
   +------------------------------------------------------+--------------------------------------------------------------------------------------------------+
   | :ref:`dist_docx <setupdocxCOMMANDS_dist_docx>`       | Package documents for distribution.                                                              |
   +------------------------------------------------------+--------------------------------------------------------------------------------------------------+
   | :ref:`install_docx <setupdocxCOMMANDS_install_docx>` | Install documents from sources.                                                                  |
   +------------------------------------------------------+--------------------------------------------------------------------------------------------------+

   .. raw:: html
   
      </div>
      </div>

                  

* *setup.py* common global options:

   .. raw:: html

      <style>
         div.tmptab table.docutils col {
            width: auto;
         }
         div.tmptab table td:nth-child(1) {
            width: 30ch;
         }
      </style>

      <div class="tmptab">
      <div class="overviewtab">
   
   +---------------------------------------------------------------------+-----------------------------------------------------+
   | :ref:`--sdk <setupdocxOPTIONS_sdk>`                                 | Extends the dependencies for development utilities. |
   +---------------------------------------------------------------------+-----------------------------------------------------+
   | :ref:`--no-install-requires <setupdocxOPTIONS_no-install-requires>` | Deactivates pre-requisites.                         |
   +---------------------------------------------------------------------+-----------------------------------------------------+
   | :ref:`--offline <setupdocxOPTIONS_offline>`                         | Deactivates PyPi access.                            |
   +---------------------------------------------------------------------+-----------------------------------------------------+
   | :ref:`--help-setupdocx <setupdocxOPTIONS_help-setupdocx>`           | Displays help for *setupdocx*.                      |
   +---------------------------------------------------------------------+-----------------------------------------------------+

   .. raw:: html
   
      </div>
      </div>


.. _setupdocxCLISYNOPSIS:

SYNOPSIS
========

.. parsed-literal::

   :ref:`setup.py <SETUP_PY>` :ref:`[Global-OPTIONS] <setupdocxCLIOPTIONS>` :ref:`[COMMANDS-with-context-OPTIONS] <setupdocxCOMMANDS>` 

.. _setupdocxCLIOPTIONS:


OPTIONS
=======

.. index::
   pair: options; --sdk
   pair: setupdocx; --sdk

.. _setupdocxOPTIONS_sdk:

-\-sdk
------
Supports a separate dependency list for the build and packaging environment.
The following informal convention has to be implemented within the file *setup.py*.

   .. parsed-literal::
   
      __sdk = False
      """Set by the option "--sdk". Controls the installation environment."""
   
      if '--sdk' in sys.argv:
          _sdk = True
          sys.argv.remove('--sdk')
   
   
      _packages_sdk = find_packages(include=['setupdocx'] )  # your development packages
      """Python packages to be installed."""
   
   
      if __sdk: # pragma: no cover
          try:
              import sphinx_rtd_theme  # @UnusedImport
          except:
              sys.stderr.write("WARNING: Cannot import package 'sphinx_rtd_theme', cannot create local 'ReadTheDocs' style.")

          _install_requires.extend(
              [
                  'sphinx >= 1.4',
                  'epydoc >= 3.0',
              ]
          )
   
          _packages = _packages_sdk

For an example refer to *setup.py* of *setupdocx*.

.. index::
   pair: options; --no-install-requires
   pair: setupdocx; --no-install-requires

.. _setupdocxOPTIONS_no-install-requires:

-\-no-install-requires
----------------------
Suppresses installation dependency checks,
requires appropriate PYTHONPATH.
The following informal convention has to be implemented within the file *setup.py*.

   .. parsed-literal::
   
      __no_install_requires = False
   
      if '--no-install-requires' in sys.argv:
          __no_install_requires = True
          sys.argv.remove('--no-install-requires')
   
   
      if __no_install_requires:
          print("#")
          print("# Changed to offline mode, ignore install dependencies completely.")
          print("# Requires appropriate PYTHONPATH.")
          print("# Ignored dependencies are:")
          print("#")
          for ir in _install_requires:
              print("#   "+str(ir))
          print("#")
          _install_requires=[]

For an example refer to *setup.py* of *setupdocx*.

.. index::
   pair: options; --offline
   pair: setupdocx; --offline

.. _setupdocxOPTIONS_offline:

-\-offline
----------
Sets online dependencies to offline, or ignores online
dependencies.
The following informal convention has to be implemented within the file *setup.py*.

   .. parsed-literal::
   
      __offline = False
   
      if '--offline' in sys.argv:
          __offline = True
          __no_install_requires = True
          sys.argv.remove('--offline')

For an example refer to *setup.py* of *setupdocx*.

.. index::
   pair: options; --help-commands
   pair: setupdocx; --help-commands

.. _setupdocxOPTIONS_help-commands:

-\-help-commands
----------------
The option '--help-commands' itself is not part of the *setupdocx*, but it lists all
successfull integrated extension commands.
Thus the current extension commands has to be visible for validation. 

.. index::
   pair: options; --help-setupdocx
   pair: setupdocx; --help-setupdocx

.. _setupdocxOPTIONS_help-setupdocx:

-\-help-setupdocx
-----------------
Special help for *setupdocx*.

For an example refer to *setup.py* of *setupdocx*.

.. _setupdocxCOMMANDS:


COMMANDS
========
The commands could be combined within one call and are than processed from-left-to-right.
But be aware that each command is a separate module, thus only knows it's own options,
which are the right-hand side options util the following next command.
The context options for each command has to be provided separately.
For example the change of the document
e.g. by :ref:`--name <setupdocxbuild_OPTIONS_name>`,
or :ref:`--docname <setupdocxbuild_OPTIONS_docname>`,
requires the appropriate parameter for each following command. 

   .. index::
      pair: command; build_docx
      pair: command; dist_docx
      pair: command; install_docx

   
   .. raw:: html

      <div class="tmptab">
      <div class="overviewtab">
   
   +--------------------------------------------------------------------------------------------------+------------------------------------+
   | :ref:`setupdocxCOMMANDS_build_docx`   [:ref:`build_docx-options <setupdocxbuild_OPTIONS>`]       | create documents                   |
   +--------------------------------------------------------------------------------------------------+------------------------------------+
   | :ref:`setupdocxCOMMANDS_build_apidoc`   [:ref:`build_apidoc-options <setupapidocbuild_OPTIONS>`] | create API reference only          |
   +--------------------------------------------------------------------------------------------------+------------------------------------+
   | :ref:`setupdocxCOMMANDS_build_apiref`   [:ref:`build_apiref-options <setupapirefbuild_OPTIONS>`] | create javadoc style API reference |
   +--------------------------------------------------------------------------------------------------+------------------------------------+
   | :ref:`setupdocxCOMMANDS_dist_docx`    [:ref:`dist_docx-options <setupdocxbuild_OPTIONS>`]        | package documents                  |
   +--------------------------------------------------------------------------------------------------+------------------------------------+
   | :ref:`setupdocxCOMMANDS_install_docx` [:ref:`install_docx-options <setupdocxbuild_OPTIONS>`]     | install documents                  |
   +--------------------------------------------------------------------------------------------------+------------------------------------+


   .. raw:: html
   
      </div>
      </div>


.. index::
   pair: command; build_docx
   pair: setupdocx; build_docx

.. _setupdocxCOMMANDS_build_docx:

build_docx
----------

Creates Sphinx based documentation with optional embedded javadoc-style
API reference by epydoc, html only.
The command calls for the creation of the sphinx documents customizable 
scripts - see :ref:`--build-apidoc <setupdocxbuild_OPTIONS_build_apidoc>` 
, :ref:`--build-doc  <setupdocxbuild_OPTIONS_build_doc>`, and
:ref:`--build-apiref  <setupdocxbuild_OPTIONS_build_apiref>` - 
and passes the parameters as environment variables,
see :ref:`setupdocx_ENV_call_environment`.
 
.. _setupdocxbuild_OPTIONS:

.. index::
   pair: build_docx; --apidoc

.. _setupdocxbuild_OPTIONS_apidoc:

-\-apidoc
^^^^^^^^^
   Enables the creation call for the API documentation.
   
      .. parsed-literal::
      
         --apidoc
   
         # default := '' # off

   Sets the environment variable :ref:`DOCX_APIDOC <setupdocx_ENV_DOCX_APIDOC>` to 
   the value '*1*' when active.


.. index::
   pair: build_docx; --apiref

.. _setupdocxbuild_OPTIONS_apiref:

-\-apiref
^^^^^^^^^
   Enables the creation of the API reference.
   
      .. parsed-literal::
      
         --apiref
   
         # default := '' # off

   Sets the environment variable :ref:`DOCX_APIREF <setupdocx_ENV_DOCX_APIREF>`
   to the value '*1*' when active.


.. index::
   pair: break_on_err; --break-on-err

.. _setupdocxbuild_OPTIONS_break_on_err:

-\-break-on-err
^^^^^^^^^^^^^^^
   Exits the build process on first error. 
   
      .. parsed-literal::
      
         --break-on-error
   
         # default := False

   Sets the environment variable :ref:`DOCX_BREAKONERR <setupdocx_ENV_DOCX_BREAKONERR>`
   to the value '*1*' when active.


.. index::
   pair: build_docx; --build-apiref

.. _setupdocxbuild_OPTIONS_build_apiref:

-\-build-apiref=
^^^^^^^^^^^^^^^^
   Sets the build script for the *apiref*.
   
      .. parsed-literal::
      
         --apiref=(
             <path-to-script>    # calls the script
         )
   
         # default := :ref:`<confdir>/call_apiref.sh <CALL_APIREF>`
   
   In case the provided value is a call name only the following locations 
   are searched.
   
      0. current configuration directory
      1. document source for subdirectory 'conf'
      2. the 'conf' directory within the package *setupdocx* 

   If the parameter is not provided and not present in *setup.conf*,
   the default resolution is:
   
      0. the  default value from the class member *docx_defaults*
      1. *call_ref* from current configuration directory
      2. *call_ref* from document source for subdirectory 'conf'
      3. *call_ref* from the 'conf' directory within the package *setupdocx* 

   The called final tool is currently by default *epydoc*.

      .. parsed-literal::
      
         setup.py build_docx --apiref --build-apiref=<confdir>/call_apiref.sh

   The current release supports by default *bash* scripts,
   this could be varied as required, e.g. by a *DOS* batch script, or a *PowerShell* script,
   or simply by a *Python* script. 
 
   See also :ref:`Call Environment <setupdocx_ENV_call_environment>`.
 

.. index::
   pair: build_docx; --build-apidoc

.. _setupdocxbuild_OPTIONS_build_apidoc:

-\-build-apidoc=
^^^^^^^^^^^^^^^^
   Sets the called *build-apidoc* for document creation.
   
      .. parsed-literal::
      
         --build-apidoc=(
             <path-to-script>    # calls the script
             | sphinx-apidoc     # calls <confdir>/call_sphinx_apidoc.sh
             | ''                # the build stage is suppressed
         )
   
         # default := :ref:`<confdir>/call_apidoc.sh <CALL_APIDOC>`
   
   In case the provided value is a call name only the following locations 
   are searched.
   
      0. current configuration directory
      1. document source for subdirectory 'conf'
      2. the 'conf' directory within the package *setupdocx* 

   If the parameter is not provided and not present in *setup.conf*,
   the default resolution is:
   
      0. the  default value from the class member *docx_defaults*
      1. *call_apidoc* from current configuration directory
      2. *call_apidoc* from document source for subdirectory 'conf'
      3. *call_apidoc* from the 'conf' directory within the package *setupdocx* 

   The called final tool is currently by default *sphinx-apidoc*.

      .. parsed-literal::
      
         setup.py build_docx --build-apidoc=<confdir>/call_apidoc.sh

   The current release supports by default *bash* scripts,
   this could be varied as required, e.g. by a *DOS* batch script, or a *PowerShell* script,
   or simply by a *Python* script. 
   
   See also :ref:`Call Environment <setupdocx_ENV_call_environment>`.

.. index::
   pair: build_docx; --build-dir

.. _setupdocxbuild_OPTIONS_build_dir:

-\-build-dir=
^^^^^^^^^^^^^
   The base directory of the build directory tree.
   
      .. parsed-literal::
      
         --build-dir=(
             <path-to-build-root>    # sets the build root directory
         )
   
         # default := build/
   
   The resulting actual build directory:
   
      .. parsed-literal::
      
         build/apidoc/sphinx
   
   This directory is used as temporary build directory for all calls of the same *build-dir*.
   Sets the environment variable :ref:`DOCX_BUILDDIR <setupdocx_ENV_DOCX_BUILDDIR>`.
 

.. index::
   pair: build_docx; --build-doc

.. _setupdocxbuild_OPTIONS_build_doc:

-\-build-doc=
^^^^^^^^^^^^^
   Sets the called *build-doc* for document creation.
   
      .. parsed-literal::
      
         --build-doc=(
             <path-to-script>    | calls the script
             | sphinx            # calls <confdir>/call_sphinx.sh
             | ''                | the build stage is suppressed
         )
   
         # default := :ref:`<confdir>/call_doc.sh <CALL_DOC>`

   In case the provided value is a call name only the following locations 
   are searched.
   
      0. current configuration directory
      1. document source for subdirectory 'conf'
      2. the 'conf' directory within the package *setupdocx* 

   If the parameter is not provided and not present in *setup.conf*,
   the default resolution is:
   
      0. the  default value from the class member *docx_defaults*
      1. *call_doc* from current configuration directory
      2. *call_doc* from document source for subdirectory 'conf'
      3. *call_doc* from the 'conf' directory within the package *setupdocx* 
   
   The called final tool is currently by default *sphinx-build*,
   which is called by the created *Makefile* with the option *html*.

      .. parsed-literal::
      
         setup.py build_docx --build-doc=<confdir>/call_doc.sh
   
         # default := :ref:`<confdir>/call_doc.sh <CALL_DOC>`
   
   The current release supports by default *bash* scripts,
   this could be varied as required, e.g. by a *DOS* batch script, or a *PowerShell* script. 
   
   See also :ref:`Call Environment <setupdocx_ENV_call_environment>`.
   

.. index::
   pair: build_docx; --build-reldir

.. _setupdocxbuild_OPTIONS_build_reldir:

-\-build-reldir=
^^^^^^^^^^^^^^^^
   The relative directory of the build directory tree.
   
      .. parsed-literal::
      
         --build-reldir=(
             <relative-path-to-build-dir>    # sets the build subdirectory
         )
   
         # default := apidoc/sphinx
   
   The resulting actual build directory:
   
      .. parsed-literal::
      
         build/apidoc/sphinx
   
   This directory is used as temporary build directory for all calls of the same *build-dir*.
   Sets the environment variable :ref:`DOCX_BUILDRELDIR <setupdocx_ENV_DOCX_BUILDRELDIR>`.


.. index::
   pair: build_docx; --build-type
   pair: --build-type; sphinx

.. _setupdocxbuild_OPTIONS_build_proc:

-\-build-proc=
^^^^^^^^^^^^^^
The build procesor.

   .. parsed-literal::
   
      build-proc := (
             sphinx
           | sphinx-build
           | sphinx-apidoc
           | epydoc
           | ...
      )

      # default := sphinx == sphinx-build

The build processor sets the following defaults for the build calls.

   .. raw:: html
   
      <div class="indextab">
      <div class="nonbreakheadtab">
      <div class="autocoltab">

   +---------------------------------------------------------------+-----------------------------------------+
   |                                                               | default                                 |
   +===============================================================+=========================================+
   | :ref:`build-doc <setupdocxbuild_OPTIONS_build_doc>`           | :ref:`call_doc.sh <CALL_DOC>`    (1)    |
   +---------------------------------------------------------------+-----------------------------------------+
   | :ref:`build-apidoc <setupdocxbuild_OPTIONS_build_apidoc>`     | :ref:`call_apidoc.sh <CALL_APIDOC>` (2) |
   +---------------------------------------------------------------+-----------------------------------------+
   | :ref:`build-apiref <setupdocxbuild_OPTIONS_build_apiref>` (4) | :ref:`call_apiref.sh <CALL_APIREF>` (3) |
   +---------------------------------------------------------------+-----------------------------------------+

   .. raw:: html
   
      </div>
      </div>
      </div>

   (1) 
       curently the same

   (2)
       curently the same

   (3)
       curently the same

   (4)
       called when option *--apiref* is present
      
.. index::
   pair: builder; --builder
   pair: --builder; sphinx

.. _setupdocxbuild_OPTIONS_builder:

-\-builder=
^^^^^^^^^^^
The builder, which includes all tools of the specific software package called the *builder*.
The builder may contain one or more build-processors, e.g. *sphinx-build*, see also 
:ref:`--build-proc <setupdocxbuild_OPTIONS_build_proc>`.

.. note::

   Not all are available for the initial relase. 

   .. parsed-literal::
   
      builder := (
             sphinx
           | epydoc
           | docbook
           | doxygen
           | latex
           | mkdocs
           | pandoc
           | perldoc
           | texinfo
           | texinfo
           | txt2tags
      )

      # default := sphinx
      
Sets the environment variable :ref:`DOCX_BUILDER <setupdocx_ENV_DOCX_BUILDER>`.
The builde sets the following defaults for the build calls, and eventually
the document type parameters when required. 

   
   .. raw:: html
   
      <div class="indextab">
      <div class="nonbreakheadtab">
      <div class="autocoltab">

   +---------------------------------------------------------------+-----------------------------------------+
   |                                                               | default                                 |
   +===============================================================+=========================================+
   | :ref:`build-doc <setupdocxbuild_OPTIONS_build_doc>`           | :ref:`call_doc.sh <CALL_DOC>`    (1)    |
   +---------------------------------------------------------------+-----------------------------------------+
   | :ref:`build-apidoc <setupdocxbuild_OPTIONS_build_apidoc>`     | :ref:`call_apidoc.sh <CALL_APIDOC>` (2) |
   +---------------------------------------------------------------+-----------------------------------------+
   | :ref:`build-apiref <setupdocxbuild_OPTIONS_build_apiref>` (4) | :ref:`call_apiref.sh <CALL_APIREF>` (3) |
   +---------------------------------------------------------------+-----------------------------------------+

   .. raw:: html
   
      </div>
      </div>
      </div>

   (1) 
       curently the same

   (2)
       curently the same

   (3)
       curently the same

   (4)
       called when option *--apiref* is present

      
.. index::
   pair: build_docx; --cap
   pair: --cap; capbilities
   pair: --cap; capbilities.json
   pair: --cap; capbilities.xml
   pair: --cap; capbilities.yaml

.. _setupdocxbuild_OPTIONS_cap:

-\-cap
^^^^^^
A comma separated list of or a single capabilities file.
In case of a list each will be superporsed successively.
The default loads the file in the orginal builder directory only.
Non existing files raise an exception.

.. parsed-literal::

   cap := <capability-file-path> [',' <cap>]
   capability-file-path := <builder-path> <ossep> <capability-file>
   builder-path :=  "full path prefix to capabilities file abs or rel"
   capability-file :=(
        capabilities.json
      | capabilities.xml
      | capabilities.yaml
   )
   ossep := "OS path separator"

.. note::

   This is an advanced option foreseen for development and test, thus
   should not applied regularly. It is strongly recommended to use
   the default contained in the builder subdirectory. 


.. index::
   pair: build_docx; --clean
   pair: --clean; call_doc.sh
   pair: --clean; call_apidoc.sh
   pair: --clean; call_apiref.sh

.. _setupdocxbuild_OPTIONS_clean:

-\-clean
^^^^^^^^
Cleans the output of the called external tool.


.. index::
   pair: build_docx; --clean-all

.. _setupdocxbuild_OPTIONS_clean_all:

-\-clean-all
^^^^^^^^^^^^
Cleans the build directories '*apidoc*', and '*apiref*'.


.. index::
   pair: build_docx; --config-path
   pair: --config-path; call_doc.sh
   pair: --config-path; call_apidoc.sh
   pair: --config-path; call_apiref.sh
   pair: --config-path; conf.py
   pair: --config-path; epydoc.css
   pair: --config-path; epydoc.conf
   pair: --config-path; logo.png
   pair: --config-path; favicon.ico
   pair: --config-path; _themes
   pair: --config-path; _templates
   pair: --config-path; _static

.. _setupdocxbuild_OPTIONS_config_path:

-\-config-path=
^^^^^^^^^^^^^^^
   The configuration directory.
   The directory contains the production and runtime data for 
   configuration, style setup, the theme, etc..
   The following figure depicts an example including the directories
   *_build*, *_static*, *_templates*, and *_themes*. These produce a
   compatible directory structure to *sphinx-apidoc* with the provided
   structural compatible build utilities 
   :ref:`make.bat <MAKE_BAT>` and :ref:`Makefile <MAKEFILE>`.
   The latter are adapted to the call interface based on the *setupdocx*
   environment variables - see :ref:`ENVIRONMENT <setupdocx_ENV_call_environment>`.
   
   The project *setupdocx* for example does not utilize *sphinx-apidoc* at all.

      .. parsed-literal::

         rtd
         └── docsrc
             ├── conf.py           # required for doc / sphinx-build withouth sphinx-apidoc
             │                     # else optional
             ├── epydoc.conf       # required for apiref/epydoc
             ├── index.rst         # opt.
             ├── make_docx.bat     # opt. supports more 'targets'
             ├── Makefile_docx     # opt. supports more targets
             ├── _build
             ├── _static
             │   ├── custom.css    # opt.
             │   ├── epydoc.css    # opt.
             │   ├── favicon.ico   # opt. rec. size 32x32
             │   └── logo.png      # opt. rec. size 64x64
             ├── _templates
             └── _themes

   Including optional creation scripts customized for the specific document.

      .. parsed-literal::

         config-path := (
            <path-to-configuration-directory>
            | <confname>
         )
         
         # default := setupdocx/conf/<build-proc>/default/


   This also contains the logo and the favicon.
   The expected default contents are:


      .. raw:: html
   
         <div class="indextab">
         <div class="nonbreakheadtab">
         <div class="autocoltab">
   
      +---------------------------------------------+--------------------------------------------+--------------------------------------------------------------+
      | file                                        | content                                    | remarks                                                      |
      +=============================================+============================================+==============================================================+
      | :ref:`call_doc.sh <CALL_DOC>`               | customized create command                  | see :ref:`Call Environment <setupdocx_ENV_call_environment>` |
      +---------------------------------------------+--------------------------------------------+--------------------------------------------------------------+
      | :ref:`call_apidoc.sh <CALL_APIDOC>`         | customized sphinx-apidoc                   | see :ref:`Call Environment <setupdocx_ENV_call_environment>` |
      +---------------------------------------------+--------------------------------------------+--------------------------------------------------------------+
      | :ref:`call_apiref.sh <CALL_APIREF>`         | customized API reference                   | see :ref:`Call Environment <setupdocx_ENV_call_environment>` |
      +---------------------------------------------+--------------------------------------------+--------------------------------------------------------------+
      | :ref:`conf.py <CONFIGURATIONTEMPLATES>`     | Sphinx configuration file                  | The current version uses Sphinx, this may change             |
      +---------------------------------------------+--------------------------------------------+--------------------------------------------------------------+
      | :ref:`epydoc.css <CONFIGURATIONTEMPLATES>`  | epydoc style sheet                         | The current version uses Epydoc, this may change             |
      +---------------------------------------------+--------------------------------------------+--------------------------------------------------------------+
      | :ref:`epydoc.conf <CONFIGURATIONTEMPLATES>` | epydoc configuration                       | The current version uses Epydoc, this may change             |
      +---------------------------------------------+--------------------------------------------+--------------------------------------------------------------+
      | :ref:`logo.png <CONFIGURATIONTEMPLATES>`    | used logo as *PNG*, recommended size 64x64 | Copied into <build-directory>/_static                        |
      +---------------------------------------------+--------------------------------------------+--------------------------------------------------------------+
      | :ref:`favicon.ico <CONFIGURATIONTEMPLATES>` | favicon as *ICO*,  recommended size 32x32  | Copied into <build-directory>/_static                        |
      +---------------------------------------------+--------------------------------------------+--------------------------------------------------------------+
   
      .. raw:: html
      
         </div>
         </div>
         </div>


   The following optional subdirectories are copied into the build directory
   when present:
   
      .. raw:: html
      
         <div class="indextab">
         <div class="nonbreakheadtab">
         <div class="autocoltab">
   
      +--------------------------------------------+-----------------------------+------------------------------------------------+
      | directory                                  | content                     | remarks                                        |
      +============================================+=============================+================================================+
      | :ref:`_themes <CONFIGURATIONTEMPLATES>`    | customized sphinx-themes    | copied to <build-directory>/_themes            |
      +--------------------------------------------+-----------------------------+------------------------------------------------+
      | :ref:`_templates <CONFIGURATIONTEMPLATES>` | customized sphinx-templates | copied to <build-directory>/_templates         |
      +--------------------------------------------+-----------------------------+------------------------------------------------+
      | :ref:`_static <CONFIGURATIONTEMPLATES>`    | arbitrary data              | content copied into <build-directory>/_static  |
      +--------------------------------------------+-----------------------------+------------------------------------------------+
   
      .. raw:: html
      
         </div>
         </div>
         </div>

   Sets the environment variable :ref:`DOCX_CONFDIR <setupdocx_ENV_DOCX_CONFDIR>`.


.. index::
   pair: build_docx; --copyright

.. _setupdocxbuild_OPTIONS_copyright:

-\-copyright=
^^^^^^^^^^^^^
A fixed text as copyright notice.
The text is used literally, the default is::

   (C) <year> <author>


.. index::
   pair: build_docx; --debug

.. _setupdocxbuild_OPTIONS_debug:

-\-debug
^^^^^^^^
   Raises the debug flag by '1'.

   Sets the incremented environment variable :ref:`DOCX_DEBUG <setupdocx_ENV_DOCX_DEBUG>`.

.. index::
   pair: build_docx; --docname

.. _setupdocxbuild_OPTIONS_docname:

-\-docname=
^^^^^^^^^^^
   The name of the created document. In case of the document type *html*
   this is the directory name.
   This could be different from the :ref:`--name <setupdocxbuild_OPTIONS_name>`,
   e.g. in order to create the same document based on different themes. 
   
      .. parsed-literal::
      
         docname := <name-of-file-or-directory>
   
         # default := *self.name*

   Sets the environment variable :ref:`DOCX_DOCNAME <setupdocx_ENV_DOCX_DOCNAME>`.

.. index::
   pair: build_docx; --docsource

.. _setupdocxbuild_OPTIONS_docsource:

-\-docsource=
^^^^^^^^^^^^^
   Set the directory of the document sources.

   default := *docsrc/*
   
   For example:
   
      .. parsed-literal::
      
         setup.py build_docx --docsource=docsrc/

   Sets the environment variable :ref:`DOCX_DOCSRC <setupdocx_ENV_DOCX_DOCSRC>`.


.. index::
   pair: build_docx; --doctemplate

.. _setupdocxbuild_OPTIONS_doctemplate:

-\-doctemplate=
^^^^^^^^^^^^^^^
   Set the template for the document. The template is a subdirectory within the
   configuration directory of the builder (see *--builder*). The template 
   subdirectory contains the configuration templates of the provided document
   types (see *--doctemplate*). The current present list of templates within the 
   serach path (see *--config-path*) is available by the options *--list-templates*
   and *--list-templates-std*. For example::
   
      .. parsed-literal::
      
         (3.8.0) [acue@lap001 setupdocx]$ python setup.py build_docx --list-templates-std
         
         running build_docx
         
         available builder templates for: epydoc - setupdocx.config.epydoc
                   embedded/sphinx/default                  - html
                   embedded/sphinx/rtd/iframe               - html
                   embedded/sphinx/white-green/iframe       - html
                   standalone                               - html
         
         available builder templates for: sphinx - setupdocx.config.sphinx
                   agogo                                    - html
                   alabaster                                - html
                   bizstyle                                 - html
                   bootstrap                                - html
                   default                                  - html
                   default_                                 - html
                   guzzle                                   - html
                   nature                                   - html
                   pydoc2                                   - html
                   pydoc3                                   - html
                   rtd                                      - epub
                   rtd                                      - html
                   rtd                                      - man
                   rtd                                      - pdf
                   rtd                                      - singlehtml
                   rtd-github                               - html
                   rtd-readthedocs                          - html
                   sphinxdoc                                - html
                   traditional                              - html
         
         (3.8.0) [acue@lap001 setupdocx]$ 

   For example:
   
      .. parsed-literal::
      
         setup.py build_docx --doctemplate=

   Sets the environment variable :ref:`DOCX_DOCTEMPLATE <setupdocx_ENV_DOCX_DOCTEMPLATE>`.


.. index::
   pair: build_docx; --doctype

.. _setupdocxbuild_OPTIONS_doctype:

-\-doctype=
^^^^^^^^^^^
   Set the format type of the created documentation.
   The supported types conssit of the pimary and the secondary format types.
   The primary format types are supported for all processing tools, where possible.
   These values are mapped as required to specific call parameters within the
   call wrapper e.g. :ref:`call_doc.sh <CALL_DOC>`.  
   The secondary format types are specific to the actuall used processing tool,
   thus are not permitted in all call contexts.
   
   The *build_docx* supports a specific subset of the caled tools.
   Thus in some cases the processing tools has to be executed explicitly.
   This is supported by the dynamic created environment scripts for console usage,
   see  :ref:`persistent environment <DYNAMIC_ENVIRONMENT_SCRIPTS>`.
   
      .. parsed-literal::
      
         docname := (
            
            # primary types
              'html'            # directory containing the document
            | 'singlehtml'      # directory containing the document with one 'html' file
            | 'epub'            # a single file
            | 'man'             # directory containing multiple documents
            | 'mangz'           # directory containing multiple compressed documents
            | 'pdf'             # a single file

            # secondary types
            | 'latex'           # a single file
            | 'latexpdf'        # a single file
            | 'latexpdfja'      # a single file

            | 'devhelp'         # directory containing the document
            | 'htmlhelp'        # directory containing the document
            | 'qthelp'          # directory containing the document
         )
   
         # default := *html*
   
   For example:
   
      .. parsed-literal::
      
         setup.py build_docx --doctype=html

   Sets the environment variable :ref:`DOCX_DOCTYPE <setupdocx_ENV_DOCX_DOCTYPE>`.


.. index::
   pair: build_docx; --indexsrc

.. _setupdocxbuild_OPTIONS_indexsrc:

-\-indexsrc
^^^^^^^^^^^
   The source file to be copied into the build directory with the target name "*index.rst*".
   
      .. parsed-literal::
      
         indexsrc := <file-path-name-index-replacement>
   
         # default := *index.rst*
   
   For the current version this file simply replaces the output 'index.rst' of *sphinx-apidoc*.
   The user is responsible for the correct content. 
   
   For example
   
      .. parsed-literal::
      
         setup.py build_docx --indexsrc=docsrc/index_rtd.rst
   
   for a special variant for *sphinx_rtd_theme* or the online *Read-The0Docs*. 
   While the same directory contains also the generic default file "*docsrc/index.rst*"
   for other themes.

   Sets the environment variable :ref:`DOCX_INDEXSRC <setupdocx_ENV_DOCX_INDEXSRC>`.


.. index::
   pair: build_docx; --quiet

.. _setupdocxbuild_OPTIONS_quiet:

-\-quiet
^^^^^^^^
   Quiet flag, disables console output for informal displays.

   Sets the environment variable :ref:`DOCX_QUIET <setupdocx_ENV_DOCX_QUIET>`.

.. index::
   pair: build_docx; --rawdoc

.. _setupdocxbuild_OPTIONS_rawdoc:

-\-rawdoc
^^^^^^^^^
   Creates documentation based on the output of the generators *apidoc* only.
   Supresses the copy of the documents from the subdirectory *docsrc* including
   the *index.rst*.
   If you need a document still contains some minor modifications, define minal
   configuration template.
   
   default := *None*

   Sets the environment variable :ref:`DOCX_RAWDOC <setupdocx_ENV_DOCX_RAWDOC>`.

.. index::
   pair: build_docx; --epydoc-conf

.. _setupdocxbuild_OPTIONS_epydoc_conf:

-\-ref-conf=
^^^^^^^^^^^^
   Configuration file for the called apiref,
   see :ref:`call_apiref.sh <CALL_APIREF>`
   
      .. parsed-literal::
      
         setup.py build_docx --epydoc-conf=<file-path-name>
   
         # default := dopcsrc/epydoc.conf


.. index::
   pair: build_docx; --list-templates

.. _setupdocxbuild_OPTIONS_list_templates:

-\-list-templates=
^^^^^^^^^^^^^^^^^^
   Displays lists of provided configuration templates from multiple paths.
   Supports multiple display options for the format of the paths.
   
      .. parsed-literal::

         setup.py build_docx --list-templates=<parameters>
   
         parameters := '"' 
            + ['baselist=' <searchpath> [';'] ] 
            +  ['display=' <display-format> [';'] ]
            '"'
         searchpath :=  <path> [<sep> <searchpath>]
         sep := os.pathsep
         display-format := (
              None     # <template-name>
            | short    # <tool>.<template-name>
            | full     # as provided
            | abs      # absolute
            | rel      # relative
         )
         
         see also :ref:`setupdocx.conf_list <API_setupdocx.conf_list>`.

   Example:
      The following call lists multiple directories:

         .. parsed-literal::
   
            python setup.py build_docx \\
                --list-templates="baselist=conf_docs:setupdocx/configurations;display=None;"

            # wrapped for readability


.. index::
   pair: build_docx; --list-templates-std

.. _setupdocxbuild_OPTIONS_list_templates_std:

-\-list-templates-std
^^^^^^^^^^^^^^^^^^^^^
   Displays the list of provided configuration templates.
   
      .. parsed-literal::
      
         setup.py build_docx --list-templates-std
   
    Example: 

       .. parsed-literal::
   
          python setup.py build_docx --list-templates-std

    The current list is:

      .. parsed-literal::
   
         available templates: mkdocs
         
         available templates: sphinx
              agogo
              alabaster
              bizstyle
              default
              epub
              guzzle_sphinx_theme
              man
              nature
              pdf
              sphinx_bootstrap_theme
              sphinx_rtd_on_github
              sphinx_rtd_theme
              sphinxdoc
              traditional
    

.. index::
   pair: build_docx; --name

.. _setupdocxbuild_OPTIONS_name:

-\-name=
^^^^^^^^
   The name of the package. This is used by default as the output name
   of the document, see also :ref:`--docname <setupdocxbuild_OPTIONS_docname>`.
   
      .. parsed-literal::
      
         setup.py build_docx --name=<package-name>
   
         # default := <current-package-name> - self.name

   Sets the environment variable :ref:`DOCX_NAME <setupdocx_ENV_DOCX_NAME>`.

.. index::
   pair: build_docx; --no-exec

.. _setupdocxbuild_OPTIONS_no_exec:

-\-no-exec
^^^^^^^^^^
   Print only, do not execute
   
      .. parsed-literal::
      
         setup.py build_docx --no-exec
   
         # default := False


.. index::
   pair: build_docx; --no-exec-max
   pair: build_docx; -N

.. _setupdocxbuild_OPTIONS_no_exec_max:

-\-no-exec-max
^^^^^^^^^^^^^^
   Print only all calls in the workflow despite the final call of the external tools.
   This displays the resulting calls of the all levels.
   
      .. parsed-literal::
      
         setup.py dist_docx --no-exec-max
         setup.py dist_docx -N
   
         # default: False

   Custom scripts have to comply to these convention.

   See also :ref:`--no-exec <setupdocxdist_OPTIONS_no_exec>`.


.. index::
   pair: build_docx; --set-release

.. _setupdocxbuild_OPTIONS_set_release:

-\-set-release
^^^^^^^^^^^^^^
   Release to be set for the document.
   This is used literally.
   
      .. parsed-literal::
      
         setup.py build_docx --set-release=<arbitrary-string>
         arbitrary-string := "probably not too long, and if possible ASCII only :-)"

   Sets the environment variable :ref:`DOCX_RELEASE <setupdocx_ENV_DOCX_RELEASE>`.

.. index::
   pair: build_docx; --set-version

.. _setupdocxbuild_OPTIONS_set_version:

-\-set-version
^^^^^^^^^^^^^^
   Version number to be set for the document.
   Requires digits and dots '.' only:
   
      .. parsed-literal::
      
         setup.py build_docx --set-version=11.22.33
         setup.py build_docx --set-version=11.22
         setup.py build_docx --set-version=11
   
   Normalizes to a 3-number version identifier:
   
      .. parsed-literal::
      
         11.22.33
         11.22.0
         11.0.0

   Sets the environment variable :ref:`DOCX_VERSION <setupdocx_ENV_DOCX_VERSION>`.

.. index::
   pair: build_docx; --srcdir

.. _setupdocxbuild_OPTIONS_srcdir:

-\-srcdir=
^^^^^^^^^^
   The name of the directories containing the source code of the project.
   Either a single name, or a string containing semicolon separated
   list of paths, similar to DOS-search paths. This syntax permits seamless
   inclusions of *URIs*.  

      .. parsed-literal::
      
         srcdir := <dir-name>[';'<srcdir>]
   
         # default := <package-name>

   For example:

      .. parsed-literal::
      
         setup.py build_docx --srcdir=<package-name>

   Sets the environment variable :ref:`DOCX_SRCDIR <setupdocx_ENV_DOCX_SRCDIR>`.
   

.. index::
   pair: build_docx; --verbose

.. _setupdocxbuild_OPTIONS_verbose:

-\-verbose
^^^^^^^^^^
   Verbose flag for the local command context.
   Each repetition raises the level. The option :ref:`--quiet <setupdocxbuild_OPTIONS_verbose>`
   resets the current counter to zero, while following *--verbose* flags continue to count
   than form zero on,
   see :ref:`semantics of verbose and quiet <SEMANTICS_VERBOSE_AND_QUIET>`.

      .. parsed-literal::
      
         setup.py build_docx --verbose -v --verbose -v

   The behaviour is defined a bit special:
   
      0. when a global option *--verbose* is set only, this is inherited by the local option 
      1. the local options replaces the global default
      2. the option is normalized to *1* in combination with the flag *--quiet* 

   For additional details refer :ref:`Howto Apply Verbose and Quiet <HOWTO_VERBOSE_AND_QUIET>`.


.. index::
   pair: build_docx; --verbose-ext

.. _setupdocxbuild_OPTIONS_verbose_ext:

-\-verbose-ext
^^^^^^^^^^^^^^
   Verbose flag passed transparently to the called external tools.
   The integer value defines the level.
   The value is combined with the current quiet mode,
   see :ref:`semantics of verbose and quiet <SEMANTICS_VERBOSE_AND_QUIET>`.
   
      .. parsed-literal::
      
         setup.py build_docx --verbose-ext=2
         setup.py build_docx -x 2

   For additional details refer :ref:`Called Subcommands <HOWTO_VERBOSE_AND_QUIET_SUBCOMMANDS>`.



.. index::
   pair: command; build_apidoc
   pair: setupdocx; build_apidoc

.. _setupdocxCOMMANDS_build_apidoc:

build_apidoc
------------

Creates a document with contents from the extracted in-line documentation only.
The command calls for the creation of the documents customizable 
scripts - :ref:`--build-apidoc  <setupdocxbuild_OPTIONS_build_apidoc>` - 
and passes the parameters as environment variables,
see :ref:`setupdocx_ENV_call_environment`.
For supported formats refer to :ref:`setupdocxapidoc_OPTIONS_doctype`
 
.. _setupapidocbuild_OPTIONS:

.. index::
   pair: build_apidoc; --build-apidoc

.. _setupdocxapidoc_OPTIONS_build_apidoc:

-\-build-apidoc=
^^^^^^^^^^^^^^^^
   Sets the build script for the *apidoc*.
   
      .. parsed-literal::
      
         --apidoc=(
             <path-to-script>    # calls the script
         )
   
         # default := :ref:`<config-path>/call_apidoc.sh <CALL_APIDOC>`
   
   In case the provided value is a call name only the following locations 
   are searched.
   
      0. current configuration directory
      1. document source for subdirectory 'conf'
      2. the 'conf' directory within the package *setupdocx* 

   If the parameter is not provided and not present in *setup.conf*,
   the default resolution is:
   
      0. the  default value from the class member *docx_defaults*
      1. *call_ref* from current configuration directory
      2. *call_ref* from document source for subdirectory 'conf'
      3. *call_ref* from the 'conf' directory within the package *setupdocx* 

   The called final tool is currently by default *epydoc*.

      .. parsed-literal::
      
         setup.py build_apidoc --apidoc --build-apidoc=<config-path>/call_apidoc.sh

   The current release supports by default *bash* scripts,
   this could be varied as required, e.g. by a *DOS* batch script, or a *PowerShell* script,
   or simply by a *Python* script. 
 
   See also :ref:`Call Environment <setupdocx_ENV_call_environment>`.


.. index::
   pair: build_apidoc; --build-dir

.. _setupdocxapidoc_OPTIONS_build_dir:

-\-build-dir=
^^^^^^^^^^^^^
   The base directory of the build directory tree.
   
      .. parsed-literal::
      
         --build-dir=(
             <path-to-build-root>    # sets the build root directory
         )
   
         # default := build/
   
   The resulting actual build directory:
   
      .. parsed-literal::
      
         build/apidoc/sphinx
   
   This directory is used as temporary build directory for all calls of the same *build-dir*.
   Sets the environment variable :ref:`DOCX_BUILDDIR <setupdocx_ENV_DOCX_BUILDDIR>`. 


.. index::
   pair: build_apidoc; --clean
   pair: --clean; call_apiref.sh

.. _setupdocxapidoc_OPTIONS_clean:

-\-clean
^^^^^^^^
Cleans the output of the called external tool.

.. index::
   pair: build_doc; --config-path
   pair: --config-path; call_apdoc.sh
   pair: --config-path; custom.css
   pair: --config-path; conf.py
   pair: --config-path; logo.png
   pair: --config-path; favicon.ico

.. _setupdocxapidoc_OPTIONS_config_path:

-\-config-path=
^^^^^^^^^^^^^^^
   The configuration directory.
   The directory contains the production and runtime data for 
   configuration and style setup.
   The following figure depicts an example.
   
      .. parsed-literal::

         apidoc_only
         ├── call_apidoc.sh        # optional custom script
         ├── epydoc.conf
         └── docsrc
             ├── epydoc.css
             ├── favicon.ico
             └── logo.png

   Including optional creation scripts customized for the specific document.

      .. parsed-literal::

         config-path := (
            <path-to-configuration-directory>
            | <confname>
         )
         
         # default := setupdocx/conf/<build-proc>/default/


   This also contains the logo and the favicon.
   The expected default contents are:


      .. raw:: html
   
         <div class="indextab">
         <div class="nonbreakheadtab">
         <div class="autocoltab">
   
      +---------------------------------------------+--------------------------------------------+--------------------------------------------------------------+
      | file                                        | content                                    | remarks                                                      |
      +=============================================+============================================+==============================================================+
      | :ref:`call_apiref.sh <CALL_APIREF>`         | customized API reference                   | see :ref:`Call Environment <setupdocx_ENV_call_environment>` |
      +---------------------------------------------+--------------------------------------------+--------------------------------------------------------------+
      | :ref:`epydoc.css <CONFIGURATIONTEMPLATES>`  | epydoc style sheet                         | The current version uses Epydoc, this may change             |
      +---------------------------------------------+--------------------------------------------+--------------------------------------------------------------+
      | :ref:`epydoc.conf <CONFIGURATIONTEMPLATES>` | epydoc configuration                       | The current version uses Epydoc, this may change             |
      +---------------------------------------------+--------------------------------------------+--------------------------------------------------------------+
      | :ref:`logo.png <CONFIGURATIONTEMPLATES>`    | used logo as *PNG*, recommended size 64x64 | Copied into <build-directory>                                |
      +---------------------------------------------+--------------------------------------------+--------------------------------------------------------------+
      | :ref:`favicon.ico <CONFIGURATIONTEMPLATES>` | favicon as *ICO*,  recommended size 32x32  | Copied into <build-directory>                                |
      +---------------------------------------------+--------------------------------------------+--------------------------------------------------------------+
   
      .. raw:: html
      
         </div>
         </div>
         </div>

   Sets the environment variable :ref:`DOCX_CONFDIR <setupdocx_ENV_DOCX_CONFDIR>`.

.. index::
   pair: build_apidoc; --docname

.. _setupdocxapidoc_OPTIONS_docname:

-\-docname=
^^^^^^^^^^^
   The name of the created document. In case of the document type *html*
   this is the directory name.
   This could be different from the :ref:`--name <setupdocxbuild_OPTIONS_name>`,
   e.g. in order to create the same document based on different themes. 
   
      .. parsed-literal::
      
         docname := <name-of-file-or-directory>
   
         # default := *self.name*

   Sets the environment variable :ref:`DOCX_DOCNAME <setupdocx_ENV_DOCX_DOCNAME>`.

.. index::
   pair: build_apidoc; --docsource

.. _setupdocxapidoc_OPTIONS_docsource:

-\-docsource=
^^^^^^^^^^^^^
   Set the directory of the document sources.

   default := *docsrc/*
   
   For example:
   
      .. parsed-literal::
      
         setup.py apiref_docx --docsource=docsrc/

   Sets the environment variable :ref:`DOCX_DOCSRC <setupdocx_ENV_DOCX_DOCSRC>`.


.. index::
   pair: build_apidoc; --doctype

.. _setupdocxapidoc_OPTIONS_doctype:

-\-doctype=
^^^^^^^^^^^
   Set the type of the created documentation.
   
      .. parsed-literal::
      
         docname := (
            # primary format types
              'html'
            | 'pdf'

            # secondary format types
            | 'auto'      # PDF
            | 'latexpdf'  # PDF
            | 'pdflatex'  # PDF

            | 'ps'
            | 'dvi'
            | 'latex'
            | 'tex'
         )
   
         # default := *html*


   For example:
   
      .. parsed-literal::
      
         setup.py apiref_docx --doctype=html

   Sets the environment variable :ref:`DOCX_DOCTYPE <setupdocx_ENV_DOCX_DOCTYPE>`.


.. index::
   pair: build_apidoc; --epydoc-conf

.. _setupdocxapidoc_OPTIONS_epydoc_conf:

-\-ref-conf=
^^^^^^^^^^^^
   Configuration file for the called apiref,
   see :ref:`call_apiref.sh <CALL_APIREF>`
   
      .. parsed-literal::
      
         setup.py apiref_docx --epydoc-conf=<file-path-name>
   
         # default := dopcsrc/epydoc.conf

.. index::
   pair: build_apidoc; --name

.. _setupdocxapidoc_OPTIONS_name:

-\-name=
^^^^^^^^
   The name of the package. This is used by default as the output name
   of the document, see also :ref:`--docname <setupdocxbuild_OPTIONS_docname>`.
   
      .. parsed-literal::
      
         setup.py apiref_docx --name=<package-name>
   
         # default := <current-package-name> - self.name

   Sets the environment variable :ref:`DOCX_NAME <setupdocx_ENV_DOCX_NAME>`.

.. index::
   pair: build_apidoc; --no-exec

.. _setupdocxapidoc_OPTIONS_no_exec:

-\-no-exec
^^^^^^^^^^
   Print only, do not execute
   
      .. parsed-literal::
      
         setup.py apiref_docx --no-exec
   
         # default := False

.. index::
   pair: build_apidoc; --set-release

.. _setupdocxapidoc_OPTIONS_set_release:

-\-set-release
^^^^^^^^^^^^^^
   Release to be set for the document.
   This is used literally.
   
      .. parsed-literal::
      
         setup.py apiref_docx --set-release=<arbitrary-string>
         arbitrary-string := "probably not too long, and if possible ASCII only :-)"

   Sets the environment variable :ref:`DOCX_RELEASE <setupdocx_ENV_DOCX_RELEASE>`.

.. index::
   pair: build_apidoc; --set-version

.. _setupdocxapidoc_OPTIONS_set_version:

-\-set-version
^^^^^^^^^^^^^^
   Version number to be set for the document.
   Requires digits and dots '.' only:
   
      .. parsed-literal::
      
         setup.py apiref_docx --set-version=11.22.33
         setup.py apiref_docx --set-version=11.22
         setup.py apiref_docx --set-version=11
   
   Normalizes to a 3-number version identifier:
   
      .. parsed-literal::
      
         11.22.33
         11.22.0
         11.0.0

   Sets the environment variable :ref:`DOCX_VERSION <setupdocx_ENV_DOCX_VERSION>`.

.. index::
   pair: build_apidoc; --srcdir

.. _setupdocxapidoc_OPTIONS_srcdir:

-\-srcdir=
^^^^^^^^^^
   The name of the directories containing the source code of the project.
   Either a single name, or a string containing semicolon separated
   list of paths, similar to DOS-search paths. This syntax permits seamless
   inclusions of *URIs*.  

      .. parsed-literal::
      
         srcdir := <dir-name>[';'<srcdir>]
   
         # default := <package-name>

   For example:

      .. parsed-literal::
      
         setup.py apiref_docx --srcdir=<package-name>

   Sets the environment variable :ref:`DOCX_SRCDIR <setupdocx_ENV_DOCX_SRCDIR>`.
   

.. index::
   pair: build_apidoc; --verbose

.. _setupdocxapidoc_OPTIONS_verbose:

-\-verbose
^^^^^^^^^^
   Verbose flag for the local command context.
   Each repetition raises the level. The option :ref:`--quiet <setupdocxapiref_OPTIONS_verbose>`
   resets the current counter to zero, while following *--verbose* flags continue to count
   than form zero on,
   see :ref:`semantics of verbose and quiet <SEMANTICS_VERBOSE_AND_QUIET>`.

      .. parsed-literal::
      
         setup.py install_docx --verbose -v --verbose -v

   The behaviour is defined a bit special:
   
      0. when a global option *--verbose* is set only, this is inherited by the local option 
      1. the local options replaces the global default
      2. the option is normalized to *1* in combination with the flag *--quiet* 

   For additional details refer :ref:`Howto Apply Verbose and Quiet <HOWTO_VERBOSE_AND_QUIET>`.


.. index::
   pair: build_apidoc; --verbose-ext

.. _setupdocxapidoc_OPTIONS_verbose_ext:

-\-verbose-ext
^^^^^^^^^^^^^^
   Verbose flag passed transparently to the called external tools.
   The integer value defines the level.
   The value is combined with the current quiet mode,
   see :ref:`semantics of verbose and quiet <SEMANTICS_VERBOSE_AND_QUIET>`.

      .. parsed-literal::
      
         setup.py build_apidoc --verbose-ext=2
         setup.py build_apidoc -x 2

   For additional details refer :ref:`Called Subcommands <HOWTO_VERBOSE_AND_QUIET_SUBCOMMANDS>`.



.. index::
   pair: command; build_apiref
   pair: setupdocx; build_apiref

.. _setupdocxCOMMANDS_build_apiref:

build_apiref
------------

Creates *Epydoc* based standalone javadoc-style API reference.
The command calls for the creation of the documents customizable 
scripts - :ref:`--build-apiref  <setupdocxbuild_OPTIONS_build_apiref>` - 
and passes the parameters as environment variables,
see :ref:`setupdocx_ENV_call_environment`.
For supported formats refer to :ref:`setupdocxapiref_OPTIONS_doctype`
 
.. _setupapirefbuild_OPTIONS:

.. index::
   pair: build_apiref; --build-apiref

.. _setupdocxapiref_OPTIONS_build_apiref:

-\-build-apiref=
^^^^^^^^^^^^^^^^
   Sets the build script for the *apiref*.
   
      .. parsed-literal::
      
         --apiref=(
             <path-to-script>    # calls the script
         )
   
         # default := :ref:`<config-path>/call_apiref.sh <CALL_APIREF>`
   
   In case the provided value is a call name only the following locations 
   are searched.
   
      0. current configuration directory
      1. document source for subdirectory 'conf'
      2. the 'conf' directory within the package *setupdocx* 

   If the parameter is not provided and not present in *setup.conf*,
   the default resolution is:
   
      0. the  default value from the class member *docx_defaults*
      1. *call_ref* from current configuration directory
      2. *call_ref* from document source for subdirectory 'conf'
      3. *call_ref* from the 'conf' directory within the package *setupdocx* 

   The called final tool is currently by default *epydoc*.

      .. parsed-literal::
      
         setup.py build_docx --apiref --build-apiref=<config-path>/call_apiref.sh

   The current release supports by default *bash* scripts,
   this could be varied as required, e.g. by a *DOS* batch script, or a *PowerShell* script,
   or simply by a *Python* script. 
 
   See also :ref:`Call Environment <setupdocx_ENV_call_environment>`.


.. index::
   pair: build_apiref; --build-dir

.. _setupdocxapiref_OPTIONS_build_dir:

-\-build-dir=
^^^^^^^^^^^^^
   The base directory of the build directory tree.
   
      .. parsed-literal::
      
         --build-dir=(
             <path-to-build-root>    # sets the build root directory
         )
   
         # default := build/
   
   The resulting actual build directory:
   
      .. parsed-literal::
      
         build/apidoc/sphinx
   
   This directory is used as temporary build directory for all calls of the same *build-dir*.
   Sets the environment variable :ref:`DOCX_BUILDDIR <setupdocx_ENV_DOCX_BUILDDIR>`. 


.. index::
   pair: build_apiref; --clean
   pair: --clean; call_apiref.sh

.. _setupdocxapiref_OPTIONS_clean:

-\-clean
^^^^^^^^
Cleans the output of the called external tool.

.. index::
   pair: build_apiref; --config-path
   pair: --config-path; call_apiref.sh
   pair: --config-path; epydoc.css
   pair: --config-path; epydoc.conf
   pair: --config-path; logo.png
   pair: --config-path; favicon.ico

.. _setupdocxapiref_OPTIONS_config_path:

-\-config-path=
^^^^^^^^^^^^^^^
   The configuration directory.
   The directory contains the production and runtime data for 
   configuration and style setup.
   The following figure depicts an example.
   
      .. parsed-literal::

         apiref_only
         ├── call_apiref.sh        # optional custom script
         ├── epydoc.conf
         └── docsrc
             ├── epydoc.css
             ├── favicon.ico
             └── logo.png

   Including optional creation scripts customized for the specific document.

      .. parsed-literal::

         config-path := (
            <path-to-configuration-directory>
            | <confname>
         )
         
         # default := setupdocx/conf/<build-proc>/default/


   This also contains the logo and the favicon.
   The expected default contents are:


      .. raw:: html
   
         <div class="indextab">
         <div class="nonbreakheadtab">
         <div class="autocoltab">
   
      +---------------------------------------------+--------------------------------------------+--------------------------------------------------------------+
      | file                                        | content                                    | remarks                                                      |
      +=============================================+============================================+==============================================================+
      | :ref:`call_apiref.sh <CALL_APIREF>`         | customized API reference                   | see :ref:`Call Environment <setupdocx_ENV_call_environment>` |
      +---------------------------------------------+--------------------------------------------+--------------------------------------------------------------+
      | :ref:`epydoc.css <CONFIGURATIONTEMPLATES>`  | epydoc style sheet                         | The current version uses Epydoc, this may change             |
      +---------------------------------------------+--------------------------------------------+--------------------------------------------------------------+
      | :ref:`epydoc.conf <CONFIGURATIONTEMPLATES>` | epydoc configuration                       | The current version uses Epydoc, this may change             |
      +---------------------------------------------+--------------------------------------------+--------------------------------------------------------------+
      | :ref:`logo.png <CONFIGURATIONTEMPLATES>`    | used logo as *PNG*, recommended size 64x64 | Copied into <build-directory>                                |
      +---------------------------------------------+--------------------------------------------+--------------------------------------------------------------+
      | :ref:`favicon.ico <CONFIGURATIONTEMPLATES>` | favicon as *ICO*,  recommended size 32x32  | Copied into <build-directory>                                |
      +---------------------------------------------+--------------------------------------------+--------------------------------------------------------------+
   
      .. raw:: html
      
         </div>
         </div>
         </div>

   Sets the environment variable :ref:`DOCX_CONFDIR <setupdocx_ENV_DOCX_CONFDIR>`.

.. index::
   pair: build_apiref; --docname

.. _setupdocxapiref_OPTIONS_docname:

-\-docname=
^^^^^^^^^^^
   The name of the created document. In case of the document type *html*
   this is the directory name.
   This could be different from the :ref:`--name <setupdocxbuild_OPTIONS_name>`,
   e.g. in order to create the same document based on different themes. 
   
      .. parsed-literal::
      
         docname := <name-of-file-or-directory>
   
         # default := *self.name*

   Sets the environment variable :ref:`DOCX_DOCNAME <setupdocx_ENV_DOCX_DOCNAME>`.

.. index::
   pair: build_apiref; --docsource

.. _setupdocxapiref_OPTIONS_docsource:

-\-docsource=
^^^^^^^^^^^^^
   Set the directory of the document sources.

   default := *docsrc/*
   
   For example:
   
      .. parsed-literal::
      
         setup.py apiref_docx --docsource=docsrc/

   Sets the environment variable :ref:`DOCX_DOCSRC <setupdocx_ENV_DOCX_DOCSRC>`.


.. index::
   pair: build_apiref; --doctype

.. _setupdocxapiref_OPTIONS_doctype:

-\-doctype=
^^^^^^^^^^^
   Set the type of the created documentation.
   
      .. parsed-literal::
      
         docname := (
            # primary format types
              'html'
            | 'pdf'

            # secondary format types
            | 'auto'      # PDF
            | 'latexpdf'  # PDF
            | 'pdflatex'  # PDF

            | 'ps'
            | 'dvi'
            | 'latex'
            | 'tex'
         )
   
         # default := *html*


   For example:
   
      .. parsed-literal::
      
         setup.py apiref_docx --doctype=html

   Sets the environment variable :ref:`DOCX_DOCTYPE <setupdocx_ENV_DOCX_DOCTYPE>`.


.. index::
   pair: build_apiref; --epydoc-conf

.. _setupdocxapiref_OPTIONS_epydoc_conf:

-\-ref-conf=
^^^^^^^^^^^^
   Configuration file for the called apiref,
   see :ref:`call_apiref.sh <CALL_APIREF>`
   
      .. parsed-literal::
      
         setup.py apiref_docx --epydoc-conf=<file-path-name>
   
         # default := dopcsrc/epydoc.conf

.. index::
   pair: build_apiref; --name

.. _setupdocxapiref_OPTIONS_name:

-\-name=
^^^^^^^^
   The name of the package. This is used by default as the output name
   of the document, see also :ref:`--docname <setupdocxbuild_OPTIONS_docname>`.
   
      .. parsed-literal::
      
         setup.py apiref_docx --name=<package-name>
   
         # default := <current-package-name> - self.name

   Sets the environment variable :ref:`DOCX_NAME <setupdocx_ENV_DOCX_NAME>`.

.. index::
   pair: build_apiref; --no-exec

.. _setupdocxapiref_OPTIONS_no_exec:

-\-no-exec
^^^^^^^^^^
   Print only, do not execute
   
      .. parsed-literal::
      
         setup.py apiref_docx --no-exec
   
         # default := False

.. index::
   pair: build_apiref; --set-release

.. _setupdocxapiref_OPTIONS_set_release:

-\-set-release
^^^^^^^^^^^^^^
   Release to be set for the document.
   This is used literally.
   
      .. parsed-literal::
      
         setup.py apiref_docx --set-release=<arbitrary-string>
         arbitrary-string := "probably not too long, and if possible ASCII only :-)"

   Sets the environment variable :ref:`DOCX_RELEASE <setupdocx_ENV_DOCX_RELEASE>`.

.. index::
   pair: build_apiref; --set-version

.. _setupdocxapiref_OPTIONS_set_version:

-\-set-version
^^^^^^^^^^^^^^
   Version number to be set for the document.
   Requires digits and dots '.' only:
   
      .. parsed-literal::
      
         setup.py apiref_docx --set-version=11.22.33
         setup.py apiref_docx --set-version=11.22
         setup.py apiref_docx --set-version=11
   
   Normalizes to a 3-number version identifier:
   
      .. parsed-literal::
      
         11.22.33
         11.22.0
         11.0.0

   Sets the environment variable :ref:`DOCX_VERSION <setupdocx_ENV_DOCX_VERSION>`.

.. index::
   pair: build_apiref; --srcdir

.. _setupdocxapiref_OPTIONS_srcdir:

-\-srcdir=
^^^^^^^^^^
   The name of the directories containing the source code of the project.
   Either a single name, or a string containing semicolon separated
   list of paths, similar to DOS-search paths. This syntax permits seamless
   inclusions of *URIs*.  

      .. parsed-literal::
      
         srcdir := <dir-name>[';'<srcdir>]
   
         # default := <package-name>

   For example:

      .. parsed-literal::
      
         setup.py apiref_docx --srcdir=<package-name>

   Sets the environment variable :ref:`DOCX_SRCDIR <setupdocx_ENV_DOCX_SRCDIR>`.
   

.. index::
   pair: apiref_docx; --verbose

.. _setupdocxapiref_OPTIONS_verbose:

-\-verbose
^^^^^^^^^^
   Verbose flag for the local command context.
   Each repetition raises the level. The option :ref:`--quiet <setupdocxapiref_OPTIONS_verbose>`
   resets the current counter to zero, while following *--verbose* flags continue to count
   than form zero on,
   see :ref:`semantics of verbose and quiet <SEMANTICS_VERBOSE_AND_QUIET>`.

      .. parsed-literal::
      
         setup.py install_docx --verbose -v --verbose -v

   The behaviour is defined a bit special:
   
      0. when a global option *--verbose* is set only, this is inherited by the local option 
      1. the local options replaces the global default
      2. the option is normalized to *1* in combination with the flag *--quiet* 

   For additional details refer :ref:`Howto Apply Verbose and Quiet <HOWTO_VERBOSE_AND_QUIET>`.


.. index::
   pair: build_apiref; --verbose-ext

.. _setupdocxapiref_OPTIONS_verbose_ext:

-\-verbose-ext
^^^^^^^^^^^^^^
   Verbose flag passed transparently to the called external tools.
   The integer value defines the level.
   The value is combined with the current quiet mode,
   see :ref:`semantics of verbose and quiet <SEMANTICS_VERBOSE_AND_QUIET>`.

      .. parsed-literal::
      
         setup.py build_docx --verbose-ext=2
         setup.py build_docx -x 2

   For additional details refer :ref:`Called Subcommands <HOWTO_VERBOSE_AND_QUIET_SUBCOMMANDS>`.


.. index::
   pair: command; dist_docx
   pair: setupdocx; dist_docx
   single: bz2
   single: lzma
   single: tar
   single: tar.gz
   single: tgz
   single: zip

.. _setupdocxCOMMANDS_dist_docx:

dist_docx
---------

.. _setupdocx_dist_names:

Creates a distribution package of the documentation.
The naming convention is based on the common naming scheme of installation packages.


* multi-file documents:

  Multi-file documents consist of multiple files with a master file as the landing point.
  A typical example is the document type *html*.

   .. parsed-literal::

      unpackname = <:ref:`name <setupdocxdist_OPTIONS_name>`> + "-doc-" + <:ref:`doctype <setupdocxdist_OPTIONS_doctype>`> [ + "-" + <:ref:`version <setupdocxdist_OPTIONS_set_version>`>] [ + "-" + <:ref:`release <setupdocxdist_OPTIONS_set_release>`>] [ + "-" + <:ref:`date <setupdocxdist_OPTIONS_date>`>] [ + "-" + <:ref:`platform <setupdocxdist_OPTIONS_plat_name>`>] + os.sep

* single-file documents:

  In case of a single file document the file is either contained in a directory, compressed at the top
  level without a container directory, or simply compressed by itself with 
  :ref:`gzip <setupdocxdist_OPTIONS_format>`. 
  The standard behaviour is to compress single file documents without a container directory.
  Thus these are decompressed by default into the same directory as the archive. This is the default behaviour for all
  archive type capable of archiving directories.

  The case of compressed single files results in an archive for each contained file within the directory,
  which are extrated within the same directory.
  This is the behavior of the compression defined by *gzip*.

      .. parsed-literal::
   
         unpackname = <original-file-name-of-document> 
  
  The handling of the case with a containing directory has to be forced by the flag
  :ref:`--forcedir <setupdocxdist_OPTIONS_forcedir>`.
  The resulting behaviour is the same as for multi-file documents where the file is contained within
  the unpack directory.

      .. parsed-literal::
   
         unpackname = <:ref:`name <setupdocxdist_OPTIONS_name>`> + "-doc-" + <:ref:`doctype <setupdocxdist_OPTIONS_doctype>`> [ + "-" + <:ref:`version <setupdocxdist_OPTIONS_set_version>`>] [ + "-" + <:ref:`release <setupdocxdist_OPTIONS_set_release>`>] [ + "-" + <:ref:`date <setupdocxdist_OPTIONS_date>`>] [ + "-" + <:ref:`platform <setupdocxdist_OPTIONS_plat_name>`>]

* multiple single-file documents:

  Multiple single file documents bundled together in a shared directory.
  A typical example is *man* and *mangz* where multiple man pages are created for a single package.
  Same for *pdf* manals combined with separate *howto* and *faq* within a shared document directoy.
  These are by default handeled similar to documents consisting of multiple files, and are packed
  within a single unpack directory containing the original document files.

   .. parsed-literal::

      unpackname = <:ref:`name <setupdocxdist_OPTIONS_name>`> + "-doc-" + <:ref:`doctype <setupdocxdist_OPTIONS_doctype>`> [ + "-" + <:ref:`version <setupdocxdist_OPTIONS_set_version>`>] [ + "-" + <:ref:`release <setupdocxdist_OPTIONS_set_release>`>] [ + "-" + <:ref:`date <setupdocxdist_OPTIONS_date>`>] [ + "-" + <:ref:`platform <setupdocxdist_OPTIONS_plat_name>`>] + os.sep


For example: 

   * multi-file documents:
   
     A single directory with multiple files, typical example is *html*, but also
     *singlehtml*, which has one html page, but still requires additional media such as images,
     scripts, and style sheets.

      Input:
   
         .. parsed-literal::
         
            <original-file-name-of-document>/<file-parts>
   
      Archive contents:

         .. parsed-literal::
         
            setupdocx-doc-html-1.3.5-alpha-2019.05.01.x86_64.<:ref:`format <setupdocxdist_OPTIONS_format>`>:<original-file-name-of-document>/<file-parts> 
            setupdocx-doc-html-1.3.5-alpha.x86_64.<:ref:`format <setupdocxdist_OPTIONS_format>`>:<original-file-name-of-document>/<file-parts>
            setupdocx-doc-html-1.3.5.amd64.<:ref:`format <setupdocxdist_OPTIONS_format>`>:<original-file-name-of-document>/<file-parts>
            setupdocx-doc-html-alpha.amd64.<:ref:`format <setupdocxdist_OPTIONS_format>`>:<original-file-name-of-document>/<file-parts>
            setupdocx-doc-html.amd64.<:ref:`format <setupdocxdist_OPTIONS_format>`>:<original-file-name-of-document>/<file-parts>

      Output:
   
         .. parsed-literal::
         
            <original-file-name-of-document>/<file-parts> 
   
   * single-file documents and multiple single-file documents:

     A single file as the resulting document, typical examples are *pdf* and *epub*.
   
      Input:
   
      .. parsed-literal::
      
         <original-file-name-of-document>
   
      Archive contents:
      
         Default:

            .. parsed-literal::
            
               setupdocx-doc-html-1.3.5-alpha-2019.05.01.amd64.<:ref:`format <setupdocxdist_OPTIONS_format>`>:<original-file-name-of-document> 
               setupdocx-doc-html-1.3.5-alpha.amd64.<:ref:`format <setupdocxdist_OPTIONS_format>`>:<original-file-name-of-document>
               setupdocx-doc-html-1.3.5.x86_64.<:ref:`format <setupdocxdist_OPTIONS_format>`>:<original-file-name-of-document>
               setupdocx-doc-html-alpha.x86_64.<:ref:`format <setupdocxdist_OPTIONS_format>`>:<original-file-name-of-document>
               setupdocx-doc-html.x86_64.<:ref:`format <setupdocxdist_OPTIONS_format>`>:<original-file-name-of-document>

         With forced container directory:

            .. parsed-literal::
            
               setupdocx-doc-html-1.3.5-alpha-2019.05.01.arm7hl.<:ref:`format <setupdocxdist_OPTIONS_format>`>:<origial-container-directory>/<original-file-name-of-document> 
               setupdocx-doc-html-1.3.5-alpha.arm64.<:ref:`format <setupdocxdist_OPTIONS_format>`>:<origial-container-directory>/<original-file-name-of-document>
               setupdocx-doc-html-1.3.5.armhfp.<:ref:`format <setupdocxdist_OPTIONS_format>`>:<origial-container-directory>/<original-file-name-of-document>
               setupdocx-doc-html-alpha.i686.<:ref:`format <setupdocxdist_OPTIONS_format>`>:<origial-container-directory>/<original-file-name-of-document>
               setupdocx-doc-html.x86.<:ref:`format <setupdocxdist_OPTIONS_format>`>:<origial-container-directory>/<original-file-name-of-document>

      Output:
      
         Default:
   
            .. parsed-literal::
            
               <original-file-name-of-document>

         With forced container directory - :ref:`--forcedir <setupdocxdist_OPTIONS_forcedir>`:
   
            .. parsed-literal::
            
               <origial-container-directory>/<original-file-name-of-document>
   

.. note::

   The :ref:`version <setupdocxdist_OPTIONS_set_version>` and the :ref:`release <setupdocxdist_OPTIONS_set_release>`
   are optional. 
   The release is a provided literal string which could replace version completely.

   The version is extracted from the metadata of the package.

.. _setupdocxdist_OPTIONS:

.. index::
   pair: dist_docx; --append

.. _setupdocxdist_OPTIONS_append:

-\-append
^^^^^^^^^
   Append files to existing archive.
   The default is to create new and replace the previous.
   Can be used to add new unpack-dir to an existing archive.
   
      .. parsed-literal::
      
         setup.py dist_docx --append
   
         # default: False


.. index::
   pair: dist_docx; --build-dir

.. _setupdocxdist_OPTIONS_build_dir:

-\-build-dir=
^^^^^^^^^^^^^
   The location of the compiled document.
   The document has to be already created by the command :ref:`build_docx <setupdocxCOMMANDS_build_docx>`.
   
      .. parsed-literal::
      
         setup.py dist_docx -\-build-dir=<processed-document>
         
         # default 'build/'


.. index::
   pair: dist_docx; --clean

.. _setupdocxdist_OPTIONS_clean:

-\-clean
^^^^^^^^
Cleans the output of the created previous distribution.

.. index::
   pair: dist_docx; --date

.. _setupdocxdist_OPTIONS_date:

-\-date
^^^^^^^
   Adds the current date to the archive name:
   
      .. parsed-literal::
      
         setup.py dist_docx --date

   The output format is:

      .. parsed-literal::
      
         date := YYYY.MM.DD

.. index::
   pair: dist_docx; --debug

.. _setupdocxdist_OPTIONS_set_debug:

-\-debug
^^^^^^^^
   Debug level:
   
      .. parsed-literal::
      
         setup.py dist_docx --debug=3
         setup.py dist_docx --debug=
         setup.py dist_docx -d 3

.. index::
   pair: dist_docx; --dist-dir

.. _setupdocxdist_OPTIONS_dist_dir:

-\-dist-dir=
^^^^^^^^^^^^
   Archive location for creation:
   
      .. parsed-literal::
      
         setup.py dist_docx --dist-dir=<output-location-for-archive>
   
         # default 'dist/'


.. index::
   pair: dist_docx; --doctype

.. _setupdocxdist_OPTIONS_doctype:

-\-doctype=
^^^^^^^^^^^
   The document type to pack.
   
      .. parsed-literal::

         doctype := (
              'html'
            | 'epub'
            | 'man'
            | 'pdf'

            | 'latex'
            | 'latexpdf'
            | 'latexpdfja'
            | 'singlehtml'

            | 'devhelp'
            | 'htmlhelp'
            | 'qthelp'
         )
   
         # default 'html'

   For example:
   
      .. parsed-literal::
      
         setup.py dist_docx --doctype='html'
   
   The internally called subsystems such as *sphinx* may provide more formats,
   when required these has to be called by the interface of the subsystem.


.. index::
   pair: dist_docx; --extra-suffixes

.. _setupdocxdist_OPTIONS_extra_suffixes:

-\-extra-suffixes=
^^^^^^^^^^^^^^^^^^
   Adds additional valid input suffixes for single file documents.
   Single file documents are validated by suffixes, e.g. '.pdf' or '.epub'.
   The same in case of '*doctype=man*', for each manpage the suffixes are checked
   as a single digit - '*.[0-9]*'. In case of '*doctype=mangz*' checked as '*.gz*'.
   For additional non-digit suffixes extra suffixes are added to 
   the validation list.

      .. parsed-literal::
      
         extra-suffixes := <valid-suffix> [, <extra-suffixes>] 
         valid-suffix := "any literal suffix with a leading dot - '.'"

   For example:
   
      .. parsed-literal::
      
         setup.py dist_docx --dist-dir=<output-location-for-archive>
   
         # default 'dist/'


.. index::
   pair: dist_docx; --force

.. _setupdocxdist_OPTIONS_force:

-\-force
^^^^^^^^
Force to processing by deactivating non-essential checks.
Suppresses validation.

default: False


.. index::
   pair: dist_docx; --forcedir

.. _setupdocxdist_OPTIONS_forcedir:

-\-forcedir
^^^^^^^^^^^
Force to pack all types by containing directories including single document types such as PDF.
Else the types PDF, and EPUB are compressed without the containing directory.

default: False


.. index::
   pair: dist_docx; --type
   triple: dist_docx; --type; zip
   triple: dist_docx; --type; targz
   triple: dist_docx; --type; tar
   triple: dist_docx; --type; lzma
   triple: dist_docx; --type; bzip2
   triple: dist_docx; --type; tgz

.. _setupdocxdist_OPTIONS_format:

-\-formats=
^^^^^^^^^^^
The archive types.
A comma separated list of types of the created packages.
Default is 'zip', see also '--help-formats'.

   .. parsed-literal::

      --formats := <arch-type> [',' <formats>]

      arch-type := "see following table"

Current available types are:

   .. raw:: html
   
      <div class="indextab">
      <div class="nonbreakheadtab">
      <div class="autocoltab">

   +--------+---------+----------------------------------------------------------------+
   | option | suffix  | remark                                                         |
   +========+=========+================================================================+
   | bzip2  | .bz2    |                                                                |
   +--------+---------+----------------------------------------------------------------+
   | gzip   | .gz     | Applicable to single file documents only - pdf, epub, man, ps. |
   +--------+---------+----------------------------------------------------------------+
   | lzma   | .lzma   | Python3.3+. Python2.7 with backports.lzma [backlzma]_          |
   +--------+---------+----------------------------------------------------------------+
   | tar    | .tar    |                                                                |
   +--------+---------+----------------------------------------------------------------+
   | targz  | .tar.gz |                                                                |
   +--------+---------+----------------------------------------------------------------+
   | tgz    | .tgz    |                                                                |
   +--------+---------+----------------------------------------------------------------+
   | xz     | .xz     | Python3.3+. Python2.7 with backports.lzma [backlzma]_          |
   +--------+---------+----------------------------------------------------------------+
   | zip    | .zip    |                                                                |
   +--------+---------+----------------------------------------------------------------+

   .. raw:: html
   
      </div>
      </div>
      </div>


.. index::
   pair: dist_docx; --help-doctypes

.. _setupdocxdist_OPTIONS_help_doctypes:

-\-help-doctypes
^^^^^^^^^^^^^^^^
Enumerates available document types.


.. index::
   pair: dist_docx; --help-formats

.. _setupdocxdist_OPTIONS_help_formats:

-\-help-formats
^^^^^^^^^^^^^^^
Enumerates available distribution formats.


.. index::
   pair: dist_docx; --name

.. _setupdocxdist_OPTIONS_name:

-\-name=
^^^^^^^^
   The name of the package
   
      .. parsed-literal::
      
         setup.py dist_docx --name=<package-name>
   
         # default := <current-package-name>

.. index::
   pair: dist_docx; --name-in

.. _setupdocxdist_OPTIONS_name_in:

-\-name-in=
^^^^^^^^^^^
   The name of the input package
   
      .. parsed-literal::
      
         setup.py dist_docx --name-in=<package-name>
   
         # default := self.name

.. index::
   pair: dist_docx; --name-out

.. _setupdocxdist_OPTIONS_name_out:

-\-name-out=
^^^^^^^^^^^^
   The name of the package part of the output archive 
   
      .. parsed-literal::
      
         setup.py dist_docx --name0out=<package-name>
   
         # default := self.name

.. index::
   pair: dist_docx; --no-exec
   pair: dist_docx; -n

.. _setupdocxdist_OPTIONS_no_exec:

-\-no-exec
^^^^^^^^^^
   Print only, do not execute.
   This displays the resulting calls of the first level only.
   
      .. parsed-literal::
      
         setup.py dist_docx --no-exec
         setup.py dist_docx -n
   
         # default: False

.. index::
   pair: dist_docx; --plat-name

.. _setupdocxdist_OPTIONS_plat_name:

-\-plat-name=
^^^^^^^^^^^^^
The optional name of the platform.
The name could be an arbitrary string, even though it shold comply to the common labels.
The name is be added to the archive name.
Even though the document itself is platform independent, the contents may not.

.. index::
   pair: dist_docx; --quiet

.. _setupdocxdist_OPTIONS_quiet:

-\-quiet=
^^^^^^^^^
Sets the quiet flag, for the special implementation in compliance
of *distutils* see :ref:`Howto Apply Verbose and Quiet <HOWTO_VERBOSE_AND_QUIET>`.


.. index::
   pair: dist_docx; --set-release

.. _setupdocxdist_OPTIONS_set_release:

-\-set-release=
^^^^^^^^^^^^^^^
   A user provided release string. The string is added to the Version of created archive
   
      .. parsed-literal::
      
         setup.py dist_docx --set-version=<valid-version-string>
   
         # default: <year>.<month>.<day>


.. index::
   pair: dist_docx; --set-version

.. _setupdocxdist_OPTIONS_set_version:

-\-set-version
^^^^^^^^^^^^^^
   Version of created archive. Extracted from the packages metadata as provided by the
   call of '*setup*' in '*setup.py*'.
   
      .. parsed-literal::
      
         setup.py dist_docx --set-version=<valid-version-string>
   
         # default: <year>.<month>.<day>


.. index::
   pair: dist_docx; --verbose

.. _setupdocxdist_OPTIONS_verbose:

-\-verbose
^^^^^^^^^^
   Verbose flag for the local command context.
   Each repetition raises the level. The option :ref:`--quiet <setupdocxdist_OPTIONS_verbose>`
   resets the current counter to zero, while following *--verbose* flags continue to count
   than form zero on,
   see :ref:`semantics of verbose and quiet <SEMANTICS_VERBOSE_AND_QUIET>`.

      .. parsed-literal::
      
         setup.py dist_docx --verbose -v --verbose -v

   The behaviour is defined a bit special:
   
      0. when a global option *--verbose* is set only, this is inherited by the local option 
      1. the local options replaces the global default
      2. the option is normalized to *1* in combination with the flag *--quiet* 

   For additional details refer :ref:`Howto Apply Verbose and Quiet <HOWTO_VERBOSE_AND_QUIET>`.


.. index::
   pair: command; install_docx
   pair: setupdocx; install_docx

.. _setupdocxCOMMANDS_install_docx:

install_docx
------------
Install a local copy from the build directory of the previously build documents in
accordance to PEP-370.
When the build target has changed e.g. by :ref:`--name <setupdocxbuild_OPTIONS_name>`,
or :ref:`--docname <setupdocxbuild_OPTIONS_docname>`,
than the appropriate name has to be provided for the *install_docx* too. 


.. _setupdocxinstall_OPTIONS:

.. index::
   pair: install_docx; --build-dir

.. _setupdocxinstall_OPTIONS_build_dir:

-\-build-dir=
^^^^^^^^^^^^^
   The location of the compiled document.
   The document has to be already created by the command :ref:`build_docx <setupdocxCOMMANDS_build_docx>`.
   
      .. parsed-literal::
      
         setup.py install_docx --build-dir=<source-directory>
   
         # default: 'build'


.. index::
   pair: install_docx; --clean

.. _setupdocxinstall_OPTIONS_clean:

-\-clean
^^^^^^^^
Cleans the output of the created previous installation.

.. index::
   pair: install_docx; --debug

.. _setupdocxinstall_OPTIONS_debug:

-\-debug
^^^^^^^^
   Debug flag.
   
      .. parsed-literal::
      
         setup.py install_docx --debug


.. index::
   pair: install_docx; --docname

.. _setupdocxinstall_OPTIONS_docname:

-\-docname=
^^^^^^^^^^^
   The name of the created document. In case of the document type *html*
   this is the directory name.
   This could be different from the :ref:`--name <setupdocxinstall_OPTIONS_name>`,
   e.g. in order to create the same document based on different themes. 
   
      .. parsed-literal::
      
         docname := <name-of-file-or-directory>
   
         # default := *self.name*


.. index::
   pair: install_docx; --doctype

.. _setupdocxinstall_OPTIONS_doctype:

-\-doctype=
^^^^^^^^^^^
   Document type to install. 
   The document type controls the actual target structure.

   This varies in dependence of the type, so for example the man pages [man]_ are subdivided
   into sections, where the files are separated automatically by their section numbers. 
   This places the files into the section structure in companion with other man pages. 
   The section directories are created automatically when not yet present. 

   The behaviour could be forced to the installation of the named document package 
   with the option :ref:`--forcedir <setupdocxinstall_OPTIONS_forcedir>` 

   
      .. parsed-literal::

         doctype := (
              'html'
            | 'epub'
            | 'man'
            | 'pdf'

            | 'latex'
            | 'latexpdf'
            | 'latexpdfja'
            | 'singlehtml'

            | 'devhelp'
            | 'htmlhelp'
            | 'qthelp'
         )
   
         # default 'html'

   With the call:   
   
      .. parsed-literal::
      
         setup.py install_docx --doctype='html'
   
         # default: html


.. index::
   pair: install_docx; --forcedir

.. _setupdocxinstall_OPTIONS_forcedir:

-\-forcedir
^^^^^^^^^^^
Force to instal all types by containing directories including single document types such as *pdf*,
and structured types like man pages.
Else the types :ref:`pdf <setupdocxinstall_OPTIONS_doctype>`, 
:ref:`epub <setupdocxinstall_OPTIONS_doctype>`, and other single file documents are compressed
without the containing directory, 
while the types :ref:`man <setupdocxinstall_OPTIONS_doctype>`
and :ref:`mangz <setupdocxinstall_OPTIONS_doctype>` are by default installed
into a man page section tree structure [man]_.

The flag changes the behaviour to the installation of the flat document directory
of the package without the consideration of the man structure.
In case of single documents these are stored with their directory prefix.
Thus the documents are unpacked within their original directory.

The flag has no effect for multi-file documents of types like :ref:`html <setupdocxinstall_OPTIONS_doctype>`
and :ref:`singlehtml <setupdocxinstall_OPTIONS_doctype>`.

default: False


.. index::
   pair: install_docx; --name

.. _setupdocxinstall_OPTIONS_name:

-\-name=
^^^^^^^^
   Package name, changes 'self.name'.
   
      .. parsed-literal::
      
         setup.py install_docx --name=<self-name>
   
         # default: self.name


.. index::
   pair: install_docx; --no-exec

.. _setupdocxinstall_OPTIONS_no_exec:

-\-no-exec
^^^^^^^^^^
   Print only, do not execute.
   
      .. parsed-literal::
      
         setup.py install_docx --no-exec


.. index::
   pair: install_docx; --target-dir=

.. _setupdocxinstall_OPTIONS_target_dir:

-\-target-dir
^^^^^^^^^^^^^
   Installation target directory.
   The complete path for the location of the installed document,
   excluding the document name.
   
      .. parsed-literal::
      
         setup.py install_docx --target-dir=<target-directory>
   
   Default is in user data, see also PEP-370.
   Either
   
      .. parsed-literal::
   
         ~/.local/doc/en/html/man3/"+str(self.docname)
   
   , or 
   
      .. parsed-literal::
   
         %APPDATA%/doc/en/html/man3/"+str(self.docname)


.. index::
   pair: install_docx; --verbose

.. _setupdocxinstall_OPTIONS_verbose:

-\-verbose
^^^^^^^^^^
   Verbose flag for the local command context.
   Each repetition raises the level. The option :ref:`--quiet <setupdocxinstall_OPTIONS_verbose>`
   resets the current counter to zero, while following *--verbose* flags continue to count
   than form zero on,
   see :ref:`semantics of verbose and quiet <SEMANTICS_VERBOSE_AND_QUIET>`.

      .. parsed-literal::
      
         setup.py install_docx --verbose -v --verbose -v

   The behaviour is defined a bit special:
   
      0. when a global option *--verbose* is set only, this is inherited by the local option 
      1. the local options replaces the global default
      2. the option is normalized to *1* in combination with the flag *--quiet* 

   For additional details refer :ref:`Howto Apply Verbose and Quiet <HOWTO_VERBOSE_AND_QUIET>`.




.. index::
   triple: env; DOCX_APIDOC; --apidoc
   triple: env; DOCX_APIREF; --apiref
   triple: env; DOCX_BREAKONERR; --break-on-err
   triple: env; DOCX_BUILDDIR; --build-dir
   triple: env; DOCX_BUILDER; --builder
   triple: env; DOCX_BUILDRELDIR; --build-reldir
   triple: env; DOCX_CLEAN; --clean
   triple: env; DOCX_CONFDIR; --confdir
   triple: env; DOCX_DOCNAME; --docname
   triple: env; DOCX_DOCSRC; --source-dir
   triple: env; DOCX_DOCTYPE; --doctype
   triple: env; DOCX_INDEXSRC; --indexsrc
   triple: env; DOCX_NAME; --name
   triple: env; DOCX_NOEXEC; --noexec
   triple: env; DOCX_RAWDOC; --rawdoc
   triple: env; DOCX_RELEASE; --set-release
   triple: env; DOCX_SRCDIR; --srcdir
   triple: env; DOCX_VERBOSE; --verbose
   triple: env; DOCX_VERBOSEX; --verbosex
   triple: env; DOCX_VERSION; --set-version


.. _setupdocx_ENV_call_environment:

ENVIRONMENT
===========

The command calls for the creation of the sphinx documents customizable 
scripts - see :ref:`--build-apidoc <setupdocxbuild_OPTIONS_build_apidoc>` 
, :ref:`--build-doc  <setupdocxbuild_OPTIONS_build_doc>`, and
:ref:`--build-apiref  <setupdocxbuild_OPTIONS_build_apiref>` - 
and passes the following environment variables as parameters.

.. _DYNAMIC_ENVIRONMENT_SCRIPTS:

The environment is passed to all commands.
In addition two files were created for test and debugging purposes in order to use the command 
line tools and the make files from the console.

* setenv.sh  - sets and exports the environment variables, compatible to *bash*, *ksh*, *sh*, etc.
* setenv.bat - sets and exports the environment variables, compatible to *CMD.EXE*

The environment variables are:

   .. raw:: html
         
      <div class="indextab">
      <div class="nonbreakheadtab">
      <div class="autocoltab">

   +----------------------------------------------------------+-------------------------------------------------------------+---------------------------+
   | environment variable                                     | corresponding option                                        | default                   |
   +==========================================================+=============================================================+===========================+
   | :ref:`DOCX_APIDOC <setupdocx_ENV_DOCX_APIDOC>`           | :ref:`--apidoc <setupdocxbuild_OPTIONS_apidoc>`             | ''                        |
   +----------------------------------------------------------+-------------------------------------------------------------+---------------------------+
   | :ref:`DOCX_APIREF <setupdocx_ENV_DOCX_APIREF>`           | :ref:`--apiref <setupdocxbuild_OPTIONS_apiref>`             | ''                        |
   +----------------------------------------------------------+-------------------------------------------------------------+---------------------------+
   | :ref:`DOCX_BUILDER <setupdocx_ENV_DOCX_BUILDER>`         | :ref:`--builder <setupdocxbuild_OPTIONS_builder>`           | sphinx                    |
   +----------------------------------------------------------+-------------------------------------------------------------+---------------------------+
   | :ref:`DOCX_BUILDDIR <setupdocx_ENV_DOCX_BUILDDIR>`       | :ref:`--build-dir <setupdocxbuild_OPTIONS_build_dir>`       | build/                    |
   +----------------------------------------------------------+-------------------------------------------------------------+---------------------------+
   | :ref:`DOCX_BUILDRELDIR <setupdocx_ENV_DOCX_BUILDRELDIR>` | :ref:`--build-reldir <setupdocxbuild_OPTIONS_build_reldir>` | apidoc/sphinx/            |
   +----------------------------------------------------------+-------------------------------------------------------------+---------------------------+
   | :ref:`DOCX_CLEAN <setupdocx_ENV_DOCX_CLEAN>`             | :ref:`--clean <setupdocxbuild_OPTIONS_clean>`               | False                     |
   +----------------------------------------------------------+-------------------------------------------------------------+---------------------------+
   | :ref:`DOCX_CONFDIR <setupdocx_ENV_DOCX_CONFDIR>`         | :ref:`--confdir <setupdocxbuild_OPTIONS_config_path>`       | docsrc/conf/              |
   +----------------------------------------------------------+-------------------------------------------------------------+---------------------------+
   | :ref:`DOCX_DEBUG <setupdocx_ENV_DOCX_DEBUG>`             | :ref:`--debug <setupdocxbuild_OPTIONS_debug>`               | 0                         |
   +----------------------------------------------------------+-------------------------------------------------------------+---------------------------+
   | :ref:`DOCX_DOCNAME <setupdocx_ENV_DOCX_DOCNAME>`         | :ref:`--docname <setupdocxbuild_OPTIONS_docname>`           | self.name (package-name)  |
   +----------------------------------------------------------+-------------------------------------------------------------+---------------------------+
   | :ref:`DOCX_DOCSRC <setupdocx_ENV_DOCX_DOCSRC>`           | :ref:`--docsource <setupdocxbuild_OPTIONS_docsource>`       | docsrc/                   |
   +----------------------------------------------------------+-------------------------------------------------------------+---------------------------+
   | :ref:`DOCX_DOCTYPE <setupdocx_ENV_DOCX_DOCTYPE>`         | :ref:`--doctype <setupdocxbuild_OPTIONS_doctype>`           | html                      |
   +----------------------------------------------------------+-------------------------------------------------------------+---------------------------+
   | :ref:`DOCX_EMBED <setupdocx_ENV_DOCX_EMBED>`             | --                                                          | ''                        |
   +----------------------------------------------------------+-------------------------------------------------------------+---------------------------+
   | :ref:`DOCX_INDEXSRC <setupdocx_ENV_DOCX_INDEXSRC>`       | :ref:`--indexsrc <setupdocxbuild_OPTIONS_indexsrc>`         | "index.rst"               |
   +----------------------------------------------------------+-------------------------------------------------------------+---------------------------+
   | :ref:`DOCX_LIB <setupdocx_ENV_DOCX_LIB>`                 | --                                                          | os.path.dirname(__file__) |
   +----------------------------------------------------------+-------------------------------------------------------------+---------------------------+
   | :ref:`DOCX_NAME <setupdocx_ENV_DOCX_NAME>`               | :ref:`--name <setupdocxbuild_OPTIONS_name>`                 | self.name (package-name)  |
   +----------------------------------------------------------+-------------------------------------------------------------+---------------------------+
   | :ref:`DOCX_NOEXEC <setupdocx_ENV_DOCX_NOEXEC>`           | :ref:`--no-exec <setupdocxbuild_OPTIONS_no_exec>`           | ''                        |
   +----------------------------------------------------------+-------------------------------------------------------------+---------------------------+
   | :ref:`DOCX_QUIET <setupdocx_ENV_DOCX_QUIET>`             | :ref:`--quiet <setupdocxbuild_OPTIONS_quiet>`               | 0                         |
   +----------------------------------------------------------+-------------------------------------------------------------+---------------------------+
   | :ref:`DOCX_RAWDOC <setupdocx_ENV_DOCX_RAWDOC>`           | :ref:`--rawdoc <setupdocxbuild_OPTIONS_rawdoc>`             | ''                        |
   +----------------------------------------------------------+-------------------------------------------------------------+---------------------------+
   | :ref:`DOCX_RELEASE <setupdocx_ENV_DOCX_RELEASE>`         | :ref:`--set-release <setupdocxbuild_OPTIONS_set_release>`   | <YYYY-MM-DD>              |
   +----------------------------------------------------------+-------------------------------------------------------------+---------------------------+
   | :ref:`DOCX_SRCDIR <setupdocx_ENV_DOCX_SRCDIR>`           | :ref:`--srcdir <setupdocxbuild_OPTIONS_srcdir>`             | self.name (package-name)  |
   +----------------------------------------------------------+-------------------------------------------------------------+---------------------------+
   | :ref:`DOCX_DOCTEMPLATE <setupdocx_ENV_DOCX_DOCTEMPLATE>` | :ref:`--doctemplate <setupdocxbuild_OPTIONS_doctemplate>`   | 'default'                 |
   +----------------------------------------------------------+-------------------------------------------------------------+---------------------------+
   | :ref:`DOCX_VERBOSE <setupdocx_ENV_DOCX_VERBOSE>`         |                                                             | 0                         |
   +----------------------------------------------------------+-------------------------------------------------------------+---------------------------+
   | :ref:`DOCX_VERBOSEX <setupdocx_ENV_DOCX_VERBOSEX>`       | :ref:`--verbose-ext <setupdocxbuild_OPTIONS_verbose_ext>`   | 0                         |
   +----------------------------------------------------------+-------------------------------------------------------------+---------------------------+
   | :ref:`DOCX_VERSION <setupdocx_ENV_DOCX_VERSION>`         | :ref:`--set-version <setupdocxbuild_OPTIONS_set_version>`   | <setup.py>                |
   +----------------------------------------------------------+-------------------------------------------------------------+---------------------------+
   
   
   .. raw:: html
   
      </div>
      </div>
      </div>
 
.. index::
   pair: build_docx; DOCX_APIDOC
   pair: --apidoc; DOCX_APIDOC

.. _setupdocx_ENV_DOCX_APIDOC:

DOCX_APIDOC
-----------
   Enables the creation of the API documentation.
   Is set by the option :ref:`--apidoc <setupdocxbuild_OPTIONS_apidoc>` to '*1*' when enabled.
   The default value is an empty string '', for disabled.


.. index::
   pair: build_docx; DOCX_APIREF
   pair: dist_docx; DOCX_APIREF
   pair: install_docx; DOCX_APIREF
   pair: --apiref; DOCX_APIREF

.. _setupdocx_ENV_DOCX_APIREF:

DOCX_APIREF
-----------
   Enables the creation of the API reference.
   Is set by the option :ref:`--apiref <setupdocxbuild_OPTIONS_apiref>` to '*1*' when enabled.
   The default value is an empty string '', for disabled.


.. index::
   pair: build_docx; DOCX_BREAKONERR
   pair: dist_docx; DOCX_BREAKONERR
   pair: install_docx; DOCX_BREAKONERR
   pair: break_on_err; DOCX_BREAKONERR
   pair: --break-on-err; DOCX_BREAKONERR

.. _setupdocx_ENV_DOCX_BREAKONERR:

DOCX_BREAKONERR
---------------
   Enables the immediate termination after an error.
   The default behaviour is to ignore.
   Is set by the option :ref:`--break-on-err <setupdocxbuild_OPTIONS_break_on_err>`.
   The default value is 'build/', for the standard subdirectory.


.. index::
   pair: build_docx; DOCX_BUILDDIR
   pair: dist_docx; DOCX_BUILDDIR
   pair: install_docx; DOCX_BUILDDIR
   pair: --build-dir; DOCX_BUILDDIR

.. _setupdocx_ENV_DOCX_BUILDDIR:

DOCX_BUILDDIR
-------------
   Sets the intermediate build directory.
   Is set by the option :ref:`--build-dir <setupdocxbuild_OPTIONS_build_dir>`.
   The default value is 'build/', for the standard subdirectory.


.. index::
   pair: build_docx; DOCX_BUILDER
   pair: dist_docx; DOCX_BUILDER
   pair: install_docx; DOCX_BUILDER
   pair: --builder; DOCX_BUILDER

.. _setupdocx_ENV_DOCX_BUILDER:

DOCX_BUILDER
------------
   Sets the intermediate builder package.
   Is set by the option :ref:`--builder <setupdocxbuild_OPTIONS_builder>`.
   The default value is 'sphinx', for the standard package.


.. index::
   pair: build_docx; DOCX_BUILDRELDIR
   pair: dist_docx; DOCX_BUILDRELDIR
   pair: install_docx; DOCX_BUILDRELDIR
   pair: --build-dir; DOCX_BUILDRELDIR

.. _setupdocx_ENV_DOCX_BUILDRELDIR:

DOCX_BUILDRELDIR
----------------
   Sets the intermediate subdirectory of the build directory.
   Is set by the option :ref:`--build-reldir <setupdocxbuild_OPTIONS_build_reldir>`.
   The default value is 'apidoc/sphinx', for the standard subdirectory.


.. index::
   pair: build_docx; DOCX_CLEAN
   pair: --clean; DOCX_CLEAN

.. _setupdocx_ENV_DOCX_CLEAN:

DOCX_CLEAN
----------
Sets the clean flag for the called wrapper.
Cleans the output of the external tools.

.. index::
   pair: build_docx; DOCX_CONFDIR
   pair: dist_docx; DOCX_CONFDIR
   pair: install_docx; DOCX_CONFDIR
   pair: --confdir; DOCX_CONFDIR

.. _setupdocx_ENV_DOCX_CONFDIR:

DOCX_CONFDIR
------------
   Sets the configuration directory.
   Is set by the option :ref:`--confdir <setupdocxbuild_OPTIONS_config_path>`.
   The default value is 'docsrc/conf/', for the standard source directory.


.. index::
   pair: build_docx; DOCX_DEBUG
   pair: dist_docx; DOCX_DEBUG
   pair: install_docx; DOCX_DEBUG
   pair: --debug; DOCX_DEBUG

.. _setupdocx_ENV_DOCX_DEBUG:

DOCX_DEBUG
----------
   Raises the debug state.

.. index::
   pair: build_docx; DOCX_DOCNAME
   pair: dist_docx; DOCX_DOCNAME
   pair: install_docx; DOCX_DOCNAME
   pair: --docname; DOCX_DOCNAME

.. _setupdocx_ENV_DOCX_DOCNAME:

DOCX_DOCNAME
------------
   Sets the document name, this alters the default name set by :ref:`setupdocx_ENV_DOCX_DOCNAME`.
   Is set by the option :ref:`--docname <setupdocxbuild_OPTIONS_docname>`.
   The default value is 'self.name(package-name)', for the current
   package name as set in the :ref:`setup.py <SETUP_PY>` by the derived classes from
   :ref:`SETUP_PY`.

   See also :ref:`DOCX_NAME <setupdocx_ENV_DOCX_NAME>`.
               

.. index::
   pair: build_docx; DOCX_DOCSRC
   pair: dist_docx; DOCX_DOCSRC
   pair: install_docx; DOCX_DOCSRC
   pair: --docsource; DOCX_DOCSRC

.. _setupdocx_ENV_DOCX_DOCSRC:

DOCX_DOCSRC
-----------
   Sets the document source directory.
   Is set by the option :ref:`--docsource <setupdocxbuild_OPTIONS_docsource>`.
   The default value is 'docsrc/', for the standard source directory.
                           


.. index::
   pair: build_docx; DOCX_DOCTYPE
   pair: dist_docx; DOCX_DOCTYPE
   pair: install_docx; DOCX_DOCTYPE
   pair: --doctype; DOCX_DOCTYPE

.. _setupdocx_ENV_DOCX_DOCTYPE:

DOCX_DOCTYPE
------------
   Sets the created document type.
   Is set by the option :ref:`--doctype <setupdocxbuild_OPTIONS_doctype>`.
   The default value is 'html', for the standard format.
                                   

.. index::
   pair: build_docx; DOCX_EMBED

.. _setupdocx_ENV_DOCX_EMBED:

DOCX_EMBED
----------
   Sets the flag for the embedding of the subdocuments into the main document.
   When not set, the called subscipts should be aware to create a standalone
   document.                                   


.. index::
   pair: build_docx; DOCX_INDEXSRC
   pair: dist_docx; DOCX_INDEXSRC
   pair: install_docx; DOCX_INDEXSRC
   pair: --indexsrc; DOCX_INDEXSRC

.. _setupdocx_ENV_DOCX_INDEXSRC:

DOCX_INDEXSRC
-------------
   Sets the index file.
   The index file is copied into the build directory and replaces the a
   file created by the production step :ref:`call_apidoc.sh <CALL_APIDOC>`.
   Is set by the option :ref:`--indexsrc <setupdocxbuild_OPTIONS_indexsrc>`.
   The default value is 'docsrc/index.rst', for the standard file name.


.. index::
   pair: build_docx; DOCX_LIB
   pair: dist_docx; DOCX_LIB
   pair: install_docx; DOCX_LIB

.. _setupdocx_ENV_DOCX_LIB:

DOCX_LIB
--------
   Sets the package path to the current package *setupdocx*.
   The package contains default components to be used by copy into the
   build directory of the created document.

   See also :ref:`Makefile_docx <MAKEFILE>` and :ref:`make_docx <MAKE_BAT>`.


.. index::
   pair: build_docx; DOCX_NAME
   pair: dist_docx; DOCX_NAME
   pair: install_docx; DOCX_NAME
   pair: --name; DOCX_NAME

.. _setupdocx_ENV_DOCX_NAME:

DOCX_NAME
---------
   Sets the name of the package.
   Is set by the option :ref:`--name <setupdocxbuild_OPTIONS_name>`.
   The default value is 'self.name(package-name)', for the current
   package name as set in the :ref:`setup.py <SETUP_PY>` by the derived classes from
   :ref:`SETUP_PY`.

   See also :ref:`DOCX_DOCNAME <setupdocx_ENV_DOCX_DOCNAME>`.


.. index::
   pair: build_docx; DOCX_NOEXEC
   pair: --name; DOCX_NOEXEC

.. _setupdocx_ENV_DOCX_NOEXEC:

DOCX_NOEXEC
-----------
   Sets the no-exec flag.
   Is set by the option :ref:`--no-exec <setupdocxbuild_OPTIONS_no_exec>`.
   The default value is *False* at environment the empty string - ''.

   See also :ref:`DOCX_DOCNAME <setupdocx_ENV_DOCX_NOEXEC>`.

.. index::
   pair: build_docx; DOCX_QUIET
   pair: dist_docx; DOCX_QUIET
   pair: install_docx; DOCX_QUIET
   pair: --quiet; DOCX_QUIET

.. _setupdocx_ENV_DOCX_QUIET:

DOCX_QUIET
----------
   Disables the verbose output, is treated by teh *setuptools* framework as
   negative option. for the special behavior refer to the option *--verbose*.

      .. parsed-literal::
      
         setup.py -build_docx -q 
         setup.py -build_docx -quiet 
         setup.py -q -build_docx  
         setup.py --quiet -build_docx  

   See also :ref:`DOCX_QUIET <setupdocx_ENV_DOCX_QUIET>`.

.. index::
   pair: build_docx; DOCX_RAWDOC
   pair: dist_docx; DOCX_RAWDOC
   pair: install_docx; DOCX_RAWDOC
   pair: --rawdoc; DOCX_RAWDOC

.. _setupdocx_ENV_DOCX_RAWDOC:

DOCX_RAWDOC
-----------
   Disables the production step :ref:`call_apidoc.sh <CALL_APIDOC>`,
   thus no custom files are added to the current build.
   In combination with :ref:`--apidoc <setupdocxbuild_OPTIONS_apidoc>`
   the pure output from *sphinx-apidoc* is used as the resulting document.
   Is set by the option :ref:`--rawdoc <setupdocxbuild_OPTIONS_rawdoc>`.
   The default value is '', for non-disabled.


.. index::
   pair: build_docx; DOCX_RELEASE
   pair: dist_docx; DOCX_RELEASE
   pair: install_docx; DOCX_RELEASE
   pair: --release; DOCX_RELEASE

.. _setupdocx_ENV_DOCX_RELEASE:

DOCX_RELEASE
------------
   Sets the release information.
   Is set by the option :ref:`--set-release <setupdocxbuild_OPTIONS_set_release>`.
   The default value is '<YYYY-MM-DD>', for the current date.


.. index::
   pair: build_docx; DOCX_SRCDIR
   pair: dist_docx; DOCX_SRCDIR
   pair: install_docx; DOCX_SRCDIR
   pair: --srcdir; DOCX_SRCDIR

.. _setupdocx_ENV_DOCX_SRCDIR:

DOCX_SRCDIR
-----------
The name of the directories containing the source code of the project.
Either a single name, or a string containing semicolon separated
list of paths, similar to DOS-search paths. This syntax permits seamless
inclusions of *URIs*.  

   .. parsed-literal::
   
      DOCX_SRCDIR := <dir-name>[';'<srcdir>]

      # default := <package-name>


.. index::
   pair: build_docx; DOCX_DOCTEMPLATE
   pair: dist_docx; DOCX_DOCTEMPLATE
   pair: install_docx; DOCX_DOCTEMPLATE
   pair: --doctemplate; DOCX_DOCTEMPLATE

.. _setupdocx_ENV_DOCX_DOCTEMPLATE:

DOCX_DOCTEMPLATE
----------------
The name of the configuration template to be used.
Is set by the option :ref:`--doctemplate <setupdocxbuild_OPTIONS_doctemplate>`.
The default value is *default* - which is a currently a copy of *alabaster* - the
hard-coded default of the *Sphinx* release at the time of writing. 
For the contained standard templates see *--list-templates-std*.

   .. parsed-literal::
   
      DOCX_DOCTEMPLATE := <template-name>

      # default := 'default'


.. index::
   pair: build_docx; DOCX_VERBOSE
   pair: dist_docx; DOCX_VERBOSE
   pair: install_docx; DOCX_VERBOSE
   pair: --verbose; DOCX_VERBOSE

.. _setupdocx_ENV_DOCX_VERBOSE:

DOCX_VERBOSE
------------
   Raises the displayed state.
   This value is supported by *distutils* as global option, thus could
   be applied multiple times.
   The default value is '0', for the minimal output.

      .. parsed-literal::
      
         setup.py --verbose --verbose --verbose build_docx
         setup.py  -v -v -v -v build_docx

   The following draft convention for the cumulative output of
   threshold levels is implemented:

   0. No extra output
   1. Basic display of control flow.
   2. Display of resulting interface data.
   3. Display of maximum output. 

   For the verbose flag of called external tools 
   see :ref:`--verbose-ext <setupdocxbuild_OPTIONS_verbose_ext>`
   and :ref:`DOCX_VERBOSEX <setupdocx_ENV_DOCX_VERBOSEX>`.

.. index::
   pair: build_docx; DOCX_VERBOSEX
   pair: dist_docx; DOCX_VERBOSEX
   pair: install_docx; DOCX_VERBOSEX
   pair: --verbose; DOCX_VERBOSEX

.. _setupdocx_ENV_DOCX_VERBOSEX:

DOCX_VERBOSEX
-------------
   Activates the verbose flag(s) for called external tools when supported.
   These are currently *sphinx-build* and *epydoc*, which support the repetition
   of teh verbose flag *-v*.
   Raises the displayed state by the number of the provided integer value.
   Is set by the option :ref:`--verbose-ext <setupdocxbuild_OPTIONS_verbose_ext>`.
   The default value is '0', for the minimal output.


.. index::
   pair: build_docx; DOCX_VERSION
   pair: dist_docx; DOCX_VERSION
   pair: install_docx; DOCX_VERSION
   pair: --build-dir; DOCX_VERSION

.. _setupdocx_ENV_DOCX_VERSION:

DOCX_VERSION
------------
   Sets the version.
   Is set by the option :ref:`--set-version <setupdocxbuild_OPTIONS_set_version>`.
   The default value is defined in :ref:`setup.py <SETUP_PY>`, by the variable
   *__version__*. 


DESCRIPTION
===========

The call interface 'setupdocx' provides command line extensions for 
the command line call interface of *setup.py*.
The curent version supports extension *commands*, future versions will
support *extension-points*.

The build process is based on tools for the processing of sources and the resulting
reST formats. The current toolset comprises *sphinx-build*, *sphinx-apidoc*, and *epydoc*.
The intermediate documents are created within the directory:

   .. parsed-literal::

      <build-dir>/apidoc/sphinx
 
When finished the document is transferred into the directory:

   .. parsed-literal::

      <build-dir>/doc/<docname>

Thus within the same build directory only one document can be created at one time.
When parallel build is required use different build directories 
:ref:`--build-dir <setupdocxbuild_OPTIONS_build_dir>`.

.. _setupdocxEXAMPLES:
 

EXAMPLES
========

.. _examples:

0. Import in your :ref:`setup.py <SETUP_PY>` for example:

      ::
      
         #
         # setup extension modules
         #
         from setupdocx import usage
         from setuptestx.testx import TestX  # for unit tests

         from setupdocx.build_docx import BuildDocX      # create documents
         from setupdocx.dist_docx import DistDocX        # package documents
         from setupdocx.install_docx import InstallDocX  # install documents manually, or from sources
   
   
         class build_docx(BuildDocX):
             def __init__(self, *args, **kargs):
                 BuildDocX.__init__(self, *args, **kargs)
                 self.name = 'setupdocx'                      # your package name
         
             
         class dist_docx(BuildDocX):
             def __init__(self, *args, **kargs):
                 BuildDocX.__init__(self, *args, **kargs)
                 self.name = 'setupdocx'                      # your package name

         class install_docx(InstallDocX):
             def __init__(self, *args, **kargs):
                 InstallDocX.__init__(self, *args, **kargs)
                 self.name = 'setupdocx'                      # your package name
         
         
         class testx(TestX):
             def __init__(self, *args, **kargs):
                 TestX.__init__(self, *args, **kargs)
                 self.name = 'setupdocx'                      # your package name

1. Hook them in e.g. as a command in your :ref:`setup.py <SETUP_PY>` by:

      .. parsed-literal::
      
         setup(
             cmdclass={                           # see [setuppy]_ and :ref:`setup.py <SETUP_PY>` 
                 'build_docx': build_docx,
                 'dist_docx': dist_docx,
                 'install_docx': install_docx,
                 'testx': testx,
             },
             ...
         )


2. Use them from the command line call for example by:

      .. parsed-literal::
      
         python :ref:`setup.py <SETUPPYSRC>` :ref:`--help-setupdocx <setupdocxOPTIONS_help-setupdocx>` 
         
         python :ref:`setup.py <SETUPPYSRC>` --help-commands           # see [setuppy]_  and :ref:`setup.py <SETUP_PY>`
   
         python :ref:`setup.py <SETUPPYSRC>` :ref:`build_docx <setupdocxCOMMANDS_build_docx>` --help

         python :ref:`setup.py <SETUPPYSRC>` :ref:`build_docx <setupdocxCOMMANDS_build_docx>`

         python :ref:`setup.py <SETUPPYSRC>` :ref:`install_docx <setupdocxCOMMANDS_install_docx>`


SEE ALSO
========
   :ref:`QUICKSTART`, :ref:`setup.py <SETUPPYSRC>`, :ref:`setup.conf <SETUP_CONF>`,
   :ref:`setupdocx <SETUPLIBCOMMANDSCLI>`,
   [setuptools]_, [distutils]_


LICENSE
=======
   :ref:`modified Artistic License <MODIFIED_ARTISTIC_LICENSE_20>` = :ref:`ArtisticLicense20 <ARTISTIC_LICENSE_20>` + :ref:`Peer-to-Peer-Fairplay-amendments <LICENSES_AMENDMENTS>` 

   For configuration files only:
      :ref:`MIT License <MIT_LICENSE>` 

COPYRIGHT
=========
   Copyright (C)2019 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez
