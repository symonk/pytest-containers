from typing import Protocol


class Servicable(Protocol):
    """Implicit interface for something that can be stopped and started."""

    def start(self):
        """Start the services."""

    def stop(self):
        """Stop the services."""


class Spawnable(Protocol):
    """Implicit interface for something that can run a subprocess."""

    def spawn(self):
        """Run the subprocess."""
