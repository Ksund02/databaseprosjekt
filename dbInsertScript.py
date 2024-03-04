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
cursor.execute('''CREATE TABLE IF NOT EXISTS prisgrupperITeaterstykker
                (prisgruppe_id INTEGER,
                teaterstykke_id INTEGER,
                pris INTEGER NOT NULL,
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

cursor.execute('''CREATE TABLE IF NOT EXISTS ansatt
               (ansatt_id INTEGER PRIMARY KEY,
               navn TEXT NOT NULL,
               epost TEXT NOT NULL,
               ansattStatus TEXT NOT NULL)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS oppgaver
               (theaterstykke_id INTEGER NOT NULL,
               oppgavetype TEXT NOT NULL,
               PRIMARY KEY(theaterstykke_id, oppgavetype),
               FOREIGN KEY(theaterstykke_id) REFERENCES teaterstykker(id))''')

cursor.execute('''CREATE TABLE IF NOT EXISTS ansattIoppgave
               (ansatt_id INTEGER NOT NULL,
               teaterstykke_id INTEGER NOT NULL,
               oppgavetype TEXT NOT NULL,
               PRIMARY KEY(teaterstykke_id, oppgavetype),
               FOREIGN KEY(ansatt_id) REFERENCES ansatt(ansatt_id),
               FOREIGN KEY(teaterstykke_id) REFERENCES teaterstykker(id),
               FOREIGN KEY(oppgavetype) REFERENCES oppgaver(oppgavetype))''')


con.commit()

# insert teaterstykker
if(con.execute('''SELECT * FROM teaterstykker''').fetchone() == None):
    con.execute('''INSERT INTO teaterstykker (id, name) VALUES (1, 'Kongsemnene')''')
    con.execute('''INSERT INTO teaterstykker (id, name) VALUES (2, 'Størst av alt er kjærligheten')''')

# insert Saler
if(con.execute('''SELECT * FROM Teatersal''').fetchone() == None):
    con.execute('''INSERT INTO Teatersal (Sesong, SalNavn, antallPlasser) VALUES ('vinter2024', 'gamle scene', 332)''')
    con.execute('''INSERT INTO Teatersal (Sesong, SalNavn, antallPlasser) VALUES ('vinter2024', 'hovedscene', 516)''')
    con.execute('''INSERT INTO Teatersal (Sesong, SalNavn, antallPlasser) VALUES ('vår2024', 'gamle scene', 332)''')
    con.execute('''INSERT INTO Teatersal (Sesong, SalNavn, antallPlasser) VALUES ('vår2024', 'hovedscene', 516)''')

# insert foretillinger

KongesemneneForestillinger = ['2024-02-01', '2024-02-02', '2024-02-03', '2024-02-05', '2024-02-06']
StørstAvAltErKjærlighetenForestillinger = ['2024-02-03', '2024-02-06', '2024-02-07', '2024-02-12', '2024-02-13, 2024-02-14']
if(con.execute('''SELECT * FROM forestilling''').fetchone() == None):
    id =0
    for i in KongesemneneForestillinger:
        con.execute('''INSERT INTO forestilling (forestilling_id, sesong, salNavn, dato, klokkeslett, teaterstykke_id) VALUES (id, 'vinter2024', 'hovedscene', i, '19:00', 1)''')
        id += 1
    for i in StørstAvAltErKjærlighetenForestillinger:
        con.execute('''INSERT INTO forestilling (forestilling_id, sesong, salNavn, dato, klokkeslett, teaterstykke_id) VALUES (id, 'vinter2024', 'gamle scene', i, '18:30', 2)''')
        id += 1
    con.commit()


# insert prisgrupper
if(con.execute('''SELECT * FROM prisgrupper''').fetchone() == None):
    con.execute('''INSERT INTO prisgrupper (id, prisgruppe) VALUES (1, 'Ordinær')''')
    con.execute('''INSERT INTO prisgrupper (id, prisgruppe) VALUES (2, 'Honør')''')
    con.execute('''INSERT INTO prisgrupper (id, prisgruppe) VALUES (3, 'Student')''')
    con.execute('''INSERT INTO prisgrupper (id, prisgruppe) VALUES (4, 'Barn')''')
    con.execute('''INSERT INTO prisgrupper (id, prisgruppe) VALUES (5, 'Gruppe 10')''')
    con.execute('''INSERT INTO prisgrupper (id, prisgruppe) VALUES (6, 'Gruppe honør 10')''')
    con.commit()

# insert prisgrupperITeaterstykker
Kongesemnene = [1,2,3,5,6]
StørstAvAltErKjærligheten = [1,2,3,4,5,6]
KongesemnenePriser = [450,380,280,420,360]
StørstAvAltErKjærlighetenPriser = [350,300,220,220,320,270]

if(con.execute('''SELECT * FROM prisgrupperITeaterstykker''').fetchone() == None):
    for i in range(len(Kongesemnene)):
        con.execute('''INSERT INTO prisgrupperITeaterstyker (prisgruppe_id, teaterstykke_id, pris) VALUES (kongesemnene[i], 1, KongesemnenePriser[i])''')
    for i in range(len(StørstAvAltErKjærligheten)):
        con.execute('''INSERT INTO prisgrupperITeaterstyker (prisgruppe_id, teaterstykke_id, pris) VALUES (StørstAvAltErKjærligheten[i], 2, StørstAvAltErKjærlighetenPriser[i])''')
    con.commit()

#TODO: insert stoler
#TODO: insert billetter
#TODO: insert ansatt
#TODO: insert oppgaver
#TODO: insert ansattIoppgave
#TODO: insert akt
#TODO: insert roller
#TODO: insert skuespillere
#TODO: insert skuespillerIRolle
#TODO: insert rolleiakt

# Insert data

gamleScene = 'db-projekt/gamle-scene.txt'
hovedScene = 'db-projekt/hoved-scenen.txt'

# les gamle scene data

openFile = open(gamleScene, 'r')
lines = openFile.readlines()
openFile.close()
lines = [line.strip() for line in lines]
# for line in lines:





con.close()