#  Copyright (c) Matteo Ferreri 2024.

import bleak
from bleak import BLEDevice, BleakGATTServiceCollection, BleakGATTCharacteristic
from bleak.backends.service import BleakGATTService


async def find_all_device() -> list[BLEDevice]:
    devices = await bleak.BleakScanner.discover()
    return devices


async def find_device_by_name(name: str) -> BLEDevice | None:
    devices = await find_all_device()
    for device in devices:
        if device.name == name:
            return device
    return None


async def find_device_by_address(device_address: str) -> BLEDevice | None:
    devices = await find_all_device()
    for device in devices:
        if device.address == device_address:
            return device
    return None


async def create_client_by_device(device: BLEDevice) -> bleak.BleakClient:
    return bleak.BleakClient(device.address)


async def create_client_by_address(device_address: str) -> bleak.BleakClient:
    return bleak.BleakClient(device_address)


async def connect_to_device(client: bleak.BleakClient):
    await client.connect()


async def get_services_by_client(client: bleak.BleakClient) -> BleakGATTServiceCollection:
    return await client.get_services()


async def get_service_by_handle(services: BleakGATTServiceCollection, handle: int) -> BleakGATTService | None:
    for service in services:
        if service.handle == handle:
            return service
    return None


async def get_service_by_uuid(services: BleakGATTServiceCollection, uuid: str) -> BleakGATTService | None:
    for service in services:
        if service.uuid == uuid:
            return service

    return None


def get_characteristics_by_service(service: BleakGATTService) -> list[BleakGATTCharacteristic]:
    return  service.characteristics


def get_rx_uuid(characteristics: list[BleakGATTCharacteristic]) -> str:
    for characteristic in characteristics:
        for property in characteristic.properties:
            if property == "notify":
                return characteristic.uuid
    return ""


def get_tx_uuid(characteristics: list[BleakGATTCharacteristic]) -> str:
    for characteristic in characteristics:
        if characteristic.properties == "write":
            return characteristic.uuid
    return ""


async def read_data_by_client(client: bleak.BleakClient, rx_uuid: str, value: str = "utf-8",
                              error: str = "ignore") -> str:
    data = await client.read_gatt_char(rx_uuid)
    return data.decode(value, error).strip()


async def close_connection(client: bleak.BleakClient):
    await client.disconnect()


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
