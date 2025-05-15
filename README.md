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

The performance of the Hidden Markov Model was evaluated through a comprehensive validation pipeline using two independent test sets (set_1 and set_2) constructed from SwissProt sequences. The key steps and metrics include:
Threshold Optimization:
A range of E-value cutoffs (from 0.1 to 1e-30) was explored to identify the optimal threshold for classification. The best performance, in terms of Matthews Correlation Coefficient (MCC), was achieved at a threshold of 0.01, which was selected as the final decision boundary.
Confusion Matrix Analysis:
At the optimal threshold:
On set_1:
True Positives (TP): 194
False Positives (FP): 0
False Negatives (FN): 0
True Negatives (TN): 286,421
MCC: 1.000
On set_2:
TP: 193
FP: 0
FN: 1
TN: 286,421
MCC: 0.997
ROC Analysis:
ROC curves were plotted for both validation sets by transforming E-values into confidence scores (−log₁₀(E)). The Area Under the Curve (AUC) reached:
AUC = 1.000 for both set_1 and set_2, indicating perfect or near-perfect discrimination between true Kunitz domain sequences and negatives.
Robustness and Generalization:
The model’s performance remained stable across validation sets, showing no overfitting and excellent generalization to unseen data. False positives were entirely absent, and false negatives were minimal (1 out of 194), suggesting the HMM is both highly sensitive and specific.
Visual Evidence:
Supporting figures (ROC curves, confusion matrices, structural overlays) are available in the images/ folder and discussed in detail in report.pdf.
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

