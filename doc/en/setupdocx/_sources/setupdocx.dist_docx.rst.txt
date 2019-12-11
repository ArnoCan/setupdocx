
.. _setupdocxDISTDOCX:

.. raw:: html

   <div class="shortcuttab">


setupdocx.dist_docx
===================

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
      
      Options for 'dist_docx' command:
        --append          append files to existing archive, default: create new,can
                          be used to add new unpack-dir
        --build-dir       document source location, default 'build/', reads the
                          prepared documents from <build-dir>/doc/<document-name>
        --date            adds the build date to the archive name, default
                          '<year>.<month>.<day>'
        --debug           debug flag
        --dist-dir        archive location for creation, default 'dist/'
        --doctype         document type to pack, default: 'html', see '--help-
                          doctypes'
        --extra-suffixes  comma separated list of extra suffixes, single file-
                          documents are validated by suffixes, e.g. '.pdf' or
                          '.epub', non-digit suffixes for man pages require extra
                          suffixes, see manualsdefault: ''
        --force           Force to processing by deactivating non-essential checks,
                          suppresses validation, default: False
        --forcedir        Force to pack directories, in case of single document
                          types such as PDF too. Else the types PDF, and EPUB are
                          compressed without the containing directory. The name of
                          single-file documents is changed when archive name,
                          version, etc. are provided. Default: False
        --formats         comma separated list of types of the created packages,
                          default: 'zip', see '--help-formats'
        --help-doctypes   List available document formats.
        --help-formats    List available distribution formats.
        --name            changes package name 'self.name', see also '--name-in' and
                          '--name-out'
        --name-in         input package name, default 'self.name'
        --name-out        output package name, default 'self.name'
        --no-exec (-n)    print only, do not execute
        --plat-name       platform name to add to name, default: ''
        --quiet (-q)      quiet of current context, resets verbosity of applied
                          context to '0', default: off
        --set-release     The release of the package
        --set-version     sets version of created archive, default: ''
        --verbose (-v)    raises verbosity of current context, supports repetition,
                          each raises the command verbosity level of the context by
                          one 
      
      usage: setup.py [global_opts] cmd1 [cmd1_opts] [cmd2 [cmd2_opts] ...]
         or: setup.py --help [cmd1 cmd2 ...]
         or: setup.py --help-commands
         or: setup.py cmd --help
      
      
      Help on usage extensions by setupdocx
         --help-setupdocx

Module
------
.. automodule:: setupdocx.dist_docx


DistDocX
--------
.. autoclass:: DistDocX

.. _SPEC_DistDocX_finalize_options:

finalize_options
^^^^^^^^^^^^^^^^
.. automethod:: DistDocX.finalize_options

.. _SPEC_DistDocX_initialize_options:

initialize_options
^^^^^^^^^^^^^^^^^^
.. automethod:: DistDocX.initialize_options

.. _SPEC_DistDocX_run:

run
^^^
.. automethod:: DistDocX.run

Exceptions
----------

.. autoexception:: SetuplibDistDocXError

.. raw:: html

   </div>

