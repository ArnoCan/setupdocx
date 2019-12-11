
.. _SETUP_PY:

setup.py
========

For the commands provided by :ref:`setupdocx <SETUPLIB_COMMANDS>` refer to:

   +---------------------------------------------------+----------------------------------------------------------------+--------------------------------------------+---------------------------------------------------------------------+
   | summary                                           | cli options                                                    | module                                     | code                                                                |
   +===================================================+================================================================+============================================+=====================================================================+
   | :ref:`setup.py build_docx <SETUP_BUILD_DOCX>`     | :ref:`build_docx-context-options <setupdocxbuild_OPTIONS>`     | :ref:`build_docx <setupdocxBUILDDOCX>`     | `BuildDocX <_modules/setupdocx/build_docx.html#BuildDocX>`_         |
   +---------------------------------------------------+----------------------------------------------------------------+--------------------------------------------+---------------------------------------------------------------------+
   | :ref:`setup.py build_apiref <SETUP_BUILD_APIREF>` | :ref:`build_apiref-context-options <setupapirefbuild_OPTIONS>` | :ref:`build_apiref <setupdocxBUILDAPIREF>` | `BuildAPIrefX <_modules/setupdocx/build_apiref.html#BuildApirefX>`_ |
   +---------------------------------------------------+----------------------------------------------------------------+--------------------------------------------+---------------------------------------------------------------------+
   | :ref:`setup.py dist_docx <SETUP_DIST_DOCX>`       | :ref:`dist_docx-context-options <setupdocxbuild_OPTIONS>`      | :ref:`dist_docx <setupdocxDISTDOCX>`       | `DistDocX <_modules/setupdocx/dist_docx.html#DistDocX>`_            |
   +---------------------------------------------------+----------------------------------------------------------------+--------------------------------------------+---------------------------------------------------------------------+
   | :ref:`setup.py install_docx <SETUP_INSTALL_DOCX>` | :ref:`install_docx-context-options <setupdocxbuild_OPTIONS>`   | :ref:`install_docx <setupdocxINSTALLDOCX>` | `InstallDocX <_modules/setupdocx/install_docx.html#InstallDocX>`_   |
   +---------------------------------------------------+----------------------------------------------------------------+--------------------------------------------+---------------------------------------------------------------------+

Module
------

The *setup.py* of the *setupdocx* itself serves as a pattern for the provided libraries.
All *Python* projects of the author are based on the *setupdocx*,
some examples are:

* ePyUnit - [EPYUNIT]_ 
* filesysobjects - [FILESYSOBJECTS]_ 
* jsondata - [JSONDATA]_
* platformids - OS Type and Distribution IDs of System Platforms - [platformids]_
* platformids - [platformids]_ 
* pysourceinfo - [PYSOURCEINFO]_ 
* pythonids - Python Interpreter and Compiler IDs - [pythonids]_ 
* syscalls - [SYSCALLS]_


For the commands provided by :ref:`setupdocx <SETUPLIB_COMMANDS>` refer to:

   +---------------------------------------------------+-----------------------------------------------------+-------------------------------------------+------------------------------------------------------------------+
   | summary                                           | cli options                                         | module                                    | code                                                             |
   +===================================================+=====================================================+===========================================+==================================================================+
   | :ref:`setup.py build_docx <SETUP_BUILD_DOCX>`     | :ref:`build_docx <setupdocxCOMMANDS_build_docx>`    | :ref:`build_docx <setupdocxBUILDDOCX>`    | `BuildDocX <_modules/setupdocx/build_docx.html#BuildDocX>`_      |
   +---------------------------------------------------+-----------------------------------------------------+-------------------------------------------+------------------------------------------------------------------+
   | :ref:`setup.py dist_docx <SETUP_DIST_DOCX>`       | :ref:`dist_docx <setupdocxCOMMANDS_dist_docx>`      | :ref:`dist_docx <setupdocxDISTDOCX>`      | `DistDocX <_modules/setupdocx/dist_docx.html#DistDocX>`_         |
   +---------------------------------------------------+-----------------------------------------------------+-------------------------------------------+------------------------------------------------------------------+
   | :ref:`setup.py install_docx <SETUP_INSTALL_DOCX>` | :ref:`install_docx <setupdocxCOMMANDS_install_docx>`| :ref:`install_docx <setupdocxINSTALLDOCX>`| `InstallDocX <_modules/setupdocx/install_docx.html#InstallDocX>`_|
   +---------------------------------------------------+-----------------------------------------------------+-------------------------------------------+------------------------------------------------------------------+



.. automodule:: .setup

build_docx
----------
.. autoclass:: setup.build_docx

dist_docx
---------
.. autoclass:: setup.dist_docx

install_docx
------------
.. autoclass:: setup.install_docx


.. _SETUPPYSRC:

Source
------
The *setup.py* of the *setupdocx* itself serves as a pattern for the provided libraries.
All *Python* projects of the author are based on the *setupdocx*,
some examples are:

* ePyUnit - [EPYUNIT]_ 
* filesysobjects - [FILESYSOBJECTS]_ 
* jsondata - [JSONDATA]_
* platformids - OS Type and Distribution IDs of System Platforms - [platformids]_
* platformids - [platformids]_ 
* pysourceinfo - [PYSOURCEINFO]_ 
* pythonids - Python Interpreter and Compiler IDs - [pythonids]_ 
* syscalls - [SYSCALLS]_

.. literalincludewrap:: _static/setup.py
   :language: python
   :linenos:

.. only:: builder_html

   Download
   --------
   
   `setup.py <_static/setup.py>`_

   