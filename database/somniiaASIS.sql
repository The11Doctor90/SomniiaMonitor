/*
 * Copyright (c) Matteo Ferreri 2024.
 */

-- Users Table
CREATE TABLE IF NOT EXISTS users (
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    tax_id TEXT PRIMARY KEY,
    birth_date NUMERIC NOT NULL,
    gender TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);


-- Contacts Table
CREATE TABLE IF NOT EXISTS contacts(
    email TEXT NOT NULL,
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
    mac_addr TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    status TEXT
);

-- Analyses Table
CREATE TABLE IF NOT EXISTS analyses (
    start DATETIME DEFAULT CURRENT_TIMESTAMP,
    stop DATETIME DEFAULT CURRENT_TIMESTAMP,
    code TEXT PRIMARY KEY,
    sleeper_tax_id TEXT,
    id_doctor_tax_id TEXT,
    mask_mac_addr TEXT,
    FOREIGN KEY (sleeper_tax_id) REFERENCES sleepers(sleeper_tax_id) ON DELETE SET NULL,
    FOREIGN KEY (id_doctor_tax_id) REFERENCES doctors(doctor_tax_id) ON DELETE SET NULL,
    FOREIGN KEY (mask_mac_addr) REFERENCES masks(mac_addr) ON DELETE SET NULL
);

-- EKG Signal Table
CREATE TABLE IF NOT EXISTS ekg_signals (
    time INTEGER NOT NULL ,
    ekg_signal INTEGER NOT NULL,
    analysis_code TEXT,
    FOREIGN KEY (analysis_code) REFERENCES analyses(code) ON DELETE CASCADE
);

-- EKG Parameter Table
CREATE TABLE IF NOT EXISTS ekg_parameters (
    time INTEGER NOT NULL ,
    hr INTEGER NOT NULL ,
    hrv INTEGER NOT NULL ,
    rr_interval INTEGER NOT NULL ,
    analysis_code TEXT,
    FOREIGN KEY (analysis_code) REFERENCES analyses(code) ON DELETE CASCADE
);

-- EEG Signal Table
CREATE TABLE IF NOT EXISTS eeg_signals (
    time INTEGER NOT NULL ,
    channel_1 INTEGER NOT NULL,
    channel_2 INTEGER NOT NULL,
    channel_3 INTEGER NOT NULL,
    analysis_code TEXT,
    FOREIGN KEY (analysis_code) REFERENCES analyses(code) ON DELETE CASCADE
);

-- PPG Parameter Table
CREATE TABLE IF NOT EXISTS ppg_params (
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
    time INTEGER NOT NULL ,
    stage TEXT NOT NULL,
    analysis_code TEXT,
    FOREIGN KEY (analysis_code) REFERENCES analyses(code) ON DELETE CASCADE
);

-- Temperature Table
CREATE TABLE IF NOT EXISTS temperature (
    time INTEGER NOT NULL,
    value REAL NOT NULL,
    analysis_code TEXT,
    FOREIGN KEY (analysis_code) REFERENCES analyses(code) ON DELETE CASCADE
);