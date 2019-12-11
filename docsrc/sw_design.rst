.. _SW_DESIGN:

***************
Software Design
***************

The *setupdocx* provides

* commands and entry points for *setup.py*
* extensions for *sphinx*

For the understanding of the command resolution it is essential to know the basic principle
of the software design.
Thus it is recommend to be read in particular for the users which are going to apply
the *build_docx* and *dist_docx* commands for the creation of packages.

Commands and Entry Points
=========================
The provided command classes classes are foreseen to be used as entry points.
The undelying classes are applicable as base classes for custom commands too.

The basic architecture separates the *builder* and the *configuration*.
The builder are mayor parts of the provided commands, which by default construct
the parameters for the call of a *call-wrapper*.
The *call-wrapper* itself finishes the specific command line call parameters and 
executes the wrapped executable as a subprocess.
The suppored default builder is *sphinx*, which ocnsists of two major executables

* *sphinx-build* - the final document creator
* *sphinx-apidoc* - the extractor of inline documentation from the source code

Almost each component could be altered by command line parameters, thus easily
adapted to other builders.
The wrappe scipts could be altered too to an user defined script implemented in an 
arbitrary programming/scripting language.
The parameters are passed by schell environment variables -
:ref:`ENVIRONMENT <setupdocx_ENV_call_environment>`.

The available builders and configurations are searched by the commandline options
*--builder-path* and *config-path*.
The names of the corresponding subdirectories are the literal names of the 
*--builder* option.

.. only:: singlehtml

   .. container:: figabstract
   
      .. figurewrap:: _static/source-dir-tree.png
         :width-singlehtml: 400
         :target-html: _static/source-dir-tree.png
         :align: center
         
      Figure: setupdocx builders 


.. only:: not singlehtml

   .. figurewrap:: _static/source-dir-tree.png
      :width: 400
      :target-html: _static/source-dir-tree.png
      :align: center
      
      Figure: setupdocx builders


The builder is provided by a subdirectory containing the required call wrappers.
The call wrappers actually execute the document renderer.
This enables the option of late assembly of the call parameters for the 
command line based call interface.
The principle also enables the option to use almost any document renderer
by customized call wrappers.
The application of a common controller with the two-level passing of the call parameters
in particular provides the tight integration of the utilized tools into a seamless processing flow. 

The following figure depicts a typical structure with the executable *<builder-component-m>*,
and the setup configuration of the builder stored in a file named *capabilities*.  

.. only:: singlehtml

   .. container:: figabstract
   
      .. figurewrap:: _static/component-structure.png
         :width-singlehtml: 600
         :target-html: _static/component-structure.png
         :align: center
         
      Figure: Integration of the builder


.. only:: not singlehtml

   .. figurewrap:: _static/component-structure.png
      :width: 600
      :target-html: _static/component-structure.png
      :align: center
      
      Figure: Integration of the builder

The file *capabilities* has actually a postfix of the applied syntax type, which is either 
provided by the call, or selected automatically if not stated else.
The syntax is transparently resolved by *yapydata.datatree* [datatree]_, which currently
supports the syntaxes::

   INI, JSON, XML, YAML

The read *capabilities* file is than scanned into the internal data tree as *JSON*
compatible data graph.
The data tree is actually superposed, where the non-touched default values are kept.
This procedure could be repeated by multiple files - see also :ref:`--cap <setupdocxbuild_OPTIONS_cap>`. 

The standard default configuration of *setupdocx* supports the builders *sphinx* and *epydoc*,
where *sphinx* comprises the wrappers for the API generation *call_apidoc* and the main renderer
*call_docx*.
These files again have actually suffixes, which will be selected automatically, the current default
is *.sh* for *shell* - preferebly *bash* - calls.

.. only:: singlehtml

   .. container:: figabstract
   
      .. figurewrap:: _static/source-dir-tree-sphinx.png
         :width-singlehtml: 500
         :target-html: _static/source-dir-tree-sphinx.png
         :align: center
         
      Figure: setupdocx standard sphinx setup


