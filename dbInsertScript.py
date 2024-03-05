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
    con.execute('''INSERT INTO Teatersal (Sesong, SalNavn, TeaterstykkeID) VALUES ('vinter2024', 'gamle scene', 1)''')
    con.execute('''INSERT INTO Teatersal (Sesong, SalNavn, TeaterstykkeID) VALUES ('vinter2024', 'hovedscene', 2)''')
    con.execute('''INSERT INTO Teatersal (Sesong, SalNavn, TeaterstykkeID) VALUES ('vår2024', 'gamle scene', 1)''')
    con.execute('''INSERT INTO Teatersal (Sesong, SalNavn, TeaterstykkeID) VALUES ('vår2024', 'hovedscene', 2)''')

#insert forestillinger
kongesemneneForestillinger = ['2024-02-01', '2024-02-02', '2024-02-03', '2024-02-05', '2024-02-06']
størstAvAltErKjærlighetenForestillinger = ['2024-02-03', '2024-02-06', '2024-02-07', '2024-02-12', '2024-02-13', '2024-02-14']
if(con.execute('''SELECT * FROM Forestilling''').fetchone() == None):
    id = 0
    for i in kongesemneneForestillinger:
        con.execute(f"INSERT INTO forestilling (ForestillingID, Dato, Klokkeslett, TeaterstykkeID) VALUES ({id}, '{i}', '19:00', 1)")
        id += 1
    for i in størstAvAltErKjærlighetenForestillinger:
        con.execute(f"INSERT INTO forestilling (ForestillingID, Dato, Klokkeslett, TeaterstykkeID) VALUES ({id}, '{i}', '18:30', 2)")
        id += 1
    con.commit()

kongesemnene = [0, 1, 2, 4, 5]
størstAvAltErKjærligheten = [0, 1, 2, 3, 4, 5]
prisgruppeNavnListe = ["Ordinær","Honnør","Student","Barn","Gruppe 10","Gruppe Honnør"]
kongesemnenePriser = [450, 380, 280, 420, 360]
størstAvAltErKjærlighetenPriser = [350, 300, 220, 220, 320, 270]
# insert prisgrupper
if(con.execute('''SELECT * FROM Prisgruppe''').fetchone() == None):
    for i in range(len(kongesemnene)):
        con.execute(f"INSERT INTO Prisgruppe (TeaterstykkeID, PrisgruppeNavn, Pris) VALUES (1, '{prisgruppeNavnListe[kongesemnene[i]]}', {kongesemnenePriser[i]})")
    for i in range(len(størstAvAltErKjærligheten)):
        con.execute(f"INSERT INTO Prisgruppe (TeaterstykkeID, PrisgruppeNavn, Pris) VALUES (2, '{prisgruppeNavnListe[størstAvAltErKjærligheten[i]]}', {størstAvAltErKjærlighetenPriser[i]})")
    con.commit()

sesonger = ["vinter2024", "vår2024"]
gamleSceneOppsett = ["galleri","balkong","parkett"]
gamleSceneStolerGalleri = [[33,18,17], [28,27,22,17],[18,16,17,18,18,17,18,17,17,14]]


# insert stoler gamle scene og hovedscene
if(con.execute('''SELECT * FROM Stol''').fetchone() == None):
    for sesong in sesonger:
        for område in gamleSceneOppsett:
            for rad in range(len(gamleSceneStolerGalleri[gamleSceneOppsett.index(område)])):
                for stol in range(gamleSceneStolerGalleri[gamleSceneOppsett.index(område)][rad]):
                    con.execute(f"INSERT INTO Stol (Sesong, Salnavn, Stolnummer, Radnummer, Områdenavn) VALUES ('{sesong}', 'gamle scene', {stol+1}, {rad+1}, '{område}')")
    con.commit()
    for sesong in sesonger:
        for stol in range(524):
            if stol < 504:
                con.execute(f"INSERT INTO Stol (Sesong, Salnavn, Stolnummer, Radnummer, Områdenavn) VALUES ('{sesong}', 'hovedscene', {stol+1}, {(stol)//28 +1}, 'parkett')")
            elif (stol < 514 and stol > 503):
                con.execute(f"INSERT INTO Stol (Sesong, Salnavn, Stolnummer, Radnummer, Områdenavn) VALUES ('{sesong}', 'hovedscene', {stol+1}, {(stol-504)//5 +1}, 'nedre galleri')")
            elif (stol < 524 and stol > 513):
                con.execute(f"INSERT INTO Stol (Sesong, Salnavn, Stolnummer, Radnummer, Områdenavn) VALUES ('{sesong}', 'hovedscene', {stol+1}, {(stol-514)//5 +1}, 'øvre galleri')")
    con.commit()
    for i in range(495,499):
        con.execute(f"DELETE FROM Stol WHERE Stolnummer = {i} AND Salnavn = 'hovedscene' AND Sesong = 'vår2024'")
        con.execute(f"DELETE FROM Stol WHERE Stolnummer = {i} AND Salnavn = 'hovedscene' AND Sesong = 'vinter2024'")
    for i in range(467,471):
        con.execute(f"DELETE FROM Stol WHERE Stolnummer = {i} AND Salnavn = 'hovedscene' AND Sesong = 'vår2024'")
        con.execute(f"DELETE FROM Stol WHERE Stolnummer = {i} AND Salnavn = 'hovedscene' AND Sesong = 'vinter2024'")
    con.commit()

    


