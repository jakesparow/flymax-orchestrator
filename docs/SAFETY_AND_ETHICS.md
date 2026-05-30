# Safety & Ethics

FlyMax controls things that fly near people and aggregates data about a sensitive,
dual-use technology. Two hard commitments govern everything: **machines must fail
safe**, and **the open data layer must not become a surveillance or targeting tool.**

This is a blueprint. Items marked *(planned)* are not yet implemented — they gate the
move from simulation to real hardware.

---

## Part 1 — Flight safety (host-side, never trust the LLM)

The reasoning model proposes; deterministic host code disposes. An LLM is allowed to
*draft* a plan. It is never the thing that keeps a drone inside the fence.

**Principles**
1. **Validate before arm.** Every plan passes pure-function guards before any backend
   connects. A failing guard means no motor spins. *(planned: `flymax/safety/guards.py`)*
2. **The guards do not call the model.** Geofence, altitude, speed, and abort checks
   are plain code with deterministic outputs. Reproducible, testable, auditable.
3. **ABORT is LLM-independent.** The operator's stop word triggers `emergency_land()`
   directly. A drone flying near a person cannot depend on a network round-trip to
   stop. *(planned)*
4. **Fail safe on loss.** Battery below threshold, link loss, or timeout each map to a
   declared per-leg fallback (`abort` / `rtl` / `land` / `hover`). *(partially planned)*
5. **Predict, don't just react.** Reject a leg whose *planned* path would exit the safe
   envelope, rather than only catching the breach after it happens. *(planned)*
6. **Tamper-evident logs.** Every decision and telemetry event is recorded in an
   append-only, hash-chained run log so any flight can be replayed and verified. *(planned)*

**Hardware rule (today):** real flight is indoor, netted, sub-250g (DGCA-exempt)
only, with a physical kill switch, until the software guards above are implemented and
tested and the operator is certified. See `CONTRIBUTING.md` → Hardware safety.

The adversarial test set (`tests/fixtures/unsafe/`) and the blocking safety CI gate are
tracked in the [100-task build plan](https://flymax.getmaxglobal.com/build), Step 2.

---

## Part 2 — Compliance

- **India / DGCA** is the first regulator: Digital Sky RED/YELLOW/GREEN airspace,
  NPNT-style permission artefacts, UIN + RPC operator identity. The plan: resolve a
  zone and bind operator identity *before* a motor arms; default-deny unknown zones.
  *(planned — build plan Step 3.)*
- **Remote ID / OpenDroneID** is the global identity-broadcast standard. We both
  *emit* it (our drones) and *ingest* it (the data network). Speaking it is the price
  of admission to world-level data.
- Every refusal must trace to a named regulation, never a guess (`docs/COMPLIANCE.md`,
  planned).

---

## Part 3 — Data ethics (the open map must not harm)

A public world map of flying machines — including defence and anti-drone categories —
is **dual-use**. It can inform, or it can surveil and target. We choose the first and
design against the second.

**Rules for the data network** (enforced in `flymax-site`, see `docs/DATA_NETWORK.md`):
1. **Opt-in for people.** Personal/hobby operators appear only if they choose to. A
   precise home location is never shown — location is coarsened to city level.
2. **Open feeds stay as their source intends.** Government/ADS-B/Remote-ID data is
   shown under its own terms and license; we don't relabel or re-sell it as ours.
3. **Sensitive categories are handled with restraint.** Defence/"war-drone" data, where
   shown at all, comes only from already-public official feeds, is clearly attributed,
   and is never enriched into targeting-grade intelligence. When in doubt, we don't
   publish.
4. **Consent and licensing are explicit.** Listing requires agreeing to clear terms; a
   public data license governs reuse; there is a documented takedown process.
5. **No impersonation, no fake verification.** A verified-operator badge is earned by a
   real DGCA artefact, never seeded.
6. **Abuse review before launch of any sensitive layer.** New public layers ship with a
   written "how could this be misused, and what stops it" note.

If a feature can't satisfy these, it doesn't ship. The trust this protects is the
entire moat — governments and citizens share data with a neutral party, not a weapon.
