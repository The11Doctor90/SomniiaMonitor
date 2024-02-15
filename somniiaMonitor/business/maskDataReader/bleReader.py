#  Copyright (c) Matteo Ferreri 2024.

import asyncio

import bleak
from bleak import BLEDevice, BleakGATTServiceCollection, BleakGATTCharacteristic
from bleak.backends.service import BleakGATTService

_MASK_SERVICE = "7DEF8317-7300-4EE6-8849-46FACE74CA2A"
_MASK_RX = "7DEF8317-7301-4EE6-8849-46FACE74CA2A"
_MASK_TX = "7DEF8317-7302-4EE6-8849-46FACE74CA2A"

__loop = asyncio.get_event_loop()


def find_all_device() -> list[BLEDevice]:
    ble_devices = []
    devices = __loop.run_until_complete(bleak.BleakScanner.discover())
    if len(devices) > 0:
        for device in devices:
            if device.name == "Smart_Mask":
                ble_devices.append(device)

    return ble_devices


def find_device_by_address(device_address: str) -> BLEDevice | None:
    devices = find_all_device()
    for device in devices:
        if device.address == device_address:
            return device
    return None


def create_client_by_address(device_address: str) -> bleak.BleakClient:
    return bleak.BleakClient(device_address)


def connect_to_device(client: bleak.BleakClient):
    try:
        __loop.run_until_complete(client.connect())
    except RuntimeError as e:
        print("errore connection to device")


def close_connection(client: bleak.BleakClient):
    try:
        __loop.run_until_complete(client.disconnect())

    except RuntimeError as e:
        print("errore close connection")


def read_data_by_client(client: bleak.BleakClient, rx_uuid: str, value: str = "utf-8",
                        error: str = "ignore") -> list:
    try:
        data = asyncio.run(client.read_gatt_char(rx_uuid))
        return convert_data_string_into_list(data.decode(value, error).strip())
    except RuntimeError as e:
        print("ead_data_by_clien")
    return []


def convert_data_string_into_list(data: str) -> list:
    return data.split(',')


@DeprecationWarning
def select_device_by_list(devices_list: list[BLEDevice]):
    # Stampa l'elenco delle porte seriali disponibili
    print("Dispositivi disponibili:")
    for i, device_info in enumerate(devices_list, start=1):
        print(f"{i}. {device_info.name} - {device_info.address}")

    # L'utente seleziona la porta seriale
    selected_index = int(input("Seleziona il numero del device: ")) - 1

    if 0 <= selected_index < len(devices_list):
        selected_device = devices_list[selected_index].address
        return selected_device
    else:
        return None
