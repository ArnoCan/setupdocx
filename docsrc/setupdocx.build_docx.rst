
.. _setupdocxBUILDDOCX:

.. raw:: html

   <div class="shortcuttab">
   <div class="nonbreakheadtab">
   <div class="autocoltab">


setupdocx.build_docx
====================


.. only:: builder_man

   SYNOPSIS
   --------

   python setup.py build_docx

.. only:: not builder_man

   The standard implementation::

      python setup.py build_docx

Tested alternative implementations::

      ipython setup.py build_docx
      jython  setup.py build_docx  # requires special install of setuptools, refer to the manuals 
      pypy    setup.py build_docx
      ipw.exe setup.py build_docx  # IronPython on Windows

.. only:: builder_man

   DESCRIPTION
   -----------

Call for the online description of current options::

      python setup.py build_docx --help

The detailed description is available in the manual.

   .. parsed-literal::
   
      (3.8.0) [acue@lap001 setupdocx]$ python setup.py build_docx  --help
      
      
      Synopsis:
        setup.py [global-options] build_docx [build_docx-options]
      
      Global options for 'setup.py':
        --dry-run (-n)  don't actually do anything
        --help (-h)     show detailed help message
        --no-user-cfg   ignore pydistutils.cfg in your home directory
        --quiet (-q)    run quietly (turns verbosity off)
        --verbose (-v)  run verbosely (default)
      
      Options for 'build_docx' command:
        --apiref                Calls the script 'call_apiref.sh', creates the API
                                reference and integrates into sphinx, else sphinx
                                only. default: None
        --break-on-err          Sets the environment variable 'DOCX_BREAKONERR' for
                                the called wrapper script. Breaks after the first
                                error state from the called builder. Default: 'off'
        --builder               The builder to be used for the processing of the
                                document. See '--help-builder'. Default: 'sphinx'
        --builder-path          The directory path of the builder. Default:
                                '<SETUPDOCX-PYTHONPATH>/setupdocx/builder/'
        --build-dir             The name of the build directory. Default: 'build/'
        --build-reldir          The name of the relative build subdirectory.
                                Default: 'apidoc/<builder>/'
        --cap                   The initial default values, for an example see the
                                builder capabilities.One or more values separated by
                                comma ','.No search operation, the name bust be an
                                existing file path name.This is an expert and
                                developer option, which should not be used
                                regularly.Default:
                                'setupdocx/builder/<builder>/capabilities'
        --clean                 Removes the cached previous build. The default
                                directory is '<build-dir>/apidoc'.Default: False
        --clean-all             Removes the complete build directory before calling
                                the wrapper. The default directory is '<build-
                                dir>'.Default: False
        --config-path           Directory containing configuration files. See '--
                                list-templates-std' and '--list-templates'. Default:
                                '<docsource>/config/'. 
        --copyright             A copyright text to be used literally. Default: (C)
                                <year> <author>. 
        --debug (-d)            Raises degree of debug traces of current context.
                                Supports repetition. Each raises the command
                                verbosity level of the context by one.
        --docname               The document output name. Default: attribute of
                                derived class self.name
        --docsource             The name of the document source directory. Default:
                                docsrc/
        --doctemplate           The document template directory relative to '--
                                config-path'. See '--list-templates-std' and '--list
                                -templates'. Default: default/html
        --doctype               The document type to create. See '--help-doctypes'
                                for common types, for present types see '--list-
                                templates-std' and '--list-templates'. Default:
                                'html', 
        --executable            The executable called by the wrapper. Supports
                                relative and absolute file path names. Default:
                                'sphinx-build'
        --executableopts        Additional options to be passed to the executable.
                                Default: ''
        --executableopts-reset  Initialize empty options for the called executable.
                                Default: False
        --help-doctypes         List of available document formats.
        --indexsrc              The source file to be copied as 'index.rst'.
                                Default: 'index.rst'
        --list-templates-std    List provided configuration templates.
        --list-templates        Lists the configuration templates with filter
                                parameter, see manuals. Default: same as list-
                                templates-std
        --name                  The name of the package. Default: attribute of
                                derived class self.name
        --noexec (-n)           Print the call of the selected level only, do not
                                execute. The value is an integer, decremented by
                                each level until '0',which is the level to be
                                printed.
        --quiet (-q)            Quiet the current context, resets verbosity of
                                applied context to '0'. Default: off
        --rawdoc (-r)           Use the generated documents by 'apidoc' only.
        --srcdir                Source directory.
        --set-release           The release of the package.Default:
                                distribution.metadata.version
        --set-version           The version of the package. Default:
                                distribution.metadata.version
        --status                The status in accordance to the trove classifiers.
                                Default: '' - empty
        --wrapper               The wrapper called by the builder. Supports pure
                                file names only. Default: 'call_doc.sh'
        --wrapperopts           Additional options to be passed to the called
                                wrapper. Default: ''
        --wrapperopts-reset     Drop generated options for the wrapper, does not
                                effect environment. Default: False
        --verbose (-v)          Raises verbosity of current context. Supports
                                repetition. Each raises the command verbosity level
                                of the context by one.
        --apidoc                Calls the script 'call_apidoc.sh', creates the API
                                documentation and integrates into sphinx, else
                                sphinx-build only. default: None
        --builder               Builder to be used for the document processing.
                                Default: 'sphinx' dependent of the doctype resulting
                                in pure 'sphinx-build' for inherent document types,
                                or 'sphinx-build' + 'make' for external types
                                defined by '--doctype' e.g. such as 'html' or
                                'epub'. For called code-analysis tools see '--
                                builder-apidoc' and '--builder-apiref'.See '--help-
                                builder' for a list of available builders.
        --build-apidoc          the name of the called script for the creation of
                                the API documentation, default: '<conf-
                                dir>/call_apidoc.sh'
        --build-apiref          the name of the called script for the creation of
                                the API reference, default: '<conf-
                                dir>/call_apiref.sh'
        --build-doc             the name of the called script for the sphinx
                                document creation, default: '<conf-dir>/call_doc.sh'

      (3.8.0) [acue@lap001 setupdocx]$ 


