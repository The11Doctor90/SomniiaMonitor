import matplotlib.pyplot as plt
import numpy as np
from itertools import count
from matplotlib.animation import FuncAnimation
from queue import Queue
import threading
from IPython.display import display, clear_output

# Imposta il numero massimo di punti visualizzati sull'asse x
max_points_on_x = 10


# Funzione per generare dati finti
def generate_fake_data():
    return np.random.rand()


# Inizializzazione del grafico
fig, ax = plt.subplots()
x_data, y_data = [], []
line, = ax.plot(x_data, y_data)

# Coda per la comunicazione tra i thread
data_queue = Queue()


# Funzione di aggiornamento chiamata ad ogni frame dell'animazione
def update(frame):
    while not data_queue.empty():
        data = data_queue.get()
        x_data.append(data['x'])
        y_data.append(data['y'])
        line.set_data(x_data[-max_points_on_x:], y_data[-max_points_on_x:])
        ax.relim()
        ax.autoscale_view()
        if len(x_data) > max_points_on_x:
            ax.set_xlim(x_data[-max_points_on_x], x_data[-1])
    return line,


# Creazione di un contatore infinito
counter = count()


# Funzione per simulare l'arrivo di dati dall'esterno
def receive_external_data(x, y):
    while True:
        data = {'x': x, 'y': y}
        data_queue.put(data)


def main():
    # Creazione del thread per simulare i dati dall'esterno
    data_thread = threading.Thread(target=receive_external_data)
    data_thread.start()

    # Creazione dell'animazione senza blit
    ani = FuncAnimation(fig, update, frames=None, interval=200, cache_frame_data=False)

    plt.show()

    # Attendi il completamento del thread di simulazione dei dati
    data_thread.join()

    plt.close()


if __name__ == "__main__":
    main()
