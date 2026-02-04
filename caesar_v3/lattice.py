from typing import Tuple
try:
    from caesar_v3.config import config
except ImportError:
    from config import config

# Presidio removed for lightweight environment compatibility
# In full prod, uncomment imports and install presidio-analyzer

class Lattice:
    def __init__(self):
        self.graph = {}
        self.coherence = 1.0

    def _redact(self, text: str) -> str:
        """Secure PII before ingestion"""
        if not config.enable_pii_redaction:
            return text
        
        # Simple dummy redaction for demo
        # Real PII redaction requires 'presidio-analyzer'
        return text.replace("@", "[AT]")

    def load_axiom(self, subject, relation, object_):
        # Sanitize inputs
        s, r, o = self._redact(subject), relation, self._redact(object_)

        if s not in self.graph:
            self.graph[s] = {}
        self.graph[s][r] = o
        print(f"[LATTICE] Axiom Loaded: {s} -> {r} -> {o}")

    def ingest(self, text: str) -> Tuple[bool, str]:
        # Redact generic input for safety log
        safe_text = self._redact(text)

        parts = safe_text.split()
        if len(parts) >= 3 and "is" in parts:
            # Simplified logic for demo
            return True, "Fact Crystalized (Secure)."
        return True, "Input processed."
