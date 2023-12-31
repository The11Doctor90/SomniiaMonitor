import asyncio
from bleak import BleakScanner, BleakClient


async def main() -> None:
    devices = await BleakScanner.discover()

    # Stampa la lista dei dispositivi trovati con i loro indici
    for i, device in enumerate(devices):
        print(f"[{i}] Nome: {device.name}, Indirizzo: {device.address}")

    # Chiedi all'utente di scegliere un dispositivo
    selected_index = int(input("Inserisci l'indice del dispositivo desiderato: "))

    if 0 <= selected_index < len(devices):
        selected_device = devices[selected_index]

        client = BleakClient(selected_device)
        await client.connect(timeout=15)

        try:
            await client.pair()
        except NotImplementedError:
            # This is expected on Mac
            pass


if __name__ == "__main__":
    asyncio.run(main())
