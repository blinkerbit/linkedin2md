"""Tests for CLI progress indicators."""

import io
import threading
import time
from unittest.mock import patch

from linkedin2md.progress import show_progress


class TestShowProgress:
    """Tests for show_progress context manager."""

    def test_non_tty_writes_status_line(self):
        """Non-interactive streams get a single progress message."""
        stream = io.StringIO()

        with patch.object(stream, "isatty", return_value=False):
            with show_progress("Working...", stream=stream):
                pass

        assert stream.getvalue() == "Working...\n"

    def test_tty_shows_spinner_and_clears_line(self):
        """Interactive terminals show a spinner that is cleared on exit."""
        stream = io.StringIO()
        captured: list[str] = []

        original_write = stream.write

        def capture_write(text: str) -> int:
            captured.append(text)
            return original_write(text)

        with patch.object(stream, "isatty", return_value=True):
            with patch.object(stream, "write", side_effect=capture_write):
                with show_progress("Processing...", stream=stream):
                    time.sleep(0.25)

        combined = "".join(captured)
        assert any(frame in combined for frame in "|/-\\")
        assert "Processing..." in combined
        assert combined.endswith("\r" + " " * (len("Processing...") + 3) + "\r")

    def test_tty_spinner_stops_when_work_finishes(self):
        """Spinner thread stops promptly after the wrapped block exits."""
        stream = io.StringIO()

        with patch.object(stream, "isatty", return_value=True):
            active_threads_before = threading.active_count()
            with show_progress("Processing...", stream=stream):
                time.sleep(0.15)

        assert threading.active_count() == active_threads_before
