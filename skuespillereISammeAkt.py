import sqlite3

con = sqlite3.connect('teater.db')

cursor = con.cursor()

# with open('getActorsInSamePlay.sql', 'r') as file:
#     result = cursor.executescript(file.read())

# inputNavn = input("Skriv inn navn: ")
inputNavn = 'Arturo Scotti'

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
        SELECT distinct Akt1.Aktnummer, Akt1.TeaterstykkeID
        FROM Ansatt AS Ansatt1
            INNER JOIN SkuespillerAnsatt
                USING (AnsattID)
            INNER JOIN Rolle
                USING (TeaterstykkeID, Rollenavn)
            INNER JOIN RolleIAkt
                USING (TeaterstykkeID, Rollenavn)
            INNER JOIN Akt AS Akt1
                USING (TeaterstykkeID, AktNummer)
        WHERE Ansatt1.Navn = "{inputNavn}" AND Ansatt2.Navn <> Ansatt1.Navn)
''')


for row in result:
    print(inputNavn +" | " + row[0] + " | " + row[1])

