.. image:: http://img.shields.io/pypi/v/stdout-stderr-capturing.svg
    :target: https://pypi.org/project/stdout-stderr-capturing
    :alt: This package on the Python Package Index

.. image:: https://github.com/Josef-Friedrich/stdout_stderr_capturing/actions/workflows/tests.yml/badge.svg
    :target: https://github.com/Josef-Friedrich/stdout_stderr_capturing/actions/workflows/tests.yml
    :alt: Tests

stdout_stderr_capturing
=======================

Capture the stdout or stderr output as a list in a context manager block (with).

Maybe better alternatives:

* `capturer <https://pypi.org/project/capturer>`_ https://github.com/xolox/python-capturer
* `stdio-mgr <https://pypi.org/project/stdio-mgr>`_
* `OutputCatcher <https://pypi.org/project/OutputCatcher>`_
* `wurlitzer <https://pypi.org/project/wurlitzer>`_

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
