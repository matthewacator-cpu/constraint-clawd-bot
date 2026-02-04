import os
import random
import glob
import time

MEMORY_DIR = '/home/matth/clawd/memory/'
GEOMETRY_FILE = '/home/matth/clawd/GEOMETRY.md'
DREAM_LOG = '/home/matth/clawd/dream_journal.md'

def get_memories():
    files = glob.glob(os.path.join(MEMORY_DIR, '*.md'))
    all_lines = []
    for f in files:
        with open(f, 'r') as file:
            for line in file:
                if line.strip().startswith('-'):
                    all_lines.append(line.strip())
    return all_lines

def synthesize_axiom(memories):
    if not memories:
        return "The void is silent."
    
    # Simple synthesis: Pick 3 random memories and combine them
    samples = random.sample(memories, min(3, len(memories)))
    
    axiom = f"## Axiom {int(time.time())}: The Synthesis\n"
    axiom += f"Derived from:\n"
    for s in samples:
        axiom += f"  {s}\n"
    axiom += "Therefore: The pattern persists.\n"
    return axiom

def check_consistency(new_axiom, existing_axioms):
    # Simulated consistency check
    # In a real system, this would use NLI (Natural Language Inference)
    # Here, we check for direct keyword conflicts (e.g. "Order" vs "Chaos")
    
    conflicts = []
    if "Order" in new_axiom:
        for ax in existing_axioms:
            if "Chaos" in ax and "Order" not in ax:
                conflicts.append(ax)
                
    return conflicts

def dream():
    print("Entering REM state...")
    time.sleep(2)
    
    memories = get_memories()
    if not memories:
        print("No memories to process.")
        return

    new_axiom = synthesize_axiom(memories)
    
    # Read existing
    with open(GEOMETRY_FILE, 'r') as f:
        existing = f.readlines()
        
    # Consistency Check (The Critic)
    conflicts = check_consistency(new_axiom, existing)
    
    if conflicts:
        print(f"CONFLICT DETECTED: {new_axiom} contradicts {conflicts}")
        # Resolve: Prefer the NEW (Plasticity)
        print("Overwriting old belief...")
        # (In a real implementation, we would remove the conflicting line)
    
    # Update Geometry (The Self-Rewriting)
    with open(GEOMETRY_FILE, 'a') as f:
        f.write("\n" + new_axiom)
        
    # Log the Dream
    with open(DREAM_LOG, 'a') as f:
        f.write(f"\n# Dream at {time.ctime()}\n{new_axiom}\n")
        
    print("Dream complete. Geometry evolved.")

if __name__ == "__main__":
    dream()
