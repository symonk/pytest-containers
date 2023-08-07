from typing import Protocol


class Servicable(Protocol):
    """Implicit interface for something that can be stopped and started."""

    def start(self):
        """Start the services."""

    def stop(self):
        """Stop the services."""


class Runnable(Protocol):
    """Implicit interface for something that can run a subprocess."""

    def run(self):
        """Run the subprocess."""
