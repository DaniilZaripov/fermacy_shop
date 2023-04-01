from database import connect_db


def get_drugs():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
    SELECT Drugs.id, Drugs.name, Drugs.price, Drugs.expiration_date, Providers.name AS provider_name
    FROM Drugs
    JOIN Providers ON Drugs.provider_id = Providers.id
    """)

    drugs = cursor.fetchall()
    cursor.close()
    connection.close()

    return drugs


def get_drug_names():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("SELECT DISTINCT name FROM Drugs")

    drug_names = cursor.fetchall()
    cursor.close()
    connection.close()

    return [drug_name[0] for drug_name in drug_names]


def get_drug_info(drug_name):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT Drugs.id, Drugs.name, Drugs.price, Drugs.expiration_date, Providers.name, Pharmacies_Drugs.pharmacy_id, Pharmacies_Drugs.count, Pharmacies.name, Pharmacies.address "
        "FROM Drugs "
        "JOIN Providers ON Drugs.provider_id = Providers.id "
        "JOIN Pharmacies_Drugs ON Drugs.id = Pharmacies_Drugs.drug_id "
        "JOIN Pharmacies ON Pharmacies_Drugs.pharmacy_id = Pharmacies.id "
        "WHERE Drugs.name = ?", (drug_name,))

    result = cursor.fetchall()
    cursor.close()
    connection.close()

    return result


def get_all_drugs():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("SELECT DISTINCT name FROM Drugs")

    result = cursor.fetchall()
    cursor.close()
    connection.close()

    return [drug[0] for drug in result]