Module
------
.. automodule:: setupdocx.build_docx


BuildDocX
---------
.. autoclass:: BuildDocX

.. _SPEC_BuildDocX_call_environment:

call_environment
^^^^^^^^^^^^^^^^
.. automethod:: BuildDocX.call_environment


.. _SPEC_BuildDocX_call_epilogue:

call_epilogue
^^^^^^^^^^^^^
.. automethod:: BuildDocX.call_epilogue


.. _SPEC_BuildDocX_call_prologue:

call_prologue
^^^^^^^^^^^^^
.. automethod:: BuildDocX.call_prologue


.. _SPEC_BuildDocX_finalize_options:

finalize_options
^^^^^^^^^^^^^^^^
.. automethod:: BuildDocX.finalize_options


.. _SPEC_BuildDocX_initialize_options:

initialize_options
^^^^^^^^^^^^^^^^^^
.. automethod:: BuildDocX.initialize_options


.. _SPEC_BuildDocX_run:

run
^^^
.. automethod:: BuildDocX.run

   For the called custom worker scripts refer to:

      +-------------------------------------+--------------------------------------------+
      | [docs]                              | [source]                                   |
      +=====================================+============================================+
      | :ref:`call_apidoc.sh <CALL_APIDOC>` | `call_apidoc.sh <_static/call_apidoc.sh>`_ |
      +-------------------------------------+--------------------------------------------+
      | :ref:`call_apiref.sh <CALL_APIREF>` | `call_apiref.sh <_static/call_apiref.sh>`_ |
      +-------------------------------------+--------------------------------------------+
      | :ref:`call_doc.sh <CALL_DOC>`       | `call_doc.sh <_static/call_doc.sh>`_       |
      +-------------------------------------+--------------------------------------------+

   For the passed environment variables see :ref:`ENVIRONMENT <setupdocx_ENV_call_environment>`.
   

