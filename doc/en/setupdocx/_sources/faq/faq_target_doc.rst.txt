


Can I change the target name of a document?
-------------------------------------------
Use the parameter *--docname*.
This is a two step-approach, because the install_docx is here
designed for the literal installation of a document as a
blackbox only.
Else it may to have some more knowledge of the document structures,
which is already implemented in the builder module and their wrappers.

#. Use the parameter  *--docname* for *build_docx*::

      python setup.py build_docx --docname=my-other-name

   Creates an document within the build directory(--build-dir)::
   
      input_name = build/doc/<my-other-name>

#. Use the parameter  *--docname* for *install_docx*::

      python setup.py install_docx --docname=my-other-name

   Sets the input name::
   
      input_name = build/doc/<my-other-name>

   and the output name::
   
      output_name = <target-dir/doc/<my-other-name>

   See also --target-dir.

