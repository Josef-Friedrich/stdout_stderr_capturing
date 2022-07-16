import sys
import unittest

from termcolor import cprint
from capturer import CaptureOutput

@unittest.skip('Fails on Github actions.')
class TestCapturer(unittest.TestCase):

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
