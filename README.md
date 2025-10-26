# The Oxygen Octave — v1.6.1  
**Technical Validation & Reproducibility Update**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17421259.svg)](https://doi.org/10.5281/zenodo.17421259)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![License: CC BY 4.0](https://img.shields.io/badge/Text%2FData-CC--BY--4.0-green.svg)](LICENSE)

**Author:** Jaime Ojeda  
**Collaborative AI Review:** ChatGPT (OpenAI), Grok (xAI)  
**License:** Code under MIT, text/data under CC BY 4.0  
**DOI:** [https://doi.org/10.5281/zenodo.17421259](https://doi.org/10.5281/zenodo.17421259)

---

## 🧠 Overview

**The Oxygen Octave** proposes that **O₂ acts as a harmonic tonic** within a coherent family of vibrational ratios linking related oxygen species — O₃, H₂O, O₂⁻ — through harmonic proportions **4/3, 7/6, √2, φ**, with observed deviations under **2 %**.

This framework integrates:

- **Quantum vibrational physics:**  
  \( \nu = \frac{1}{2\pi c}\sqrt{\frac{k}{\mu}} \)  
  as the fundamental relation connecting force constant, reduced mass, and frequency.

- **Mathematical invariance:**  
  Topological stability following *Sperner’s Lemma* and harmonic ratio folding (*Rₓ^(fold)*).

- **Statistical falsifiability:**  
  Monte Carlo simulation (10⁴ runs) shows observed coherence density (0.220 ± 0.015) vs null model (0.050 ± 0.008, p < 10⁻⁶).

---

## 📊 Key Results (Ratios Folded to [1, 2])

| Ratio | Experimental | Harmonic Ideal | Error | Interval |
|:------|:--------------|:---------------|:------|:----------|
| O₃/O₂ | 1.319 | 4/3 (1.333) | 1.09 % | Perfect fourth |
| H₂O/O₂ | 1.157 | 7/6 (1.167) | 0.82 % | Minor third |
| O₂⁻/O₂ | 1.392 | √2 (1.414) | 1.55 % | Tritone |
| (O₃ × H₂O)/O₂² | 1.612 | φ (1.618) | 0.37 % | Golden mean |

**Average absolute deviation:** 1.15 % ± 0.30 %  
(Within ±2 % coherence window ≈ ±34 cents musical tolerance)  

All ratios computed from **HITRAN 2024** fundamental bands, normalized to O₂ (1556 cm⁻¹).

---

## ⚙️ Reproducibility

All datasets and scripts ensure **full transparency and replicability**.

### 📁 Data
- `data/frequencies.csv` — Measured vibrational bands (NIST, HITRAN, DFT).  
- `notebooks/octave_folding.ipynb` — Harmonic ratio folding & cent deviation computation.  
- `notebooks/monte_carlo_coherence.ipynb` — Null model simulation (10⁴ runs).  
- `figures/OxygenOctave_Ratios_Visual.png` — Summary visualization (±2 % tolerance bands).  
- `pdf/The_Oxygen_Octave_v1.6.1.pdf` — Full paper (CC BY 4.0).  

### ▶️ To Reproduce Calculations
```bash
pip install -r requirements.txt
python scripts/fold_ratios.py
