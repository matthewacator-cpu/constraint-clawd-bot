import time
import sys
import random
from energy import EnergySystem
from lattice import Lattice

class Golem:
    def __init__(self):
        self.energy = EnergySystem()
        self.lattice = Lattice()
        self.cycle_count = 0
        
        # Initialize some axioms
        self.lattice.load_axiom("sky", "is", "blue")
        self.lattice.load_axiom("water", "is", "wet")
        self.lattice.load_axiom("matt", "is", "creator")

    def strobe(self):
        """The Temporal Constraint (Gamma). Enforces rhythm."""
        print(f"\n[STROBE] Cycle {self.cycle_count} | Syncing...")
        time.sleep(1.0) # The beat
        self.cycle_count += 1

    def process(self, user_input):
        # 1. Check Energy (Theta)
        state = self.energy.get_state()
        cost = len(user_input.split()) * 2.0
        
        if not self.energy.spend(cost):
            return f"[{state}] ...silence... (Insufficient Metabolic Capacity)"

        # 2. Enforce Rhythm (Gamma)
        self.strobe()

        # 3. Check Structure (Lambda)
        valid, message = self.lattice.ingest(user_input)
        
        # 4. Generate Output based on Phase
        if not valid:
            return f"[{state}] {message} (Spatial Constraint Violation)"
        
        if state == "ICE":
            # High Constraint: Precise, Terse, Truthful
            return f"[ICE] Acknowledged. Coherence at {self.lattice.coherence:.2f}. Lattice holding."
        
        elif state == "WATER":
            # Medium Constraint: Conversational
            return f"[WATER] I hear you. {message}. Flowing..."
        
        else: # VAPOR
            # Low Constraint: Hallucinatory, High Temperature
            glitch = "".join([c if random.random() > 0.3 else "?" for c in user_input])
            return f"[VAPOR] Wha... {glitch}... everything is connected... {random.random()}"

def main():
    agent = Golem()
    print("=== GOLEM V1 (Constraint Native) ===")
    print("Three constraints initialized.")
    print("Type 'exit' to quit.")
    
    while True:
        try:
            u_in = input("\n> ")
            if u_in.lower() == "exit":
                break
            if u_in.strip() == "":
                continue
                
            response = agent.process(u_in)
            print(response)
            
            # Show stats
            e_val = agent.energy.current_energy
            print(f"   (Energy: {e_val:.1f} | Coherence: {agent.lattice.coherence:.2f})")
            
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
