# Contributing

Pre-alpha. The author is still finding the shape. Three things help most right now:

1. **Run the smoke test.** `pip install -e ".[dev]"` then `pytest`. If it fails on your platform, open an issue with the traceback.
2. **Critique the Mission schema.** `flymax/missions/schema.py`. The whole repo's safety guarantee leans on this. If you see a hole, open an issue.
3. **Implement a backend.** Gazebo and Crazyflie are both `NotImplementedError` stubs. Either one merged would unblock real flight.

## Local dev

```bash
git clone <your-fork>
cd flymax-orchestrator
python -m venv .venv && source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -e ".[dev]"
pytest
```

## Style

- `black` formats. `ruff` lints. `mypy` strict on the way (not yet).
- Type hints required on every public function.
- Pydantic models for every cross-module data structure.
- No silent fallbacks: if the orchestrator can't plan safely, it returns an empty-legs Mission with `metadata.refusal_reason`.

## Safety

If you're contributing flight code: assume an operator's drone is one bug away from a wall. Default to RTL on any uncertainty. The repo's CI will reject PRs that weaken `SafetyConstraints` without an explicit issue link explaining why.

## License

MIT. See [LICENSE](LICENSE). Contributors agree their contributions are MIT.
