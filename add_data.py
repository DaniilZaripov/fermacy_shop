from database import connect_db


def add_pharmacy(name, address, phone):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("INSERT INTO Pharmacies (name, address, phone) VALUES (?, ?, ?)", (name, address, phone))

    connection.commit()
    cursor.close()
    connection.close()


def add_provider(name, address, phone):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("INSERT INTO Providers (name, address, phone) VALUES (?, ?, ?)", (name, address, phone))

    connection.commit()
    cursor.close()
    connection.close()


def add_drug(name, price, expiration_date, provider_id):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("INSERT INTO Drugs (name, price, expiration_date, provider_id) VALUES (?, ?, ?, ?)",
                   (name, price, expiration_date, provider_id))

    connection.commit()
    cursor.close()
    connection.close()


def add_pharmacy_drug(drug_id, pharmacy_id, count):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("INSERT INTO Pharmacies_Drugs (drug_id, pharmacy_id, count) VALUES (?, ?, ?)",
                   (drug_id, pharmacy_id, count))

    connection.commit()
    cursor.close()
    connection.close()


def clear_all_tables():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM Pharmacies_Drugs")
    cursor.execute("DELETE FROM Drugs")
    cursor.execute("DELETE FROM Providers")
    cursor.execute("DELETE FROM Pharmacies")

    connection.commit()
    cursor.close()
    connection.close()


clear_all_tables()
# Добавление аптек
add_pharmacy("Филиал аптеки №1", "ул. Ленина, 1", "+7 900 123 45 67")
add_pharmacy("Филиал аптеки №2", "ул. Гагарина, 2", "+7 900 765 43 21")
add_pharmacy("Филиал аптеки №3", "ул. Космонавтов, 3", "+7 900 456 78 90")

# Добавление поставщиков
add_provider("Поставщик №1", "ул. Мира, 10", "+7 900 111 22 33")
add_provider("Поставщик №2", "ул. Звездная, 5", "+7 900 444 55 66")
add_provider("Поставщик №3", "ул. Восхода, 7", "+7 900 777 88 99")

# Добавление лекарств
add_drug("Аспирин", 50.0, "2024-12-31", 1)
add_drug("Аспирин", 45.0, "2025-01-31", 2)
add_drug("Аспирин", 55.0, "2025-02-28", 3)
add_drug("Парацетамол", 80.0, "2025-06-30", 1)
add_drug("Парацетамол", 85.0, "2025-07-31", 2)
add_drug("Парацетамол", 90.0, "2025-08-31", 3)
add_drug("Ибупрофен", 70.0, "2025-05-31", 1)
add_drug("Ибупрофен", 75.0, "2025-06-30", 2)
add_drug("Ибупрофен", 65.0, "2025-07-31", 3)

# Добавление информации о наличии лекарств в аптеках
add_pharmacy_drug(1, 1, 100)  # Аспирин доступен в Аптеке 1, количество 100
add_pharmacy_drug(2, 1, 120)  # Аспирин доступен в Аптеке 1, количество 120
add_pharmacy_drug(3, 1, 140)  # Аспирин доступен в Аптеке 1, количество 140
add_pharmacy_drug(4, 1, 50)  # Парацетамол доступен в Аптеке 1, количество 50
add_pharmacy_drug(5, 1, 60)  # Парацетамол доступен в Аптеке 1, количество 60
add_pharmacy_drug(6, 1, 70)  # Парацетамол доступен в Аптеке 1, количество 70
add_pharmacy_drug(7, 1, 80)  # Ибупрофен доступен в Аптеке 1, количество 80
add_pharmacy_drug(8, 1, 90)  # Ибупрофен доступен в Аптеке 1, количество 90
add_pharmacy_drug(9, 1, 100)  # Ибупрофен доступен в Аптеке 1, количество 100

add_pharmacy_drug(1, 2, 200)  # Аспирин доступен в Аптеке 2, количество 200
add_pharmacy_drug(2, 2, 180)  # Аспирин доступен в Аптеке 2, количество 180
add_pharmacy_drug(3, 2, 160)  # Аспирин доступен в Аптеке 2, количество 160
add_pharmacy_drug(4, 2, 100)  # Парацетамол доступен в Аптеке 2, количество 100
add_pharmacy_drug(5, 2, 120)  # Парацетамол доступен в Аптеке 2, количество 120
add_pharmacy_drug(6, 2, 140)  # Парацетамол доступен в Аптеке 2, количество 140
add_pharmacy_drug(7, 2, 150)  # Ибупрофен доступен в Аптеке 2, количество 150
add_pharmacy_drug(8, 2, 170)  # Ибупрофен доступен в Аптеке 2, количество 170
add_pharmacy_drug(9, 2, 190)  # Ибупрофен доступен в Аптеке 2, количество 190

add_pharmacy_drug(1, 3, 300)  # Аспирин доступен в Аптеке 3, количество 300
add_pharmacy_drug(2, 3, 280)  # Аспирин доступен в Аптеке 3, количество 280
add_pharmacy_drug(3, 3, 260)  # Аспирин доступен в Аптеке 3, количество 260
add_pharmacy_drug(4, 3, 150)  # Парацетамол доступен в Аптеке 3, количество 150
add_pharmacy_drug(5, 3, 180)  # Парацетамол доступен в Аптеке 3, количество 180
add_pharmacy_drug(6, 3, 210)  # Парацетамол доступен в Аптеке 3, количество 210
add_pharmacy_drug(7, 3, 220)  # Ибупрофен доступен в Аптеке 3, количество 220
add_pharmacy_drug(8, 3, 240)  # Ибупрофен
