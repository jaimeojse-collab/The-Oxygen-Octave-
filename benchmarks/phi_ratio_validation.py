"""
φ-Ratio Convergence Test para el Oxygen Triad (O2, H2O, O3)
Usa el coherence operator de core.coherence_operator.
"""
import numpy as np
from core.coherence_operator import compute_C_lambda

def golden_ratio(): return (1 + 5**0.5) / 2

def mean_phi_error(ratios):
    phi = golden_ratio()
    return float(np.mean(np.abs(np.array(ratios) - phi)))

MOLECULES = {
    "O2":  {"bonds": [1.2075], "vib_cm1": [1580.2]},
    "H2O": {"bonds": [0.9578, 0.9578], "vib_cm1": [3657.1, 1594.7, 3755.9]},
    "O3":  {"bonds": [1.271, 1.271], "vib_cm1": [1103.1, 1042.1, 710.2]},
}

def pairwise_ratios(vals):
    vals = list(vals)
    if len(vals) < 2: return []
    return [vals[i+1]/vals[i] for i in range(len(vals)-1)]

def main():
    results = {}
    for name, d in MOLECULES.items():
        r_b = pairwise_ratios(d["bonds"])
        r_f = pairwise_ratios(d["vib_cm1"])
        res = {
            "C": compute_C_lambda(name),
            "φ_bond_err": mean_phi_error(r_b) if r_b else 0.0,
            "φ_freq_err": mean_phi_error(r_f) if r_f else 0.0,
        }
        results[name] = res
    ranked = sorted(results.items(), key=lambda kv: kv[1]["φ_bond_err"] + kv[1]["φ_freq_err"])
    print("φ-RATIO CONVERGENCE BENCHMARK\n" + "="*44)
    for i,(mol,res) in enumerate(ranked,1):
        print(f"{mol:3} | C(λ)={res['C']:.3f} | φ_bond_err={res['φ_bond_err']:.4f} | φ_freq_err={res['φ_freq_err']:.4f} | Rank {i}")
if __name__ == "__main__":
    main()