.. _SPEC_BuildDocX_join_sphinx_mod_epydoc:

join_sphinx_mod_epydoc
^^^^^^^^^^^^^^^^^^^^^^
.. note::

   This is method is displayed for general documetation purposes only.
   Currently hardcoded, will be changed for flexible customization in
   future releases.

.. automethod:: BuildDocX.join_sphinx_mod_epydoc

Exceptions
----------

.. autoexception:: SetuplibBuildDocXError

.. raw:: html

   </div>
   </div>
   </div>

.. only:: builder_man

   The call wraps the command for the  generation of the API reference documentation 
   - currently *epydoc* by default.
   The interface is provided by environment variables.

   ENVIRONMENT
   -----------
   
   The following variables as set for the environment of the called wrapper. 

      .. raw:: html
            
         <div class="indextab">
         <div class="nonbreakheadtab">
         <div class="autocoltab">
   
      +----------------------------------------------------+-----------------------------------------------------------+---------------------------+
      | environment variable                               | corresponding option                                      | default                   |
      +====================================================+===========================================================+===========================+
      | :ref:`DOCX_APIDOC <setupdocx_ENV_DOCX_APIDOC>`     | :ref:`--apidoc <setupdocxbuild_OPTIONS_apidoc>`           | ''                        |
      +----------------------------------------------------+-----------------------------------------------------------+---------------------------+
      | :ref:`DOCX_APIREF <setupdocx_ENV_DOCX_APIREF>`     | :ref:`--apiref <setupdocxbuild_OPTIONS_apiref>`           | ''                        |
      +----------------------------------------------------+-----------------------------------------------------------+---------------------------+
      | :ref:`DOCX_BUILDDIR <setupdocx_ENV_DOCX_BUILDDIR>` | :ref:`--build-dir <setupdocxbuild_OPTIONS_build_dir>`     | build/                    |
      +----------------------------------------------------+-----------------------------------------------------------+---------------------------+
      | :ref:`DOCX_CLEAN <setupdocx_ENV_DOCX_CLEAN>`       | :ref:`--clean <setupdocxbuild_OPTIONS_clean>`             | ''                        |
      +----------------------------------------------------+-----------------------------------------------------------+---------------------------+
      | :ref:`DOCX_CONFDIR <setupdocx_ENV_DOCX_CONFDIR>`   | :ref:`--confdir <setupdocxbuild_OPTIONS_config_path>`     | docsrc/conf/              |
      +----------------------------------------------------+-----------------------------------------------------------+---------------------------+
      | :ref:`DOCX_DOCNAME <setupdocx_ENV_DOCX_DOCNAME>`   | :ref:`--docname <setupdocxbuild_OPTIONS_docname>`         | self.name (package-name)  |
      +----------------------------------------------------+-----------------------------------------------------------+---------------------------+
      | :ref:`DOCX_DOCSRC <setupdocx_ENV_DOCX_DOCSRC>`     | :ref:`--docsource <setupdocxbuild_OPTIONS_docsource>`     | docsrc/                   |
      +----------------------------------------------------+-----------------------------------------------------------+---------------------------+
      | :ref:`DOCX_DOCTYPE <setupdocx_ENV_DOCX_DOCTYPE>`   | :ref:`--doctype <setupdocxbuild_OPTIONS_doctype>`         | html                      |
      +----------------------------------------------------+-----------------------------------------------------------+---------------------------+
      | :ref:`DOCX_INDEXSRC <setupdocx_ENV_DOCX_INDEXSRC>` | :ref:`--indexsrc <setupdocxbuild_OPTIONS_indexsrc>`       | "index.rst"               |
      +----------------------------------------------------+-----------------------------------------------------------+---------------------------+
      | :ref:`DOCX_LIB <setupdocx_ENV_DOCX_LIB>`           | --                                                        | os.path.dirname(__file__) |
      +----------------------------------------------------+-----------------------------------------------------------+---------------------------+
      | :ref:`DOCX_NAME <setupdocx_ENV_DOCX_NAME>`         | :ref:`--name <setupdocxbuild_OPTIONS_name>`               | self.name (package-name)  |
      +----------------------------------------------------+-----------------------------------------------------------+---------------------------+
      | :ref:`DOCX_NOEXEC <setupdocx_ENV_DOCX_NOEXEC>`     | :ref:`--no-exec <setupdocxbuild_OPTIONS_no_exec>`         | ''                        |
      +----------------------------------------------------+-----------------------------------------------------------+---------------------------+
      | :ref:`DOCX_RAWDOC <setupdocx_ENV_DOCX_RAWDOC>`     | :ref:`--rawdoc <setupdocxbuild_OPTIONS_rawdoc>`           | ''                        |
      +----------------------------------------------------+-----------------------------------------------------------+---------------------------+
      | :ref:`DOCX_RELEASE <setupdocx_ENV_DOCX_RELEASE>`   | :ref:`--set-release <setupdocxbuild_OPTIONS_set_release>` | <YYYY-MM-DD>              |
      +----------------------------------------------------+-----------------------------------------------------------+---------------------------+
      | :ref:`DOCX_SRCDIR <setupdocx_ENV_DOCX_SRCDIR>`     | :ref:`--srcdir <setupdocxbuild_OPTIONS_srcdir>`           | self.name (package-name)  |
      +----------------------------------------------------+-----------------------------------------------------------+---------------------------+
      | :ref:`DOCX_VERBOSE <setupdocx_ENV_DOCX_VERBOSE>`   |                                                           | 0                         |
      +----------------------------------------------------+-----------------------------------------------------------+---------------------------+
      | :ref:`DOCX_VERBOSEX <setupdocx_ENV_DOCX_VERBOSEX>` | :ref:`--verbose-ext <setupdocxbuild_OPTIONS_verbose_ext>` | 0                         |
      +----------------------------------------------------+-----------------------------------------------------------+---------------------------+
      | :ref:`DOCX_VERSION <setupdocx_ENV_DOCX_VERSION>`   | :ref:`--set-version <setupdocxbuild_OPTIONS_set_version>` | <setup.py>                |
      +----------------------------------------------------+-----------------------------------------------------------+---------------------------+
   
   
      .. raw:: html
      
         </div>
         </div>
         </div>

   The values are initialized by priority from the following sources:
   
   0. by their corresponding command line options or by the  of *build_docx*
   1. by the configuration file of the builder '<builder>/capabilities.<ext>', where the following
      extensions are supported:

         cfg, conf, ini, inix, json, properties, xml, yaml

   2. by their hardcoded final default values


   SEE ALSO
   --------

      setupdocx(1), call_doc.sh(1), call_apidoc.sh(1),
      
      online: 
         http://setupdocx.readthedocs.org/,
         https://setupdocx.sourceforge.io/

   LICENSE
   -------

      :ref:`modified Artistic License <MODIFIED_ARTISTIC_LICENSE_20>` = :ref:`ArtisticLicense20 <ARTISTIC_LICENSE_20>` + :ref:`Peer-to-Peer-Fairplay-amendments <LICENSES_AMENDMENTS>` 
   
   
.. only:: not builder_man


   .. _CALL_APIREF_SOURCE:
   
   .. only:: builder_html
   
      Source
      ------
   
   .. literalincludewrap:: _static/call_apiref.sh
      :language: bash
      :linenos:
   
   .. only:: builder_html
   
      Download
      --------
      
      `call_apiref.sh <_static/call_apiref.sh>`_
