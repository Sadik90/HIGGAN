<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=13&duration=3000&pause=1000&color=534AB7&center=true&vCenter=true&width=700&lines=Deep+Generative+AI+%C3%97+Structural+Bioinformatics+%C3%97+Molecular+Simulation;DCGAN+%E2%86%92+Docking+%E2%86%92+100+ns+MD+%E2%86%92+Half-life+Optimization;6+Lead+CPP-ACP+Candidates+%7C+Zero+Predicted+Toxicity" alt="Typing SVG" />

# Computational Discovery of Half-Life-Optimized<br>Cell-Penetrating Anticancer Peptides

**A DCGAN-based framework for de novo CPP-ACP design targeting the HIF-1/p300 interface in breast cancer**

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![PyTorch](https://img.shields.io/badge/PyTorch-DeepLearning-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)](https://pytorch.org)
[![DCGAN](https://img.shields.io/badge/Model-DCGAN-534AB7?style=flat-square)](.)
[![Docking](https://img.shields.io/badge/Docking-ADCP%20%2B%20HADDOCK-D85A30?style=flat-square)](.)
[![MD](https://img.shields.io/badge/MD-NAMD%20100ns-1D9E75?style=flat-square)](.)
[![Leads](https://img.shields.io/badge/Lead%20Peptides-6%20Candidates-085041?style=flat-square)](.)
[![Toxicity](https://img.shields.io/badge/Toxicity-None%20Predicted-brightgreen?style=flat-square)](.)
[![License](https://img.shields.io/badge/License-Research-blue?style=flat-square)](.)

---

| Validity | Uniqueness | Lead Candidates | Predicted Toxicity |
|:---:|:---:|:---:|:---:|
| **100%** | **100%** | **6** | **0** |

</div>

---

## Overview

**HIF-1α** (Hypoxia-Inducible Factor 1-alpha) is a master regulator of tumor adaptation to low-oxygen environments. Its interaction with the transcriptional co-activator **p300** activates a cascade of oncogenic genes driving angiogenesis, metabolic reprogramming, and therapeutic resistance in breast cancer. This protein–protein interface (PDB: **1P4Q**) has long been considered "undruggable" by conventional small molecules.

This project presents a **Deep Convolutional Generative Adversarial Network (DCGAN)** framework that *creates entirely new peptide sequences* — Cell-Penetrating Anticancer Peptides (CPP-ACPs) — designed to disrupt this interface. Unlike virtual screening, the model generates novel sequences from scratch, followed by a rigorous multi-stage computational validation pipeline culminating in **six highly promising lead candidates**.

> **TL;DR** — Train DCGAN on validated ACPs → generate novel CPP-ACPs → screen physicochemistry/activity/safety → dock against HIF-1/p300 → validate by 100 ns MD → optimize half-life via cholesterol conjugation → **6 non-toxic leads with favorable drug-like properties**.

---

## Biological Motivation

```
         Hypoxic Tumor Environment
                    │
                    ▼
          HIF-1α  Stabilization
                    │
                    ▼
           Nuclear Translocation
                    │
                    ▼
       HIF-1α + p300 Complex Formation          ← Our CPP-ACPs disrupt here
                    │
                    ▼
   VEGF · GLUT1 · EPO · MDR1 · CA9 · LDHA
                    │
                    ▼
  Angiogenesis · Tumor Survival · Metastasis
                    │
                    ▼
          Breast Cancer Progression
```

---

## Computational Pipeline

```
  ┌──────────────────────────────────────────┐
  │   Experimentally Validated ACP Dataset   │
  └────────────────────┬─────────────────────┘
                       │
                       ▼
          ┌────────────────────────┐
          │     DCGAN Training     │
          │  Generator + Discrim.  │
          └────────────┬───────────┘
                       │
                       ▼
          ┌────────────────────────┐
          │  Novel CPP-ACP Library │
          │  (100% valid, unique)  │
          └────────────┬───────────┘
                       │
         ┌─────────────┼─────────────┐
         ▼             ▼             ▼
   Physicochem.   CPP & ACP     Toxicity &
   Screening      Prediction    Hemolysis
         │             │             │
         └─────────────┼─────────────┘
                       │
                       ▼
          ┌────────────────────────┐
          │  ADCP CrankPep Docking │
          │  (HIF-1/p300, 1P4Q)   │
          └────────────┬───────────┘
                       │
                       ▼
          ┌────────────────────────┐
          │    HADDOCK Docking     │
          │  H-bonds · vdW · Elec  │
          └────────────┬───────────┘
                       │
                       ▼
          ┌────────────────────────┐
          │  100 ns MD Simulation  │
          │  NAMD · RMSD · RMSF   │
          └────────────┬───────────┘
                       │
                       ▼
          ┌────────────────────────┐
          │ Cholesterol Conjugation│
          │  PepADMET Half-life    │
          └────────────┬───────────┘
                       │
                       ▼
     ┌─────────────────────────────────┐
     │   6 Optimized CPP-ACP Leads     │
     │   High affinity · Stable ·      │
     │   Non-toxic · Extended t½       │
     └─────────────────────────────────┘
```

---

## Deep Learning Architecture

### Generator

Transforms Gaussian latent noise into novel peptide sequences by learning the distribution of experimentally validated ACPs.

| Layer | Operation |
|---|---|
| 1 | Dense (latent → hidden) |
| 2 | Transposed Conv1D + Batch Norm + ReLU |
| 3 | Transposed Conv1D + Batch Norm + ReLU |
| 4 | Transposed Conv1D + Batch Norm + ReLU |
| 5 | Output Conv1D (one-hot channels) |

### Discriminator

Distinguishes real validated peptides from generated sequences.

| Layer | Operation |
|---|---|
| 1 | Conv1D + Batch Norm + LeakyReLU |
| 2 | Conv1D + Batch Norm + LeakyReLU |
| 3 | Flatten → Fully Connected |
| 4 | Sigmoid output |

### Training Strategy

- Deep Convolutional GAN architecture
- Batch normalization throughout
- Label smoothing for training stability
- Adversarial optimization with diversity preservation

**Results:** 100% validity · 100% uniqueness · High novelty · High sequence diversity

---

## Screening Pipeline

### Stage 1 — Physicochemical Characterization

| Property | Criterion |
|---|---|
| Net charge | +2 to +7 |
| Hydrophobicity | GRAVY score filter |
| Amphipathicity | Helical wheel analysis |
| Molecular weight | 1–5 kDa |
| Isoelectric point | pI > 7 |

### Stage 2 — Biological Activity Prediction

- **Cell-penetrating ability** — CPPpred
- **Anticancer activity** — ACP-ADA, iACP
- **Anti-breast cancer activity** — specialized classifier

### Stage 3 — Safety Evaluation

- **Toxicity** — ToxinPred (non-toxic required)
- **Hemolysis** — HemoPI (non-hemolytic required)
- **Drug-likeness** — Lipinski-based filters

Only high-confidence candidates passing all three stages proceed to structural analysis.

---

## Structural Validation

### ADCP CrankPep

Flexible peptide docking against the HIF-1/p300 interface (PDB: **1P4Q**) evaluated:

- Binding affinity (kcal/mol)
- Peptide conformation at the interface
- Contact residue mapping

### HADDOCK Protein–Peptide Docking

Data-driven docking assessed the quality of:

- Hydrogen bonding network
- Electrostatic interactions
- Van der Waals contacts
- Interface buried surface area

Lead peptides demonstrated **stronger interaction profiles** than reference peptides from the literature.

---

## Molecular Dynamics Simulation

Best-ranked complexes were subjected to **100 ns all-atom MD simulations** using NAMD with the CHARMM36 force field in explicit solvent.

**Trajectory analyses:**

| Metric | Description |
|---|---|
| RMSD | Backbone stability over time |
| RMSF | Per-residue flexibility |
| Rg | Radius of gyration / compactness |
| Contacts | Interface contact persistence |

All six lead complexes maintained **stable binding** throughout the full 100 ns trajectory.

---

## Half-Life Optimization

### Cholesterol Conjugation

Lead peptides were cholesterol-modified at the N- or C-terminus to enhance:

- Proteolytic resistance
- Membrane anchoring and cellular uptake
- Biological stability and circulation time

### PepADMET Pharmacokinetic Prediction

Half-life was predicted across three biologically relevant compartments:

| Compartment | Pre-conjugation | Post-conjugation |
|---|---|---|
| Human blood | Baseline | **Improved** |
| Mouse blood | Baseline | **Improved** |
| Mouse intestine | Baseline | **Improved** |

---

## Key Findings

| Metric | Outcome |
|---|---|
| Deep learning model | DCGAN |
| Target interface | HIF-1α/p300 (PDB: 1P4Q) |
| Generated library | Novel CPP-ACPs (100% valid, 100% unique) |
| Docking platforms | ADCP CrankPep + HADDOCK |
| MD simulation | NAMD — 100 ns, stable complexes confirmed |
| Toxicity | ✅ None predicted |
| Hemolysis | ✅ Not hemolytic |
| Half-life | ✅ Extended via cholesterol conjugation |
| Final lead candidates | **6 optimized CPP-ACPs** |

---

## Installation

```bash
# Clone the repository
git clone https://github.com/Sadik90/HIGGAN.git
cd HIGGAN

# Create and activate environment
conda create -n higgan python=3.9
conda activate higgan

# Install dependencies
pip install -r requirements.txt
```

### Requirements

```text
torch>=2.0
numpy>=1.24
pandas>=2.0
scikit-learn>=1.3
biopython>=1.81
matplotlib>=3.7
rdkit
mdanalysis
```

---

## Resources

| Tool | Purpose |
|---|---|
| [APD3](https://aps.unmc.edu/AP/) | Antimicrobial/anticancer peptide database |
| [CancerPPD](http://crdd.osdd.net/raghava/cancerppd/) | Anticancer peptide source |
| [RCSB PDB 1P4Q](https://www.rcsb.org/structure/1P4Q) | HIF-1α/p300 complex structure |
| [ADCP CrankPep](https://ccsb.scripps.edu/adcp/) | Flexible peptide docking |
| [HADDOCK](https://wenmr.science.uu.nl/haddock2.4/) | Protein–peptide docking |
| [NAMD](https://www.ks.uiuc.edu/Research/namd/) | Molecular dynamics simulation |
| [PepADMET](https://biosig.lab.uq.edu.au/pepADMET/) | Peptide pharmacokinetics |

---

## Future Work

- [ ] Experimental peptide synthesis and purification
- [ ] In vitro validation in TNBC cell lines (MDA-MB-231, BT-549)
- [ ] In vivo pharmacokinetic and efficacy evaluation
- [ ] Multi-objective reinforcement learning for peptide optimization
- [ ] Clinical translation pipeline for peptide therapeutics

---

## Citation

If you use this work, please cite:

```bibtex
@article{bhattarai2025hifgan,
  title   = {Computational Discovery of Half-Life-Optimized Cell-Penetrating Anticancer Peptides Using
Deep Generative Modeling},
  author  = {Bhattarai, Sadik and Chong, Kil To and Tayara, Hilal},
  journal = {Submitted},
  year    = {2026}
}
```

**Related publications:**

> Bhattarai, S., Chong, K. T., & Tayara, H. (2025). GAN-ML: Advancing anticancer peptide prediction through innovative Deep Convolution Generative Adversarial Network data augmentation technique. *Chemometrics and Intelligent Laboratory Systems*, 262, 105390.

> Bhattarai, S., Tayara, H., & Chong, K. T. (2024). Advancing peptide-based cancer therapy with AI: in-depth analysis of state-of-the-art AI models. *Journal of Chemical Information and Modeling*, 64(13), 4941–4957.

> Bhattarai, S., et al. (2022). ACP-ADA: a boosting method with data augmentation for improved prediction of anticancer peptides. *International Journal of Molecular Sciences*, 23(20), 12194.

---

## Author

**Sadik Bhattarai**
PhD Scholar — Computational Drug Engineering
Juyong Bio, South Korea
Jeonbuk National University, South Korea

[![Email](https://img.shields.io/badge/Email-bhattarai.sadik2009%40gmail.com-534AB7?style=flat-square&logo=gmail&logoColor=white)](mailto:bhattarai.sadik2009@gmail.com)

---

<div align="center">

**Deep Learning · Structural Biology · Molecular Simulation · AI-driven Drug Discovery**

*Built with PyTorch · ADCP CrankPep · HADDOCK · NAMD · PepADMET*

</div>


