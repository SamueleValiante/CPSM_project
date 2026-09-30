import tkinter as tk
from tkinter import ttk


def mostra_menu_frequenze(self):
    self._clear_contenuto()
    ttk.Label(self.contenuto, text="Seleziona un indicatore per vedere le frequenze:", font=("Arial", 13)).pack(pady=10)

    for campo in ["Offerte di lavoro", "Stipendio medio (€)", "Età media", "Esperienza media (anni)"]:
        ttk.Button(
            self.contenuto,
            text=campo,
            command=lambda c=campo: mostra_frequenze(self, c)
        ).pack(fill=tk.X, padx=40, pady=5)

    self.descrizione.aggiorna_testo(
        " Seleziona una metrica per analizzare le frequenze assolute, relative e cumulative dei linguaggi."
    )

def mostra_frequenze(self, campo):
    self._clear_contenuto()

    ttk.Label(self.contenuto, text=f"Tabella frequenze - {campo}", font=("Arial", 12, "bold")).pack(pady=10)

    valori = []
    for l in self.linguaggi:
        if campo == "Offerte di lavoro":
            valori.append((l.nome, l.offerte_lavoro))
        elif campo == "Stipendio medio (€)":
            valori.append((l.nome, l.stipendio_medio))
        elif campo == "Età media":
            valori.append((l.nome, l.eta_media))
        elif campo == "Esperienza media (anni)":
            valori.append((l.nome, l.esperienza_media))

    valori.sort(key=lambda x: x[1])
    totale = sum(val[1] for val in valori)
    cumulata = 0

    colonne = ("Linguaggio", "Frequenza assoluta", "Frequenza relativa (%)", "Frequenza cumulata (%)")

    frame_tabella = ttk.Frame(self.contenuto)
    frame_tabella.pack(fill=tk.BOTH, expand=True)

    tabella = ttk.Treeview(frame_tabella, columns=colonne, show='headings', height=17)
    tabella.pack(fill=tk.BOTH, expand=True)

    for col in colonne:
        tabella.heading(col, text=col)
        tabella.column(col, anchor=tk.CENTER, width=180)

    for nome, valore in valori:
        freq_rel = valore / totale * 100
        cumulata += freq_rel
        tabella.insert("", "end", values=(
            nome,
            valore,
            f"{freq_rel:.2f}",
            f"{cumulata:.2f}"
        ))

    self.descrizione.aggiorna_testo(
        f" Frequenze per {campo}:\n"
        "- Frequenza assoluta: valore per linguaggio\n"
        "- Frequenza relativa: percentuale sul totale\n"
        "- Frequenza cumulata: somma progressiva delle percentuali"
    )
