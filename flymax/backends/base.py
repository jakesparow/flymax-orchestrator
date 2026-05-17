"""Backend abstract base — every concrete backend (Gazebo, Crazyflie, PX4) implements this."""

from __future__ import annotations
from abc import ABC, abstractmethod
from collections.abc import AsyncIterator

from ..missions import Mission, TelemetryEvent


class Backend(ABC):
    """Abstract drone-fleet executor.

    The orchestrator hands a Mission to a Backend. The Backend is responsible for:
      - connecting to the drones (real or simulated),
      - executing each Leg in sequence,
      - enforcing the Mission.safety constraints,
      - streaming TelemetryEvents back.
    """

    name: str = "abstract"

    @abstractmethod
    async def connect(self, mission: Mission) -> None:
        """Establish radio/SITL/MAVLink links to every drone in mission.fleet."""

    @abstractmethod
    async def execute(self, mission: Mission) -> AsyncIterator[TelemetryEvent]:
        """Execute the mission. Yields a stream of TelemetryEvents until completion or abort."""

    @abstractmethod
    async def emergency_land(self) -> None:
        """Immediately land every connected drone. Operator-triggered hard stop."""

    @abstractmethod
    async def disconnect(self) -> None:
        """Cleanly close links."""
