#  Copyright (c) Matteo Ferreri 2023.
import bleak


async def discover_devices():
    devices = await bleak.discover()
    for device in devices:
        print(f"Nome: {device.name}, Indirizzo: {device.address}")


if __name__ == "__main__":
    import asyncio

    loop = asyncio.get_event_loop()
    loop.run_until_complete(discover_devices())
