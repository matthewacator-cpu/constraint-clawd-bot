import json

class Lattice:
    def __init__(self):
        # The World Model. A simple Graph: {Subject: {Relation: Object}}
        self.graph = {}
        # Coherence Score (0.0 to 1.0)
        self.coherence = 1.0

    def load_axiom(self, subject, relation, object_):
        if subject not in self.graph:
            self.graph[subject] = {}
        self.graph[subject][relation] = object_
        print(f"[LATTICE] Axiom Loaded: {subject} -> {relation} -> {object_}")

    def check_consistency(self, subject, relation, object_):
        # If we know X is Y, and input says X is NOT Y, reject.
        # Simplistic logic for prototype
        if subject in self.graph:
            if relation in self.graph[subject]:
                known_object = self.graph[subject][relation]
                if known_object != object_:
                    return False, f"Conflict: Known ({subject} {relation} {known_object}) vs Input ({object_})"
        return True, "Consistent"

    def ingest(self, text):
        # A real implementation would parse S-V-O here.
        # For prototype, we just look for simple commands like "A is B"
        parts = text.split()
        if len(parts) == 3 and parts[1] == "is":
            sub, rel, obj = parts[0], parts[1], parts[2]
            is_consistent, msg = self.check_consistency(sub, rel, obj)
            
            if is_consistent:
                self.load_axiom(sub, rel, obj)
                self.coherence = min(1.0, self.coherence + 0.05)
                return True, "Fact Crystalized."
            else:
                self.coherence = max(0.0, self.coherence - 0.1)
                return False, f"REJECTED: {msg}"
        return True, "Input processed (No structural change)."
