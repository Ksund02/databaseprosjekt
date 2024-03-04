import sqlite3
con = sqlite3.connect('teater.db')

cursor = con.cursor()

# Create tables

#Teatersal
cursor.execute('''CREATE TABLE IF NOT EXISTS Teatersal
               (Sesong TEXT NOT NULL,
               Salnavn TEXT NOT NULL,
               TeaterstykkeID INTEGER,
               PRIMARY KEY(Sesong, Salnavn),
               FOREIGN KEY(TeaterstykkeID) REFERENCES Teaterstykke(TeaterstykkeID))''')

#Stol
cursor.execute('''CREATE TABLE IF NOT EXISTS Stol
                (Sesong TEXT NOT NULL,
                Salnavn TEXT NOT NULL,
                Stolnummer INTEGER NOT NULL,
                Radnummer INTEGER NOT NULL,
                Områdenavn TEXT NOT NULL,
                FOREIGN KEY(Sesong, Salnavn) REFERENCES Teatersal(Sesong, Salnavn),
                PRIMARY KEY(Sesong, Salnavn, Stolnummer, Radnummer, Områdenavn))''')

#Forestilling
cursor.execute('''CREATE TABLE IF NOT EXISTS Forestilling
               (ForestillingID INTEGER PRIMARY KEY,
               Dato TEXT,
               Klokkeslett TEXT,
               TeaterstykkeID INTEGER NOT NULL,
               FOREIGN KEY(TeaterstykkeID) REFERENCES Teaterstykke(TeaterstykkeID))''')

#Billett
cursor.execute('''CREATE TABLE IF NOT EXISTS Billett
               (BillettID INTEGER PRIMARY KEY,
               Sesong TEXT NOT NULL,
               Salnavn TEXT NOT NULL,
               Stolnummer INTEGER NOT NULL,
               Radnummer INTEGER NOT NULL,
               Områdenavn TEXT NOT NULL,
               FOREIGN KEY(Sesong, Salnavn, Stolnummer, Radnummer, Områdenavn) REFERENCES Stol(Sesong, Salnavn, Stolnummer, Radnummer, Områdenavn))''')

#ForestillingBillett
cursor.execute('''CREATE TABLE IF NOT EXISTS ForestillingBillett
               (BillettID INTEGER PRIMARY KEY,
               ForestillingID INTEGER NOT NULL,
               FOREIGN KEY(ForestillingID) REFERENCES Forestilling(ForestillingID))''')

#Billettgruppe
cursor.execute('''CREATE TABLE IF NOT EXISTS Billettgruppe
               (BillettID INTEGER PRIMARY KEY,
               TeaterstykkeID INTEGER NOT NULL,
               Prisgruppenavn TEXT,
               FOREIGN KEY(TeaterstykkeID, Prisgruppenavn) REFERENCES Prisgruppe(TeaterstykkeID, Prisgruppenavn))''')

#BillettKjøp
cursor.execute('''CREATE TABLE IF NOT EXISTS BillettKjøp
               (BillettID INTEGER NOT NULL,
               KundeProfilID INTEGER NOT NULL,
               Dato TEXT,
               Tid TEXT,
               PRIMARY KEY(BillettID, KundeProfilID),
               FOREIGN KEY(BillettID) REFERENCES Billett(BilletID)
               FOREIGN KEY(KundeProfilID) REFERENCES KundeProfil(KundeProfilID))''')

#KundeProfil
cursor.execute('''CREATE TABLE IF NOT EXISTS KundeProfil
               (KundeProfilID INTEGER PRIMARY KEY,
               Mobilnummer INTEGER,
               Navn TEXT,
               Adresse TEXT)''')

#Teaterstykke
cursor.execute('''CREATE TABLE IF NOT EXISTS Teaterstykke
                (TeaterstykkeID INTEGER PRIMARY KEY,
                Name TEXT)''')