#TODO: insert billetter
#TODO: insert ansatt
    
#TODO: insert oppgaver
# skriver [rolle, ansattnavn, ansattnavn...]
kongesemneneOppgaver = [["inspirent", "Randi Andersen Gafseth", "Emily F. Luthentun"],["sufflør", "Ann Eli Aasgård"],[ "maskeansvarlig","Marianne Aunvik"], ["teknisk koordinator", "Martin Didrichsen"],["lysdesign","Eivind Myren"], ["dramaturg", "Mina Rype Stokke"], ["regi og musikkutvelgelse", "Yury Butusov"], ["scenografi og kostymer", "Aleksandr Shishkin-Hokisai"], ["lysmester", "Are Skarra Kvitnes"], ["lysbordoperatør", "Roger Indgul", "Oliver Løding","Harald Soltvedt" ], ["lyddesign", "Anders Schille"], ["rekvisittansvarlig", "Karl-Martin Hoddevik"], ["sceneansvarlig", "Geir Dyrdal"], ["stykkeansvarlig kostyme", "Trine Bjørhusdal"], ["stykkeansvarlig påkledere","Renee Desmond"], ["tapetserer", "Charlotta Winger"], ["snekker", "Egil Buseth"], ["metallarbeider", "Per Arne Johansen"], ["malersal","Toril Skipnes","Anita Gundersen"]]
størstAvAltErKjærlighetenOppgaver = [["Regi", "Jonas Corell Petersen"], ["scenografi og kostymer", "David Gehrt"], ["musikalsk ansvarlig","Gaute Tønder"], ["lysdesign","Magnus Mikaelsen"], ["dramaturg", "Kristoffer Spender"], ["inspirent", "Line Åmil"], ["sufflør", "Lars Magnus Krogh Utne"], ["maskeansvarlig", "Livinger Ferner Diesen"], ["stykkeansvarlig rekvisitt", "Espen Høyem"], ["stykkeansvarlig kostyme", "Kjersti Eckhoff"], ["stykkeansvarlig påkledere", "Ida Marie Brønstad"], ["lyddesign", "Jan Magne Høyes","Siril Gaare"], ["videodesign","Stein Jørgen Øien"], ["lysbordoperator","Steffen Telstad"], ["sceneansvarlig", "Erik Chan"], ["snekker","Olav Rui"], ["metallarbeider", "Per Arne Johansen"], ["malersal", "Toril Skipnes","Anita Gundersen"]]
# if(con.execute('''SELECT * FROM oppgave''').fetchone() == None):
#     for i in kongesemneneOppgaver:
#         con.execute(f"INSERT INTO oppgave (TeaterstykkeID, Oppgavetype, AnsattID) VALUES (1, '{i}', NULL)")
#     for i in størstAvAltErKjærlighetenOppgaver:
#         con.execute(f"INSERT INTO oppgave (TeaterstykkeID, Oppgavetype, AnsattID) VALUES (2, '{i}', NULL)")
#     con.commit()
skuespillereOgDemsRollerKongs = [["Arturo Scotti", "Haakon Haakonssønn"],["Ingunn Beate Strige Øyen","Inga fra Vartejg (Haakons mor)"],["Hans Petter Nilsen","Skule jarl"],["Madeleine Brandtzæg Nilsen", "Fru Ragnhild (Skules hustru)"],
     ["Synnøve Fossum Eriksen","Margrete (Skules datter)" ], ["Emma Caroline Deichmann","Sigrid (Skules søster) / Ingebjørg"], ["Thomas Jensen Takyi","Biskop Nikolas"],
     ["Per Bogstad Gulliksen", "Gregorius Jonssønn"],["Isak Holmen Sørensen","Paal Flida / Trønder"],["Fabian Heidelberg Lunde","Baard Bratte / Trønder"],["Emil Olafsson", "Jatgeir Skald / Dagfinn Bonde"],["Snorre Ryen Tøndel","Peter (prest og Ingebjørgs sønn)"]]
skuespillereKjærlighet = ["Sunniva Du Mond Nordal","Jo Saberniak","Marte M. Steinholt","Tor Ivar Hagen","Trond-Ove Skrødal","Natalie Grøndahl Tangen", "Åsmund Flaten"]
    
    
    
    
    
    
    
    
    
    
    
    



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