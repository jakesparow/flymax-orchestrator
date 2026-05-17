"""Real Crazyflie 2.1+ backend via cflib (bitcraze/crazyflie-lib-python).

STUB. Lands when Crazyflies arrive (Phase 2).
"""

from __future__ import annotations
from collections.abc import AsyncIterator

from ..missions import Mission, TelemetryEvent
from .base import Backend


class CrazyflieBackend(Backend):
    name = "crazyflie"

    async def connect(self, mission: Mission) -> None:
        raise NotImplementedError(
            "Crazyflie backend is not wired yet. Phase 2 — needs hardware "
            "(Crazyflie 2.1+ Getting Started Bundle from MG Super Labs India)."
        )

    async def execute(self, mission: Mission) -> AsyncIterator[TelemetryEvent]:
        if False:
            yield TelemetryEvent(  # pragma: no cover
                drone_id="", timestamp=0.0, position=mission.fleet[0].id, battery_pct=0, state="idle"  # type: ignore
            )
        raise NotImplementedError

    async def emergency_land(self) -> None:
        raise NotImplementedError

    async def disconnect(self) -> None:
        return
