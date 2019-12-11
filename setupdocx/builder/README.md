Each subdirectory contains a specific 'builder', which represents
a specific tool-set. The tool-set represents the specific controller
of document creation process. The tool-set is hereby eventually
structured into multiple tools which provide parts of the supported
functionalty.

The current core tool-set is 'sphinx', which provides the required
parts of functionalities by the tools:

* sphinx-apidoc - extraction of inline documentation
* sphinx-build - compilation of the final documents

The required core functionality for the extraction of the API refrence
is here provided by the external tool-set:

* epydoc - extraction of structured and formalized API reference

Additional toolsets will be added stepwise.

The user can easily define it's own tool-sets which are scanned and
initialized automatically during the initialization.
