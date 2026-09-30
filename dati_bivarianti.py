import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from scipy.stats import linregress

def mostra_dati_bivarianti(self):
    self._clear_contenuto()

    ttk.Label(self.contenuto, text="Analisi Bivariata", font=("Arial", 14, "bold")).pack(pady=10)

    # Etichette delle variabili disponibili
    opzioni = [
        "Offerte di lavoro",
        "Stipendio medio (€)",
        "Età media",
        "Esperienza media (anni)"
    ]

    # Frame per la selezione
    selezione_frame = ttk.Frame(self.contenuto)
    selezione_frame.pack(pady=10)

    ttk.Label(selezione_frame, text="Variabile X:").grid(row=0, column=0, padx=5, pady=5)
    x_var = ttk.Combobox(selezione_frame, values=opzioni, state="readonly")
    x_var.grid(row=0, column=1, padx=5, pady=5)

    ttk.Label(selezione_frame, text="Variabile Y:").grid(row=1, column=0, padx=5, pady=5)
    y_var = ttk.Combobox(selezione_frame, values=opzioni, state="readonly")
    y_var.grid(row=1, column=1, padx=5, pady=5)

    variabili = ["Offerte di lavoro", "Stipendio medio (€)", "Età media", "Esperienza media (anni)"]

    def get_valori(label):
        if label == "Offerte di lavoro":
            return np.array([l.offerte_lavoro for l in self.linguaggi])
        elif label == "Stipendio medio (€)":
            return np.array([l.stipendio_medio for l in self.linguaggi])
        elif label == "Età media":
            return np.array([l.eta_media for l in self.linguaggi])
        elif label == "Esperienza media (anni)":
            return np.array([l.esperienza_media for l in self.linguaggi])

    def esegui_analisi():
        # Cancella solo eventuali risultati precedenti, non tutta la GUI
        for widget in self.contenuto.pack_slaves():
            if isinstance(widget, ttk.LabelFrame) or isinstance(widget, FigureCanvasTkAgg):
                widget.destroy()

        x_label = x_var.get()
        y_label = y_var.get()

        # Controllo validità selezione
        if not x_label or not y_label:
            ttk.Label(self.contenuto, text=" Seleziona due variabili.", foreground="red").pack(pady=5)
            return
        if x_label == y_label:
            ttk.Label(self.contenuto, text=" Seleziona due variabili diverse.", foreground="red").pack(pady=5)
            return

        # Estrai dati
        x = get_valori(x_label)
        y = get_valori(y_label)

        # Calcoli statistici
        slope, intercept, r_value, p_value, std_err = linregress(x, y)
        y_pred = slope * x + intercept

        # Frame con risultati
        frame = ttk.LabelFrame(self.contenuto, text="Risultati", padding=10)
        frame.pack(fill=tk.X, padx=20, pady=10)

        ttk.Label(frame, text=f"Variabile X: {x_label}").pack(anchor="w")
        ttk.Label(frame, text=f"Variabile Y: {y_label}").pack(anchor="w")
        ttk.Label(frame, text=f"Coefficiente di correlazione (r): {r_value:.3f}").pack(anchor="w")
        ttk.Label(frame, text=f"Retta stimata: y = {intercept:.2f} + {slope:.2f}x").pack(anchor="w")

        # Grafico
        fig, ax = plt.subplots(figsize=(5, 4))
        ax.scatter(x, y, color='blue', label='Dati osservati')
        ax.plot(x, y_pred, color='red', label='Retta stimata')
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        ax.set_title("Diagramma a dispersione")
        ax.legend()

        canvas = FigureCanvasTkAgg(fig, master=self.contenuto)
        canvas.draw()
        canvas.get_tk_widget().pack(padx=10, pady=10)

        self.descrizione.aggiorna_testo(
            f" Relazione tra {x_label} e {y_label}:\n"
            "- Diagramma a dispersione\n"
            "- Retta di regressione stimata\n"
            "- Coefficiente r → forza della correlazione"
        )

    # Bottone di analisi
    ttk.Button(self.contenuto, text="Genera Analisi", command=esegui_analisi).pack(pady=10)
