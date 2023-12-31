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

            # Connettersi al dispositivo selezionato
            async with bleak.BleakClient(selected_device.address) as client:
                # Verificare se il dispositivo supporta il servizio desiderato
                services = await client.get_services()
                for service in services:
                    print(f"Servizio: {service.uuid}")

                    # Specifica il UUID del servizio desiderato
                    if service.uuid == "0000xxxx-0000-1000-8000-00805F9B34FB":  # Sostituisci con il tuo UUID
                        # Leggere caratteristiche del servizio
                        characteristics = service.characteristics
                        for char in characteristics:
                            print(f"Caratteristica: {char.uuid}")

                            # Specifica il UUID della caratteristica desiderata
                            if char.uuid == "0000yyyy-0000-1000-8000-00805F9B34FB":  # Sostituisci con il tuo UUID
                                # Leggere i dati dalla caratteristica
                                data = await client.read_gatt_char(char.uuid)
                                print(f"Dati ricevuti: {data}")
        else:
            print("Indice del dispositivo non valido.")
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    asyncio.run(discover_and_connect())
