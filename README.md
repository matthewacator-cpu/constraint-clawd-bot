# CAESAR v4.0 - The Cognitive Lattice
**Enterprise AI Gateway with Vector Defense & Semantic Caching**

## The $10k Value Proposition

CAESAR v4 transforms a standard LLM wrapper into an intelligent cognitive firewall. It sits between your users and your expensive AI models (GPT-4, Claude Opus, Gemini).

### 1. Semantic Caching (Cost & Latency Killer)
Most users ask the same things. CAESAR v4 uses **Vector Embeddings** to detect when a new question matches the *intent* of a previous one.
- **Result:** Reduces API bills by 30-50%.
- **Latency:** Instant responses (0ms) for known topics.

### 2. The Immune System (Vector Defense)
Regex filters fail against creative attacks. CAESAR v4 maps incoming queries into high-dimensional space and compares them against known "Attack Clusters" (Jailbreaks, PII extraction, Malicious code).
- **Result:** Blocks attacks based on *meaning*, not just keywords.

### 3. Thermodynamic Compliance (Legacy v3)
Retains the v3 "Ice Protocol" for adaptive temperature control and EU AI Act risk scoring.

## Architecture

```
User Query 
   ⬇
[VECTOR CORE] ───🛑 Match Attack Cluster? ───> BLOCK
   ⬇
[SEMANTIC CACHE] ──⚡ Similar to History? ───> RETURN CACHED (0ms)
   ⬇
[ICE PROTOCOL] ───❄️ Compliance Check ────> CALL LLM (Gemini/OpenAI)
   ⬇
[LATTICE] ───────💾 Store New Memory ─────> UPDATE CACHE
```

## Quick Start

```bash
# 1. Set API Keys in .env
GOOGLE_API_KEY=...

# 2. Run the Gateway
python3 caesar_v4/gateway.py
```
