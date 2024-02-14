import sys

from termcolor import cprint

from stdout_stderr_capturing import Capturing


class TestCapturing:
    def test_stdout(self) -> None:
        with Capturing() as output:
            print("line 1")
            print("line 2")
        assert output == ["line 1", "line 2"]

    def test_method_tostring(self) -> None:
        with Capturing() as output:
            print("line 1")
        assert output.tostring() == "line 1"

    def test_argument_stream_stdout_with_stdout(self) -> None:
        with Capturing(stream="stdout") as output:
            print("line 1")
        assert output == ["line 1"]

    def test_argument_stream_stdout_with_stderr(self) -> None:
        with Capturing(stream="stdout") as output:
            print("line 1", file=sys.stderr)
        assert output == []

    def test_argument_stream_stderr_with_stdout(self) -> None:
        with Capturing(stream="stderr") as output:
            print("line 1")
        assert output == []

    def test_argument_stream_stderr_with_stderr(self) -> None:
        with Capturing(stream="stderr") as output:
            print("line 1", file=sys.stderr)
        assert output == ["line 1"]

    def test_argument_clean_ansi_true(self) -> None:
        with Capturing(clean_ansi=True) as output:
            cprint("line 1", color="red")
        assert output == ["line 1"]

    def test_argument_clean_ansi_false(self) -> None:
        with Capturing(clean_ansi=False) as output:
            cprint("line 1", color="red")
        assert "line 1" in output[0]
