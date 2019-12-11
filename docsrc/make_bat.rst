
.. _MAKE_BAT:

make_docx.bat
=============

.. only:: builder_man

   SYNOPSIS
   --------

      make_docx.bat

   DESCRIPTION
   -----------

The *make_docx.bat* implements a execution wrapper wrapper for the creation of the documents.
Similar to *make.bat*.
The curent final default call is:

   .. parsed-literal::

      sphinx-build


.. only:: builder_man

   ENVIRONMENT
   -----------
   
   The following environment variables as set by their corresponding command line
   options of *build_docx* are passed as parameters.
   
   
      .. raw:: html
            
         <div class="indextab">
         <div class="nonbreakheadtab">
         <div class="autocoltab">
   
   +----------------------------------------------------+-----------------------------------------------------------+--------------------------+
   | environment variable                               | corresponding option                                      | default                  |
   +====================================================+===========================================================+==========================+
   | :ref:`DOCX_APIREF <setupdocx_ENV_DOCX_APIREF>`     | :ref:`--apiref <setupdocxbuild_OPTIONS_apiref>`           | ''                       |
   +----------------------------------------------------+-----------------------------------------------------------+--------------------------+
   | :ref:`DOCX_BUILDDIR <setupdocx_ENV_DOCX_BUILDDIR>` | :ref:`--build-dir <setupdocxbuild_OPTIONS_build_dir>`     | build/                   |
   +----------------------------------------------------+-----------------------------------------------------------+--------------------------+
   | :ref:`DOCX_CONFDIR <setupdocx_ENV_DOCX_CONFDIR>`   | :ref:`--confdir <setupdocxbuild_OPTIONS_config_path>`     | docsrc/conf/             |
   +----------------------------------------------------+-----------------------------------------------------------+--------------------------+
   | :ref:`DOCX_DOCNAME <setupdocx_ENV_DOCX_DOCNAME>`   | :ref:`--docname <setupdocxbuild_OPTIONS_docname>`         | self.name (package-name) |
   +----------------------------------------------------+-----------------------------------------------------------+--------------------------+
   | :ref:`DOCX_DOCSRC <setupdocx_ENV_DOCX_DOCSRC>`     | :ref:`--docsource <setupdocxbuild_OPTIONS_docsource>`     | docsrc/                  |
   +----------------------------------------------------+-----------------------------------------------------------+--------------------------+
   | :ref:`DOCX_INDEXSRC <setupdocx_ENV_DOCX_INDEXSRC>` | :ref:`--indexsrc <setupdocxbuild_OPTIONS_indexsrc>`       | "index.rst"              |
   +----------------------------------------------------+-----------------------------------------------------------+--------------------------+
   | :ref:`DOCX_DOCTYPE <setupdocx_ENV_DOCX_DOCTYPE>`   | :ref:`--doctype <setupdocxbuild_OPTIONS_doctype>`         | html                     |
   +----------------------------------------------------+-----------------------------------------------------------+--------------------------+
   | :ref:`DOCX_NAME <setupdocx_ENV_DOCX_NAME>`         | :ref:`--name <setupdocxbuild_OPTIONS_name>`               | self.name (package-name) |
   +----------------------------------------------------+-----------------------------------------------------------+--------------------------+
   | :ref:`DOCX_RAWDOC <setupdocx_ENV_DOCX_RAWDOC>`     | :ref:`--rawdoc <setupdocxbuild_OPTIONS_rawdoc>`           | ''                       |
   +----------------------------------------------------+-----------------------------------------------------------+--------------------------+
   | :ref:`DOCX_RELEASE <setupdocx_ENV_DOCX_RELEASE>`   | :ref:`--set-release <setupdocxbuild_OPTIONS_set_release>` | <YYYY-MM-DD>             |
   +----------------------------------------------------+-----------------------------------------------------------+--------------------------+
   | :ref:`DOCX_VERBOSE <setupdocx_ENV_DOCX_VERBOSE>`   |                                                           | 0                        |
   +----------------------------------------------------+-----------------------------------------------------------+--------------------------+
   | :ref:`DOCX_VERSION <setupdocx_ENV_DOCX_VERSION>`   | :ref:`--set-version <setupdocxbuild_OPTIONS_set_version>` | <setup.py>               |
   +----------------------------------------------------+-----------------------------------------------------------+--------------------------+
   
   
      .. raw:: html
      
         </div>
         </div>
         </div>

   SEE ALSO
   --------

      setupdocx(1), call_doc.sh(1)

   LICENSE
   -------

      :ref:`modified Artistic License <MODIFIED_ARTISTIC_LICENSE_20>` = :ref:`ArtisticLicense20 <ARTISTIC_LICENSE_20>` + :ref:`Peer-to-Peer-Fairplay-amendments <LICENSES_AMENDMENTS>` 
   
   
   COPYRIGHT
   ---------

      Copyright (C)2019 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez

.. only:: not builder_man

   .. _CALL_DOC_SOURCE:
   
   .. only:: builder_html
   
      Source
      ------
   
   .. literalincludewrap:: _static/make_docx.bat
      :language: sh
      :linenos:
   
   
   .. only:: builder_html
   
      Download
      --------
   
      `make_docx.bat <_static/make_docx.bat>`_