#Prisgruppe
cursor.execute('''CREATE TABLE IF NOT EXISTS Prisgruppe
                (TeaterstykkeID INTEGER NOT NULL,
                PrisgruppeNavn TEXT NOT NULL,
                Pris INTEGER,
                PRIMARY KEY(TeaterstykkeID, PrisgruppeNavn),
                FOREIGN KEY(TeaterstykkeID) REFERENCES Teaterstykke(TeaterstykkeID))''')

#Rolle
cursor.execute('''CREATE TABLE IF NOT EXISTS Rolle
                (TeaterstykkeID INTEGER NOT NULL,
                Rollenavn TEXT,
                PRIMARY KEY(Rollenavn, TeaterstykkeID),
                FOREIGN KEY(TeaterstykkeID) REFERENCES Teaterstykke(TeaterstykkeID))''')

#Akt
cursor.execute('''CREATE TABLE IF NOT EXISTS Akt
                (Aktnummer INTEGER NOT NULL,
                TeaterstykkeID INTEGER NOT NULL,
                Aktnavn TEXT,
                PRIMARY KEY(Aktnummer, TeaterstykkeID),
                FOREIGN KEY(TeaterstykkeID) REFERENCES Teaterstykke(TeaterstykkeID))''')

#SkuespillerAnsatt
cursor.execute('''CREATE TABLE IF NOT EXISTS SkuespillerAnsatt
                (TeaterstykkeID INTEGER NOT NULL,
                Rollenavn TEXT NOT NULL,
                AnsattID INTEGER NOT NULL,
                PRIMARY KEY(TeaterstykkeID, Rollenavn, AnsattID),
                FOREIGN KEY(TeaterstykkeID) REFERENCES Teaterstykke(TeaterstykkeID),
                FOREIGN KEY(TeaterstykkeID, Rollenavn) REFERENCES Rolle(TeaterstykkeID, Rollenavn))''')

#RolleIAkt
cursor.execute('''CREATE TABLE IF NOT EXISTS RolleIAkt
                (Rollenavn TEXT NOT NULL,
                Aktnummer INTEGER NOT NULL,
                TeaterstykkeID INTEGER NOT NULL,
                PRIMARY KEY(Rollenavn, Aktnummer, TeaterstykkeID),
                FOREIGN KEY(TeaterstykkeID, Rollenavn) REFERENCES Rolle(TeaterstykkeID, Rollenavn),
                FOREIGN KEY(TeaterstykkeID, Aktnummer) REFERENCES Akt(TeaterstykkeID, Aktnummer))''')

#Ansatt
cursor.execute('''CREATE TABLE IF NOT EXISTS Ansatt
               (AnsattID INTEGER PRIMARY KEY,
               Navn TEXT,
               Epost TEXT,
               AnsattStatus TEXT,
               TeaterStykkeID INTEGER NOT NULL,
               FOREIGN KEY(TeaterStykkeID) REFERENCES Teaterstykke(TeaterstykkeID))''')

#Oppgave
cursor.execute('''CREATE TABLE IF NOT EXISTS Oppgave
               (TeaterStykkeID INTEGER NOT NULL,
               Oppgavetype TEXT NOT NULL,
               AnsattID INTEGER NOT NULL,
               PRIMARY KEY(TeaterStykkeID, Oppgavetype),
               FOREIGN KEY(TeaterStykkeID, Oppgavetype) REFERENCES Oppgave(TeaterStykkeID, Oppgavetype),
               FOREIGN KEY(AnsattID) REFERENCES Ansatt(AnsattID))''')


con.commit()

# insert teaterstykker
if(con.execute('''SELECT * FROM Teaterstykke''').fetchone() == None):
    con.execute('''INSERT INTO Teaterstykke (TeaterstykkeID, Name) VALUES (1, 'Kongsemnene')''')
    con.execute('''INSERT INTO Teaterstykke (TeaterstykkeID, Name) VALUES (2, 'Størst av alt er kjærligheten')''')

