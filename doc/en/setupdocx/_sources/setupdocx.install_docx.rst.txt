
.. _setupdocxINSTALLDOCX:

.. raw:: html

   <div class="shortcuttab">


setupdocx.install_docx
======================

For current help refer tot the online help:

   .. parsed-literal::
   
      python setup.py dist_docx --help

Alternative implementations are:

   .. parsed-literal::
   
      ipython setup.py dist_docx --help
      jython  setup.py dist_docx --help  # requires special install of setuptools, refer to the manuals 
      pypy    setup.py dist_docx --help

      ipw.exe setup.py dist_docx --help  # IronPython on Windows

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
      
      Options for 'install_docx' command:
        --name          package name, changes 'self.name', default: 'self.name'
        --build-dir     installation source, default 'build', resulting in the
                        created document 'build/apidoc/<docname>'
        --docname       document name, could be different from '--name' used as the
                        input and the output name of the document, default:
                        'self.name'
        --no-exec (-n)  print only, do not execute
        --target-dir    installation target directory, PEP-370, user data directory,
                        default '/user/data/' + 'doc/en/html/man3'
        --doctype       document type to install, default 'html' only
        --no-exec (-n)  print only, do not execute
        --debug         debug flag
        --verbose       verbose flag
      
      usage: setup.py [global_opts] cmd1 [cmd1_opts] [cmd2 [cmd2_opts] ...]
         or: setup.py --help [cmd1 cmd2 ...]
         or: setup.py --help-commands
         or: setup.py cmd --help
      
      
      Help on usage extensions by setupdocx
         --help-setupdocx

Module
------
.. automodule:: setupdocx.install_docx


InstallDocX
-----------
.. autoclass:: InstallDocX

.. _SPEC_InstallDocX_finalize_options:

finalize_options
^^^^^^^^^^^^^^^^
.. automethod:: InstallDocX.finalize_options

.. _SPEC_InstallDocX_initialize_options:

initialize_options
^^^^^^^^^^^^^^^^^^
.. automethod:: InstallDocX.initialize_options

.. _SPEC_InstallDocX_run:

run
^^^
.. automethod:: InstallDocX.run

Exceptions
----------

.. autoexception:: SetupDocXInstallError

.. raw:: html

   </div>

