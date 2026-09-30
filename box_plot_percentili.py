import tkinter as tk
from tkinter import ttk


def mostra_menu_boxplot(self):
    self._clear_contenuto()

    ttk.Label(self.contenuto, text="Seleziona un dato per visualizzare il boxplot", font=("Arial", 13)).pack(pady=10)

    for campo in ["Offerte di lavoro", "Stipendio medio (€)", "Età media", "Esperienza media (anni)"]:
        ttk.Button(
            self.contenuto,
            text=campo,
            command=lambda c=campo: mostra_boxplot_percentili(self, c)
        ).pack(fill=tk.X, padx=20, pady=5)

    self.descrizione.aggiorna_testo(testo=" Clicca su un campo per visualizzare il suo boxplot grafico con outlier.")


def calcola_percentile(valori_ordinati, percentile):
    n = len(valori_ordinati)
    k = (n - 1) * percentile / 100
    f = int(k)
    c = f + 1
    if c >= n:
        return valori_ordinati[-1]
    return valori_ordinati[f] + (valori_ordinati[c] - valori_ordinati[f]) * (k - f)


def mostra_boxplot_percentili(self, campo):
    self._clear_contenuto()

    ttk.Label(self.contenuto, text=f" Boxplot per: {campo}", font=("Arial", 14, "bold")).pack(pady=10)

    # Estrae i valori
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

    valori.sort()
    q1 = calcola_percentile(valori, 25)
    q2 = calcola_percentile(valori, 50)
    q3 = calcola_percentile(valori, 75)
    iqr = q3 - q1
    min_val = min(valori)
    max_val = max(valori)

    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outlier = [x for x in valori if x < lower_bound or x > upper_bound]
    valori_senza_outlier = [x for x in valori if lower_bound <= x <= upper_bound]
    min_no_outlier = min(valori_senza_outlier)
    max_no_outlier = max(valori_senza_outlier)

    # Visualizzazione numerica
    ttk.Label(self.contenuto, text=f"Q1: {q1:.2f}\n   Q2 (Mediana): {q2:.2f}\n   Q3: {q3:.2f}\n").pack(anchor="w", padx=10)
    ttk.Label(self.contenuto, text=f"Estremi: [{min_no_outlier:.2f}, {max_no_outlier:.2f}]").pack(anchor="w", padx=10)

    # Canvas per il boxplot
    canvas = tk.Canvas(self.contenuto, width=500, height=120, bg="white", highlightthickness=1, highlightbackground="black")
    canvas.pack(pady=15)

    # Funzione per convertire valore → posizione x
    def scale(x):
        return 50 + (x - min_val) / (max_val - min_val) * 400  # margine 50 px

    # Disegna boxplot
    y_center = 60
    canvas.create_line(scale(min_no_outlier), y_center, scale(max_no_outlier), y_center, fill="black")  # linea orizzontale
    canvas.create_rectangle(scale(q1), y_center - 15, scale(q3), y_center + 15, fill="#a7d0f5", outline="black")  # box
    canvas.create_line(scale(q2), y_center - 15, scale(q2), y_center + 15, fill="black", width=2)  # mediana
    canvas.create_line(scale(min_no_outlier), y_center - 10, scale(min_no_outlier), y_center + 10, fill="black")  # min
    canvas.create_line(scale(max_no_outlier), y_center - 10, scale(max_no_outlier), y_center + 10, fill="black")  # max

    # Disegna outlier
    for val in outlier:
        canvas.create_oval(scale(val) - 3, y_center - 3, scale(val) + 3, y_center + 3, fill="red")

    self.descrizione.aggiorna_testo(testo="Boxplot grafico: con quartili")
