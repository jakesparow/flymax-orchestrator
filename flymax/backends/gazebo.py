"""Gazebo Harmonic + ROS 2 Humble + crazyflie_simulation backend.

STUB. Full implementation lands when the simulator is set up end-to-end.
The shape is here so the orchestrator + CLI compile and route a `--backend gazebo` flag.
"""

from __future__ import annotations
from collections.abc import AsyncIterator

from ..missions import Mission, TelemetryEvent
from .base import Backend


class GazeboBackend(Backend):
    name = "gazebo"

    async def connect(self, mission: Mission) -> None:
        raise NotImplementedError(
            "Gazebo backend is not wired yet. See docs/setup-gazebo.md for the install path."
        )

    async def execute(self, mission: Mission) -> AsyncIterator[TelemetryEvent]:
        # silence type checker; never reached until connect() is implemented
        if False:
            yield TelemetryEvent(  # pragma: no cover
                drone_id="", timestamp=0.0, position=mission.fleet[0].id, battery_pct=0, state="idle"  # type: ignore
            )
        raise NotImplementedError

    async def emergency_land(self) -> None:
        raise NotImplementedError

    async def disconnect(self) -> None:
        return
