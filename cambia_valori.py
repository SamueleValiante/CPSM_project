import tkinter as tk
from tkinter import ttk, messagebox
from frequenze import mostra_menu_frequenze
import traceback

def form_cambia_valori(self):
    form = tk.Toplevel(self.root)
    form.title("Modifica linguaggio")
    form.geometry("350x300")
    form.grab_set()

    var_nome = tk.StringVar()
    ttk.Label(form, text="Linguaggio:").pack()
    scelta = ttk.Combobox(form, values=[l.nome for l in self.linguaggi], state="readonly", textvariable=var_nome)
    scelta.pack()

    entries = {}
    for campo in ["Offerte di lavoro", "Stipendio medio (€)", "Età media", "Esperienza media (anni)"]:
        ttk.Label(form, text=campo).pack()
        e = ttk.Entry(form)
        e.pack()
        entries[campo] = e

    self.descrizione.aggiorna_testo(
        " Modifica i valori di un linguaggio selezionato. I dati verranno aggiornati automaticamente dopo il salvataggio.")

    def carica(_):
        nome = var_nome.get()
        l = next((x for x in self.linguaggi if x.nome == nome), None)
        if l:
            entries["Offerte di lavoro"].delete(0, tk.END)
            entries["Offerte di lavoro"].insert(0, l.offerte_lavoro)
            entries["Stipendio medio (€)"].delete(0, tk.END)
            entries["Stipendio medio (€)"].insert(0, l.stipendio_medio)
            entries["Età media"].delete(0, tk.END)
            entries["Età media"].insert(0, l.eta_media)
            entries["Esperienza media (anni)"].delete(0, tk.END)
            entries["Esperienza media (anni)"].insert(0, l.esperienza_media)

    scelta.bind("<<ComboboxSelected>>", carica)
    scelta.current(0)
    carica(None)

    def salva():
        try:
            nome = var_nome.get()
            l = next((x for x in self.linguaggi if x.nome == nome), None)
            if l is None:
                messagebox.showerror("Errore", "Linguaggio non trovato.")
                return
            l.offerte_lavoro = int(entries["Offerte di lavoro"].get())
            l.stipendio_medio = int(entries["Stipendio medio (€)"].get())
            l.eta_media = int(entries["Età media"].get())
            l.esperienza_media = float(entries["Esperienza media (anni)"].get())
            messagebox.showinfo("Salvato", "Dati aggiornati")

            mostra_menu_frequenze(self)

            if hasattr(self, "aggiorna_grafico_corrente"):
                self.aggiorna_grafico_corrente()  # aggiorna il grafico aperto
            form.destroy()

        except ValueError:
            messagebox.showerror("Errore", "I valori devono essere numeri validi.")
        except Exception as e:
            # Mostra il traceback completo sulla console o log per debug
            print("Errore in salva():", e)
            traceback.print_exc()
            messagebox.showerror("Errore", f"Errore inatteso: {e}")

    ttk.Button(form, text="Salva", command=salva).pack(pady=10)