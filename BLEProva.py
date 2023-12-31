#  Copyright (c) Matteo Ferreri 2023.
import pygatt


def discover_devices():
    # Creare un oggetto GATTToolBackend
    adapter = pygatt.GATTToolBackend()

    try:
        # Inizializzare il backend
        adapter.start()

        # Scansionare i dispositivi BLE nelle vicinanze
        devices = adapter.scan(timeout=5)

        # Stampa i nomi dei dispositivi trovati
        for device in devices:
            print(f"Nome: {device['name']}, Indirizzo: {device['address']}")

    except pygatt.exceptions.BLEError as e:
        print(f"Errore durante la scansione BLE: {e}")

    finally:
        # Arrestare il backend quando hai finito
        adapter.stop()


if __name__ == "__main__":
    discover_devices()
