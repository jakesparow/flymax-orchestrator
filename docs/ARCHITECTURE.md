# Architecture

## Overview

```
   operator ──► CLI / web / voice
                    │
                    ▼
              Orchestrator
                    │
        ┌───────────┴───────────┐
        │ plan(goal) → Mission  │   ← Claude (sonnet) with mission schema
        │ fly(mission, backend) │
        └───────────┬───────────┘
                    │ Mission (typed JSON, pydantic-validated)
                    ▼
                 Backend (one of)
                    │
        ┌───────┬───┴───┬───────┐
        │       │       │       │
        ▼       ▼       ▼       ▼
      dryrun  gazebo crazyflie px4
       (now)  (P1)    (P2)    (P4)
```

## Why decompose into Mission JSON

Three reasons.

1. **Auditability.** Every flight is a typed artifact. We can store every plan, replay it, diff it, sign it.
2. **Backend portability.** The same JSON flies in sim or on hardware. The orchestrator never knows which.
3. **Safety guardrails.** Pydantic validation rejects bad plans BEFORE they reach a motor. The schema enforces altitude limits, geofence, speed caps, and a mandatory abort keyword.

## Threat model (early draft)

| Threat | Mitigation |
|---|---|
| LLM hallucinates an out-of-bounds waypoint | Pydantic + SafetyConstraints reject before backend ever sees it. |
| Operator types ABORT | Backend honours `emergency_land_keyword` regardless of mission state. |
| Network loss mid-flight | `Leg.on_failure` defines per-leg fallback (rtl / land / hover / abort). Default `rtl`. |
| Drone hits low battery | Backend monitors `battery_pct`; below `safety.low_battery_pct` it auto-RTLs. |
| Two operators issue conflicting commands | Only one orchestrator instance per fleet. Web UI (later) serialises operator input. |

## Why this is dual-use with our SaaS agent fleet

The exact same primitives (dispatch a typed task to a worker, watch a kanban, nudge on completion, log every decision) show up in our healthcare RCM agent fleet ([getmaxglobal.com](https://getmaxglobal.com)). Different effectors, same orchestration brain. We build it once, evolve it together, and the FlyMax repo is the public open-source proof of the pattern.

## Phase ladder

- **Phase 0** (now) — repo skeleton, mission schema, dryrun backend, smoke test.
- **Phase 1** — Gazebo + ROS 2 + crazyflie_simulation. 1-drone 4-waypoint mission flies in sim. ~30 days.
- **Phase 2** — Real Crazyflie 2.1+ with cflib. Same JSON, swap backend. ~60 days from start.
- **Phase 3** — 2-drone formation, ESP32-CAM visual trigger, first public demo video. ~90 days.
- **Phase 4** — PX4 / Pixhawk outdoor. DGCA Digital Sky compliance. Q4 2026.
- **Phase 5+** — Foundation-model-conditioned policies (π0 / GR00T-style). 2027.

## Open questions (for early contributors)

1. Should `Mission` be content-addressable (hash → store) so plans are inherently audit-stable?
2. Do we go full ROS 2 for everything, or keep cflib direct for Crazyflie (no ROS overhead) and ROS 2 for PX4?
3. How do we expose the orchestrator's reasoning trail (the Claude tool calls) without bloating the audit log?

Open issues and PRs welcome.
