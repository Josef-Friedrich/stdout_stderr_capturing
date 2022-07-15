stdout_stderr_capturing
=======================

Capture the stdout or stderr output as a list in a context manager block (with).

Maybe better alternatives:

* https://capturer.readthedocs.io/en/latest/
* https://github.com/bskinn/stdio-mgr
* https://github.com/minrk/wurlitzer
* https://pypi.org/project/OutputCatcher/0.0.9/#files

Capture stdout:

.. code:: python

    with Capturing() as output:
        print('line 1')

    print(output[0])

is equivalent to

.. code:: python

    with Capturing(stream='stdout') as output:
        print('line 1')

Capture stderr:

.. code:: python

    with Capturing(stream='stderr') as output:
        print('line 1', file=sys.stderr)
