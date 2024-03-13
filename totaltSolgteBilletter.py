import sqlite3
from re import findall

con = sqlite3.connect('teater.db')
cursor = con.cursor()

def totaltSolgteBilletter(dato):
    if findall(r"^\d{4}-\d{2}-\d{2}$", dato):
        resultat = cursor.execute(f'''
            SELECT Teaterstykke.Name AS Forestillingsnavn, COUNT(BillettID) AS "Antall solgte billetter"
            FROM Forestilling
                INNER JOIN ForestillingBillett
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
