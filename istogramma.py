import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def mostra_menu_istogramma(app):
    app._clear_contenuto()

    ttk.Label(app.contenuto, text="Scegli un indicatore da visualizzare come istogramma:", font=("Arial", 12)).pack(pady=10)

    for campo in ["Offerte di lavoro", "Stipendio medio (€)", "Età media", "Esperienza media (anni)"]:
        ttk.Button(
            app.contenuto,
            text=campo,
            command=lambda c=campo: mostra_istogramma(app, c)  # ✅ corretto!
        ).pack(fill=tk.X, padx=40, pady=5)

    app.descrizione.aggiorna_testo(
        "Seleziona una metrica da visualizzare come istogramma tra offerte, stipendi, età o esperienza."
    )


def mostra_istogramma(app, campo):
    app._clear_contenuto()
    valori = []
    for l in app.linguaggi:
        if campo == "Offerte di lavoro":
            valori.append(l.offerte_lavoro)
            ampiezza = 500
        elif campo == "Stipendio medio (€)":
            valori.append(l.stipendio_medio)
            ampiezza = 5000
        elif campo == "Età media":
            valori.append(l.eta_media)
            ampiezza = 2.5
        elif campo == "Esperienza media (anni)":
            valori.append(l.esperienza_media)
            ampiezza = 0.25

    bin_min = int(min(valori) // ampiezza) * ampiezza
    bin_max = int(max(valori) // ampiezza + 1) * ampiezza
    bins = np.arange(bin_min, bin_max + ampiezza, ampiezza)

    for widget in app.contenuto.winfo_children():
        if isinstance(widget, FigureCanvasTkAgg):
            widget.get_tk_widget().destroy()

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.hist(valori, bins=bins, edgecolor='black')
    ax.set_title(f"Istogramma di '{campo}'")
    ax.set_xlabel(campo)
    ax.set_ylabel("Frequenza")

    canvas = FigureCanvasTkAgg(fig, master=app.contenuto)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True, pady=10)

    app.descrizione.aggiorna_testo(f"Istogramma per: {campo}.\nEvidenzia la distribuzione dei valori in classi.")

    app.aggiorna_grafico_corrente = lambda: mostra_istogramma(app, campo)
