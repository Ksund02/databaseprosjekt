import sqlite3
con = sqlite3.connect('teater.db')

cursor = con.cursor()

# Create tables
cursor.execute('''CREATE TABLE IF NOT EXISTS prisgrupper
                (id INTEGER NOT NULL PRIMARY KEY,
                prisgruppe TEXT)''')
#teaterstykker
cursor.execute('''CREATE TABLE IF NOT EXISTS teaterstykker
                (id INTEGER NOT NULL PRIMARY KEY,
                name TEXT)''')

#prisgrupperITeaterstyker
cursor.execute('''CREATE TABLE IF NOT EXISTS prisgrupperITeaterstyker
                (prisgruppe_id INTEGER,
                teaterstykke_id INTEGER,
                PRIMARY KEY(prisgruppe_id, teaterstykke_id),
                FOREIGN KEY(prisgruppe_id) REFERENCES prisgrupper(id),
                FOREIGN KEY(teaterstykke_id) REFERENCES teaterstykker(id))''')

#akt
cursor.execute('''CREATE TABLE IF NOT EXISTS akt
                (aktnummer INTEGER NOT NULL,
                teaterstykke_id INTEGER NOT NULL,
                aktNavn TEXT,
                PRIMARY KEY(aktnummer, teaterstykke_id),
                FOREIGN KEY(teaterstykke_id) REFERENCES teaterstykker(id))''')
#roller
cursor.execute('''CREATE TABLE IF NOT EXISTS roller
                (teaterstykke_id INTEGER NOT NULL,
                rollenavn TEXT,
                PRIMARY KEY(rollenavn, teaterstykke_id),
                FOREIGN KEY(teaterstykke_id) REFERENCES teaterstykker(id))''')
#skuespillere
cursor.execute('''CREATE TABLE IF NOT EXISTS skuespillere
                (id INTEGER PRIMARY KEY,
                navn TEXT)''')
#skuespillerIRolle
cursor.execute('''CREATE TABLE IF NOT EXISTS skuespillerIRolle
                (skuespiller_id INTEGER NOT NULL,
                rolleNavn INTEGER NOT NULL,
                teaterstykke_id INTEGER NOT NULL,
                PRIMARY KEY(teaterstykke_id, rolleNavn),
                FOREIGN KEY(skuespiller_id) REFERENCES skuespillere(id),
                FOREIGN KEY(teaterstykke_id) REFERENCES teaterstykker(id),
                FOREIGN KEY(rolleNavn) REFERENCES roller(rolleNavn))''')
#rolleiakt
cursor.execute('''CREATE TABLE IF NOT EXISTS rolleiakt
                (rolleNavn INTEGER NOT NULL,
                aktNummer INTEGER NOT NULL,
                teaterstykke_id INTEGER NOT NULL,
                PRIMARY KEY(rolleNavn, teaterstykke_id),
                FOREIGN KEY(rolleNavn) REFERENCES roller(rolleNavn),
                FOREIGN KEY(teaterstykke_id) REFERENCES teaterstykker(id),
                FOREIGN KEY(aktNummer) REFERENCES akt(aktnummer))''')
#teatersal
cursor.execute('''CREATE TABLE IF NOT EXISTS Teatersal
               (Sesong TEXT NOT NULL,
               SalNavn TEXT NOT NULL,
               antallPlasser INTEGER NOT NULL)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS stoler
                (sesong TEXT NOT NULL,
                salNavn TEXT NOT NULL,
                stolNummer INTEGER NOT NULL,
                FOREIGN KEY(sesong) REFERENCES Teatersal(Sesong),
                FOREIGN KEY(salNavn) REFERENCES Teatersal(SalNavn))''')

cursor.execute('''CREATE TABLE IF NOT EXISTS forestilling
               (forestilling_id INTEGER PRIMARY KEY,
               sesong TEXT NOT NULL,
               salNavn TEXT NOT NULL,
               dato TEXT NOT NULL,
               klokkeslett TEXT NOT NULL,
               teaterstykke_id INTEGER NOT NULL,
               FOREIGN KEY(sesong) REFERENCES Teatersal(Sesong),
               FOREIGN KEY(salNavn) REFERENCES Teatersal(SalNavn),
               FOREIGN KEY(teaterstykke_id) REFERENCES teaterstykker(id))''')

cursor.execute('''CREATE TABLE IF NOT EXISTS billett
               (billett_id INTEGER PRIMARY KEY,
               pris INTEGER NOT NULL,
               prisgruppe_id INTEGER NOT NULL,
               stolNR INTEGER NOT NULL,
               radNR INTEGER NOT NULL,
               Områdenavn TEXT NOT NULL,
               forestilling_id INTEGER NOT NULL,
               FOREIGN KEY(prisgruppe_id) REFERENCES prisgrupper(id),
               FOREIGN KEY(forestilling_id) REFERENCES forestilling(forestilling_id))''')


con.commit()
