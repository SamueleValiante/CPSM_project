import tkinter as tk
from tkinter import ttk
from descrizione import Descrizione
from linguaggio import Linguaggio
from calcolo_indici import mostra_menu_indici
from frequenze import mostra_menu_frequenze
from cambia_valori import form_cambia_valori
from grafici import mostra_menu_grafici
from box_plot_percentili import mostra_menu_boxplot
from intervalli import mostra_intervalli_rappresentativi
from dati_bivarianti import mostra_dati_bivarianti
from istogramma import mostra_menu_istogramma


class App:
    def __init__(self, root):
        self.root = root
        root.title("Analisi Linguaggi di Programmazione")
        root.geometry("1200x700")

        self.linguaggi = [
            Linguaggio("Python", 4800, 55000, 29, 3.5),
            Linguaggio("JavaScript", 5300, 50000, 27, 3.0),
            Linguaggio("C++", 3000, 60000, 32, 5.5),
            Linguaggio("Java", 4200, 53000, 30, 4.0),
            Linguaggio("Go", 2200, 64000, 31, 4.5),
            Linguaggio("Rust", 1000, 58000, 30, 5.0),
            Linguaggio("C#", 3600, 52000, 28, 3.8),
            Linguaggio("PHP", 2500, 45000, 29, 4.2),
            Linguaggio("TypeScript", 2100, 51000, 27, 3.1),
            Linguaggio("Swift", 1900, 57000, 30, 4.0),
            Linguaggio("Kotlin", 1600, 54000, 28, 3.7),
            Linguaggio("Ruby", 1200, 49000, 31, 4.5),
            Linguaggio("Scala", 900, 56000, 33, 5.2),
            Linguaggio("Perl", 700, 48000, 35, 6.0),
            Linguaggio("Dart", 600, 50000, 29, 3.3),
            Linguaggio("Lua", 500, 47000, 32, 4.7),
        ]

        # sidebar sx
        self.sidebar_sx()

        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        # Contenuto centrale (scrollabile)
        self.contenuto_centrale()

        # Sidebar destra
        self.sidebar_destra()

        self.mostra_freq()
        self.tabella = None
        self.canvas = None

    def _clear_contenuto(self):
        for widget in self.contenuto.winfo_children():
            widget.destroy()

    def sidebar_sx(self):
        sidebar = ttk.Frame(self.root, width=180, relief=tk.RIDGE)
        sidebar.grid(row=0, column=0, sticky="ns")
        sidebar.grid_propagate(False)

        ttk.Button(sidebar, text="Tabella", command=lambda: mostra_menu_frequenze(self)).pack(fill=tk.X, pady=5, padx=10)
        ttk.Button(sidebar, text="Grafici", command=lambda: mostra_menu_grafici(self)).pack(fill=tk.X, pady=5, padx=10)
        ttk.Button(sidebar, text="Istogramma", command=lambda: mostra_menu_istogramma(self)).pack(fill=tk.X, pady=5, padx=10)
        ttk.Button(sidebar, text="Indici", command=lambda: mostra_menu_indici(self)).pack(fill=tk.X, pady=5, padx=10)
        ttk.Button(sidebar, text="Percentili", command=lambda: mostra_menu_boxplot(self)).pack(fill=tk.X, pady=5, padx=10)
        ttk.Button(sidebar, text="Intervalli", command=lambda: mostra_intervalli_rappresentativi(self)).pack(fill=tk.X, pady=5, padx=10)
        ttk.Button(sidebar, text="Dati bivarianti", command=lambda: mostra_dati_bivarianti(self)).pack(fill=tk.X, pady=5, padx=10)
        ttk.Button(sidebar, text="Cambia dati", command=lambda: form_cambia_valori(self)).pack(fill=tk.X, pady=5, padx=10)
        ttk.Button(sidebar, text="Esci", command=self.root.quit).pack(fill=tk.X, pady=5, padx=10)

    def contenuto_centrale(self):
        canvas_frame = ttk.Frame(self.root)
        canvas_frame.grid(row=0, column=1, sticky="nsew")

        canvas = tk.Canvas(canvas_frame)
        canvas.pack(side="left", fill="both", expand=True)

        scroll_y = ttk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
        scroll_y.pack(side="right", fill="y")

        self.contenuto = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=self.contenuto, anchor="nw")

        self.contenuto.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.bind("<Configure>", lambda e: canvas.itemconfig("all", width=e.width))

    def sidebar_destra(self):
        sidebar_dx = ttk.Frame(self.root, width=220, relief=tk.RIDGE)
        sidebar_dx.grid(row=0, column=2, sticky="ns")
        sidebar_dx.grid_propagate(False)

        self.descrizione = Descrizione(self.root)
        self.descrizione.aggiorna_testo(
            "Visualizza statistiche sui linguaggi:\n"
            "- Tabella con valori\n"
            "- Grafici a torta per ciascun indicatore\n"
            "- Modifica i dati dinamicamente"
        )

    def mostra_freq(self):
        mostra_menu_frequenze(self)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
