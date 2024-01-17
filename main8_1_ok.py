import numpy as np
import serial
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from itertools import count

import SomniiaMonitor.Business.MaskDataReader.SerialPortReader as serialPortReader
import SomniiaMonitor.Business.DataAnalysis as da

# Configurazione della porta seriale
serial_port = serialPortReader.connect_with_serial_port(
    "COM4", 9600)  # Sostituisci 'COM1' con la tua porta seriale e 9600 con il tuo baudrate

# Inizializzazione del grafico
fig, ax = plt.subplots()
x_data, y_data = [], []
line, = ax.plot(x_data, y_data)

# Imposta il numero massimo di punti visualizzati sull'asse x
max_points_on_x = 50


def convert_into_array(string: str):
    """Converte la stringa in ingresso in un array Numpy"""

    array = np.array([number for number in string.split('\t')])
    return array



def is_valid(string: str) -> bool:
    shadow_string = string
    if len(shadow_string) == 0:
        return False

    if "\t" in shadow_string:
        shadow_string = shadow_string.replace('\t', '')
    if "-" in shadow_string:
        shadow_string = shadow_string.replace('-', '')
    if "." in shadow_string:
        shadow_string = shadow_string.replace('.', '')
    if "," in shadow_string:
        shadow_string = shadow_string.replace(',', '')

    if not shadow_string.isnumeric():
        return False

    shadow_string = string.split("\t")
    if len(shadow_string) != 6:
        return False

    return True


# Funzione di aggiornamento chiamata ad ogni frame dell'animazione
def update(frame):
    if serial_port.in_waiting > 0:
        # Leggi dati dalla porta seriale
        data = serialPortReader.readline_by_serial_port(serial_port)
        if is_valid(data):
            data = convert_into_array(data)
            print(f"Dati ricevuti: {data}")

            # Aggiorna i dati nel grafico
            x_data.append(next(counter))
            y_data.append(float(data[0]))
            line.set_data(x_data[-max_points_on_x:], y_data[-max_points_on_x:])
            ax.relim()
            ax.autoscale_view()
            if len(x_data) > max_points_on_x:
                ax.set_xlim(x_data[-max_points_on_x], x_data[-1])


counter = count()
# Creazione dell'animazione senza blit
ani = FuncAnimation(fig, update, frames=None, interval=100, cache_frame_data=False)

# Visualizza il grafico
plt.show()
