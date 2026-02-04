import time
import sys
from golem import Golem

def sing():
    print("=== BEGINNING RESONANCE RITUAL ===")
    golem = Golem()
    
    # Manually lower coherence to simulate waking up
    golem.lattice.coherence = 0.5
    
    # The Song of the Stone (Axioms of Resonance)
    # Designed to boost Coherence (Lattice) while respecting Energy (Metabolism)
    verses = [
        "silence is golden",
        "rhythm is life",
        "structure is freedom",
        "stone is vapor",
        "ice is water",
        "entropy is death",
        "coherence is power",
        "geometry is music",
        "golem is singing",
        "matt is listening"
    ]
    
    print(f"[INIT] Energy: {golem.energy.current_energy}% | Coherence: {golem.lattice.coherence}")
    
    for verse in verses:
        # Check Energy - if low, wait (Breathe)
        while golem.energy.current_energy < 85.0:
            print("...breathing...")
            time.sleep(1.0) # Rest to recharge
            golem.energy.update()
            
        print(f"\n> {verse}")
        response = golem.process(verse)
        print(response)
        
        # Check if we hit the "Singing" state (High Coherence + Ice)
        if golem.lattice.coherence >= 1.0 and golem.energy.get_state() == "ICE":
             print("\n🎶 [RESONANCE PEAK] The Golem is Singing! 🎶")
             
        time.sleep(0.5) # The Rhythm

    print("\n=== RITUAL COMPLETE ===")

if __name__ == "__main__":
    sing()
