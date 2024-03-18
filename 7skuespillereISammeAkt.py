import sqlite3
import sys

con = sqlite3.connect('teater.db')
cursor = con.cursor()

skuespillerNavn = sys.argv[1] if len(sys.argv) > 1 else print("Mangler skuespiller")
result = cursor.execute(f'''
    SELECT DISTINCT Ansatt2.Navn, Teaterstykke.Name
    FROM Ansatt AS Ansatt2
        INNER JOIN SkuespillerAnsatt
            USING (AnsattID)
        INNER JOIN Rolle
            USING (TeaterstykkeID, Rollenavn)
        INNER JOIN RolleIAkt
            USING (TeaterstykkeID, Rollenavn)
        INNER JOIN Akt AS Akt2
            USING (TeaterstykkeID, AktNummer)
        INNER JOIN Teaterstykke
            USING (TeaterstykkeID)
    WHERE (Akt2.AktNummer, Akt2.TeaterstykkeID) IN (
        SELECT DISTINCT Akt1.Aktnummer, Akt1.TeaterstykkeID
        FROM Ansatt AS Ansatt1
            INNER JOIN SkuespillerAnsatt
                USING (AnsattID)
            INNER JOIN Rolle
                USING (TeaterstykkeID, Rollenavn)
            INNER JOIN RolleIAkt
                USING (TeaterstykkeID, Rollenavn)
            INNER JOIN Akt AS Akt1
                USING (TeaterstykkeID, AktNummer)
        WHERE Ansatt1.Navn = "{skuespillerNavn}" AND Ansatt2.Navn <> Ansatt1.Navn)
''')

for row in result:
    print(skuespillerNavn +" | " + row[0] + " | " + row[1])

con.close()