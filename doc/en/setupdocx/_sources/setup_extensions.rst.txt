
.. _SETUPLIBEXTENSIONS: 



Setup Extensions
================

The *setuptools* or *distutils* support the possibility of the extension 
by entry points and locally by additional commands.
The *setupdocx* is designed to be applied in both variants.

* entry points:

  Standard applications and users should use only this globally installed
  extenstions.

* local custom commands:

  Local custom extensions of the classes could be used for special
  document formatters and complex parameter design.

Entry Points
^^^^^^^^^^^^
The so called entry points support a global installation of the commands as public
components for shared use.
These are thereafter availabe as a usual *setup.py* command and coud be listed
by the option::

   python setup.py --help-commands

Alternatively by the advanced command *list_entry_points* provided by the library
*setuplib* [setuplib]_::

   python setup.py list_entry_points

See also help for options::

   python setup.py list_entry_points -h

No modification of the *setup.py* is required.

Local Custom Commands
^^^^^^^^^^^^^^^^^^^^^
Extension commands, or command classes are based on 

.. parsed-literal::

   distutils.cmd.Command
   
.. note::

   These work with *distutils* as well as with the newer *setuptools*,
   both libraries are at the time of the writing of this document internally deeply coupled.

The derived command classes define custom commands and add these to the internal dispatcher by inserting
the list of new commands into the setup call:

.. parsed-literal::

   setup(
       author="Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez",
       license="Artistic-License-2.0 + Forced-Fairplay-Constraints",
       cmdclass={
           'build_docx': build_docx,
           'dist_docx': dist_docx,
           'install_docx': install_docx,
       },
   )

Refer to the :ref:`setup.py <SETUP_PY>` including :ref:`setup.conf <SETUP_CONF>`
as an example, which uses *setupdocx* itself before the installation,
thus preferebly uses the explict extension classes instead of the extension points.

