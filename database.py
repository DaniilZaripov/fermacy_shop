import sqlite3


def connect_db():
    return sqlite3.connect("pharmacy_shop.db")


def create_tables():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Pharmacies (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        address TEXT NOT NULL,
        phone TEXT NOT NULL
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Providers (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        address TEXT NOT NULL,
        phone TEXT NOT NULL
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Drugs (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        expiration_date DATE NOT NULL,
        provider_id INTEGER NOT NULL,
        FOREIGN KEY (provider_id) REFERENCES Providers (id)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Pharmacies_Drugs (
        drug_id INTEGER NOT NULL,
        pharmacy_id INTEGER NOT NULL,
        count INTEGER NOT NULL,
        PRIMARY KEY (drug_id, pharmacy_id),
        FOREIGN KEY (drug_id) REFERENCES Drugs (id),
        FOREIGN KEY (pharmacy_id) REFERENCES Pharmacies (id)
    );
    """)

    connection.commit()
    cursor.close()
    connection.close()
