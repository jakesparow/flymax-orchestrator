"""Smoke tests — the mission schema parses the example, the dryrun backend runs it."""

from __future__ import annotations
import asyncio
from pathlib import Path

import pytest

from flymax.backends import get_backend
from flymax.missions import Mission
from flymax.orchestrator import load_mission


EXAMPLE = Path(__file__).parent.parent / "examples" / "two_drone_patrol.json"


def test_example_mission_loads() -> None:
    m = load_mission(EXAMPLE)
    assert isinstance(m, Mission)
    assert m.name == "two-drone-indoor-patrol"
    assert len(m.fleet) == 2
    assert len(m.legs) == 1
    assert len(m.legs[0].waypoints) == 5


def test_dryrun_backend_streams_events() -> None:
    m = load_mission(EXAMPLE)
    backend = get_backend("dryrun")

    async def run() -> list:
        events = []
        await backend.connect(m)
        async for ev in backend.execute(m):
            events.append(ev)
        await backend.disconnect()
        return events

    events = asyncio.run(run())
    # Each of 5 waypoints emitted for 2 drones = 10 flying events, plus 2 landed terminals
    assert len(events) == 12
    assert events[-1].state == "landed"
    assert events[-2].state == "landed"


def test_safety_constraints_have_defaults() -> None:
    m = load_mission(EXAMPLE)
    assert m.safety.max_altitude_m == 2.0
    assert m.safety.emergency_land_keyword == "ABORT"


def test_unknown_backend_raises() -> None:
    with pytest.raises(ValueError):
        get_backend("unobtanium")
