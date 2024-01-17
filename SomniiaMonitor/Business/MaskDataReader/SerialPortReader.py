#  Copyright (c) Matteo Ferreri 2024.
import time

import serial
import serial.tools.list_ports


def select_serial_port() -> list:
    # Ottieni l'elenco delle porte seriali disponibili
    available_ports = list(serial.tools.list_ports.comports())
    time.sleep(3)

    return available_ports


def select_serial_port_by_list(serial_port_list: list):
    # Stampa l'elenco delle porte seriali disponibili
    print("Porte seriali disponibili:")
    for i, port_info in enumerate(serial_port_list, start=1):
        print(f"{i}. {port_info.device} - {port_info.manufacturer} ({port_info.description})")

    # L'utente seleziona la porta seriale
    selected_index = int(input("Seleziona il numero della porta seriale: ")) - 1

    if 0 <= selected_index < len(serial_port_list):
        selected_port = serial_port_list[selected_index].device
        return selected_port
    else:
        return None


def connect_with_serial_port(port: any, baudrate: int = 115200, timeout: int = 1):
    # Configura e apri la porta seriale
    ser = serial.Serial(port, baudrate=baudrate, timeout=timeout)
    return ser


def close_serial_port_connection(serial_port):
    # Chiudi la porta seriale alla fine
    serial_port.close()


def readline_by_serial_port(serial_port, value: str = "utf-8", error: str = "ignore") -> str:
    data = serial_port.readline().decode(value, error).strip()
    return data
