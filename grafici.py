import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def mostra_menu_grafici(self):
    self._clear_contenuto()
    ttk.Label(self.contenuto, text="Scegli un indicatore da visualizzare come grafico:", font=("Arial", 12)).pack(
        pady=10)

    campo = 0

    for campo in ["Offerte di lavoro", "Stipendio medio (€)", "Età media", "Esperienza media (anni)"]:
        ttk.Button(
            self.contenuto,
            text=campo,
            command=lambda c=campo: mostra_grafico(self, c)
        ).pack(fill=tk.X, padx=40, pady=5)

    self.descrizione.aggiorna_testo(
        " Seleziona una metrica da visualizzare come grafico tra offerte, stipendi, età o esperienza.")


def mostra_grafico(self, campo):
    self._clear_contenuto()
    self.ultimo_campo_grafico = campo  # memorizza il campo selezionato

    ttk.Label(self.contenuto, text=f"{campo} - scegli il tipo di grafico:", font=("Arial", 12)).pack(pady=10)

    grafico_var = tk.StringVar(value="Torta")
    tipi = ["Torta", "Barre verticali", "Barre orizzontali", "Linee"]
    menu = ttk.Combobox(self.contenuto, values=tipi, textvariable=grafico_var, state="readonly")
    menu.pack(pady=5)

    frame_canvas = ttk.Frame(self.contenuto)
    frame_canvas.pack(fill=tk.BOTH, expand=True)

    def aggiorna_grafico(*args):
        # controlla se frame_canvas esiste ancora
        if not frame_canvas.winfo_exists():
            return

        for widget in frame_canvas.winfo_children():
            widget.destroy()

        etichette = [l.nome for l in self.linguaggi]
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

        totale = sum(valori)
        percentuali = [(nome, val / totale * 100) for nome, val in zip(etichette, valori)]

        fig, ax = plt.subplots(figsize=(9, 6),
                               subplot_kw={'projection': 'polar'} if grafico_var.get() == "Radar" else {})

        tipo = grafico_var.get()
        desc = ""

        if tipo == "Torta":
            ax.pie(valori, labels=etichette, autopct='%1.1f%%', startangle=140, textprops={'fontsize': 10})
            ax.set_title(f"{campo} (Torta)")
            ax.axis('equal')
            desc = f" Grafico a torta per: {campo}.\nMostra la distribuzione percentuale."
        elif tipo == "Barre verticali":
            ax.bar(etichette, valori, color='skyblue')
            ax.set_title(f"{campo} (Barre verticali)")
            ax.set_ylabel(campo)
            ax.tick_params(axis='x', rotation=45)
            desc = f" Grafico a barre verticali per: {campo}.\nConfronta i valori assoluti tra i linguaggi."
        elif tipo == "Barre orizzontali":
            ax.barh(etichette, valori, color='lightgreen')
            ax.set_title(f"{campo} (Barre orizzontali)")
            ax.set_xlabel(campo)
            desc = f" Grafico a barre orizzontali per: {campo}.\nUtile per confronti orizzontali."
        elif tipo == "Linee":
            ax.plot(etichette, valori, marker='o', linestyle='-', color='purple')
            ax.set_title(f"{campo} (Linee)")
            ax.set_ylabel(campo)
            ax.tick_params(axis='x', rotation=45)
            desc = f" Grafico a linee per: {campo}.\nEvidenzia l’andamento continuo dei dati."

        fig.tight_layout()
        canvas = FigureCanvasTkAgg(fig, master=frame_canvas)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.descrizione.aggiorna_testo(desc)

        # Salva il riferimento al metodo per usi esterni
    self.aggiorna_grafico_corrente = aggiorna_grafico

    grafico_var.trace_add("write", aggiorna_grafico)
    aggiorna_grafico()