from __future__ import annotations

import subprocess
from typing import Protocol
from typing import Sequence


class Servicable(Protocol):
    """Implicit interface for something that can be stopped and started."""

    def start(self):
        """Start the services."""

    def stop(self):
        """Stop the services."""


class Spawnable(Protocol):
    """Implicit interface for something that can run a subprocess."""

    def spawn(self, args: Sequence[str], **kwargs) -> subprocess.CompletedProcess[str]:
        """Run the subprocess."""
