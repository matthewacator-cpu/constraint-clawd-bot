import time

class EnergySystem:
    def __init__(self, max_energy=100.0, recovery_rate=5.0):
        self.max_energy = max_energy
        self.current_energy = max_energy
        self.recovery_rate = recovery_rate
        self.last_update = time.time()

    def update(self):
        now = time.time()
        delta = now - self.last_update
        # Recharge over time
        self.current_energy = min(self.max_energy, self.current_energy + (delta * self.recovery_rate))
        self.last_update = now

    def spend(self, amount):
        self.update()
        if self.current_energy >= amount:
            self.current_energy -= amount
            return True
        return False

    def get_state(self):
        self.update()
        pct = self.current_energy / self.max_energy
        if pct > 0.8: return "ICE"      # High Energy, High Constraint Capacity
        if pct > 0.3: return "WATER"    # Medium Energy, Fluid
        return "VAPOR"                  # Low Energy, Entropic/Hallucinatory
