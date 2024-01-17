#  Copyright (c) Matteo Ferreri 2024.
import time

from itertools import count

import SomniiaMonitor.Business.MaskDataReader.SerialPortReader as serialPortReader
import SomniiaMonitor.Business.DataAnalysis as da

count = 0

def main():
    ports = serialPortReader.select_serial_port()

    if ports:
        port = serialPortReader.select_serial_port_by_list(ports)
        if port:
            print(f"Hai selezionato la porta seriale: {port}")
            # Configura e apri la porta seriale
            serial_port = serialPortReader.connect_with_serial_port(port)
            try:
                while True:
                    # Leggi i dati dalla porta seriale
                    data = serialPortReader.readline_by_serial_port(serial_port)
                    if len(data) > 18:
                        data = da.convert_into_array(data)
                        print(f"Dati ricevuti: {data}")

            except KeyboardInterrupt:
                print("\nChiusura del programma.")

            finally:
                # Chiudi la porta seriale alla fine
                serialPortReader.close_serial_port_connection(serial_port)
        else:
            print("Selezione non valida.")
    else:
        print("No port fount")


if __name__ == "__main__":
    main()
