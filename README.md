# kunitz-hmm-model

Project for detecting Kunitz domains using a profile HMM.  
Master’s Degree in Bioinformatics, University of Bologna.

## 📁 Repository Structure

- `raw_data/`: Input files such as FASTA sequences and training datasets  
- `results/`: Output files including `.class` results and performance metrics  
- `images/`: Figures such as ROC curves, sequence logos, and confusion matrices  
- `kunitz_HMM.ipynb`: Jupyter notebook containing the HMM construction and evaluation pipeline  
- `report.pdf`: Final written report summarizing the project  
- `README.md`: This file

## 🧪 Project Overview

This project aims to build a **profile Hidden Markov Model (HMM)** to identify Kunitz-type protease inhibitor domains in protein sequences. The pipeline involves:

- Collecting and curating protein sequences from PDB and UniProt
- Performing multiple sequence alignment and structural alignment
- Building a profile HMM with `hmmbuild`
- Scanning sequences using `hmmsearch`
- Evaluating model performance using metrics such as **MCC**, **F1-score**, and **ROC AUC**

## 🔧 Tools & Dependencies

- [HMMER](http://hmmer.org/)
- Python 3 (with `numpy`, `matplotlib`, `seaborn`)
- CD-HIT (for redundancy reduction)
- BLAST+ (for filtering positives)
- [WebLogo](https://weblogo.berkeley.edu/) / [Skylign](https://skylign.org/) for sequence logo generation

## 📊 Results Summary

- Optimal threshold selected: `0.01` based on MCC
- AUC = 1.000 on both validation sets
- Model demonstrates strong generalization and discriminatory power

## 📝 How to Use

All steps and code used to build and evaluate the HMM model are provided in the Jupyter notebook [`kunitz_HMM.ipynb`](./kunitz_HMM.ipynb).

It includes:
- Data collection and filtering
- Multiple and structural alignment
- HMM construction and scanning
- Threshold selection and evaluation (MCC, AUC, confusion matrix, ROC curves)

Figures and results referenced in the report are saved in the `images/` and `results/` folders.

## 👩‍🎓 Author

Marina Mariano  
Master’s Degree in Bioinformatics  
University of Bologna

---

