
.. _HOWTO_VERBOSE_AND_QUIET:

Howto Apply Verbose and Quiet
-----------------------------

.. _HOWTO_VERBOSE_AND_QUIET_COMMANDS:

The Commands within setup.py
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The command classes are inherited from the base class *distutils.cmd.Command*.
These inherit also the behaviour of the options which is actually implemented in the 
module *distutils.dist* in combination with the module *distutils.fancy_getopt*.
The *distutils*  define some global options and metadata, 
with special behavior for some options.

The options *--quiet* and *--verbose* implement special behaviour and the inheritance
of the global context into the command classes context, with support of subcontext
settings.
The subcontext of the commands inherits herby the initial value, while further settings 
are effecting the context only.
The special behaviour results here in particular due to the definition of related options by 
the introduction of 'negative-options'.
Thus the values of quiet and verbose are combined into one variable *verbose*, which is
normalized to the value *verbose=1* for normal behaviour.
The verbose flag could be applied repetitive, where each raises the value of the current 
context by one - '*verbose += 1*'.
This results in the following rules:

#. The option *--quiet* resets within the applied context the value of 
   verbose to *verbose=0*.
#. The value of the global context is used to initialize the command context.
#. Each context now applies within it's own scope the options *--quiet* and *--verbose*

Thus a global *--quiet* sets the command context to quiet too, while the first *--verbose*
just normalizes the behaviour of the command context, while the second *--verbose* actually
raises the verbosity.

So when applying a command of components of *setuplib* such as *setupdocx* be aware, that the
initial value of one '*verbose=1*' is the normal display, while the value '*verbose=2*'
is actually the first level of the verbosity mode.
The value of '*verbose=0*' corresponds to *--quiet*.
When the *--quiet* option is applied in combination with one or more *--verbose* options
the options in sequential order before the *--quiet* option are resetted to zero,
while following will increment again now from zero on. 
Therefore no own global member for *quiet* is defined.

This concept is adapted by all members of the *setuplib* family such as *setupdocx*.

So far the theory, now to the actual implementation. The current release at the time of writing 
has a minor bug, which may cause some trouble when using the local context option *--verbose*.
The initialization of the command class is basically straight forward, though it transfers 
simply the value of the global context.
This behaviour changes - what I see as a bug - when local *--verbose* options are set.
The variable verbose is than reset to initially zero *verbose=0*, while the global context remains
untouched as *verbose=1*.
Thus the first *-verbose* options is without effect.

1. Example:

   For example
   
      .. parsed-literal::
   
         python setup.py build_docx
   
   results in
   
      .. parsed-literal::
   
         global:               verbose=1
         build_docx context:   verbose=1

2. Example:

   While the call:
   
      .. parsed-literal::
   
         python setup.py build_docx --verbose
   
   results also in
   
      .. parsed-literal::
   
         global:               verbose=1
         build_docx context:   verbose=1

3. Example:

   The call 
   
      .. parsed-literal::
   
         python setup.py build_docx --verbose  --verbose
   
   results in
   
      .. parsed-literal::
   
         global:               verbose=1
         build_docx context:   verbose=2

4. Example:

   The call 
   
      .. parsed-literal::
   
         python setup.py --verbose build_docx
   
   results also in
   
      .. parsed-literal::
   
         global:               verbose=2
         build_docx context:   verbose=2

5. Example:

   While the call 
   
      .. parsed-literal::
   
         python setup.py --verbose build_docx --verbose
   
   results in
   
      .. parsed-literal::
   
         global:               verbose=2
         build_docx context:   verbose=1

6. Example:

   The call 
   
      .. parsed-literal::
   
         python setup.py --quiet build_docx
   
   results in
   
      .. parsed-literal::
   
         global:               verbose=0
         build_docx context:   verbose=0

7. Example:

   The call 
   
      .. parsed-literal::
   
         python setup.py --quiet build_docx --verbose
   
   results also in
   
      .. parsed-literal::
   
         global:               verbose=0
         build_docx context:   verbose=1