# insert Saler
if(con.execute('''SELECT * FROM Teatersal''').fetchone() == None):
    con.execute('''INSERT INTO Teatersal (Sesong, SalNavn) VALUES ('vinter2024', 'gamle scene')''')
    con.execute('''INSERT INTO Teatersal (Sesong, SalNavn) VALUES ('vinter2024', 'hovedscene')''')
    con.execute('''INSERT INTO Teatersal (Sesong, SalNavn) VALUES ('vår2024', 'gamle scene')''')
    con.execute('''INSERT INTO Teatersal (Sesong, SalNavn) VALUES ('vår2024', 'hovedscene')''')

#insert forestillinger
kongesemneneForestillinger = ['2024-02-01', '2024-02-02', '2024-02-03', '2024-02-05', '2024-02-06']
størstAvAltErKjærlighetenForestillinger = ['2024-02-03', '2024-02-06', '2024-02-07', '2024-02-12', '2024-02-13', '2024-02-14']
if(con.execute('''SELECT * FROM Forestilling''').fetchone() == None):
    for id, i in enumerate(kongesemneneForestillinger):
        con.execute(f"INSERT INTO forestilling (ForestillingID, Dato, Klokkeslett, TeaterstykkeID) VALUES ({id}, '{i}', '19:00', 1)")
        id += 1
    for i in størstAvAltErKjærlighetenForestillinger:
        con.execute(f"INSERT INTO forestilling (ForestillingID, Dato, Klokkeslett, TeaterstykkeID) VALUES ({id}, '{i}', '18:30', 2)")
        id += 1
    con.commit()


# insert prisgrupper
if(con.execute('''SELECT * FROM Prisgruppe''').fetchone() == None):
    con.execute('''INSERT INTO Prisgruppe (TeaterstykkeID, PrisgruppeNavn, Pris) VALUES (1, 'Ordinær', 1)''') # TODO: Fiks priser!
    con.execute('''INSERT INTO Prisgruppe (TeaterstykkeID, PrisgruppeNavn, Pris) VALUES (2, 'Honør', 1)''')
    con.execute('''INSERT INTO Prisgruppe (TeaterstykkeID, PrisgruppeNavn, Pris) VALUES (3, 'Student', 1)''')
    con.execute('''INSERT INTO Prisgruppe (TeaterstykkeID, PrisgruppeNavn, Pris) VALUES (4, 'Barn', 1)''')
    con.execute('''INSERT INTO Prisgruppe (TeaterstykkeID, PrisgruppeNavn, Pris) VALUES (5, 'Gruppe 10', 1)''')
    con.execute('''INSERT INTO Prisgruppe (TeaterstykkeID, PrisgruppeNavn, Pris) VALUES (6, 'Gruppe honør 10', 1)''')
    con.commit()

# insert prisgrupperITeaterstykker
kongesemnene = [0, 1, 2, 4, 5]
størstAvAltErKjærligheten = [0, 1, 2, 3, 4, 5]
prisgruppeNavnListe = ["Ordinær","Honnør","Student","Barn","Gruppe 10","Gruppe Honnør"]
kongesemnenePriser = [450, 380, 280, 420, 360]
størstAvAltErKjærlighetenPriser = [350, 300, 220, 220, 320, 270]

if(con.execute('''SELECT * FROM Prisgruppe''').fetchone() == None):
    for i in range(len(kongesemnene)):
        con.execute('''INSERT INTO Prisgruppe (TeaterstykkeID, PrisgruppeNavn, Pris) VALUES (1, prisgruppeNavnListe[kongsemnene[i]], kongesemnenePriser[i])''')
    for i in range(len(størstAvAltErKjærligheten)):
        con.execute('''INSERT INTO Prisgruppe (TeaterstykkeID, PrisgruppeNavn, Pris) VALUES (2, prisgruppeNavnListe[størstAvAltErKjærligheten[i]], størstAvAltErKjærlighetenPriser[i])''')
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

gamleScene = './gamle-scene.txt'
hovedScene = './hoved-scenen.txt'

# les gamle scene data

openFile = open(gamleScene, 'r')
lines = openFile.readlines()
openFile.close()
lines = [line.strip() for line in lines]
# for line in lines:

con.close()