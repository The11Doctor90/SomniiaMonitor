/*
 * Copyright (c) Matteo Ferreri 2024.
 */

-- DROP Table
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS contacts;
DROP TABLE IF EXISTS doctors;
DROP TABLE IF EXISTS sleepers;
DROP TABLE IF EXISTS masks;
DROP TABLE IF EXISTS analyses;
DROP TABLE IF EXISTS ekg_signals;
DROP TABLE IF EXISTS ekg_parameters;
DROP TABLE IF EXISTS eeg_signals;
DROP TABLE IF EXISTS ppg_params;
DROP TABLE IF EXISTS inertial_params;
DROP TABLE IF EXISTS sleep_stages;
DROP TABLE IF EXISTS temperature;

-- Alter Table column name
-- ALTER TABLE table_name RENAME COLUMN current_name TO new_name;


-- Users Table
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT ,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    tax_id TEXT NOT NULL ,
    birth_date TEXT NOT NULL,
    gender TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    fk_doctor_id TEXT,
    fk_contact_id INTEGER,
    FOREIGN KEY (fk_doctor_id) REFERENCES doctors(doctor_id) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (fk_contact_id) references contacts(contact_id) ON UPDATE CASCADE ON DELETE CASCADE
);

-- Contacts Table
CREATE TABLE IF NOT EXISTS contacts(
    contact_id INTEGER PRIMARY KEY AUTOINCREMENT ,
    email TEXT UNIQUE NOT NULL,
    phone TEXT NOT NULL,
    address TEXT NOT NULL,
    number TEXT NOT NULL,
    city TEXT NOT NULL,
    province TEXT NOT NULL,
    zip TEXT NOT NULL ,
    country TEXT NOT NULL,
    fk_user_id INTEGER,
    FOREIGN KEY (fk_user_id) REFERENCES users(user_id) ON UPDATE CASCADE ON DELETE CASCADE
);