.. only:: not singlehtml

   .. figurewrap:: _static/source-dir-tree-sphinx.png
      :width: 500
      :target-html: _static/source-dir-tree-sphinx.png
      :align: center
      
      Figure: setupdocx standard sphinx setup

The square components represent callables - with additional file postfix,
the rounded components are logical entities, while the file symbol depicts
the capabilities setup.

The first additional variant will soon add support for the builder *mkdocs*, others are going to follow. 

.. only:: singlehtml

   .. container:: figabstract
   
      .. figurewrap:: _static/source-dir-tree-mkdocs.png
         :width-singlehtml: 500
         :target-html: _static/source-dir-tree-mkdocs.png
         :align: center
         
      Figure: setupdocx standard mkdocs setup


.. only:: not singlehtml

   .. figurewrap:: _static/source-dir-tree-mkdocs.png
      :width: 500
      :target-html: _static/source-dir-tree-mkdocs.png
      :align: center
      
      Figure: setupdocx standard mkdocs setup

Capabilites
===========

The capabilities file for the standard builder *sphinx* configures the executables
*sphinx-build* and *sphinx-apidoc*.
The file defines the default values for input and output paths, document types,
and additional processing options.
The capabilities contain the abstract features designed as a common parameter set for all
builders.
The enumeration define the valid and/or enabled set of the specific features.
Special builder options could be passed through natively as call options.
The actual implementation is proceeded within the wrapper.

The represented logical structure defines the settings for the logical components for
the document renderer - **doc** , the API extractor - **apidoc** , and the builder
selector **builder** .
Thus multiple builders could be loaded and interwork, while the entry point is defined by
the **builder[name]** attribute.

   .. parsed-literal::

      {
         **builder** {
            **name** = **sphinx**             <- the name of the current builder
         }
         
         **sphinx** {                     <- the configuration of the current builder 
            defaults{                 <- defaults to superpose hard-coded defaults
               ...
            }
            **doc** {                     <- the creation of the document - the renderer
               wrapper
               executable
               doctypes
               defaults
            }
            **apidoc** {                  <- the generation of the standard API documentation - the API extractor
               wrapper
               executable
               doctypes
               defaults
            }
         }
      } 


The implementation of the capabilities for the standard builder *sphinx* - here by *JSON* syntax - is:

   .. literalincludewrap:: _static/capabilities.json
      :language: json
      :linenos:


 
Standard Commands
=================

The current release of *setupdocx* contains the commands:

* build_docx
* build_apidoc
* build_apiref
* dist_docx
* install_docx


Extensions for Sphinx
=====================

The split of the document content and the view enables for easy and simple generation of multiple
appearences.
The introduction of the document templates also enables for the easy creation of document 
variants with adpated contents.
The casual generation of generation of the modular document variants requires in particular the
independence from refrenced file paths.

The *setupdocx* provides extensions for the typical file system path based document components:

* figures - :ref:`setupdocx.sphinx.ext.imagewrap <setupdocxSphinxExtImagewrap>`
* include files - :ref:`setupdocx.sphinx.ext.literalincludewrap <setupdocxSphinxExtLiteralIncludeWrap>`

.. only:: singlehtml

   .. container:: figabstract
   
      .. figurewrap:: _static/sphinx-extensions.png
         :width-singlehtml: 300
         :target-html: _static/sphinx-extensions.png
         :align: center
         
      Figure: sphinx extensions


.. only:: not singlehtml

   .. figurewrap:: _static/sphinx-extensions.png
      :width: 300
      :target-html: _static/sphinx-extensions.png
      :align: center
      
      Figure: sphinx extensions
 
The approach is hereby not simply based on a common directory, but enabled for the path resolution
by an upward search - which may end in a common shared directory.
All file paths are replaced by the acctual present appropriate path for the target system.  

