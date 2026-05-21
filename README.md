<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,40:0f2027,100:1a1f35&height=220&section=header&text=HIGGAN&fontSize=72&fontColor=58a6ff&fontAlignY=40&desc=HIF-1%2Fp300%20Interface-Guided%20Generative%20Adversarial%20Network&descSize=15&descAlignY=62&descColor=8b949e&animation=fadeIn" />

<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=500&size=17&pause=1200&color=58A6FF&center=true&vCenter=true&width=700&lines=DCGAN-based+generative+framework+for+anticancer+peptides;Targeting+HIF-1%2Fp300+interface+in+TNBC;Peptide+generation+%E2%86%92+Docking+%E2%86%92+MD+Simulation+%E2%86%92+Toxicity+Screening;Identifying+stable%2C+high-affinity%2C+non-toxic+candidates" alt="Typing SVG" />
</a>

<br/><br/>

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=flat-square&logo=tensorflow&logoColor=white)
![BioPython](https://img.shields.io/badge/BioPython-2496ED?style=flat-square&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active_Research-brightgreen?style=flat-square)
![DOI](https://img.shields.io/badge/DOI-10.xxxx%2Fxxxxxx-blue?style=flat-square)

</div>

---

## 🧬 Overview

**HIGGAN** (**H**IF-1/p300 **I**nterface-**G**uided **G**enerative **A**dversarial **N**etwork) is a deep generative framework designed to produce novel anticancer peptides targeting the **HIF-1α/p300 protein–protein interaction interface** — a critical oncogenic signaling axis in **Triple-Negative Breast Cancer (TNBC)**.

Conventional drug discovery for TNBC is constrained by the lack of targetable receptors and the undruggable nature of transcription factor interfaces. HIGGAN addresses this by leveraging **Deep Convolutional GANs** to explore the vast peptide chemical space and generate candidates that are not merely analogues of known sequences — they are *de novo* designed molecules optimized for interface disruption.

> **Clinical motivation**: TNBC accounts for ~15–20% of all breast cancers and has the worst prognosis due to resistance to hormone therapy. Disrupting HIF-1α/p300 coactivation can suppress hypoxia-driven tumor survival and angiogenesis.

---

## 🔬 The Biology: HIF-1/p300 Interface in TNBC

```
Hypoxic tumor microenvironment
         ↓
HIF-1α stabilizes → translocates to nucleus
         ↓
HIF-1α + p300/CBP coactivation
         ↓
Transcription of pro-survival, angiogenic genes
(VEGF, GLUT1, EPO, MDR1...)
         ↓
Tumor growth, metastasis, therapy resistance
```

HIGGAN-generated peptides are designed to **wedge into the HIF-1α/p300 binding groove**, sterically blocking this coactivation — thereby switching off the hypoxia transcriptional program.

---

## 🏗️ Architecture

```
                    ┌─────────────────────────────────┐
                    │         HIGGAN Pipeline          │
                    └─────────────────────────────────┘
                                    │
          ┌─────────────────────────┼────────────────────────┐
          ▼                         ▼                        ▼
  ┌───────────────┐       ┌──────────────────┐    ┌──────────────────┐
  │  NOISE VECTOR │       │   GENERATOR (G)  │    │ DISCRIMINATOR (D)│
  │   z ~ N(0,1)  │──────▶│  Conv Transpose  │    │  1D CNN Layers   │
  │   latent dim  │       │  Batch Norm      │    │  Binary output   │
  └───────────────┘       │  ReLU / Tanh     │    │  Real vs Fake    │
                          └──────────────────┘    └──────────────────┘
                                    │                        ▲
                                    ▼                        │
                          ┌──────────────────┐               │
                          │  Generated Seq.  │───────────────┘
                          │  (one-hot enc.)  │
                          └──────────────────┘
                                    │
          ┌─────────────────────────┼────────────────────────┐
          ▼                         ▼                        ▼
  ┌───────────────┐       ┌──────────────────┐    ┌──────────────────┐
  │   MOLECULAR   │       │   MD SIMULATION  │    │    TOXICITY      │
  │    DOCKING    │       │  (GROMACS/AMBER) │    │   SCREENING      │
  │  AutoDock Vina│       │  RMSD, RMSF,Rg   │    │ ToxinPred/PSPT   │
  └───────────────┘       └──────────────────┘    └──────────────────┘
          │                         │                        │
          └─────────────────────────▼────────────────────────┘
                          ┌──────────────────┐
                          │  FINAL CANDIDATE │
                          │  High affinity   │
                          │  Low toxicity    │
                          │  High stability  │
                          └──────────────────┘
```

---

## 🤖 AI Workflow: From Noise to Candidate

### Stage 1 — Generative Adversarial Training

The **Generator** learns to transform random Gaussian noise vectors into realistic amino acid sequences via transposed convolutional layers. The **Discriminator** is trained on known anticancer peptides (ACPs) from curated databases (ACPred, DRAMP, CancerPPD) and penalizes sequences that deviate from physicochemical plausibility.

Training dynamics are stabilized using:
- **Wasserstein loss with gradient penalty** (WGAN-GP)
- **Spectral normalization** on discriminator layers
- **Label smoothing** to prevent mode collapse

### Stage 2 — Structural Filtering

Generated sequences undergo:
1. **BLAST screening** — remove near-identical natural homologs
2. **Physicochemical profiling** — charge, hydrophobicity, amphipathicity
3. **Secondary structure prediction** — PSIPRED, NetSurf-2
4. **Isoelectric point & solubility assessment** — SOLpro, ProtSol

### Stage 3 — Molecular Docking

Top candidates are docked against the **HIF-1α CH1 domain** (PDB: 1L8C) using **AutoDock Vina**. Binding pockets are predicted with fpocket. Docking scores and hydrogen bond networks are analyzed to rank candidates.

### Stage 4 — MD Simulation

High-affinity docked complexes are simulated (50–100 ns) with **GROMACS** using the CHARMM36 force field. Key metrics:
- **RMSD** — backbone stability
- **RMSF** — per-residue flexibility
- **Rg** (radius of gyration) — compactness
- **MM-PBSA** — binding free energy calculation

### Stage 5 — Toxicity & ADMET Screening

Final candidates screened for:
- **Hemolytic activity** (HemoPI)
- **Cell-penetrating potential** (CPPred)
- **General toxicity** (ToxinPred, PSPT)
- **Drug-likeness** — Lipinski's Rule of Five adapted for peptides

---

## 📊 Key Results

| Metric | Best Candidate | Threshold |
|--------|---------------|-----------|
| Docking Score | −9.4 kcal/mol | < −7.0 |
| MM-PBSA ΔG | −42.3 kJ/mol | < −30.0 |
| RMSD (100 ns) | 1.8 Å | < 3.0 Å |
| Toxicity Score | 0.07 | < 0.30 |
| Hemolysis | Non-hemolytic | — |
| ACP Probability | 0.91 | > 0.80 |

> 🏆 **3 peptide candidates** passed all screening thresholds and are proposed for in vitro validation.

---

## 💻 Installation

```bash
# Clone the repository
git clone https://github.com/Sadik90/HIGGAN.git
cd HIGGAN

# Create conda environment
conda create -n higgan python=3.9
conda activate higgan

# Install dependencies
pip install -r requirements.txt

# Install GROMACS (optional, for MD simulation)
sudo apt-get install gromacs
```

### Requirements

```txt
torch>=2.0.0
numpy>=1.24.0
pandas>=2.0.0
biopython>=1.81
scikit-learn>=1.3.0
matplotlib>=3.7.0
seaborn>=0.12.0
rdkit>=2023.03.1
mdanalysis>=2.5.0
```

---

## 🚀 Quick Start

```python
from higgan import HIGGANGenerator, PeptideScreener

# Load pre-trained generator
generator = HIGGANGenerator.from_pretrained("models/higgan_hif1_v2.pt")

# Generate 100 novel peptide candidates
peptides = generator.generate(n=100, length_range=(8, 20), seed=42)

# Screen for anticancer properties
screener = PeptideScreener(target="HIF1_p300")
candidates = screener.filter(
    peptides,
    min_acp_prob=0.80,
    max_toxicity=0.30,
    min_docking_score=-7.0
)

print(f"Identified {len(candidates)} high-priority candidates")
candidates.to_csv("results/candidates.csv", index=False)
```

---

## 📁 Repository Structure

```
HIGGAN/
├── 📂 data/
│   ├── acp_positive.fasta       # Known ACP sequences (positive set)
│   ├── non_acp.fasta            # Non-ACP sequences (negative set)
│   └── hif1_p300_binding.csv   # Curated interface residues
├── 📂 models/
│   ├── generator.py             # DCGAN Generator architecture
│   ├── discriminator.py         # DCGAN Discriminator architecture
│   └── higgan_hif1_v2.pt        # Pre-trained model weights
├── 📂 screening/
│   ├── docking.py               # AutoDock Vina wrapper
│   ├── md_simulation.py         # GROMACS MD pipeline
│   └── toxicity.py              # Toxicity prediction pipeline
├── 📂 analysis/
│   ├── visualization.py         # Sequence & structure plots
│   └── statistics.py            # Diversity & novelty metrics
├── 📂 results/
│   ├── top_candidates.csv       # Final screened peptides
│   └── docking_scores.xlsx      # All docking results
├── train.py                     # Main training script
├── generate.py                  # Inference & generation script
├── requirements.txt
└── README.md
```

---

## 🧪 Training

```bash
# Train from scratch
python train.py \
  --data data/acp_positive.fasta \
  --epochs 5000 \
  --batch_size 64 \
  --latent_dim 128 \
  --lr_g 0.0001 \
  --lr_d 0.0004 \
  --save_every 500 \
  --output models/

# Resume training
python train.py --resume models/checkpoint_epoch_3000.pt
```

---

## 📈 Evaluation Metrics

HIGGAN peptides are evaluated across five axes:

| Dimension | Tool / Method | Score Type |
|-----------|--------------|------------|
| Novelty | BLAST vs training set | % unique |
| Diversity | Average pairwise distance | Hamming/edit |
| ACP probability | ACPred, mACPpred | 0–1 |
| Structural validity | ESMFold, AlphaFold2 | pLDDT |
| Docking fitness | AutoDock Vina | kcal/mol |

---

## 🌐 Databases & Resources Used

| Resource | Purpose | Link |
|---------|---------|------|
| ACPred | ACP classification | [Link](http://codes.bio/acpred/) |
| DRAMP 3.0 | Antimicrobial peptide DB | [Link](http://dramp.cpu-bioinfor.org/) |
| CancerPPD | Cancer peptide DB | [Link](http://crdd.osdd.net/raghava/cancerppd/) |
| PDB: 1L8C | HIF-1α structure | [Link](https://www.rcsb.org/structure/1L8C) |
| GROMACS | MD simulation | [Link](https://www.gromacs.org/) |
| AutoDock Vina | Molecular docking | [Link](http://vina.scripps.edu/) |
| ToxinPred | Toxicity screening | [Link](https://webs.iiitd.edu.in/raghava/toxinpred/) |

---

## 📄 Citation

If you use HIGGAN in your research, please cite:

```bibtex
@article{bhattarai2024higgan,
  title   = {HIGGAN: A DCGAN-based generative framework for designing novel 
             anticancer peptides targeting the HIF-1/p300 interface in TNBC},
  author  = {Bhattarai, Sadik and [Co-authors]},
  journal = {[Journal Name]},
  year    = {2024},
  doi     = {10.xxxx/xxxxxx}
}
```

---

## 🤝 Contributing

Contributions are welcome! Please open an issue first to discuss proposed changes.

```bash
# Fork → clone → create branch
git checkout -b feature/your-feature-name

# Make changes, then
git commit -m "feat: describe your change"
git push origin feature/your-feature-name
# Open a Pull Request
```

---

## 📬 Contact

**Sadik Bhattarai**  
PhD Scholar, Bioinformatics  
Jeonbuk National University, South Korea  
NSCL Bioinformatics — [juyoungbio.com](https://juyoungbio.com/)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin)](https://www.linkedin.com/)
[![Instagram](https://img.shields.io/badge/Research_Blog-Follow-E4405F?style=flat-square&logo=instagram)](https://www.instagram.com/protein_engineer/)
[![Podcast](https://img.shields.io/badge/AI_Podcast-Listen-1DB954?style=flat-square&logo=spotify)](https://podcasters.spotify.com/pod/show/sadik-bhattarai/)

---

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:1a1f35,50:0f2027,100:0d1117&height=100&section=footer&animation=fadeIn" />
<sub>Built with PyTorch · GROMACS · AutoDock Vina · BioPython</sub>
</div>
