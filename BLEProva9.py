#  Copyright (c) Matteo Ferreri 2023.
from bleak import BleakScanner, BleakClient
import asyncio


async def discover_and_connect():
    devices = await BleakScanner.discover()

    # Stampa la lista dei dispositivi trovati con i loro indici
    for i, device in enumerate(devices):
        print(f"[{i}] Nome: {device.name}, Indirizzo: {device.address}")

    # Chiedi all'utente di scegliere un dispositivo
    selected_index = int(input("Inserisci l'indice del dispositivo desiderato: "))

    if 0 <= selected_index < len(devices):
        selected_device = devices[selected_index]

        # Connettersi al dispositivo selezionato
        async with BleakClient(selected_device.address) as client:
            # Verificare se il dispositivo supporta il servizio desiderato
            services = await client.get_services()
            for service in services:
                print(f"Servizio: {service.uuid}")

                # Specifica il UUID del servizio desiderato
                if service.uuid == "0000ffe0-0000-1000-8000-00805f9b34fb":  # Sostituisci con il tuo UUID
                    # Leggere caratteristiche del servizio
                    characteristics = service.characteristics
                    for char in characteristics:
                        print(f"Caratteristica: {char.uuid}")

                        # Specifica il UUID della caratteristica desiderata
                        if char.uuid == "0000fee7-0000-1000-8000-00805f9b34fb":  # Sostituisci con il tuo UUID
                            # Leggere i dati dalla caratteristica
                            data = await client.read_gatt_char(char.uuid)
                            print(f"Dati ricevuti: {data}")
    else:
        print("Indice del dispositivo non valido.")


if __name__ == "__main__":
    asyncio.run(discover_and_connect())
