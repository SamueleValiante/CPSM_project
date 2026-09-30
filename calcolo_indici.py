import math
import tkinter as tk
from tkinter import ttk

def moda_campionaria(valori):
    frequenze = {}
    for v in valori:
        frequenze[v] = frequenze.get(v, 0) + 1

    max_freq = max(frequenze.values())
    modali = [val for val, freq in frequenze.items() if freq == max_freq]

    if len(modali) == 1:
        return modali[0]  # Una sola moda
    else:
        return "Nessuna moda"  # O più di una


def media_campionaria(valori):
    return sum(valori) / len(valori)

def mediana_campionaria(valori):
    ordinati = sorted(valori)
    n = len(ordinati)
    meta = n // 2

    if n % 2 == 0:
        return (ordinati[meta - 1] + ordinati[meta]) / 2
    else:
        return ordinati[meta]


def calcola_varianza(valori, media):
    return sum((x - media) ** 2 for x in valori) / (len(valori) - 1)

def calcola_indici_posizione(self):
    self._clear_contenuto()

    ttk.Label(self.contenuto, text="Indici di Posizione", font=("Arial", 14, "bold")).pack(pady=10)

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

        media = media_campionaria(valori)
        mediana = mediana_campionaria(valori)
        moda = moda_campionaria(valori)

        ttk.Label(frame, text=f"• Media: {media:.2f}").pack(anchor="w")
        ttk.Label(frame, text=f"    somma / N = {sum(valori)} / {len(valori)} = {media:.2f}").pack(anchor="w")

        ttk.Label(frame, text=f"• Mediana: {mediana}").pack(anchor="w")
        ordinati = sorted(valori)
        ttk.Label(frame, text=f"    Ordinati: {ordinati}").pack(anchor="w")

        ttk.Label(frame, text=f"• Moda: {moda}").pack(anchor="w")

    self.descrizione.aggiorna_testo(
        " Indici di posizione:\n"
        "- Media → centro aritmetico.\n"
        "- Mediana → valore centrale.\n"
        "- Moda → valore più frequente.\n"
        "Utili per capire dove si concentra la distribuzione."
    )

def varianza_campionaria(valori, media):
    n = len(valori)
    if n < 2:
        return 0  # O None, o lancia un'eccezione a seconda del caso
    return sum((x - media) ** 2 for x in valori) / (n - 1)


def deviazione_standard(valori, media):
    return math.sqrt(varianza_campionaria(valori, media))

def scarto_medio_assoluto(valori, media):
    return sum(abs(x - media) for x in valori) / len(valori)

def ampiezza_range(valori):
    return max(valori) - min(valori)

def coefficiente_variazione(valori, media):
    s = deviazione_standard(valori, media)
    return (s / media) * 100 if media != 0 else 0

def calcola_indici_varianza(self):
    self._clear_contenuto()

    ttk.Label(self.contenuto, text="Indici di Variabilità", font=("Arial", 14, "bold")).pack(pady=10)

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

        media = media_campionaria(valori)
        varianza = varianza_campionaria(valori, media)
        dev_std = math.sqrt(varianza)
        scarto_assoluto = scarto_medio_assoluto(valori, media)
        range_val = ampiezza_range(valori)
        coeff_var = coefficiente_variazione(valori, media)

        ttk.Label(frame, text=f"- Varianza: {varianza:.2f}").pack(anchor="w")
        ttk.Label(frame, text=f"- Deviazione standard: {dev_std:.2f}").pack(anchor="w")
        ttk.Label(frame, text=f"- Scarto medio assoluto: {scarto_assoluto:.2f}").pack(anchor="w")
        ttk.Label(frame, text=f"- Ampiezza del campo di variazione (range): {range_val}").pack(anchor="w")
        ttk.Label(frame, text=f"- Coefficiente di variazione: {coeff_var:.2f}%").pack(anchor="w")

    self.descrizione.aggiorna_testo(
        " Indici di Variabilità:\n"
        "- Varianza → dispersione quadratica attorno alla media.\n"
        "- Deviazione standard → radice della varianza.\n"
        "- Scarto medio assoluto → media degli scarti assoluti dalla media.\n"
        "- Range → differenza tra max e min.\n"
        "- Coeff. di variazione → dev. standard in percentuale sulla media."
    )

def calcola_indici_forma(self):
    self._clear_contenuto()

    ttk.Label(self.contenuto, text="Indici di Forma", font=("Arial", 14, "bold")).pack(pady=10)

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

        n = len(valori)
        media = media_campionaria(valori)
        std_dev = math.sqrt(calcola_varianza(valori, media))

        skew_sum = sum(((x - media) / std_dev) ** 3 for x in valori)
        skewness = (n / ((n - 1) * (n - 2))) * skew_sum if n >= 3 else 0

        kurtosis_sum = sum(((x - media) / std_dev) ** 4 for x in valori)
        if n >= 4:
            kurtosis = ((n * (n + 1)) / ((n - 1) * (n - 2) * (n - 3))) * kurtosis_sum
            kurtosis -= (3 * (n - 1)**2) / ((n - 2) * (n - 3))
            kurtosis += 3
        else:
            kurtosis = 0

        ttk.Label(frame, text=f"• Asimmetria: {skewness:.2f}").pack(anchor="w")
        interpretazione_as = "simmetrica" if abs(skewness) < 0.1 else (
            "asimmetrica a destra (+)" if skewness > 0 else "asimmetrica a sinistra (-)")
        ttk.Label(frame, text=f"    {interpretazione_as}").pack(anchor="w")

        ttk.Label(frame, text=f"• Curtosi: {kurtosis:.2f}").pack(anchor="w")
        if kurtosis < 3:
            tipo = "piatta (platicurtica)"
        elif kurtosis == 3:
            tipo = "normale (mesocurtica)"
        else:
            tipo = "a punta (leptocurtica)"
        ttk.Label(frame, text=f"    Distribuzione {tipo}").pack(anchor="w")

    self.descrizione.aggiorna_testo(
        " Indici di Forma (senza librerie esterne):\n"
        "- Asimmetria → simmetria della distribuzione.\n"
        "- Curtosi → forma delle code (piatta o a punta)."
    )

def mostra_menu_indici(self):
    self._clear_contenuto()

    ttk.Label(self.contenuto, text="Calcolo degli indici statistici", font=("Arial", 13)).pack(pady=10)

    ttk.Button(
        self.contenuto,
        text="Indici di posizione",
        command=lambda: calcola_indici_posizione(self)
    ).pack(fill=tk.X, padx=20, pady=5)

    ttk.Button(
        self.contenuto,
        text="Indici di variabilità",
        command=lambda: calcola_indici_varianza(self)
    ).pack(fill=tk.X, padx=20, pady=5)

    ttk.Button(
        self.contenuto,
        text="Indici di forma",
        command=lambda: calcola_indici_forma(self)
    ).pack(fill=tk.X, padx=20, pady=5)

    self.descrizione.aggiorna_testo(" Scegli il tipo di indice statistico che desideri calcolare.")
