

# Gym Capacity Tracker

## Descrizione

Il progetto Gym Capacity Tracker è uno strumento progettato per monitorare e visualizzare l'occupazione di una palestra in tempo reale. Utilizzando tecniche di web scraping, lo script estrae dati riguardanti i posti disponibili e registra queste informazioni in un file CSV. Successivamente, un altro script legge questi dati e genera un grafico che illustra l'affollamento della palestra durante la settimana, facilitando la visualizzazione degli orari di picco e di calma.

## Autore

Federico Airoldi

## Data

21 Aprile 2024

## Configurazione dell'ambiente

### Prerequisiti

Per eseguire questo progetto, assicurati di avere Python installato sulla tua macchina. Il progetto è stato sviluppato usando Python 3.8, ma dovrebbe essere compatibile con versioni successive.

### Creazione e attivazione dell'ambiente virtuale

Per isolare le dipendenze del progetto, è consigliabile utilizzare un ambiente virtuale. Ecco come puoi configurarlo:

1. **Apri il terminale** e naviga alla cartella del progetto.
2. **Crea l'ambiente virtuale** eseguendo:
   ```bash
   python -m venv venv
   ```
3. **Attiva l'ambiente virtuale**:
   - Su Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - Su macOS e Linux:
     ```bash
     source venv/bin/activate
     ```

### Installazione delle dipendenze

Con l'ambiente virtuale attivato, installa le dipendenze necessarie con il seguente comando:

```bash
pip install -r requirements.txt
```

## File `requirements.txt`

Assicurati che il file `requirements.txt` includa tutte le librerie necessarie:

```
beautifulsoup4
pandas
matplotlib
seaborn
requests
schedule
```

## Esecuzione del progetto

Con tutte le dipendenze installate, puoi eseguire gli script come segue:

- Per avviare il monitoraggio:
  ```bash
  python src/main.py
  ```
- Per visualizzare i grafici:
  ```bash
  python src/plot_capacity.py
  ```

## Struttura del progetto

Il progetto è organizzato nei seguenti file principali:

- `src/main.py`: Script per il monitoraggio dei posti liberi in palestra.
- `src/plot_capacity.py`: Script per la visualizzazione dei dati raccolti.
- `data/free_slots_data.csv`: File CSV dove vengono registrati i dati.