As could be seen from the previous examples the propagation of the cumulative values
could not be said to be linear or one-to-one.
This requires the explicit check by the - eventually inofficial API:

   .. parsed-literal::
   
      self.verbose_options = self.distribution.get_option_dict('build_docx')['verbose'][1]

Without the check of the actual number of verbose flags of the command context it is not possible
to decide whether the value has been inherited from the global context, or defined 
by local context options.  

Finally it is decided to use a small patch by adapting to the numbering scheme of
the global context.
The semantics of the context flags for verbose is redefined to the combined quiet and vebose value.

0. The global context flags are set for the local flags when no local options *--quiet*
   and *--verbose* are present.
   This is the standard behaviour.

1. To the local options the offset *1* is added when one or more local options
   *--verbose*  are set.
   
      .. parsed-literal::
      
         def finalize_options(self):
         
           # quick-and-dirty hack to resolve the inconsistency of
           # global and local verbose values of distutils
           try:
               _v_opts = self.distribution.get_option_dict('build_docx')['verbose'][1]
               if _v_opts:
                   self.verbose += 1
           except:
               # fallback to slightly erroneous behaviour when the interface 
               # of distutils changes
               pass

   For example the call:

      .. parsed-literal::
      
         python setup.py --verbose --verbose build_docx --verbose 

   results - correctly - in:

      .. parsed-literal::
      
         self.distribution.verbose == 3
         self.verbose == 2

1. The local *--quiet* flag resets the local context to zero - '*0*'.
   This is ad the actuual sequential position within the command line parameters.
   Thus the following *--verbose* flags restart again to raise the level now from *0* on. 
   This is implemented for the global options as well as for the local context options.

   For example the call:

      .. parsed-literal::
      
         python setup.py --verbose --quiet build_docx --verbose --verbose --quiet --verbose

   results - correctly - in:

      .. parsed-literal::
      
         self.distribution.verbose == 0
         self.verbose == 2

.. _SEMANTICS_VERBOSE_AND_QUIET:

The semantics for the resulting value is defined by the following table.

   .. raw:: html

      <div class="overviewtab">
      <div class="nonbreakheadtab">
      <div class="autocolumntab">

   +--------------+---------------------------------------------------------------+
   | self.verbose | description                                                   |
   +==============+===============================================================+
   | 0            | quiet mode                                                    |
   +--------------+---------------------------------------------------------------+
   | 1            | standard display mode                                         |
   +--------------+---------------------------------------------------------------+
   | >1           | additional verbose display as defined by the specific command |
   +--------------+---------------------------------------------------------------+

   .. raw:: html

      </div>
      </div>
      </div>

.. _HOWTO_VERBOSE_AND_QUIET_SUBCOMMANDS:

Called Subcommands
^^^^^^^^^^^^^^^^^^
The verbosity in order to test and debug comprises multiple levels of processes.
This is the called commands within the current process of *setup.py*, and the called subprocesses
by the wrapper scripts and the again called subprocesses for the actual used external tools,
e.g. *call_docs.sh*, which calls finally *sphinx-build*.
This requires the pass through of the values to subcommands, at least the wrapper scripts in order
to perform controlled verbose display.
The passed value is hereby provided as environment
variable :ref:`DOCX_VERBOSE <setupdocx_ENV_DOCX_VERBOSE>`.
The value follows the previously defined scheme for combined verbose and quiet values.

In addition is has proved to be practical to introduce a separate flag for the verbosity of the
external final processing tool e.g. in case of document generation.
The limit occurs here by the distutils, which supports cumulative repetition of command line options for
the *--verbose* flag only.
In order to avoid to implement a custom library the value is introduced with an option argument value:

   .. parsed-literal::
   
      --verbose-ext=<int-level>

      int-level := 0..N

The passed value is hereby again provided as environment
variable :ref:`DOCX_VERBOSEX <setupdocx_ENV_DOCX_VERBOSEX>`.
The value follows the previously defined scheme for combined verbose and quiet values.

