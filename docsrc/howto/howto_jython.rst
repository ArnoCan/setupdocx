
.. _HOWTO_JYTHON:

Howto Jython
------------
   
Jython Options
^^^^^^^^^^^^^^
E.g.:


   .. parsed-literal::  
   
      jython -Dpython.cachedir.skip=true setup.py --help
   
      python -J-Dpython.cachedir.skip=true setup.py --help

   
Howto Install Setuptools
^^^^^^^^^^^^^^^^^^^^^^^^
For the installation of the setuptool see the 
'The Definitive Guide to Jython' [JythonGuide]_.
   
Howto Online Help
^^^^^^^^^^^^^^^^^
The online help for the *testx* module is displayed by the call:

   .. parsed-literal::  
   
      jython setup.py


Howto Install Java Native Access Modules
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The 'Java Native Access' - *JNA* - modules are required 
by some of the basic prerequired modules of the author
for *Jython* on *Windows* systems.
For example for *platformids*.
The installation is simply done by copying the required modules, see also [JNA]_.

For example in case of *Windows-10* with the native *OpenSSH* server:

   .. parsed-literal::  
   
      rsync -avHPS  \\
        jna.jar \\
        jna-platform.jar \\
        win32-x86-64.jar \\
        --rsync-path='c:\\\\cygwin64\\\\bin\\\\rsync.exe' \\
        test@w10p:tmp



