#  Copyright (c) Matteo Ferreri 2024.
import sqlite3
import time
from somniiaMonitor.business.maskDataReader.ekgSignalReader import EkgSignalReader
from somniiaMonitor.business.maskDataReader.eegReader import EegReader
from somniiaMonitor.business.maskDataReader.inertialReader import InertialReader
from somniiaMonitor.business.maskDataReader.ppgReader import PpgReader
from somniiaMonitor.business.maskDataReader.stagingReader import StagingReader
from somniiaMonitor.business.maskDataReader.temperatureReader import TemperatureReader


# connect to db
def accesso_serializzato():
    connessione = sqlite3.connect('database/somniia.db')
    return connessione.cursor()


# get device id
def get_device_id(cursor: sqlite3.Cursor) -> (bool, str):
    return True, "adkolnadefkionlfweionfdnklj"


# read from ble
def read_data_from_ble():
    print("threading here")
    return
    eeg_reader = EegReader()
    ekg_reader = EkgSignalReader()
    inertial_reader = InertialReader()
    ppg_reader = PpgReader()
    staging_reader = StagingReader()
    temperature_reader = TemperatureReader()
    if eeg_reader.is_connected():
        data = eeg_reader.read()
        write_data_to_db("eeg", data)
    if ekg_reader.is_connected():
        data = ekg_reader.read()
        write_data_to_db("ekg", data)
    if inertial_reader.is_connected():
        data = inertial_reader.read()
        write_data_to_db("inertial", data)
    if ppg_reader.is_connected():
        data = ppg_reader.read()
        write_data_to_db("ppg", data)
    if staging_reader.is_connected():
        data = staging_reader.read()
        write_data_to_db("staging", data)
    if temperature_reader.is_connected():
        data = temperature_reader.read()
        write_data_to_db("temperature", data)


# write to db
def write_data_to_db(service: str, data: str):
    print("service: ", service, "\ndata: ", data)


# gestire il tutto
def start_background_thread():
    cursor = accesso_serializzato()
    does_exsist, id_device = get_device_id(cursor)
    while not does_exsist:
        time.sleep(5)
        does_exsist, id_device = get_device_id(cursor)
    while True:
        read_data_from_ble()
        time.sleep(2)