-- Doctors Table
CREATE TABLE IF NOT EXISTS doctors (
    doctor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    register_code TEXT UNIQUE NOT NULL,
    fk_user_id INTEGER,
    id_supervisor INTEGER,
    FOREIGN KEY (fk_user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (id_supervisor) REFERENCES doctors(doctor_id) ON DELETE SET NULL
);

-- Mask Table
CREATE TABLE IF NOT EXISTS masks(
    mask_id INTEGER PRIMARY KEY AUTOINCREMENT ,
    mac_addr TEXT UNIQUE NOT NULL ,
    name TEXT NOT NULL,
    status TEXT
);

-- Analyses Table
CREATE TABLE IF NOT EXISTS analyses (
    analysis_id INTEGER PRIMARY KEY AUTOINCREMENT ,
    start DATETIME DEFAULT CURRENT_TIMESTAMP,
    stop DATETIME DEFAULT CURRENT_TIMESTAMP,
    code TEXT UNIQUE NOT NULL ,
    fk_user_id INTEGER,
    fk_doctor_id INTEGER,
    fk_mask_id INTEGER,
    fk_ekg_signal_id INTEGER,
    fk_ekg_parameter_id INTEGER,
    fk_eeg_signal_id INTEGER,
    fk_ppg_param_id INTEGER,
    fk_inertial_param_id INTEGER,
    fk_sleep_stage_id INTEGER,
    fk_temperature_id INTEGER,
    FOREIGN KEY (fk_user_id) REFERENCES users(user_id) ON DELETE CASCADE ,
    FOREIGN KEY (fk_doctor_id) REFERENCES doctors(doctor_id) ON DELETE CASCADE,
    FOREIGN KEY (fk_mask_id) REFERENCES masks(mask_id) ON DELETE CASCADE,
    FOREIGN KEY (fk_ekg_signal_id) REFERENCES ekg_signals(ekg_signal_id) ON DELETE CASCADE,
    FOREIGN KEY (fk_ekg_parameter_id) REFERENCES ekg_parameters(ekg_parameter_id) ON DELETE CASCADE,
    FOREIGN KEY (fk_eeg_signal_id) REFERENCES eeg_signals(eeg_signal_id) ON DELETE CASCADE,
    FOREIGN KEY (fk_ppg_param_id) REFERENCES ppg_params(ppg_param_id) ON DELETE CASCADE,
    FOREIGN KEY (fk_inertial_param_id) REFERENCES inertial_params(inertial_param_id) ON DELETE CASCADE,
    FOREIGN KEY (fk_sleep_stage_id) REFERENCES sleep_stages(sleep_stage_id) ON DELETE CASCADE,
    FOREIGN KEY (fk_temperature_id) REFERENCES temperatures(temperature_id) ON DELETE CASCADE
);

-- EKG Signal Table
CREATE TABLE IF NOT EXISTS ekg_signals (
    ekg_signal_id INTEGER PRIMARY KEY AUTOINCREMENT ,
    time INTEGER NOT NULL ,
    ekg_signal INTEGER NOT NULL,
    fk_analysis_code TEXT,
    FOREIGN KEY (fk_analysis_code) REFERENCES analyses(code) ON DELETE CASCADE
);

-- EKG Parameter Table
CREATE TABLE IF NOT EXISTS ekg_parameters (
    ekg_parameter_id INTEGER PRIMARY KEY AUTOINCREMENT ,
    time INTEGER NOT NULL ,
    hr INTEGER NOT NULL ,
    hrv INTEGER NOT NULL ,
    rr_interval INTEGER NOT NULL ,
    fk_analysis_code TEXT,
    FOREIGN KEY (fk_analysis_code) REFERENCES analyses(code) ON DELETE CASCADE
);

-- EEG Signal Table
CREATE TABLE IF NOT EXISTS eeg_signals (
    eeg_signal_id INTEGER PRIMARY KEY AUTOINCREMENT ,
    time INTEGER NOT NULL ,
    channel_1 INTEGER NOT NULL,
    channel_2 INTEGER NOT NULL,
    channel_3 INTEGER NOT NULL,
    fk_analysis_code TEXT,
    FOREIGN KEY (fk_analysis_code) REFERENCES analyses(code) ON DELETE CASCADE
);

-- PPG Parameter Table
CREATE TABLE IF NOT EXISTS ppg_params (
    ppg_param_id INTEGER PRIMARY KEY AUTOINCREMENT ,
    time INTEGER NOT NULL ,
    hr INTEGER NOT NULL ,
    spo2 INTEGER NOT NULL ,
    pi REAL NOT NULL ,
    br INTEGER NOT NULL ,
    fk_analysis_code TEXT,
    FOREIGN KEY (fk_analysis_code) REFERENCES analyses(code) ON DELETE CASCADE
);

-- Inertial Parameter Table
CREATE TABLE IF NOT EXISTS inertial_params (
    inertial_param_id INTEGER PRIMARY KEY AUTOINCREMENT ,
    time INTEGER NOT NULL ,
    rms REAL NOT NULL,
    roll REAL NOT NULL,
    pitch REAL NOT NULL,
    yaw REAL NOT NULL,
    fk_analysis_code TEXT,
    FOREIGN KEY (fk_analysis_code) REFERENCES analyses(code) ON DELETE CASCADE
);

--  Sleep Stage Table
CREATE TABLE IF NOT EXISTS sleep_stages (
    sleep_stage_id INTEGER PRIMARY KEY AUTOINCREMENT ,
    time INTEGER NOT NULL ,
    stage TEXT NOT NULL,
    fk_analysis_code TEXT,
    FOREIGN KEY (fk_analysis_code) REFERENCES analyses(code) ON DELETE CASCADE
);

-- Temperature Table
CREATE TABLE IF NOT EXISTS temperatures (
    temperature_id INTEGER PRIMARY KEY AUTOINCREMENT ,
    time INTEGER NOT NULL,
    value REAL NOT NULL,
    fk_analysis_code TEXT,
    FOREIGN KEY (fk_analysis_code) REFERENCES analyses(code) ON DELETE CASCADE
);