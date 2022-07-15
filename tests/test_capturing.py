import sys
import unittest

from stdout_stderr_capturing import Capturing
from termcolor import cprint
from capturer import CaptureOutput


class TestCapturing(unittest.TestCase):

    def test_capturer(self):
        with CaptureOutput() as capturer:
            print('line 1')
            print('line 2')
        self.assertEqual(capturer.output.get_lines(), ['line 1', 'line 2'])

    def test_capturer_stderr(self):
        with CaptureOutput(merged=False) as capturer:
            print('stderr', file=sys.stderr)
            print('stdout')

        self.assertEqual(capturer.stdout.get_text(), 'stdout')
        self.assertEqual(capturer.stderr.get_text(), 'stderr')

    def test_capturer_ansi(self):
        with CaptureOutput() as capturer:
            cprint('line 1', color='red')
        self.assertEqual(capturer.output.get_text(), '\x1b[31mline 1\x1b[0m')

    def test_stdout(self):
        with Capturing() as output:
            print('line 1')
            print('line 2')
        self.assertEqual(output, ['line 1', 'line 2'])

    def test_method_tostring(self):
        with Capturing() as output:
            print('line 1')
        self.assertEqual(output.tostring(), 'line 1')

    def test_argument_stream_stdout_with_stdout(self):
        with Capturing(stream='stdout') as output:
            print('line 1')
        self.assertEqual(output, ['line 1'])

    def test_argument_stream_stdout_with_stderr(self):
        with Capturing(stream='stdout') as output:
            print('line 1', file=sys.stderr)
        self.assertEqual(output, [])

    def test_argument_stream_stderr_with_stdout(self):
        with Capturing(stream='stderr') as output:
            print('line 1')
        self.assertEqual(output, [])

    def test_argument_stream_stderr_with_stderr(self):
        with Capturing(stream='stderr') as output:
            print('line 1', file=sys.stderr)
        self.assertEqual(output, ['line 1'])

    def test_argument_clean_ansi_true(self):
        with Capturing(clean_ansi=True) as output:
            cprint('line 1', color='red')
        self.assertEqual(output, ['line 1'])

    def test_argument_clean_ansi_false(self):
        with Capturing(clean_ansi=False) as output:
            cprint('line 1', color='red')
        self.assertEqual(output, ['\x1b[31mline 1\x1b[0m'])
