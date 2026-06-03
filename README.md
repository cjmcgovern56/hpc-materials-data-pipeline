# Comparative DFT Study: Thermodynamic Stability & Structural Optimization of 3C-SiC vs. Diamond

This repository contains the computational workflows, input files, and structural data evaluating the energetic and geometric trade-offs of substituting Silicon into a pure Carbon diamond framework. Calculations were performed using Density Functional Theory (DFT) via **Quantum ESPRESSO** on the University of Washington's **Hyak (klone)** supercomputer cluster.

## 📌 Project Overview & Hypothesis
The goal of this study is to quantify how the introduction of the larger Silicon atom into a carbon-based lattice modifies its structural and thermodynamic properties. 

* **Structural Hypothesis:** The substitution of Silicon ($r = 1.11$ Å) into the Carbon lattice ($r = 0.77$ Å) will cause a uniform, predictable volumetric expansion of the equilibrium lattice constant relative to pure diamond.
* **Energetic Hypothesis:** The total energy per atom for 3C-SiC will be less negative (higher in energy) than diamond, indicating lower thermodynamic stability despite its cost-effectiveness and ease of doping for semiconductor applications.

## 🛠️ Computational Methodology
* **Functional:** Perdew-Burke-Ernzerhof (PBE) flavor of the Generalized Gradient Approximation (GGA).
* **Pseudopotentials:** Norm-Conserving Scalar Relativistic (ONCVPSP library).
* **Simulation Cells:** 2-atom primitive unit cells ($nat=2$) leveraging periodic boundary conditions.
* **Numerical Parameters:** Kinetic energy cutoff of **80 Ry** and a **$6 \times 6 \times 6$** Monkhorst-Pack K-point grid (established via rigorous convergence testing).
* **Optimization:** Variable-cell relaxation (`vc-relax`) utilizing Gaussian smearing (0.01 Ry) with spin polarization disabled (`nspin=1`).

## 📊 Key Findings

### 1. Structural Relaxation Data
| Material | Initial $a$ (Bohr) | Relaxed $a$ (Bohr) | Bond Length $d$ (Bohr) | Final Pressure (kbar) | Cell Change (%) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Diamond (C)** | 6.6887 | 6.6887 | 2.8963 | -0.69 | 0.00% |
| **3C-SiC** | 8.2300 | 8.2759 | 3.5836 |  0.11 | +0.56% |

### 2. Energetic Comparison
* **Diamond Energy per Atom:** -12.0598 Ry
* **3C-SiC Energy per Atom:** -10.2698 Ry
* **Thermodynamic Ground State:** Diamond (occupies a deeper minimum potential energy well by **1.79 Ry/atom**).

## 💡 Summary of Conclusions
The structural expansion of the 3C-SiC lattice to **8.28 Bohr** (+0.56%) confirms that the larger atomic volume of Silicon is the primary driver of lattice strain. This expansion directly correlates with a higher, less negative energy per atom, validating the hypothesis that the heteronuclear Si-C polar covalent bond is inherently less stable than the homonuclear C-C covalent bond. The relaxed lattice parameter for 3C-SiC (**4.379 Å**) is in excellent agreement with experimental literature values (**4.359 Å**), showcasing the predictive accuracy of the PBE-GGA functional framework.

## 🚀 How to Run the Code
To reproduce these calculations, ensure you have Quantum ESPRESSO (`pw.x`) installed and execute the input files via the command line:
```bash
pw.x -in 02_relaxation/sic.vc-relax.in > sic.vc-relax.out
