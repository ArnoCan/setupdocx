The builder 'sphinx' provides the extraction of inline API documentation
as reStructuredText modules, and the compilation into various final
representaion formats.

The tools are wrapped by the callers:

- bash:

  - call_apidoc.sh - sphinx-apidoc
  - call_doc.sh - sphinx-build

- python:

  - call_apidoc.py - sphinx-apidoc
  - call_doc.py - sphinx-build

