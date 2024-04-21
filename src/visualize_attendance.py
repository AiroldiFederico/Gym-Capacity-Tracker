import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Carica i dati
def load_data(filename):
    data = pd.read_csv(filename, names=['timestamp', 'free_slots'], header=None)
    data['timestamp'] = pd.to_datetime(data['timestamp'])
    data.set_index('timestamp', inplace=True)
    return data


# Applica la funzione di mappatura dei colori
def apply_color_map(data):
    def color_map(free_slots):
        if free_slots > 60:  # Supponendo 80 come massimo di posti
            return 'darkgreen'  # Poco affollato
        elif free_slots > 20:
            return 'yellow'  # Moderatamente affollato
        else:
            return 'darkred'  # Molto affollato

    data['color'] = data['free_slots'].apply(color_map)
    return data


# Crea il grafico
def plot_data(data):
    plt.figure(figsize=(12, 6))
    plt.scatter(data.index, data['free_slots'], color=data['color'], alpha=0.6)
    plt.title('Affollamento Settimanale della Palestra')
    plt.xlabel('Giorno e Ora')
    plt.ylabel('Posti Liberi')
    plt.grid(True)
    plt.show()


# Funzione principale per eseguire tutte le operazioni
def main():
    data = load_data('free_slots_data.csv')
    data = apply_color_map(data)
    plot_data(data)


if __name__ == "__main__":
    main()
