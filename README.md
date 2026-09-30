# Analisi Linguaggi di Programmazione

Applicazione desktop in **Python + Tkinter** per la statistica descrittiva applicata a un dataset di 16 linguaggi di programmazione (Python, JavaScript, C++, Java, Go, Rust, C#, PHP, TypeScript, Swift, Kotlin, Ruby, Scala, Perl, Dart, Lua).

Per ogni linguaggio sono disponibili quattro variabili:

| Variabile | Tipo |
|---|---|
| Offerte di lavoro | intero |
| Stipendio medio (€) | intero |
| Età media | intero |
| Esperienza media (anni) | decimale |

L'interfaccia ha una **sidebar sinistra** con i pulsanti di navigazione, un'**area centrale** scrollabile con i risultati e una **sidebar destra** che spiega in breve cosa si sta visualizzando.

---

## Funzionalità

| Pulsante | Cosa fa | File |
|---|---|---|
| **Tabella** | Frequenze assolute, relative (%) e cumulate (%) per ogni variabile | `frequenze.py` |
| **Grafici** | Torta, barre verticali, barre orizzontali, linee | `grafici.py` |
| **Istogramma** | Istogramma con classi di ampiezza adattata alla variabile | `istogramma.py` |
| **Indici** | Posizione (media, mediana, moda), variabilità (varianza, dev. standard, scarto medio assoluto, range, coeff. di variazione), forma (asimmetria, curtosi) | `calcolo_indici.py` |
| **Percentili** | Quartili, IQR, outlier e boxplot disegnato su canvas | `box_plot_percentili.py` |
| **Intervalli** | Intervallo interquartile e intervallo di Chebyshev (k=2) | `intervalli.py` |
| **Dati bivarianti** | Scatter plot, coefficiente di correlazione *r* e retta di regressione tra due variabili a scelta | `dati_bivarianti.py` |
| **Cambia dati** | Finestra per modificare i valori di un linguaggio; tabelle e grafici si aggiornano | `cambia_valori.py` |
| **Esci** | Chiude l'applicazione | `main.py` |

## Struttura del progetto

```
.
├── main.py                  # Punto di ingresso: finestra principale, dati e sidebar
├── linguaggio.py            # Classe Linguaggio (nome + 4 variabili)
├── descrizione.py           # Pannello di descrizione a destra
├── frequenze.py
├── grafici.py
├── istogramma.py
├── calcolo_indici.py
├── box_plot_percentili.py
├── intervalli.py
├── dati_bivarianti.py
├── cambia_valori.py
├── requirements.txt
└── README.md
```

---

## Requisiti

- **Python 3.8 o superiore**
- **Tkinter** (incluso nell'installer ufficiale di Python per Windows e macOS)
- Librerie esterne: `numpy`, `matplotlib`, `scipy`

Crea un file `requirements.txt` nella cartella del progetto con questo contenuto:

```
numpy
matplotlib
scipy
```

> **Linux:** Tkinter va installato a parte, ad esempio con `sudo apt install python3-tk`.

---

## Come avviare il progetto in PyCharm

### 1. Apri il progetto
1. Metti tutti i file `.py` nella stessa cartella.
2. In PyCharm: **File → Open...** e seleziona quella cartella.

### 2. Configura l'interprete (ambiente virtuale)
1. Vai su **File → Settings → Project: *nome* → Python Interpreter**
   (su macOS: **PyCharm → Settings...**).
2. Clicca **Add Interpreter → Add Local Interpreter → Virtualenv Environment**.
3. Scegli **New**, controlla che la versione di Python sia 3.8+ e conferma con **OK**.

### 3. Installa le dipendenze
Puoi scegliere uno dei due metodi.

**Dal terminale integrato di PyCharm** (con l'ambiente virtuale attivo):

```bash
pip install -r requirements.txt
```

**Oppure dall'interfaccia:** apri **Python Interpreter**, clicca **+**, cerca e installa `numpy`, `matplotlib` e `scipy`.

### 4. Avvia l'applicazione
1. Apri `main.py`.
2. Clic destro nell'editor → **Run 'main'**, oppure premi **Shift + F10**.

Si aprirà la finestra da 1200×700 con la tabella delle frequenze già visualizzata.

---

## Risoluzione dei problemi

| Problema | Soluzione |
|---|---|
| `ModuleNotFoundError: No module named 'scipy'` (o `numpy`, `matplotlib`) | Le dipendenze non sono installate nell'interprete del progetto: ripeti il passo 3 |
| `ModuleNotFoundError: No module named 'tkinter'` | Reinstalla Python includendo Tkinter (su Linux: `sudo apt install python3-tk`) |
| `ModuleNotFoundError: No module named 'linguaggio'` (o altri moduli locali) | Assicurati che tutti i file siano nella stessa cartella e che `main.py` sia lanciato da lì |
| La finestra non compare o si chiude subito | Controlla l'output nella console **Run** di PyCharm per l'errore |

---

## Note

- I dati sono definiti direttamente in `main.py` (lista `self.linguaggi`): per aggiungere o modificare un linguaggio basta intervenire lì.
- Le modifiche fatte con **Cambia dati** valgono solo per la sessione corrente: alla chiusura dell'app i dati tornano ai valori iniziali.
