import sys

import pytest
from capturer import CaptureOutput
from termcolor import cprint


@pytest.mark.skip("Fails on Github actions.")
class TestCapturer:
    def test_capturer(self) -> None:
        with CaptureOutput() as capturer:
            print("line 1")
            print("line 2")
        assert capturer.output.get_lines() == ["line 1", "line 2"]

    def test_capturer_stderr(self) -> None:
        with CaptureOutput(merged=False) as capturer:
            print("stderr", file=sys.stderr)
            print("stdout")

        assert capturer.stdout.get_text() == "stdout"
        assert capturer.stderr.get_text() == "stderr"

    def test_capturer_ansi(self) -> None:
        with CaptureOutput() as capturer:
            cprint("line 1", color="red")
        assert capturer.output.get_text() == "\x1b[31mline 1\x1b[0m"
