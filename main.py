#  Copyright (c) Matteo Ferreri 2024.
import platform
import asyncio

from kivy.app import async_runTouchApp
from kivy.uix.label import Label

import SomniiaMonitor.View.somniia_ui as fr


def main():
    frame = fr.SomniiaApp()
    frame.run()


if __name__ == "__main__":
    main()








