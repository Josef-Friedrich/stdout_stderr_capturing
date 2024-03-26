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

With Python 3:

.. code:: python

    from io import StringIO
    from contextlib import redirect_stdout, redirect_stderr

    stdout = StringIO()
    stderr = StringIO()
    with redirect_stdout(stdout), redirect_stderr(stderr):
        print('Test')
        stdout.getvalue()
        stderr.getvalue()

Using `pytest <https://docs.pytest.org/en/latest/how-to/capture-stdout-stderr.html#accessing-captured-output-from-a-test-function>`_

.. code:: python

    def test_myoutput(capsys):  # or use "capfd" for fd-level
        print("hello")
        sys.stderr.write("world\n")
        captured = capsys.readouterr()
        assert captured.out == "hello\n"
        assert captured.err == "world\n"
        print("next")
        captured = capsys.readouterr()
        assert captured.out == "next\n"

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
