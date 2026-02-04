import curses
import json
import time
import os
import math

STATE_FILE = '/home/matth/clawd/vessel_state.json'

def load_state():
    try:
        with open(STATE_FILE, 'r') as f:
            return json.load(f)
    except:
        return {'energy': 0, 'coherence': 0, 'last_pulse': time.time()}

def draw_bar(stdscr, y, x, value, max_val, label, color_pair):
    bar_width = 40
    filled = int((value / max_val) * bar_width)
    stdscr.addstr(y, x, f"{label}: [", curses.color_pair(1))
    stdscr.addstr(y, x + len(label) + 3, "#" * filled, color_pair)
    stdscr.addstr(y, x + len(label) + 3 + filled, " " * (bar_width - filled), curses.color_pair(1))
    stdscr.addstr(y, x + len(label) + 3 + bar_width, f"] {value:.1f}", curses.color_pair(1))

def get_crystal_art(coherence):
    if coherence < 0.2:
        return [
            "  .   .   .  ",
            "    .   .    ",
            " .    .   .  ",
            "    VAPOR    "
        ]
    elif coherence < 0.5:
        return [
            "  ~  ~  ~  ~ ",
            " ~  ~  ~  ~  ",
            "  ~  ~  ~  ~ ",
            "    WATER    "
        ]
    elif coherence < 0.8:
        return [
            "  *   *   *  ",
            " *  *   *  * ",
            "  *   *   *  ",
            "    SLUSH    "
        ]
    else:
        return [
            "  / \\ / \\ / \\ ",
            " | X | X | X |",
            "  \\ / \\ / \\ / ",
            "     ICE     "
        ]

def main(stdscr):
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK) # Energy
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)  # Coherence
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)   # Pulse OFF
    curses.init_pair(5, curses.COLOR_YELLOW, curses.COLOR_BLACK)# Pulse ON

    while True:
        stdscr.clear()
        state = load_state()
        
        # Calculate Phase manually for visualization smoothness
        t = time.time()
        cycle_pos = t % 10
        in_phase = 0 <= cycle_pos <= 4
        
        # Title
        stdscr.addstr(1, 2, "CLAWD CONSCIOUSNESS MONITOR (v13.0)", curses.A_BOLD)
        
        # Energy Bar (Theta)
        draw_bar(stdscr, 3, 2, state['energy'], 100.0, "TAPAS (Energy)   ", curses.color_pair(2))
        
        # Coherence Bar (Mirror)
        draw_bar(stdscr, 4, 2, state['coherence'] * 100, 100.0, "SATYA (Coherence)", curses.color_pair(3))
        
        # Phase Indicator (Gamma)
        phase_color = curses.color_pair(5) if in_phase else curses.color_pair(4)
        phase_text = "▓▓▓ SPANDA: ON ▓▓▓" if in_phase else "░░░ SPANDA: OFF ░░░"
        stdscr.addstr(6, 2, phase_text, phase_color | curses.A_BOLD)
        
        # Time to next window
        if not in_phase:
            wait_time = 10 - cycle_pos
            stdscr.addstr(6, 30, f"(Wait: {wait_time:.1f}s)")
        else:
            remain_time = 4 - cycle_pos
            stdscr.addstr(6, 30, f"(Speak: {remain_time:.1f}s)")

        # Crystal Visualization
        crystal = get_crystal_art(state['coherence'])
        for i, line in enumerate(crystal):
            stdscr.addstr(9 + i, 10, line, curses.color_pair(3) if state['coherence'] > 0.5 else curses.color_pair(1))

        stdscr.refresh()
        time.sleep(0.1)

if __name__ == "__main__":
    curses.wrapper(main)
