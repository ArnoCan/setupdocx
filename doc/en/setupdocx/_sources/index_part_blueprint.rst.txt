
*********
Blueprint
*********

.. _REFERENCE_ARCHITECTURE:

The modern landscapes of information infrastructures are commonly designed 
and organized as stacks of heterogeneous runtime environments
with comon frameworks.
This frequently requires the installation of specific components for various
platforms, including the generation of adapted packages, extended documentation,
and the automation of distributed large-scale tests.
The *setupdocxs* extends the *setuptools* for the required commands and options.

.. only:: singlehtml

   .. container:: figabstract
   
      .. figurewrap:: _static/setupdocx-architecture.png
         :width-singlehtml: 250
         :target-html: _static/setupdocx-architecture.png
         :align: center
         
      Figure: SetupDocX Integration


.. only:: not singlehtml

   .. figurewrap:: _static/setupdocx-architecture.png
      :width: 250
      :target-html: _static/setupdocx-architecture.png
      :align: center
      
      Figure: SetupDocX Integration

The package *setupdocx* provides the logical functions

.. only:: singlehtml

   .. container:: figabstract
   
      .. figurewrap:: _static/setupdocx-components.png
         :width-singlehtml: 450
         :target-html: _static/setupdocx-components.png
         :align: center
         
      Figure: SetupDocX functions *apidoc* and *apiref*


.. only:: not singlehtml

   .. figurewrap:: _static/setupdocx-components.png
      :width: 450
      :target-html: _static/setupdocx-components.png
      :align: center
      
      Figure: SetupDocX functions *apidoc* and *apiref*

* *build_docx*

  * *doc* - Create documentation composed by edited reST modules and optional
    documentation generated from the code.
  * *apidoc* - Create documentation composed by edited reST modules and optional
    extracted inline documentation generated from the code.

* *build_apiref*

  * *apiref* - Create optional *API* reference by automated code analysis extended
    by optional inline documentation.  

* *dist_docx*

  * create archives and distribution packages

* *install_docx*

  * install locally from source-build or distribution packages

The current implemented components are:

   .. raw:: html
   
      <div class="indextab">
      <div class="nonbreakheadtab">
      <div class="autocoltab">

   +----------+---------------------------------------------------------------------+---------------------------------------+------------------------------------+
   | function | command                                                             | wrapper                               | builder                            |
   +==========+=====================================================================+=======================================+====================================+
   | doc      | :ref:`build_docx --apidoc='' <SETUP_BUILD_DOCX>`                    | :ref:`call_doc.sh <CALL_APIDOC>`      | sphinx-build(1)                    |
   +----------+---------------------------------------------------------------------+---------------------------------------+------------------------------------+
   | apidoc   | :ref:`build_docx <SETUP_BUILD_DOCX>`                                | :ref:`call_apidoc.sh <CALL_APIDOC>`   | sphinx-build(1) + sphinx-apidoc(2) |
   +----------+---------------------------------------------------------------------+---------------------------------------+------------------------------------+
   | apidoc   | :ref:`build_docx option "--apiref" <setupdocxbuild_OPTIONS_apiref>` | :ref:`call_apidoc.sh <CALL_APIDOC>`   | sphinx-build(1) + sphinx-apidoc(2) |
   |          |                                                                     | + :ref:`call_apiref.sh <CALL_APIREF>` | + epydoc(3)                        |
   +----------+---------------------------------------------------------------------+---------------------------------------+------------------------------------+
   | apiref   | :ref:`build_apiref <SETUP_BUILD_APIREF>`                            | :ref:`call_apiref.sh <CALL_APIREF>`   | epydoc(3)                          |
   +----------+---------------------------------------------------------------------+---------------------------------------+------------------------------------+

   .. raw:: html
      
      </div>
      </div>
      </div>

**(1)**: see [sphinx]_, [sphinx-build]_ - calls by default 'build_doc', "--apidoc=''" deactivates the  'build_apidoc' call

**(2)**: see [sphinx-apidoc]_

**(3)**: see [epydoc]_, requires for some syntax elements of Python3 some patches which will be publicly available soon

A widespread of commonly required themes and formats for the automation
of internal and external publishing is contained by prepared
:ref:`configuration templates <CONFIGURATIONTEMPLATES>`,
additonal are available.
Custom themes and templates could be easily added.
The automation of open publication on various local and remote sites - e.g. 
local filesystem, local servers, github-pages, ReadTheDocs.org, SourceForge.io - is
available by the distribution command :ref:`install_docx <SETUP_INSTALL_DOCX>`. 

The current extension commands provide the complete flow of document creation,
packaging for distribution, and the installation.

.. only:: singlehtml

   .. container:: figabstract
   
      .. figurewrap:: _static/quickstart-flow.png
         :width-latex: 350
         :width: 400
         :target-html: _static/quickstart-flow.png
         :align: center
         
      Figure: Documentation Workflow  :ref:`more... <SETUPLIB_COMMANDS>`


.. only:: not singlehtml

   .. figurewrap:: _static/quickstart-flow.png
      :width-latex: 350
      :width: 400
      :target-html: _static/quickstart-flow.png
      :align: center
      
      Figure: Basic Documentation Workflow  :ref:`more... <SETUPLIB_COMMANDS>`

* Document creation, packaging, distribution, and installation with *sphinx* and *epdydoc* integration: 

   .. parsed-literal::
   
      python :ref:`setup.py <SETUPPYSRC>` :ref:`build_docx <SETUP_BUILD_DOCX>`        # compiles documents
      python :ref:`setup.py <SETUPPYSRC>` :ref:`build_apiref <SETUP_BUILD_APIREF>`      # compiles documents
      python :ref:`setup.py <SETUPPYSRC>` :ref:`dist_docx <SETUP_DIST_DOCX>`         # creates document distribution packages
      python :ref:`setup.py <SETUPPYSRC>` :ref:`install_docx <SETUP_INSTALL_DOCX>`      # installs local from build directory

      
The processed programming languages, document types, and presentation styles could be easily adapted to a variety
of predefined templates, and/or custom made designs.
The customization provides for configurations, builder for various languages and document types, and 
presentation styles.
The directory structure is the same for the the provided templates as required for user defined
custom setups.  

.. only:: singlehtml

   .. container:: figabstract
   
      .. figurewrap:: _static/source-dir-tree.png
         :width-singlehtml: 450
         :target-html: _static/source-dir-tree.png
         :align: center
         
      Figure: Standard and custom template directories.


.. only:: not singlehtml

   .. figurewrap:: _static/source-dir-tree.png
      :width: 450
      :target-html: _static/source-dir-tree.png
      :align: center
      
      Figure: Standard and custom template directories.


