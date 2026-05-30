# The Mission schema — single source of truth

The entire FlyMax thesis is *"the same JSON flies in sim and on hardware."* That only
holds if there is exactly **one** definition of what a Mission is. Today there are
three hand-maintained copies, and they have already drifted. This document fixes the
direction of truth and the plan to enforce it.

## The one source of truth

**`flymax/missions/schema.py` (Pydantic) is canonical.** Everything else is derived.

Regenerate the canonical JSON Schema any time the Python models change:

```bash
flymax schema --out schema/mission.schema.json
```

This writes `schema/mission.schema.json` from `Mission.model_json_schema()`. That file
is the contract the web app and any other client must follow.

## The current drift (must be reconciled)

The Python schema and the site's TypeScript schema are **not just formatted
differently — they describe different shapes.** This is a real bug waiting to happen,
because a plan authored in one cannot be trusted by the other.

| Concept | `schema.py` (Python, canonical) | `flymax-site/lib/mission.ts` (TS) |
|---|---|---|
| Waypoint | `position: {x,y,z}`, `frame`, `yaw_deg`, `hold_s`, `speed_mps` | flat `{x, y, z, dwell_s?}` |
| Leg | `drone_ids: []`, `formation`, `timeout_s`, `on_failure` | `drone_id` (single), `speed_mps` |
| Safety | `max_altitude_m`, `geofence_min/max` (Vec3 box), `max_speed_mps`, `low_battery_pct`, `emergency_land_keyword` | `max_alt_m`, `min_alt_m`, `geofence_radius_m`, `rth_battery_pct` |
| Mission | `name`, `description`, `fleet`, `legs`, `safety`, `metadata` | `name`, `goal`, `drones`, `legs`, `safety`, `home` |

Until these are unified, "same JSON flies everywhere" is aspirational, not true.

## The reconciliation plan

1. **Decide the unified shape** (one design pass). Likely outcome: adopt the Python
   structure as canonical but add the site-only display fields (`color`, `home`,
   `goal`) as optional metadata, and a radius↔box geofence adapter for the sim.
2. **Generate the TS type from the schema**, don't hand-write it:
   ```bash
   npx json-schema-to-typescript schema/mission.schema.json -o flymax-site/lib/mission.gen.ts
   ```
3. **Gate drift in CI.** A GitHub Action runs `flymax schema`, regenerates the TS,
   and fails the build if either file is stale versus the committed schema. After
   this lands, Python/TS divergence can never silently return.
4. **Derive the Anthropic tool schema** (`lib/mission-tool.ts`) from the same JSON
   Schema so the planner and the validator are guaranteed to agree.

Done in this commit: step 0 — the canonical emitter (`export_json_schema()` + the
`flymax schema` command + `schema/mission.schema.json`). Steps 1–4 are the follow-on.
