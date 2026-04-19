# constraint-clawd-bot

Constraint-native runtime components for Clawdbot, centered on energy, phase, and coherence-aware behavior.

## Overview

This repository packages a compact version of the GOLEM-style constraint system for use inside a Clawdbot workspace. Instead of treating every response as equally available, the system tracks internal state and uses that state to shape how the agent behaves over time.

It is designed as a portable subsystem for experiments in:

- bounded response generation
- phase-aware behavior
- coherence scoring
- lightweight self-regulation

## Core Components

- `vessel.py` manages energy, phase timing, and coherence updates.
- `dream.py` handles synthesis and reflective behavior.
- `GOLEM/golem.py` runs the core interaction loop.
- `GOLEM/energy.py` models energetic cost and recovery.
- `GOLEM/lattice.py` enforces structural coherence rules.
- `SOUL.md`, `AGENTS.md`, and `HEARTBEAT.md` define behavioral framing and operational guidance.

## Model

The runtime treats the agent as a constrained system with a few simple internal signals:

- energy determines how much output can be sustained
- phase determines whether the system is in a stable execution window
- coherence tracks whether new inputs preserve or degrade internal structure

These values are then used to shift the system into different behavioral states such as flowing, crystalline, turbulent, or depleted.

## Usage

1. Copy the repository contents into the target Clawdbot workspace.
2. Adjust any local file paths and identity files to match your environment.
3. Run the relevant entry point for your integration, or import the GOLEM modules into your existing bot runtime.
4. Let the heartbeat and vessel state drive ongoing calibration.

## Why It’s Useful

This repo is a good reference implementation for anyone exploring agent architectures that need more than prompt engineering alone. It demonstrates how simple runtime constraints can create noticeably different behavior without a large infrastructure footprint.

## Status

This is an experimental integration repo intended for advanced users and internal iteration. It is best viewed as a working prototype and architecture sample rather than a turnkey package.
