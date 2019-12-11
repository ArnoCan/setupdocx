
********
Abstract
********

Modern landscapes of information infrastructures are commonly designed 
and organized as stacks of runtime service environments.
The technical architecture of the service stacks consists of a wide range of
heterogenous landscapes of components frequently requiring 
adaptation and mediation - resulting in a landscape of apps for the 
creation and installation of developer and user documentation.

.. only:: singlehtml

   .. container:: figabstract
   
      .. figurewrap:: _static/quickstart-flow.png
         :width-latex: 250
         :width: 300
         :target-html: _static/quickstart-flow.png
         :align: center
         
      Figure: Workflow commands for the creation of documents :ref:`more... <REFERENCE_ARCHITECTURE>`


.. only:: not singlehtml

   .. figurewrap:: _static/quickstart-flow.png
      :width-latex: 200
      :width: 350
      :target-html: _static/quickstart-flow.png
      :align: center
      
      Figure: Workflow commands for the creation of documents  :ref:`more... <REFERENCE_ARCHITECTURE>`


The *setupdocx* supports document creation, packaging, and installation commands for various 
tools and output options as a single unified interface.
This adds the ability to switch easily between various pre-configured document configurations
of presentation and content variants.
For example in case of Sphinx and Epydoc it is easy to switch between themes, templates, and styles,
as well as configuration files by just one call parameter. 

The initial provided components for standard tools support:

* *setuptools* - *setup.py* [setuptools]_

  - :ref:`build_docx <SETUP_BUILD_DOCX>` - create documentation
  - :ref:`install_docx <SETUP_INSTALL_DOCX>` - install documentation locally
  - :ref:`dist_docx <SETUP_DIST_DOCX>` - create distribution archives and packages

| \

  The following sub commands of *build_docx* are also available as 
  standalone versions:  
   
  - :ref:`build_apidoc <SETUP_BUILD_APIDOC>` - extract API documentation as standard document by *sphinx-apidoc*
  - :ref:`build_apiref <SETUP_BUILD_APIREF>` - extract API documentation in javadoc style by *epydoc*

| \

* *Sphinx* [sphinxdoc]_ 

  - Call wrapper for *sphinx-apidoc* and *sphinx-build* / *Makefile* -  :ref:`call_doc.sh <CALL_DOC>`
    and  :ref:`call_apidoc.sh <CALL_APIDOC>`.
  - *Sphinx* extensions:

    - :ref:`sphinx.ext.imagewrap <setupdocxSphinxExtImagewrap>` - extend images with builder tags, povide dynamic search paths 
    - :ref:`sphinx.ext.literalincludewrap <setupdocxSphinxExtLiteralIncludeWrap>` - povide dynamic search paths for the include directive

| \

* *Epydoc* [epydoc]_

  - Call wrapper for *epydoc* - :ref:`call_apiref.sh <CALL_APIREF>`.

These are supported as the platform for the creation of the documentation distributions,
once the distribution packages are created, *setupdocx* is no longer required,
see :ref:`SETUPLIBPLATFROMSBUILDTARGET`.

For more on extensions refer to [setuplib]_, and [setuptools]_ .
For tested standard OS and distributions see help on `installation <install.html>`_ / :ref:`Tested OS and Python Implementations <TESTED_OS_PYTHON>`.
   
