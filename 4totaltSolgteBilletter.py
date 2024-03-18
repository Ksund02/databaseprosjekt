import sqlite3
from re import findall
import sys

con = sqlite3.connect('teater.db')
cursor = con.cursor()

dato = sys.argv[1] if len(sys.argv) > 1 else print("Mangler dato")

if findall(r"^\d{4}-\d{2}-\d{2}$", dato):
    resultat = cursor.execute(f'''
        SELECT Teaterstykke.Name AS Forestillingsnavn, COUNT(BillettID) AS "Antall solgte billetter"
        FROM Forestilling
            LEFT JOIN ForestillingBillett
                USING (ForestillingID)
            INNER JOIN Teaterstykke
                USING (TeaterstykkeID)
        WHERE Forestilling.Dato = '{dato}'
        GROUP BY ForestillingID
    ''')
    for rad in resultat:
        print(rad)
else:
    print("Bruk datoformatet 'YYYY-MM-DD'")

# Eksempeldato: '2024-02-03'