# The Oxygen Octave – v1.6.1  
### Foundations: Quantitative Correlations Across Vibrational Systems

**Author:** Jaime Ojeda
**E-mail:** jaimeojeda@gmail.com
**Collaborative AI Review:** ChatGPT (OpenAI), Grok (xAI)  
## License
Text and figures © 2025 Jaime Ojeda — released under **Creative Commons Attribution 4.0 (CC BY 4.0)**.  
Code and computational notebooks are released under the **MIT License**.  
See `LICENSE` and `LICENSE_CODE` for details. 
**DOI (Zenodo):** [(https://zenodo.org/records/17421259)]

---

## Overview
The Oxygen Octave proposes that O₂ acts as a *harmonic tonic* whose vibrational ratios with related species — O₃, H₂O, and O₂⁻ — follow coherent harmonic proportions (4/3, 7/6, √2).  
This framework combines:
- Quantum vibrational physics: \( \nu = \frac{1}{2\pi c}\sqrt{\frac{k}{\mu}} \)
- Topological invariance (Sperner’s Lemma)
- Monte Carlo statistical validation (p < 10⁻⁶)
- Reproducible harmonic folding across scales

Version 1.6.1 transforms the model from an exploratory preprint into a falsifiable, open-science framework compliant with FAIR principles.

---

## Structure
- `/data/` — raw frequencies and statistical outputs  
- `/notebooks/` — Python notebooks for harmonic ratio computation and Monte Carlo coherence simulation  
- `/figures/` — generated graphs (e.g., ratio maps, coherence density)  
- `/pdf/` — published paper (v1.6.1)  

---

## Key Results
| Ratio | Experimental | Harmonic Ideal | Error | Interval |
|-------|---------------|----------------|--------|-----------|
| O₃/O₂ | 1.319 | 4/3 (1.333) | 1.09 % | Perfect fourth |
| H₂O/O₂ | 1.157 | 7/6 (1.167) | 0.82 % | Minor third |
| O₂⁻/O₂ | 1.392 | √2 (1.414) | 1.55 % | Tritone |
| (O₃×H₂O)/O₂² | 1.612 | φ (1.618) | 0.37 % | Golden mean |

Average deviation: 1.15 % ± 0.3 %.  

---

## Statistical Validation
- **Monte Carlo runs:** 10⁴  
- **Observed coherence density:** 0.220 ± 0.015  
- **Null model (uniform Rₗₒcₐₗ):** 0.050 ± 0.008  
- **Significance:** p < 10⁻⁶  
- **Power:** > 0.99 (α = 0.01)

---

## Reproducibility
All code and data are provided under MIT License.  
To reproduce results:
```bash
pip install -r requirements.txt
jupyter notebook notebooks/octave_folding.ipynb
