# kunitz-hmm-model

Project for detecting Kunitz domains using a profile HMM.  
Master’s Degree in Bioinformatics, University of Bologna.

##  Repository Structure

- `raw_data/`: Input files such as FASTA sequences and training datasets  
- `results/`: Output files including `.class` results and performance metrics  
- `images/`: Figures such as ROC curves, sequence logos, and confusion matrices  
- `kunitz_HMM.ipynb`: Jupyter notebook containing the HMM construction and evaluation pipeline  
- `report.pdf`: Final written report summarizing the project  
- `README.md`: This file

##  Project Overview

This project aims to build a **profile Hidden Markov Model (HMM)** to identify Kunitz-type protease inhibitor domains in protein sequences. The pipeline involves:

- Collecting and curating protein sequences from PDB and UniProt
- Performing multiple sequence alignment and structural alignment
- Building a profile HMM with `hmmbuild`
- Scanning sequences using `hmmsearch`
- Evaluating model performance using metrics such as **MCC**, **F1-score**, and **ROC AUC**

##  Tools & Dependencies

- [HMMER](http://hmmer.org/)
- Python 3 (with `numpy`, `matplotlib`, `seaborn`)
- CD-HIT (for redundancy reduction)
- BLAST+ (for filtering positives)
- [WebLogo](https://weblogo.berkeley.edu/) / [Skylign](https://skylign.org/) for sequence logo generation

##  Results Summary

The model’s performance was evaluated on two independent test sets (`set_1` and `set_2`) derived from SwissProt sequences.

Below is a summary of the key evaluation metrics:

---

###  Threshold Optimization

- E-value thresholds from **0.1 to 1e-30** were scanned.  
- The **optimal threshold** selected was **1e-6**, as it maximized the **Matthews Correlation Coefficient (MCC)**.

---

###  Confusion Matrix Results (at threshold = 1e-6)

**Set 1**
- True Positives (TP): 181  
- False Positives (FP): 1
- False Negatives (FN): 1  
- True Negatives (TN): 286,415  
- **MCC:** 1.000  

**Set 2**
- True Positives (TP): 182  
- False Positives (FP): 2  
- False Negatives (FN): 3  
- True Negatives (TN): 286,415  
- **MCC:** 0.997

---

###  ROC Curve Analysis

- E-values were transformed to confidence scores using:  
  \(-\log_{10}(\text{E-value})\)
- The **Area Under the Curve (AUC)** was:
  - **AUC = 1.000** for both `set_1` and `set_2`
- This indicates **perfect or near-perfect discrimination** between true and false sequences.

---

###  Generalization

- The model shows **excellent generalization** to unseen data.
- **No overfitting** was observed.
- 1 false positive for set 1 and 2 false positives for set 2.
- 1 false negative in set 1 and 3 false nagatives for set 2.
- High **sensitivity** and **specificity**.

---

###  Visual Results

- Supporting figures (ROC curves, confusion matrices, structural overlays) are available in the `images/` folder.
- Full analysis and discussion are provided in the `report.pdf`.

---

##  How to Use

All steps and code used to build and evaluate the HMM model are provided in the Jupyter notebook [`kunitz_HMM.ipynb`](./kunitz_HMM.ipynb).

It includes:
- Data collection and filtering
- Multiple and structural alignment
- HMM construction and scanning
- Threshold selection and evaluation (MCC, AUC, confusion matrix, ROC curves)

Figures and results referenced in the report are saved in the `images/` and `results/` folders.

##  Author

Marina Mariano  
Master’s Degree in Bioinformatics  
University of Bologna
