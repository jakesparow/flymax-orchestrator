# FlyMax — Vision

> One sentence in. A formation flies. The goal is **maximum fly time for everyone** —
> make flying as ordinary, safe, and open as getting online.

FlyMax is not a drone company. The drones are the first *effectors*. What we are
building is the **open data, software, and community layer for the entire flying-
machine world** — consumer drones, commercial fleets, anti-drone systems, and
eventually eVTOL. The airframes are interchangeable. The brain, the data, and the
community are the moat.

This document is the north star. It is deliberately public: we want the world to
see where we are going and help us get there.

---

## The three rings

### Ring 1 — The open data flywheel (the foundation)
The single most valuable asset we can build is **neutral, open, world-level drone
data** that nobody else owns.

- A live world map of flying machines — **flat view and globe view** — fed by open
  government and aviation feeds (Remote ID / OpenDroneID, ADS-B, DGCA Digital Sky)
  plus *voluntary* operator listings.
- Anyone can watch. Operators who want visibility opt in; those who don't, don't.
- Categories the world can finally see in one place: consumer, commercial,
  survey/agri, public-safety, defence, anti-drone, and eVTOL.
- **Find-my-drone** — a privacy-preserving recovery service the official registries
  don't offer.
- A living **encyclopedia**: drone types, parts (with 3D part models), makers,
  history, every new startup in the space (incl. eVTOL), and the resources to learn
  it — auto-updated, not a dead wiki.

Data is the power. Visibility and market awareness follow from it.

### Ring 2 — The community & education ecosystem
Technology is only half of it. The other half is **people who fly, build, and teach.**

- Login → post, learn, and tag — closer to an educational forum than to ads.
- Every member gets real **value and a vault**: their profile, their drones, their
  flights, their certifications — something worth keeping.
- Help people get licensed; connect students and trainees to colleges, universities,
  and labs; help departments stand up their own drone labs.
- Partner with manufacturers, RPTOs, and institutions, step by step.
- The mission: **transform the world by empowering students and builders** — make
  everyone fly.

### Ring 3 — The product (money is the fuel, not the goal)
Open data and open software earn trust; a **closed, enterprise-grade edition** earns
revenue.

- **Open core (MIT):** the orchestrator (this repo) — the brain that turns a goal
  into a safe, typed flight plan and runs it on any backend.
- **Enterprise edition (closed):** fleet owners (e.g. DJI rental operators, survey
  teams) pay to manage, track live, audit, and recover their fleet — built on the
  same brain.
- Staged AI: Claude API today (bootstrapping), our own GPU/model only when scale
  justifies it. We do not build inference infrastructure prematurely.

---

## North star (vision, not roadmap)
Anti-drone & safety systems, helping developed and developing nations shape sane
drone policy, eVTOL, and — at the far horizon — flight beyond this planet. These are
the direction we point in, *not* dates we promise. Credibility comes from shipping
Ring 1 first.

## What makes us different
We are **neutral and open** where the incumbents are walled gardens. DJI, Auterion,
FlytBase, DroneDeploy and others own airframes, ground stations, or fleets. Nobody
owns the open, vendor-independent **data + orchestration + community** layer. That
neutrality is exactly why operators, institutions, and governments can trust us with
their data — and that trust is the network effect competitors can't buy.

## How we build
Sim before silicon. Open before closed. Safety host-side, never trusting the LLM.
Community value before monetization. One wedge at a time — see `docs/PRODUCT.md`
(the product + who pays) and the [100-task build plan](https://flymax.getmaxglobal.com/build).

> We make the non-believers look up.
