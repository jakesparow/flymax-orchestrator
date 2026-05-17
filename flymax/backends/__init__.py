"""Backend implementations — pluggable via mission.metadata or CLI --backend flag."""

from .base import Backend

__all__ = ["Backend", "get_backend"]


def get_backend(name: str) -> Backend:
    """Resolve a backend by name. Lazy-imports the implementation."""
    name = name.lower()
    if name == "gazebo":
        from .gazebo import GazeboBackend
        return GazeboBackend()
    if name == "crazyflie":
        from .crazyflie import CrazyflieBackend
        return CrazyflieBackend()
    if name == "dryrun":
        from .dryrun import DryRunBackend
        return DryRunBackend()
    raise ValueError(f"Unknown backend: {name!r}. Try 'gazebo', 'crazyflie', or 'dryrun'.")
