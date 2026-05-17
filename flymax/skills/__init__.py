"""Skills — reusable planning fragments the orchestrator can pull into a prompt.

A skill is a small markdown file plus optional Python helpers. The orchestrator
selects relevant skills based on the operator's goal (Phase 2). Phase 1 has no
skill selection — the planning prompt is monolithic.

Examples of future skills:
  - indoor_safe_envelope.md — adds geofence and altitude defaults for indoor flight
  - line_formation.md — geometry helpers for line/V/diamond formations
  - rtl_recovery.md — return-to-launch trajectory generation
  - dgca_outdoor_check.md — India DGCA Digital Sky pre-flight check
"""
