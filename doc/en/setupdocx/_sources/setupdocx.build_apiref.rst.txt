
.. _setupdocxBUILDAPIREF:

.. raw:: html

   <div class="shortcuttab">
   <div class="nonbreakheadtab">
   <div class="autocoltab">


setupdocx.build_apiref
======================

For current help refer to the online help:

   .. parsed-literal::
   
      python setup.py build_apiref --help

Alternative implementations are:

   .. parsed-literal::
   
      ipython setup.py build_apiref --help
      jython  setup.py build_apiref --help  # requires special install of setuptools, refer to the manuals 
      pypy    setup.py build_apiref --help

      ipw.exe setup.py build_apiref --help  # IronPython on Windows


With current output:

   .. parsed-literal::
   
      Common commands: (see '--help-commands' for more)
      
        setup.py build      will build the package underneath 'build/'
        setup.py install    will install the package
      
      Global options:
        --verbose (-v)  run verbosely (default)
        --quiet (-q)    run quietly (turns verbosity off)
        --dry-run (-n)  don't actually do anything
        --help (-h)     show detailed help message
        --no-user-cfg   ignore pydistutils.cfg in your home directory
      
      Options for 'build_apiref' command:
        --build-apiref      the name of the called script for the creation of the
                            API reference, default: <conf-dir>/call_apiref.sh
        --build-dir         the name of the build directory, default: build/
        --clean             removes the cached previous build, default: False
        --conf-dir          directory containing the configuration files, default:
                            <docsource>/conf/
        --debug (-d)        raises level of debug traces of current context,
                            supports repetition, each raises the debug level of the
                            context by one
        --docname           document output name, default: attribute of derived
                            class self.name
        --docsource         the name of the document source directory, default:
                            docsrc/
        --doctype           document type to create, default: 'html'
        --help-doctypes     List available document formats
        --name              the name of the package, default: attribute of derived
                            class self.name
        --no-exec (-n)      print only, do not execute
        --no-exec-max (-N)  print only the complete call stack, do not execute
        --rawdoc (-r)       Uses the generated documents by 'apiref' only, currently
                            the only option.
        --release           The release of the package
        --srcdir            Source directory
        --verbose (-v)      raises verbosity of current context, supports
                            repetition, each raises the command verbosity level of
                            the context 
        --verbose-ext (-x)  verbose for external tools, integer value, higher values
                            raise the level
        --version           The version of the package, default: attribute of
                            derived class self.distribution.metadata.version
      
      usage: setup.py [global_opts] cmd1 [cmd1_opts] [cmd2 [cmd2_opts] ...]
         or: setup.py --help [cmd1 cmd2 ...]
         or: setup.py --help-commands
         or: setup.py cmd --help
      
      
      Help on usage extensions by setupdocx
         --help-setupdocx


Module
------
.. automodule:: setupdocx.build_apiref


BuildApirefX
------------
.. autoclass:: BuildApirefX

.. _SPEC_BuildApirefX_finalize_options:

finalize_options
^^^^^^^^^^^^^^^^
.. automethod:: BuildApirefX.finalize_options


.. _SPEC_BuildApirefX_initialize_options:

initialize_options
^^^^^^^^^^^^^^^^^^
.. automethod:: BuildApirefX.initialize_options


.. _SPEC_BuildApirefX_run:

run
^^^
.. automethod:: BuildApirefX.run

   For the called custom worker scripts refer to:

      +-------------------------------------+--------------------------------------------+
      | [docs]                              | [source]                                   |
      +=====================================+============================================+
      | :ref:`call_apidoc.sh <CALL_APIDOC>` | `call_apidoc.sh <_static/call_apidoc.sh>`_ |
      +-------------------------------------+--------------------------------------------+
      | :ref:`call_doc.sh <CALL_DOC>`       | `call_doc.sh <_static/call_doc.sh>`_       |
      +-------------------------------------+--------------------------------------------+

   For the passed environment variables see :ref:`ENVIRONMENT <setupdocx_ENV_call_environment>`.

.. _SPEC_BuildApirefX_join_sphinx_mod_epydoc:

join_sphinx_mod_epydoc
^^^^^^^^^^^^^^^^^^^^^^
.. note::

   This is method is displayed for general documetation purposes only.
   Currently hardcoded, will be changed for flexible customization in
   future releases.

.. automethod:: BuildApirefX.join_sphinx_mod_epydoc

Exceptions
----------

.. autoexception:: SetuplibBuildApirefXError

.. raw:: html

   </div>
   </div>
   </div>

