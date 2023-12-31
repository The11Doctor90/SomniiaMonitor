import bleak
import asyncio

async def discover_and_connect():
    devices = await bleak.BleakScanner.discover()

    # Stampa la lista dei dispositivi trovati con i loro indici
    for i, device in enumerate(devices):
        print(f"[{i}] Nome: {device.name}, Indirizzo: {device.address}")

    try:
        # Chiedi all'utente di scegliere un dispositivo
        selected_index = int(input("Inserisci l'indice del dispositivo desiderato: "))

        if 0 <= selected_index < len(devices):
            selected_device = devices[selected_index]
            print(f"Hai scelto {selected_device.name} - {selected_device.address}")

            # Connettersi al dispositivo selezionato
            async with bleak.BleakClient(selected_device.address, timeout=10) as client:
                # Gestisci l'errore CancelledError durante la scansione dei servizi
                try:
                    # Ottenere la lista di tutti i servizi
                    services = await client.get_services(timeout=10)


                    for service in services:
                        print(f"Servizio: {service.uuid}")

                        # Ottenere la lista di tutte le caratteristiche nel servizio
                        characteristics = service.characteristics

                        for char in characteristics:
                            print(f"Caratteristica: {char.uuid}")

                            # Leggere i dati dalla caratteristica
                            try:
                                data = await client.read_gatt_char(char.uuid)
                                print(f"Dati ricevuti dalla caratteristica {char.uuid}: {data}")
                            except bleak.BleakError as e:
                                print(f"Errore durante la lettura dalla caratteristica {char.uuid}: {e}")

                except asyncio.CancelledError:
                    print("Operazione annullata durante la scansione dei servizi.")
        else:
            print("Indice del dispositivo non valido.")

    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    asyncio.run(discover_and_connect())
