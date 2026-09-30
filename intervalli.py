import tkinter as tk
from tkinter import ttk
import numpy as np

def mostra_intervalli_rappresentativi(self):
    self._clear_contenuto()

    ttk.Label(self.contenuto, text="Intervalli Rappresentativi", font=("Arial", 14, "bold")).pack(pady=10)

    for campo in ["Offerte di lavoro", "Stipendio medio (€)", "Età media", "Esperienza media (anni)"]:
        frame = ttk.LabelFrame(self.contenuto, text=campo, padding=10)
        frame.pack(fill=tk.X, padx=20, pady=10)

        valori = []
        for l in self.linguaggi:
            if campo == "Offerte di lavoro":
                valori.append(l.offerte_lavoro)
            elif campo == "Stipendio medio (€)":
                valori.append(l.stipendio_medio)
            elif campo == "Età media":
                valori.append(l.eta_media)
            elif campo == "Esperienza media (anni)":
                valori.append(l.esperienza_media)

        valori = np.array(valori)
        q1 = np.percentile(valori, 25)
        q3 = np.percentile(valori, 75)
        iqr = q3 - q1
        media = np.mean(valori)
        std_dev = np.std(valori)

        ttk.Label(frame, text=f"- Q1 (25° percentile): {q1:.2f}").pack(anchor="w")
        ttk.Label(frame, text=f"- Q3 (75° percentile): {q3:.2f}").pack(anchor="w")
        ttk.Label(frame, text=f"- Intervallo interquartile (IQR): {iqr:.2f}").pack(anchor="w")
        ttk.Label(frame, text=f"    [{q1:.2f}, {q3:.2f}]").pack(anchor="w")

        ttk.Label(frame, text=f"- Media: {media:.2f}").pack(anchor="w")
        ttk.Label(frame, text=f"- Deviazione standard: {std_dev:.2f}").pack(anchor="w")

        # Intervallo secondo Chebyshev con k = 2 (≥75% dei dati)
        k = 2
        inf = media - k * std_dev
        sup = media + k * std_dev
        ttk.Label(frame, text=f"- Intervallo di Chebyshev (k=2): [{inf:.2f}, {sup:.2f}]").pack(anchor="w")

    # Testo descrizione laterale
    self.descrizione.aggiorna_testo(
        "- Intervalli rappresentativi:\n"
        "- IQR (Q1-Q3) → valori centrali\n"
        "- Chebyshev (k=2) → almeno il 75% dei valori\n"
        "Utili per identificare la variabilità senza ipotesi sulla distribuzione."
    )
