
.. _LIBBASH:

libbash.sh
==========

.. only:: builder_man

   SYNOPSIS
   --------

      source libbash.sh

   DESCRIPTION
   -----------

The *libbash.sh* provides basic interfaces for wrapper scripts implemented by *bash*.
Uses environment variables for base configuration and trace output.

.. only:: builder_man

   ENVIRONMENT
   -----------
   
   Uses the following environment variables of the common call interface.

      .. raw:: html
            
         <div class="indextab">
         <div class="nonbreakheadtab">
         <div class="autocoltab">
   
      +----------------------------------------------------------+-------------------------------------------------------------+--------------------------+
      | environment variable                                     | corresponding option                                        | default                  |
      +==========================================================+=============================================================+==========================+
      | :ref:`DOCX_BREAKONERR <setupdocx_ENV_DOCX_BREAKONERR>`   | :ref:`--break-on-err <setupdocxbuild_OPTIONS_break_on_err>` | False                    |
      +----------------------------------------------------------+-------------------------------------------------------------+--------------------------+
      | :ref:`DOCX_BUILDDIR <setupdocx_ENV_DOCX_BUILDDIR>`       | :ref:`--build-dir <setupdocxbuild_OPTIONS_build_dir>`       | build/                   |
      +----------------------------------------------------------+-------------------------------------------------------------+--------------------------+
      | :ref:`DOCX_BUILDER <setupdocx_ENV_DOCX_BUILDER>`         | :ref:`--builder <setupdocxbuild_OPTIONS_builder>`           | sphinx                   |
      +----------------------------------------------------------+-------------------------------------------------------------+--------------------------+
      | :ref:`DOCX_BUILDRELDIR <setupdocx_ENV_DOCX_BUILDRELDIR>` | :ref:`--build-reldir <setupdocxbuild_OPTIONS_build_reldir>` | sphinx/apidoc/           |
      +----------------------------------------------------------+-------------------------------------------------------------+--------------------------+
      | :ref:`DOCX_CONFIGPATH <setupdocx_ENV_DOCX_CONFDIR>`      | :ref:`--config-path <setupdocxbuild_OPTIONS_config_path>`   | docsrc/conf/             |
      +----------------------------------------------------------+-------------------------------------------------------------+--------------------------+
      | :ref:`DOCX_DEBUG <setupdocx_ENV_DOCX_DEBUG>`             | :ref:`--debug <setupdocxbuild_OPTIONS_debug>`               | 0                        |
      +----------------------------------------------------------+-------------------------------------------------------------+--------------------------+
      | :ref:`DOCX_DOCNAME <setupdocx_ENV_DOCX_DOCNAME>`         | :ref:`--docname <setupdocxbuild_OPTIONS_docname>`           | self.name (package-name) |
      +----------------------------------------------------------+-------------------------------------------------------------+--------------------------+
      | :ref:`DOCX_DOCSRC <setupdocx_ENV_DOCX_DOCSRC>`           | :ref:`--docsource <setupdocxbuild_OPTIONS_docsource>`       | docsrc/                  |
      +----------------------------------------------------------+-------------------------------------------------------------+--------------------------+
      | :ref:`DOCX_DOCTEMPLATE <setupdocx_ENV_DOCX_DOCTEMPLATE>` | :ref:`--doctemplate <setupdocxbuild_OPTIONS_set_version>`   | default                  |
      +----------------------------------------------------------+-------------------------------------------------------------+--------------------------+
      | :ref:`DOCX_DOCTYPE <setupdocx_ENV_DOCX_DOCTYPE>`         | :ref:`--doctype <setupdocxbuild_OPTIONS_doctype>`           | html                     |
      +----------------------------------------------------------+-------------------------------------------------------------+--------------------------+
      | :ref:`DOCX_INDEXSRC <setupdocx_ENV_DOCX_INDEXSRC>`       | :ref:`--indexsrc <setupdocxbuild_OPTIONS_indexsrc>`         | index.rst                |
      +----------------------------------------------------------+-------------------------------------------------------------+--------------------------+
      | :ref:`DOCX_QUIET <setupdocx_ENV_DOCX_QUIET>`             | :ref:`--quiet <setupdocxbuild_OPTIONS_quiet>`               | 0                        |
      +----------------------------------------------------------+-------------------------------------------------------------+--------------------------+
      | :ref:`DOCX_RELEASE <setupdocx_ENV_DOCX_RELEASE>`         | :ref:`--set-release <setupdocxbuild_OPTIONS_set_release>`   | <YYYY-MM-DD>             |
      +----------------------------------------------------------+-------------------------------------------------------------+--------------------------+
      | :ref:`DOCX_VERBOSE <setupdocx_ENV_DOCX_VERBOSE>`         | :ref:`--verbose <setupdocxbuild_OPTIONS_verbose>`           | 1                        |
      +----------------------------------------------------------+-------------------------------------------------------------+--------------------------+
      | :ref:`DOCX_VERSION <setupdocx_ENV_DOCX_VERSION>`         | :ref:`--set-version <setupdocxbuild_OPTIONS_set_version>`   | <setup.py>               |
      +----------------------------------------------------------+-------------------------------------------------------------+--------------------------+
      | PROJECT                                                  |                                                             | optional                 |
      +----------------------------------------------------------+-------------------------------------------------------------+--------------------------+
   
   
      .. raw:: html
      
         </div>
         </div>
         </div>

   SEE ALSO
   --------

      setupdocx(1), call_doc.sh(1), call_apidoc.sh(1), call_apiref.sh(1)

   LICENSE
   -------

      :ref:`modified Artistic License <MODIFIED_ARTISTIC_LICENSE_20>` = :ref:`ArtisticLicense20 <ARTISTIC_LICENSE_20>` + :ref:`Peer-to-Peer-Fairplay-amendments <LICENSES_AMENDMENTS>` 
   
   
.. only:: not builder_man

   .. _CALL_DOC_SOURCE:
   
   .. only:: builder_html
   
      Source
      ------
   
   .. literalincludewrap:: _static/libbash.sh
      :language: bash
      :linenos:
   
   
   .. only:: builder_html
   
      Download
      --------
   
      `call_doc.sh <_static/libbash.sh>`_

