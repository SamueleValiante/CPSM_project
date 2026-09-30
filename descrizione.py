from tkinter import ttk
import tkinter as tk

class Descrizione:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent, width=220, relief=tk.RIDGE)
        self.frame.grid(row=0, column=2, sticky="ns")
        self.frame.grid_propagate(False)

        self.label = ttk.Label(self.frame, wraplength=200, justify="left", anchor="n")
        self.label.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    def aggiorna_testo(self, testo):
        self.label.config(text=testo)