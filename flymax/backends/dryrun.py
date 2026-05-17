"""Dry-run backend — never opens any radio. Logs each waypoint as if it executed.

Useful for: unit tests, CI, walking a Claude-generated plan to confirm it parses,
demoing the orchestrator without any hardware or sim.
"""

from __future__ import annotations
import asyncio
import time
from collections.abc import AsyncIterator

from ..missions import Mission, TelemetryEvent, Vec3
from .base import Backend


class DryRunBackend(Backend):
    name = "dryrun"

    def __init__(self) -> None:
        self._connected: list[str] = []

    async def connect(self, mission: Mission) -> None:
        self._connected = [d.id for d in mission.fleet]

    async def execute(self, mission: Mission) -> AsyncIterator[TelemetryEvent]:
        for leg in mission.legs:
            for wp in leg.waypoints:
                for drone_id in leg.drone_ids:
                    yield TelemetryEvent(
                        drone_id=drone_id,
                        timestamp=time.time(),
                        position=Vec3(x=wp.position.x, y=wp.position.y, z=wp.position.z),
                        battery_pct=100.0,
                        state="flying",
                        message=f"dryrun waypoint at ({wp.position.x},{wp.position.y},{wp.position.z})",
                    )
                # honour hold_s in elapsed time only, lightly
                if wp.hold_s > 0:
                    await asyncio.sleep(min(wp.hold_s, 0.05))
        for drone_id in self._connected:
            yield TelemetryEvent(
                drone_id=drone_id,
                timestamp=time.time(),
                position=Vec3(x=0, y=0, z=0),
                battery_pct=100.0,
                state="landed",
                message="dryrun complete",
            )

    async def emergency_land(self) -> None:
        # nothing to land
        return

    async def disconnect(self) -> None:
        self._connected = []
