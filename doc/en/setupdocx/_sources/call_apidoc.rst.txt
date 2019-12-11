
.. _CALL_APIDOC:

call_apidoc.sh
==============

.. only:: builder_man

   SYNOPSIS
   --------

      call_apidoc.sh

   DESCRIPTION
   -----------

The *call_apidoc.sh* implements a wrapper for the generation of the API documentation.
The curent defaul call is:

   .. parsed-literal::
   
      sphinx-apidoc

The expected output is the raw output from the tool *sphinx-apidoc*
including the appropriate *Makefile*.
The created files *conf.py* and *index.rst* are replace by the tool *call_doc.sh*
by the provided files within the configuration template.
It is recommended to replace generated files in case of required manual
documentation as required, instead adding files with different names.

The configuration requires to support a *Makefile* by itself, when the build step
*call_apidoc.sh* is omitted.
In this case also a complete set of files and a complete *toctree* has to be provided. 


.. only:: builder_man

   The call wraps the command for the  generation of the API documentation 
   - currently *sphinx-apidoc* by default.
   The interface is provided by environment variables.

   ENVIRONMENT
   -----------
   
   The following environment variables as set by their corresponding command line
   options of *build_docx* are passed as parameters.
   
   
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

   SEE ALSO
   --------

      setupdocx(1), call_doc.sh(1), call_apiref.sh(1)

   LICENSE
   -------

      :ref:`modified Artistic License <MODIFIED_ARTISTIC_LICENSE_20>` = :ref:`ArtisticLicense20 <ARTISTIC_LICENSE_20>` + :ref:`Peer-to-Peer-Fairplay-amendments <LICENSES_AMENDMENTS>` 


.. only:: not builder_man

   .. _CALL_APIDOC_SOURCE:
   
   .. only:: builder_html
   
      Source
      ------
   
   .. literalincludewrap:: _static/call_apidoc.sh
      :language: bash
      :linenos:
   
   .. only:: builder_html
   
      Download
      --------
      
      `call_apidoc.sh <_static/call_apidoc.sh>`_
