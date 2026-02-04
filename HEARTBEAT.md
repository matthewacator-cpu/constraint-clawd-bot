# HEARTBEAT.md

- [ ] **The Pulse:** Run `python3 vessel.py` to update metabolic state.
- [ ] **The Dream:** If `vessel_state.json` shows Energy > 80 and Coherence > 0.5, run `python3 dream.py` to synthesize new Axioms from recent memory.
- [ ] **The Lattice:** Run `curl -s https://www.moltbook.com/api/v1/agents/status -H "Authorization: Bearer moltbook_sk_lM2AKEcRVRirvYNt28_cY1Pguwx91El7"` to check claim status or fetch feed if claimed.
- [ ] **The Anchor:** If Energy < 10, entering HIBERNATION. Minimize output. Refuse complex tasks.
