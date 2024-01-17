#  Copyright (c) Matteo Ferreri 2024.
import asyncio
import time

from itertools import count

import SomniiaMonitor.Business.MaskDataReader.BLEreader as BLE
import SomniiaMonitor.Business.DataAnalysis as da

count = 0

async def reader():
    devices = await BLE.find_all_device()

    if devices:
        device = BLE.select_device_by_list(devices)
        if device:
            print(f"Hai selezionato il device: {device}")

            client = await BLE.create_client_by_address(device)
            await BLE.connect_to_device(client)
            services = await BLE.get_services_by_client(client)
            service = await BLE.get_service_by_handle(services, 10)
            characteristics = BLE.get_characteristics_by_service(service)
            rx_char = BLE.get_rx_uuid(characteristics)
            try:
                while True:
                    # Leggi i dati dalla porta seriale
                    data = await BLE.read_data_by_client(client, rx_char)
                    if len(data) > 18:
                        data = da.convert_into_array(data)
                        print(f"Dati ricevuti: {data}")

            except KeyboardInterrupt:
                print("\nChiusura del programma.")

            finally:
                # Chiudi la porta seriale alla fine
                await BLE.close_connection(client)
        else:
            print("Selezione non valida.")
    else:
        print("No BLE device fount")


def main():
    asyncio.run(reader())


if __name__ == "__main__":
    main()
