import matplotlib.pyplot as plt
import numpy as np
from itertools import count
from matplotlib.animation import FuncAnimation

# Imposta il numero massimo di punti visualizzati sull'asse x
max_points_on_x = 10


# Funzione per generare dati finti
def generate_fake_data():
    return np.random.rand()


# Inizializzazione del grafico
fig, ax = plt.subplots()
x_data, y_data = [], []
line, = ax.plot(x_data, y_data)


# Funzione di aggiornamento chiamata ad ogni frame dell'animazione
def update(frame):
    x_data.append(next(counter))
    y_data.append(generate_fake_data())
    line.set_data(x_data, y_data)
    ax.relim()
    ax.autoscale_view()
    if len(x_data) > max_points_on_x:
        ax.set_xlim(x_data[-max_points_on_x], x_data[-1])
    return line,


# Creazione di un contatore infinito
counter = count()

# Creazione dell'animazione senza blit
ani = FuncAnimation(fig, update, frames=None, interval=200, cache_frame_data=False)


plt.show()
