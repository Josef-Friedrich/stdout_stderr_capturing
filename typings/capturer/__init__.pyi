from _typeshed import Incomplete

DEFAULT_TEXT_ENCODING: str
GRACEFUL_SHUTDOWN_SIGNAL: Incomplete
TERMINATION_DELAY: float
PARTIAL_DEFAULT: bool
STDOUT_FD: int
STDERR_FD: int

def enable_old_api() -> None: ...
def create_proxy_method(name): ...

class MultiProcessHelper:
    processes: Incomplete
    def __init__(self) -> None: ...
    def start_child(self, target) -> None: ...
    def stop_children(self) -> None: ...
    def wait_for_children(self) -> None: ...
    def enable_graceful_shutdown(self) -> None: ...
    def raise_shutdown_request(self, signum, frame) -> None: ...

class CaptureOutput(MultiProcessHelper):
    chunk_size: Incomplete
    encoding: Incomplete
    merged: Incomplete
    relay: Incomplete
    termination_delay: Incomplete
    pseudo_terminals: Incomplete
    streams: Incomplete
    stdout_stream: Stream
    stderr_stream: Stream
    def __init__(
        self,
        merged: bool = ...,
        encoding=...,
        termination_delay=...,
        chunk_size: int = ...,
        relay: bool = ...,
    ) -> None: ...
    def initialize_stream(self, file_obj, expected_fd): ...
    def __enter__(self) -> CaptureOutput: ...
    def __exit__(
        self,
        exc_type: Incomplete | None = ...,
        exc_value: Incomplete | None = ...,
        traceback: Incomplete | None = ...,
    ) -> None: ...
    @property
    def is_capturing(self): ...
    output: PseudoTerminal
    output_queue: Incomplete
    stdout: PseudoTerminal
    stderr: PseudoTerminal
    def start_capture(self) -> None: ...
    def finish_capture(self) -> None: ...
    def allocate_pty(
        self,
        relay_fd: Incomplete | None = ...,
        output_queue: Incomplete | None = ...,
        queue_token: Incomplete | None = ...,
    ): ...
    def merge_loop(self, started_event) -> None: ...

class OutputBuffer:
    fd: Incomplete
    buffer: bytes
    def __init__(self, fd) -> None: ...
    def add(self, output) -> None: ...
    def flush(self) -> None: ...

class PseudoTerminal(MultiProcessHelper):
    encoding: Incomplete
    termination_delay: Incomplete
    chunk_size: Incomplete
    relay_fd: Incomplete
    output_queue: Incomplete
    queue_token: Incomplete
    streams: Incomplete
    output_handle: Incomplete
    def __init__(
        self,
        encoding,
        termination_delay,
        chunk_size,
        relay_fd,
        output_queue,
        queue_token,
    ) -> None: ...
    def attach(self, stream) -> None: ...
    def start_capture(self) -> None: ...
    def finish_capture(self) -> None: ...
    def close_pseudo_terminal(self) -> None: ...
    def restore_streams(self) -> None: ...
    def get_handle(self, partial=...): ...
    def get_bytes(self, partial=...): ...
    def get_lines(self, interpreted: bool = ..., partial: bool = ...) -> list[str]: ...
    def get_text(self, interpreted: bool = ..., partial: bool = ...) -> str: ...
    def save_to_handle(self, handle, partial=...) -> None: ...
    def save_to_path(self, filename, partial=...) -> None: ...
    def capture_loop(self, started_event) -> None: ...

class Stream:
    fd: Incomplete
    original_fd: Incomplete
    is_redirected: bool
    def __init__(self, fd) -> None: ...
    def redirect(self, target_fd) -> None: ...
    def restore(self) -> None: ...

class ShutdownRequested(Exception): ...
