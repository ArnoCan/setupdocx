
.. _HOWTO_CREATECONFTEMPLATES:

Create Configuration Templates
------------------------------

Configuration templates could be created easily.
The complete configuration is combined into one subdirectory structure,
where build time and runtime files are combined.
This includes the original configuration files of the used tools as well as the
eventually required runtime files such as style sheets.

Sphinx
^^^^^^
The common *Sphinx* build process for documenting *API* s  
consists of the major steps:

#. The generation of the API description as reST files. 

#. Add of manual created reST files, images, and other resources.

#. The processing of the reST files into the requested output document format.

The *setupdocx* supports the automation of all steps including the generation
of the *API* documentation and the mix-in of manual created documents.
The modification unit is hereby a file, which means files could be replaced only,
but not partially patched.

The following receipt describes the creation of the configuration, while the actual modification
of the *Sphinx* files is out of the scope of this document.
For the details about the application of *Sphinx* refer to [sphinxdoc]_.

**Sphinx Document**

#. Copy a template directory.
#. Edit the files as required.
#. Add required modified content files into the directory tree *<conf-dir>/docsrc*.
#. When required add changes to the directories:

   * *<conf-dir>/docsrc/_static* 
   * *<conf-dir>/docsrc/_themes* 
   * *<conf-dir>/docsrc/_templates* 

That's it.

**Sphinx Document with APIref**

The *setupdocx* supports in addition the mix-in of *javadoc* style *API* references
e.g. created by *epydoc* [epydoc]_ see also [EdwardLoper]_.
This requires the files:

* epydoc.conf
* epydoc.css

With the proper class for the integration,
see source example of :ref:`setup.py <SETUPPYSRC>`.

#. Either use a template with included support, or create the required files.
#. Assure, that the settings of  *target* and *css* are deactivated
   within *epydoc.conf*, else the command line parameters are ignored.


Epydoc
^^^^^^
available soon
