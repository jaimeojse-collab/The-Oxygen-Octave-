"""
Coherence operator (GETM → C(λ)) — v0.1
- Minimal, self-contained baseline so the repo runs end-to-end.
- Later versions should replace placeholders with real phase extractors
  and high-precision spectra (HITRAN/NIST/JPL).
"""

from math import pi, sqrt
import json
from pathlib import Path

DATA_PATH = Path("data/oxygen_triad/metadata.json")

def load_metadata(path=DATA_PATH):
    with open(path, "r") as f:
        return json.load(f)

# --- Simple phase encoders (v0.1) -----------------------------------------
def geometry_phase(meta):
    """Map coarse geometry to a phase [0, 2π)."""
    sym = (meta.get("symmetry") or "").lower()
    if "dinf" in sym:         # O2 linear
        return 0.0
    if "c2v" in sym and meta.get("bond_angle_deg", 180) < 120:
        return pi/2            # bent (H2O)
    if "resonance" in sym or meta.get("bond_angle_deg", 120) >= 116:
        return pi/3            # triangular-like (O3)
    return pi/4

def energy_phase(meta):
    """Cheap proxy: use inverse bond length average as a phase seed."""
    bl = meta.get("bond_length_A", 1.0)
    if isinstance(bl, list):
        bl = sum(bl)/len(bl)
    # scale to [0, 2π)
    return (2*pi) * (1.0 / max(bl, 1e-6)) % (2*pi)

def temporal_phase(meta):
    """Use dominant vibrational mode as a phase seed."""
    modes = meta.get("vibrational_modes_cm-1", [])
    if not modes:
        return 0.0
    dom = max(modes)  # pick highest freq as 'driver'
    # normalize by 4000 cm^-1 reference to [0, 2π)
    return (2*pi) * (dom / 4000.0) % (2*pi)

def medium_phase(label):
    """Environment coupling placeholder (all gas here)."""
    return pi/6  # constant for v0.1; vary later with T/P/UV

def phase_distance(phi_i, phi_j):
    """Squared circular distance."""
    d = abs(phi_i - phi_j) % (2*pi)
    d = min(d, 2*pi - d)
    return d*d

def coherence_from_phases(phases, beta=0.5):
    """
    C = exp( -β * Σ |Δφ|^2 ) over all unordered pairs.
    Returns value in (0,1].
    """
    total = 0.0
    labels = list(phases.keys())
    for i in range(len(labels)):
        for j in range(i+1, len(labels)):
            total += phase_distance(phases[labels[i]], phases[labels[j]])
    from math import exp
    return exp(-beta * total)

# --- Public API ------------------------------------------------------------
def compute_C_lambda(molecule_label: str, meta_path=DATA_PATH):
    data = load_metadata(meta_path)
    meta = data[molecule_label]
    phiG = geometry_phase(meta)
    phiE = energy_phase(meta)
    phiT = temporal_phase(meta)
    phiM = medium_phase(molecule_label)
    phases = {"G": phiG, "E": phiE, "T": phiT, "M": phiM}
    return coherence_from_phases(phases)

def quick_demo():
    for mol in ["O2", "H2O", "O3"]:
        c = compute_C_lambda(mol)
        print(f"{mol}: C(λ) = {c:.3f}")

if __name__ == "__main__":
    quick_demo()
