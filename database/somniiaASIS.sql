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
ALTER TABLE table_name RENAME COLUMN current_name TO new_name;


-- Users Table
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT ,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    tax_id TEXT UNIQUE NOT NULL ,
    birth_date TEXT NOT NULL,
    gender TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
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
    tax_id TEXT,
    FOREIGN KEY (tax_id) REFERENCES users(tax_id) ON DELETE CASCADE
);

-- Doctors Table
CREATE TABLE IF NOT EXISTS doctors (
    doctor_tax_id TEXT,
    register_code TEXT UNIQUE NOT NULL,
    id_supervisor TEXT,
    FOREIGN KEY (doctor_tax_id) REFERENCES users(tax_id) ON DELETE CASCADE,
    FOREIGN KEY (id_supervisor) REFERENCES doctors(doctor_tax_id) ON DELETE SET NULL
);

-- Sleeper Table
CREATE TABLE IF NOT EXISTS sleepers (
    sleeper_tax_id TEXT,
    FOREIGN KEY (sleeper_tax_id) REFERENCES users(tax_id) ON DELETE CASCADE
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
    sleeper_tax_id TEXT,
    id_doctor_tax_id TEXT,
    mask_mac_addr TEXT,
    FOREIGN KEY (sleeper_tax_id) REFERENCES sleepers(sleeper_tax_id) ON DELETE SET NULL,
    FOREIGN KEY (id_doctor_tax_id) REFERENCES doctors(doctor_tax_id) ON DELETE SET NULL,
    FOREIGN KEY (mask_mac_addr) REFERENCES masks(mac_addr) ON DELETE SET NULL
);

-- EKG Signal Table
CREATE TABLE IF NOT EXISTS ekg_signals (
    ekg_signal_id INTEGER PRIMARY KEY AUTOINCREMENT ,
    time INTEGER NOT NULL ,
    ekg_signal INTEGER NOT NULL,
    analysis_code TEXT,
    FOREIGN KEY (analysis_code) REFERENCES analyses(code) ON DELETE CASCADE
);

-- EKG Parameter Table
CREATE TABLE IF NOT EXISTS ekg_parameters (
    ekg_parameter_id INTEGER PRIMARY KEY AUTOINCREMENT ,
    time INTEGER NOT NULL ,
    hr INTEGER NOT NULL ,
    hrv INTEGER NOT NULL ,
    rr_interval INTEGER NOT NULL ,
    analysis_code TEXT,
    FOREIGN KEY (analysis_code) REFERENCES analyses(code) ON DELETE CASCADE
);

-- EEG Signal Table
CREATE TABLE IF NOT EXISTS eeg_signals (
    eeg_signal_id INTEGER PRIMARY KEY AUTOINCREMENT ,
    time INTEGER NOT NULL ,
    channel_1 INTEGER NOT NULL,
    channel_2 INTEGER NOT NULL,
    channel_3 INTEGER NOT NULL,
    analysis_code TEXT,
    FOREIGN KEY (analysis_code) REFERENCES analyses(code) ON DELETE CASCADE
);

-- PPG Parameter Table
CREATE TABLE IF NOT EXISTS ppg_params (
    ppg_param_id INTEGER PRIMARY KEY AUTOINCREMENT ,
    time INTEGER NOT NULL ,
    hr INTEGER NOT NULL ,
    spo2 INTEGER NOT NULL ,
    pi REAL NOT NULL ,
    br INTEGER NOT NULL ,
    analysis_code TEXT,
    FOREIGN KEY (analysis_code) REFERENCES analyses(code) ON DELETE CASCADE
);

-- Inertial Parameter Table
CREATE TABLE IF NOT EXISTS inertial_params (
    inertial_param_id INTEGER PRIMARY KEY AUTOINCREMENT ,
    time INTEGER NOT NULL ,
    rms REAL NOT NULL,
    roll REAL NOT NULL,
    pitch REAL NOT NULL,
    yaw REAL NOT NULL,
    analysis_code TEXT,
    FOREIGN KEY (analysis_code) REFERENCES analyses(code) ON DELETE CASCADE
);

--  Sleep Stage Table
CREATE TABLE IF NOT EXISTS sleep_stages (
    sleep_stage_id INTEGER PRIMARY KEY AUTOINCREMENT ,
    time INTEGER NOT NULL ,
    stage TEXT NOT NULL,
    analysis_code TEXT,
    FOREIGN KEY (analysis_code) REFERENCES analyses(code) ON DELETE CASCADE
);

-- Temperature Table
CREATE TABLE IF NOT EXISTS temperatures (
    temperature_id INTEGER PRIMARY KEY AUTOINCREMENT ,
    time INTEGER NOT NULL,
    value REAL NOT NULL,
    analysis_code TEXT,
    FOREIGN KEY (analysis_code) REFERENCES analyses(code) ON DELETE CASCADE
);