-- Users Table
CREATE TABLE IF NOT EXISTS users (
    id_user INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    surname TEXT NOT NULL,
    tax_id TEXT UNIQUE NOT NULL,
    birth_date NUMERIC NOT NULL,
    gender TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);


-- Contacts Table
CREATE TABLE IF NOT EXISTS contacts(
    id_contact INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL,
    phone TEXT NOT NULL,
    city TEXT NOT NULL,
    province TEXT NOT NULL,
    zip TEXT NOT NULL ,
    country TEXT NOT NULL,
    id_user INTEGER,
    FOREIGN KEY (id_user) REFERENCES users(id_user) ON DELETE CASCADE
);


-- Doctors Table
CREATE TABLE IF NOT EXISTS doctors (
    id_doctor INTEGER,
    register_code TEXT UNIQUE NOT NULL,
    id_supervisor INTEGER,
    FOREIGN KEY (id_doctor) REFERENCES users(id_user) ON DELETE CASCADE,
    FOREIGN KEY (id_supervisor) REFERENCES doctors(id_doctor) ON DELETE SET NULL
);

-- Sleeper Table
CREATE TABLE IF NOT EXISTS sleepers (
    id_sleeper INTEGER,
    FOREIGN KEY (id_sleeper) REFERENCES users(id_user) ON DELETE CASCADE
);


-- Mask Table
CREATE TABLE IF NOT EXISTS masks(
    id_mask INTEGER PRIMARY KEY AUTOINCREMENT,
    mac_addr TEXT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    status TEXT
);

-- Analyses Table
CREATE TABLE IF NOT EXISTS analyses (
    id_analysis INTEGER PRIMARY KEY AUTOINCREMENT,
    start DATETIME DEFAULT CURRENT_TIMESTAMP,
    stop DATETIME DEFAULT CURRENT_TIMESTAMP,
    code TEXT UNIQUE NOT NULL,
    id_sleeper INTEGER,
    id_doctor INTEGER,
    id_mask INTEGER,
    FOREIGN KEY (id_sleeper) REFERENCES sleepers(id_sleeper) ON DELETE SET NULL,
    FOREIGN KEY (id_doctor) REFERENCES doctors(id_doctor) ON DELETE SET NULL,
    FOREIGN KEY (id_mask) REFERENCES masks(id_mask) ON DELETE SET NULL
);

-- EKG Signal Table
CREATE TABLE IF NOT EXISTS ekg_signals (
    id_ekg_s INTEGER PRIMARY KEY AUTOINCREMENT,
    time INTEGER NOT NULL ,
    ekg_signal INTEGER NOT NULL,
    id_analysis INTEGER,
    FOREIGN KEY (id_analysis) REFERENCES analyses(id_analysis) ON DELETE CASCADE
);

-- EKG Parameter Table
CREATE TABLE IF NOT EXISTS ekg_parameters (
    id_ekg_p INTEGER PRIMARY KEY AUTOINCREMENT,
    time INTEGER NOT NULL ,
    hr INTEGER NOT NULL ,
    hrv INTEGER NOT NULL ,
    rr_interval INTEGER NOT NULL ,
    id_analysis INTEGER,
    FOREIGN KEY (id_analysis) REFERENCES analyses(id_analysis) ON DELETE CASCADE
);

-- EEG Signal Table
CREATE TABLE IF NOT EXISTS ekg_signals (
    id_eeg INTEGER PRIMARY KEY AUTOINCREMENT,
    time INTEGER NOT NULL ,
    channel_1 INTEGER NOT NULL,
    channel_2 INTEGER NOT NULL,
    channel_3 INTEGER NOT NULL,
    id_analysis INTEGER,
    FOREIGN KEY (id_analysis) REFERENCES analyses(id_analysis) ON DELETE CASCADE
);

-- PPG Parameter Table
CREATE TABLE IF NOT EXISTS ppg_params (
    id_ekg_s INTEGER PRIMARY KEY AUTOINCREMENT,
    time INTEGER NOT NULL ,
    hr INTEGER NOT NULL ,
    spo2 INTEGER NOT NULL ,
    pi REAL NOT NULL ,
    br INTEGER NOT NULL ,
    id_analysis INTEGER,
    FOREIGN KEY (id_analysis) REFERENCES analyses(id_analysis) ON DELETE CASCADE
);

-- Inertial Parameter Table
CREATE TABLE IF NOT EXISTS inertial_params (
    id_inertial INTEGER PRIMARY KEY AUTOINCREMENT,
    time INTEGER NOT NULL ,
    rms REAL NOT NULL,
    roll REAL NOT NULL,
    pitch REAL NOT NULL,
    yaw REAL NOT NULL,
    id_analysis INTEGER,
    FOREIGN KEY (id_analysis) REFERENCES analyses(id_analysis) ON DELETE CASCADE
);

--  Sleep Stage Table
CREATE TABLE IF NOT EXISTS sleep_stages (
    id_stage INTEGER PRIMARY KEY AUTOINCREMENT,
    time INTEGER NOT NULL ,
    stage TEXT NOT NULL,
    id_analysis INTEGER,
    FOREIGN KEY (id_analysis) REFERENCES analyses(id_analysis) ON DELETE CASCADE
);

-- Temperature Table
CREATE TABLE IF NOT EXISTS temperature (
    id_temp INTEGER PRIMARY KEY AUTOINCREMENT,
    time INTEGER NOT NULL ,
    value REAL NOT NULL,
    id_analysis INTEGER,
    FOREIGN KEY (id_analysis) REFERENCES analyses(id_analysis) ON DELETE CASCADE
);