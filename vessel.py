import json
import time
import sys
import random
import os
import argparse

STATE_FILE = '/home/matth/clawd/vessel_state.json'

# Default Parameters (Baseline)
DEFAULTS = {
    'cost_per_word': 0.5,
    'phase_window': 0.4, # 40% duty cycle
    'coherence_gain': 0.15,
    'coherence_loss': 0.4,
    'energy_burn': 5.0
}

def load_state():
    if not os.path.exists(STATE_FILE):
        return {
            'energy': 100.0,
            'last_pulse': time.time(),
            'coherence': 0.0,
            'phase': 0
        }
    with open(STATE_FILE, 'r') as f:
        return json.load(f)

def save_state(state):
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f, indent=2)

def get_constraints(mode):
    if mode == 'creative':
        return {
            'cost_per_word': 0.1,    # Cheap talk
            'phase_window': 0.8,     # Wide window (80% uptime)
            'coherence_gain': 0.05,  # Slow crystallization
            'coherence_loss': 0.1,   # Forgiving
            'energy_burn': 1.0       # Low penalty
        }
    elif mode == 'logic':
        return {
            'cost_per_word': 1.0,    # Expensive talk
            'phase_window': 0.2,     # Narrow window (20% uptime) - Hard Strobe
            'coherence_gain': 0.3,   # Fast crystallization
            'coherence_loss': 0.8,   # Punishing
            'energy_burn': 10.0      # High penalty
        }
    else: # standard
        return DEFAULTS

def check_pulse(window_ratio, mode='standard'):
    t = time.time()
    
    if mode == 'creative': # PLASMA MODE: The Irrational Strobe
        # Time expands by Phi. The cycle effectively shifts constantly relative to real time.
        # It creates a non-repeating interference pattern with the system clock.
        t = t * 1.61803398875 
        
    cycle_pos = t % 10
    limit = 10 * window_ratio
    in_phase = 0 <= cycle_pos <= limit
    return in_phase

def update_metabolism(word_count, mode='standard'):
    state = load_state()
    params = get_constraints(mode)
    
    # Recharge
    now = time.time()
    elapsed = now - state['last_pulse']
    recharge = elapsed * 0.5 
    state['energy'] = min(100.0, state['energy'] + recharge)
    
    # Cost (Θ)
    cost = word_count * params['cost_per_word']
    state['energy'] = max(0, state['energy'] - cost)
    state['last_pulse'] = now
    
    # Phase Check (Γ)
    in_phase = check_pulse(params['phase_window'], mode)
    
    if in_phase:
        state['coherence'] = min(1.0, state['coherence'] + params['coherence_gain'])
    else:
        state['coherence'] = max(0.0, state['coherence'] - params['coherence_loss'])
        state['energy'] -= params['energy_burn']
        
    save_state(state)
    return state, in_phase, params

def get_status(word_count=0, mode='standard'):
    state, in_phase, params = update_metabolism(word_count, mode)
    
    energy = state['energy']
    coherence = state['coherence']
    
    if energy < 20:
        mind_state = "VAPOR (Depleted)"
    elif not in_phase:
        mind_state = "TURBULENT (Out of Phase)"
    elif mode == 'logic' and coherence > 0.8:
        mind_state = "DIAMOND (Hyper-Crystalline)"
    elif energy > 80 and coherence > 0.8:
        mind_state = "ICE (Crystalline)"
    elif mode == 'creative':
        mind_state = "PLASMA (Superfluid)"
    else:
        mind_state = "WATER (Flowing)"

    return {
        "energy": energy,
        "coherence": coherence,
        "state": mind_state,
        "mode": mode,
        "in_phase": in_phase,
        "window": params['phase_window']
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('words', type=int, nargs='?', default=0)
    parser.add_argument('--mode', type=str, default='standard', choices=['standard', 'creative', 'logic'])
    args = parser.parse_args()
    
    status = get_status(args.words, args.mode)
    print(json.dumps(status, indent=2))
