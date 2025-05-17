import pandas as pd
import numpy as np
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt
import sys
import os

# --- Check argomenti ---
if len(sys.argv) != 2:
    print("Usage: python3 plot_roc_curve.py <set_file.class>")
    sys.exit(1)

input_file = sys.argv[1]

# Estrai nome base (es: set_1) per salvare immagine
base_name = os.path.splitext(os.path.basename(input_file))[0]
output_image = f"roc_curve_{base_name}.png"

# --- Carica i dati ---
df = pd.read_csv(input_file, sep="\t", header=None, names=["ID", "Class", "Evalue1", "Evalue2"])

# Trasforma E-value in score logaritmico (più basso = predizione migliore)
df["score"] = -np.log10(df["Evalue1"].astype(float))

# Calcola ROC
fpr, tpr, thresholds = roc_curve(df["Class"], df["score"])
roc_auc = auc(fpr, tpr)

# --- Plot ROC ---
plt.figure(figsize=(7, 6))
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (AUC = {roc_auc:.3f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--', label='Random')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title(f'ROC Curve for {base_name}')
plt.legend(loc="lower right")
plt.grid(True)

# Salva immagine
plt.savefig(output_image, dpi=300)
print(f"ROC curve saved to {output_image}")
plt.show()
