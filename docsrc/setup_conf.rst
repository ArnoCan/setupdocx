
.. _SETUP_CONF:

setup.conf
==========

Configuration parameters for the commands provided by :ref:`setupdocx <SETUPLIB_COMMANDS>` refer to:

   +---------------------------------------------------+------------------------------------------------------+------------------------------------------------------+
   | summary                                           | conf section                                         | cli command                                          |
   +===================================================+======================================================+======================================================+
   | :ref:`setup.py \<any\> <SETUP_BUILD_DOCX>`        | :ref:`metadata <setupCONF_metadata>`                 |  all                                                 |
   +---------------------------------------------------+------------------------------------------------------+------------------------------------------------------+
   | :ref:`setup.py build_docx <SETUP_BUILD_DOCX>`     | :ref:`build_docx <setupCONF_build_docx>`             | :ref:`build_docx <setupdocxCOMMANDS_build_docx>`     |
   +---------------------------------------------------+------------------------------------------------------+------------------------------------------------------+
   | :ref:`setup.py dist_docx <SETUP_DIST_DOCX>`       | :ref:`dist_docx <setupCONF_dist_docx>`               | :ref:`dist_docx <setupdocxCOMMANDS_dist_docx>`       |
   +---------------------------------------------------+------------------------------------------------------+------------------------------------------------------+
   | :ref:`setup.py install_docx <SETUP_INSTALL_DOCX>` | :ref:`install_docx <setupCONF_install_docx>`         | :ref:`install_docx <setupdocxCOMMANDS_install_docx>` |
   +---------------------------------------------------+------------------------------------------------------+------------------------------------------------------+
   | :ref:`setup.py build_apidoc <SETUP_BUILD_APIDOC>` | :ref:`build_apidoc <setupCONF_build_apidoc>`         | :ref:`build_apidoc <setupdocxCOMMANDS_build_apidoc>` |
   +---------------------------------------------------+------------------------------------------------------+------------------------------------------------------+
   | :ref:`setup.py build_apiref <SETUP_BUILD_APIREF>` | :ref:`build_apiref <setupCONF_build_apiref>`         | :ref:`build_apiref <setupdocxCOMMANDS_build_apiref>` |
   +---------------------------------------------------+------------------------------------------------------+------------------------------------------------------+


The configuration data is used as static default values for the assigned command or metadata.
The evaluation is processed in the order with the falling priority:

1. command line parameters
2. *setup.conf* config
3. default values from the derived class provided by the member *docx_defaults*.
4. hard coded final defaults 

Be aware that some parameters are combined for resulting parameter values.
When these are set static the values are used, and further evaluation is suppressed.  

For additional information refer to *distutils* [distutils]_.

.. _setupCONF_metadata:

* metadata
   The section *[metadata]* contains the parameters supported by the classes derived from
   *distutils.dist.Distribution*.
   This comprises common data and global options of the *setup* call within *setup.py*.
   See [distutils]_.

.. _setupCONF_build_docx:

* build_docx
   The section *[build_docx]* provides default values for static parameters used by *build_docx*.
   See :ref:`build_docx <setupdocxCOMMANDS_build_docx>`.

.. _setupCONF_dist_docx:

* dist_docx
   The section *[dist_docx]* provides default values for static parameters used by *dist_docx*.
   See :ref:`dist_docx <setupdocxCOMMANDS_dist_docx>`.

.. _setupCONF_install_docx:

* install_docx
   The section *[dist_docx]* provides default values for static parameters used by *install_docx*.
   See :ref:`install_docx <setupdocxCOMMANDS_install_docx>`.

.. _setupCONF_build_apidoc:

* build_apidoc
   The section *[build_apidoc]* provides default values for static parameters used by *build_apidoc*.
   See :ref:`build_apidoc <setupdocxCOMMANDS_build_apidoc>`.

.. _setupCONF_build_apiref:

* build_apiref
   The section *[build_apiref]* provides default values for static parameters used by *build_apiref*.
   See :ref:`build_apiref <setupdocxCOMMANDS_build_apiref>`.

.. _SETUPCONFSRC:

Source
------
The *setup.conf* provides static default values for command line options.
Be aware, that the most of the values are assigned dynamic at runtime.
This in particular comprises the combination of multiple entries, which is
omitted in case of provided configuration values.
The use of these values has to be considered thoroughly. 
See [distutils]_. 

.. literalincludewrap:: _static/setup.cfg
   :linenos:

.. only:: builder_html

   Download
   --------
   
   `setup.conf <_static/setup.conf>`_

.. only:: builder_man

   SEE ALSO
   --------

      setupdocx(1), call_doc.sh(1), call_apidoc.sh(1), call_apiref.sh(1)

   LICENSE
   -------

      :ref:`modified Artistic License <MODIFIED_ARTISTIC_LICENSE_20>` = :ref:`ArtisticLicense20 <ARTISTIC_LICENSE_20>` + :ref:`Peer-to-Peer-Fairplay-amendments <LICENSES_AMENDMENTS>` 
   
   
   COPYRIGHT
   ---------

      Copyright (C)2019 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez

   