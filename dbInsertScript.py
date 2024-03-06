import sqlite3
con = sqlite3.connect('teater.db')

cursor = con.cursor()

# Create tables

with open('tables.sql', 'r') as schema:
    schemaArray = schema.read().split(';')
    for command in schemaArray:
        cursor.execute(command)

con.commit()


# #Teatersal
# cursor.execute('''CREATE TABLE IF NOT EXISTS Teatersal
#                (Sesong TEXT NOT NULL,
#                Salnavn TEXT NOT NULL,
#                TeaterstykkeID INTEGER,
#                PRIMARY KEY(Sesong, Salnavn),
#                FOREIGN KEY(TeaterstykkeID) REFERENCES Teaterstykke(TeaterstykkeID))''')

# #Stol
# cursor.execute('''CREATE TABLE IF NOT EXISTS Stol
#                 (Sesong TEXT NOT NULL,
#                 Salnavn TEXT NOT NULL,
#                 Stolnummer INTEGER NOT NULL,
#                 Radnummer INTEGER NOT NULL,
#                 Omraadenavn TEXT NOT NULL,
#                 FOREIGN KEY(Sesong, Salnavn) REFERENCES Teatersal(Sesong, Salnavn),
#                 PRIMARY KEY(Sesong, Salnavn, Stolnummer, Radnummer, Omraadenavn))''')

# #Forestilling
# cursor.execute('''CREATE TABLE IF NOT EXISTS Forestilling
#                (ForestillingID INTEGER PRIMARY KEY,
#                Dato TEXT,
#                Klokkeslett TEXT,
#                TeaterstykkeID INTEGER NOT NULL,
#                FOREIGN KEY(TeaterstykkeID) REFERENCES Teaterstykke(TeaterstykkeID))''')

# #Billett
# cursor.execute('''CREATE TABLE IF NOT EXISTS Billett
#                (BillettID INTEGER PRIMARY KEY,
#                Sesong TEXT NOT NULL,
#                Salnavn TEXT NOT NULL,
#                Stolnummer INTEGER NOT NULL,
#                Radnummer INTEGER NOT NULL,
#                Omraadenavn TEXT NOT NULL,
#                FOREIGN KEY(Sesong, Salnavn, Stolnummer, Radnummer, Omraadenavn) REFERENCES Stol(Sesong, Salnavn, Stolnummer, Radnummer, Omraadenavn))''')

# #ForestillingBillett
# cursor.execute('''CREATE TABLE IF NOT EXISTS ForestillingBillett
#                (BillettID INTEGER PRIMARY KEY,
#                ForestillingID INTEGER NOT NULL,
#                FOREIGN KEY(ForestillingID) REFERENCES Forestilling(ForestillingID))''')

# #Billettgruppe
# cursor.execute('''CREATE TABLE IF NOT EXISTS Billettgruppe
#                (BillettID INTEGER PRIMARY KEY,
#                TeaterstykkeID INTEGER NOT NULL,
#                Prisgruppenavn TEXT,
#                FOREIGN KEY(TeaterstykkeID, Prisgruppenavn) REFERENCES Prisgruppe(TeaterstykkeID, Prisgruppenavn))''')

# #BillettKjop
# cursor.execute('''CREATE TABLE IF NOT EXISTS BillettKjop
#                (BillettID INTEGER NOT NULL,
#                KundeProfilID INTEGER NOT NULL,
#                Dato TEXT,
#                Tid TEXT,
#                PRIMARY KEY(BillettID, KundeProfilID),
#                FOREIGN KEY(BillettID) REFERENCES Billett(BilletID)
#                FOREIGN KEY(KundeProfilID) REFERENCES KundeProfil(KundeProfilID))''')

# #KundeProfil
# cursor.execute('''CREATE TABLE IF NOT EXISTS KundeProfil
#                (KundeProfilID INTEGER PRIMARY KEY,
#                Mobilnummer INTEGER,
#                Navn TEXT,
#                Adresse TEXT)''')

# #Teaterstykke
# cursor.execute('''CREATE TABLE IF NOT EXISTS Teaterstykke
#                 (TeaterstykkeID INTEGER PRIMARY KEY,
#                 Name TEXT)''')

# #Prisgruppe
# cursor.execute('''CREATE TABLE IF NOT EXISTS Prisgruppe
#                 (TeaterstykkeID INTEGER NOT NULL,
#                 PrisgruppeNavn TEXT NOT NULL,
#                 Pris INTEGER,
#                 PRIMARY KEY(TeaterstykkeID, PrisgruppeNavn),
#                 FOREIGN KEY(TeaterstykkeID) REFERENCES Teaterstykke(TeaterstykkeID))''')

# #Rolle
# cursor.execute('''CREATE TABLE IF NOT EXISTS Rolle
#                 (TeaterstykkeID INTEGER NOT NULL,
#                 Rollenavn TEXT,
#                 PRIMARY KEY(Rollenavn, TeaterstykkeID),
#                 FOREIGN KEY(TeaterstykkeID) REFERENCES Teaterstykke(TeaterstykkeID))''')

# #Akt
# cursor.execute('''CREATE TABLE IF NOT EXISTS Akt
#                 (Aktnummer INTEGER NOT NULL,
#                 TeaterstykkeID INTEGER NOT NULL,
#                 Aktnavn TEXT,
#                 PRIMARY KEY(Aktnummer, TeaterstykkeID),
#                 FOREIGN KEY(TeaterstykkeID) REFERENCES Teaterstykke(TeaterstykkeID))''')

# #SkuespillerAnsatt
# cursor.execute('''CREATE TABLE IF NOT EXISTS SkuespillerAnsatt
#                 (TeaterstykkeID INTEGER NOT NULL,
#                 Rollenavn TEXT NOT NULL,
#                 AnsattID INTEGER NOT NULL,
#                 PRIMARY KEY(TeaterstykkeID, Rollenavn, AnsattID),
#                 FOREIGN KEY(TeaterstykkeID) REFERENCES Teaterstykke(TeaterstykkeID),
#                 FOREIGN KEY(TeaterstykkeID, Rollenavn) REFERENCES Rolle(TeaterstykkeID, Rollenavn))''')

# #RolleIAkt
# cursor.execute('''CREATE TABLE IF NOT EXISTS RolleIAkt
#                 (Rollenavn TEXT NOT NULL,
#                 Aktnummer INTEGER NOT NULL,
#                 TeaterstykkeID INTEGER NOT NULL,
#                 PRIMARY KEY(Rollenavn, Aktnummer, TeaterstykkeID),
#                 FOREIGN KEY(TeaterstykkeID, Rollenavn) REFERENCES Rolle(TeaterstykkeID, Rollenavn),
#                 FOREIGN KEY(TeaterstykkeID, Aktnummer) REFERENCES Akt(TeaterstykkeID, Aktnummer))''')

# #Ansatt
# cursor.execute('''CREATE TABLE IF NOT EXISTS Ansatt
#                (AnsattID INTEGER PRIMARY KEY,
#                Navn TEXT,
#                Epost TEXT,
#                AnsattStatus TEXT,
#                TeaterStykkeID INTEGER NOT NULL,
#                FOREIGN KEY(TeaterStykkeID) REFERENCES Teaterstykke(TeaterstykkeID))''')

# #Oppgave
# cursor.execute('''CREATE TABLE IF NOT EXISTS Oppgave
#                (TeaterStykkeID INTEGER NOT NULL,
#                Oppgavetype TEXT NOT NULL,
#                AnsattID INTEGER NOT NULL,
#                PRIMARY KEY(TeaterStykkeID, Oppgavetype),
#                FOREIGN KEY(TeaterStykkeID, Oppgavetype) REFERENCES Oppgave(TeaterStykkeID, Oppgavetype),
#                FOREIGN KEY(AnsattID) REFERENCES Ansatt(AnsattID))''')


con.commit()

# insert teaterstykker
if(con.execute('''SELECT * FROM Teaterstykke''').fetchone() == None):
    con.execute('''INSERT INTO Teaterstykke (TeaterstykkeID, Name) VALUES (1, 'Kongsemnene')''')
    con.execute('''INSERT INTO Teaterstykke (TeaterstykkeID, Name) VALUES (2, 'Storst av alt er kjærligheten')''')

# insert Saler
if(con.execute('''SELECT * FROM Teatersal''').fetchone() == None):
    con.execute('''INSERT INTO Teatersal (Sesong, SalNavn, TeaterstykkeID) VALUES ('vinter2024', 'gamle scene', 1)''')
    con.execute('''INSERT INTO Teatersal (Sesong, SalNavn, TeaterstykkeID) VALUES ('vinter2024', 'hovedscene', 2)''')
    con.execute('''INSERT INTO Teatersal (Sesong, SalNavn, TeaterstykkeID) VALUES ('vaar2024', 'gamle scene', 1)''')
    con.execute('''INSERT INTO Teatersal (Sesong, SalNavn, TeaterstykkeID) VALUES ('vaar2024', 'hovedscene', 2)''')

#insert forestillinger
kongesemneneForestillinger = ['2024-02-01', '2024-02-02', '2024-02-03', '2024-02-05', '2024-02-06']
storstAvAltErKjærlighetenForestillinger = ['2024-02-03', '2024-02-06', '2024-02-07', '2024-02-12', '2024-02-13', '2024-02-14']
if(con.execute('''SELECT * FROM Forestilling''').fetchone() == None):
    id = 0
    for i in kongesemneneForestillinger:
        con.execute(f"INSERT INTO forestilling (ForestillingID, Dato, Klokkeslett, TeaterstykkeID) VALUES ({id}, '{i}', '19:00', 1)")
        id += 1
    for i in storstAvAltErKjærlighetenForestillinger:
        con.execute(f"INSERT INTO forestilling (ForestillingID, Dato, Klokkeslett, TeaterstykkeID) VALUES ({id}, '{i}', '18:30', 2)")
        id += 1
    con.commit()

kongesemnene = [0, 1, 2, 4, 5]
storstAvAltErKjærligheten = [0, 1, 2, 3, 4, 5]
prisgruppeNavnListe = ["Ordinær","Honnor","Student","Barn","Gruppe 10","Gruppe Honnor 10"]
kongesemnenePriser = [450, 380, 280, 420, 360]
storstAvAltErKjærlighetenPriser = [350, 300, 220, 220, 320, 270]
# insert prisgrupper
if(con.execute('''SELECT * FROM Prisgruppe''').fetchone() == None):
    for i in range(len(kongesemnene)):
        con.execute(f"INSERT INTO Prisgruppe (TeaterstykkeID, PrisgruppeNavn, Pris) VALUES (1, '{prisgruppeNavnListe[kongesemnene[i]]}', {kongesemnenePriser[i]})")
    for i in range(len(storstAvAltErKjærligheten)):
        con.execute(f"INSERT INTO Prisgruppe (TeaterstykkeID, PrisgruppeNavn, Pris) VALUES (2, '{prisgruppeNavnListe[storstAvAltErKjærligheten[i]]}', {storstAvAltErKjærlighetenPriser[i]})")
    con.commit()

sesonger = ["vinter2024", "vaar2024"]
gamleSceneOppsett = ["galleri","balkong","parkett"]
gamleSceneStolerGalleri = [[33,18,17], [28,27,22,17],[18,16,17,18,18,17,18,17,17,14]]


# insert stoler gamle scene og hovedscene
if(con.execute('''SELECT * FROM Stol''').fetchone() == None):
    for sesong in sesonger:
        for omraade in gamleSceneOppsett:
            for rad in range(len(gamleSceneStolerGalleri[gamleSceneOppsett.index(omraade)])):
                for stol in range(gamleSceneStolerGalleri[gamleSceneOppsett.index(omraade)][rad]):
                    con.execute(f"INSERT INTO Stol (Sesong, Salnavn, Stolnummer, Radnummer, Omraadenavn) VALUES ('{sesong}', 'gamle scene', {stol+1}, {rad+1}, '{omraade}')")
    con.commit()
    for sesong in sesonger:
        for stol in range(524):
            if stol < 504:
                con.execute(f"INSERT INTO Stol (Sesong, Salnavn, Stolnummer, Radnummer, Omraadenavn) VALUES ('{sesong}', 'hovedscene', {stol+1}, {(stol)//28 +1}, 'parkett')")
            elif (stol < 514 and stol > 503):
                con.execute(f"INSERT INTO Stol (Sesong, Salnavn, Stolnummer, Radnummer, Omraadenavn) VALUES ('{sesong}', 'hovedscene', {stol+1}, {(stol-504)//5 +1}, 'nedre galleri')")
            elif (stol < 524 and stol > 513):
                con.execute(f"INSERT INTO Stol (Sesong, Salnavn, Stolnummer, Radnummer, Omraadenavn) VALUES ('{sesong}', 'hovedscene', {stol+1}, {(stol-514)//5 +1}, 'ovre galleri')")
    con.commit()
    for i in range(495,499):
        con.execute(f"DELETE FROM Stol WHERE Stolnummer = {i} AND Salnavn = 'hovedscene' AND Sesong = 'vaar2024'")
        con.execute(f"DELETE FROM Stol WHERE Stolnummer = {i} AND Salnavn = 'hovedscene' AND Sesong = 'vinter2024'")
    for i in range(467,471):
        con.execute(f"DELETE FROM Stol WHERE Stolnummer = {i} AND Salnavn = 'hovedscene' AND Sesong = 'vaar2024'")
        con.execute(f"DELETE FROM Stol WHERE Stolnummer = {i} AND Salnavn = 'hovedscene' AND Sesong = 'vinter2024'")
    con.commit()

    


#TODO: insert billetter
#TODO: insert ansatt
    
kongesemneneOppgaver = [["inspirent", "Randi Andersen Gafseth", "Emily F. Luthentun"],["sufflor", "Ann Eli Aasgaard"],[ "maskeansvarlig","Marianne Aunvik"], ["teknisk koordinator", "Martin Didrichsen"],["lysdesign","Eivind Myren"], ["dramaturg", "Mina Rype Stokke"], ["regi og musikkutvelgelse", "Yury Butusov"], ["scenografi og kostymer", "Aleksandr Shishkin-Hokisai"], ["lysmester", "Are Skarra Kvitnes"], ["lysbordoperator", "Roger Indgul", "Oliver Loding","Harald Soltvedt" ], ["lyddesign", "Anders Schille"], ["rekvisittansvarlig", "Karl-Martin Hoddevik"], ["sceneansvarlig", "Geir Dyrdal"], ["stykkeansvarlig kostyme", "Trine Bjorhusdal"], ["stykkeansvarlig paakledere","Renee Desmond"], ["tapetserer", "Charlotta Winger"], ["snekker", "Egil Buseth"], ["metallarbeider", "Per Arne Johansen"], ["malersal","Toril Skipnes","Anita Gundersen"]]
storstAvAltErKjærlighetenOppgaver = [["Regi", "Jonas Corell Petersen"], ["scenografi og kostymer", "David Gehrt"], ["musikalsk ansvarlig","Gaute Tonder"], ["lysdesign","Magnus Mikaelsen"], ["dramaturg", "Kristoffer Spender"], ["inspirent", "Line aamil"], ["sufflor", "Lars Magnus Krogh Utne"], ["maskeansvarlig", "Livinger Ferner Diesen"], ["stykkeansvarlig rekvisitt", "Espen Hoyem"], ["stykkeansvarlig kostyme", "Kjersti Eckhoff"], ["stykkeansvarlig paakledere", "Ida Marie Bronstad"], ["lyddesign", "Jan Magne Hoyes","Siril Gaare"], ["videodesign","Stein Jorgen oien"], ["lysbordoperator","Steffen Telstad"], ["sceneansvarlig", "Erik Chan"], ["snekker","Olav Rui"], ["metallarbeider", "Per Arne Johansen"], ["malersal", "Toril Skipnes","Anita Gundersen"]]

fastAnsatte = ['Mira Dyrnes Askelund', 'Kine Bendixen', 'Ingrid Bergstrom', 'Stephen Brandt-Hansen', 'oyvind Brandtzæg', 'Emma Caroline Deichmann', 'Hildegunn Eggen', 'Carl Martin Eggesbo', 'Christian Eidem', 'Synnove Fossum Eriksen', 'Ragne Grande', 'Per Bogstad Gulliksen', 'Tor Ivar Hagen', 'Erik J. Hauge', 'Hallvard Holmen', 'Kenneth Homstad', 'Paal Herman Ims', 'Haakon Mjaaset Johansen', 'Janne Kokkin', 'Katja Brita Lindeberg', 'Fabian Heidelberg Lunde', 'Elisabeth Matheson', 'Kari Eline Kristvik Meinhardt', 'Marianne Meloy', 'Ivar Nergaard', 'Hans Petter Nilsen', 'Madeleine Brandtzæg Nilsen', 'Sunniva Du Mond Nordal', 'Emil Olafsson', 'Jovan Pavlovic', 'Iren Reppen', 'Jon Lockert Rohde', 'Jo Saberniak', 'Arturo Scotti', 'Trond-Ove Skrodal', 'Haakon Mustafa Akdokur Smestad', 'Marte M. Steinholt', 'Kathrine Strugstad', 'Isak Holmen Sorensen', 'Thomas Jensen Takyi', 'Natalie Grondahl Tangen', 'Snorre Ryen Tondel', 'Staale Kvarme Torring', 'Anna Ueland', 'Ingunn Beate Strige oyen']

# ansatteIkonge = []
# for i in kongesemneneOppgaver:
#     for j in i:
#         if j>0:
#             ansatteIkonge.append(j)
# ansatteIkjærlighet = []
# for i in storstAvAltErKjærlighetenOppgaver:
#     for j in i:
#         if j>0:
#             ansatteIkjærlighet.append(j)
        
        
# fastAnsatteIkonge = []
# for i in ansatteIkonge:
#     if i in fastAnsatte:
#         fastAnsatteIkonge.append(j)
# fastAnsatteIkjærlighet = []
# for i in fastAnsatteIkjærlighet:
#     if i in fastAnsatte:        
#         fastAnsatteIkjærlighet.append(j)

# insert fast ansatte
#     if(con.execute('''SELECT * FROM Ansatt''').fetchone() == None):
#         id = 0
#         for i in fastAnsatteIkonge:
#             con.execute(f"INSERT INTO Ansatt (AnsattID, Navn, Epost, AnsattStatus, TeaterstykkeID) VALUES ({id}, '{i}', NULL, 'fast', 1)")
#             id+=1
#         for i in fastAnsatteIkjærlighet:
#             con.execute(f"INSERT INTO Ansatt (AnsattID, Navn, Epost, AnsattStatus, TeaterstykkeID) VALUES ({id}, '{i}', NULL, 'fast', 2)")
#             id+=1
#         con.commit()

# if(con.execute('''SELECT * FROM Ansatt''').fetchone() == None):
#     id = 0
#     for i in fastAnsatte:
#         con.execute(f"INSERT INTO Ansatt (AnsattID, Navn, Epost, AnsattStatus, TeaterstykkeID) VALUES ({id}, '{i}', NULL, 'fast', NULL)")
#         id+=1
#     con.commit()
    
#TODO: insert oppgaver
# skriver [rolle, ansattnavn, ansattnavn...]
# if(con.execute('''SELECT * FROM oppgave''').fetchone() == None):
#     for i in kongesemneneOppgaver:
#         con.execute(f"INSERT INTO oppgave (TeaterstykkeID, Oppgavetype, AnsattID) VALUES (1, '{i}', NULL)")
#     for i in storstAvAltErKjærlighetenOppgaver:
#         con.execute(f"INSERT INTO oppgave (TeaterstykkeID, Oppgavetype, AnsattID) VALUES (2, '{i}', NULL)")
#     con.commit()
skuespillereOgDemsRollerKongs = [["Arturo Scotti", "Haakon Haakonssonn"],["Ingunn Beate Strige oyen","Inga fra Vartejg (Haakons mor)"],
                                ["Hans Petter Nilsen","Skule jarl"],["Madeleine Brandtzæg Nilsen", "Fru Ragnhild (Skules hustru)"],
                                ["Synnove Fossum Eriksen","Margrete (Skules datter)" ], ["Emma Caroline Deichmann","Sigrid (Skules soster) / Ingebjorg"],
                                ["Thomas Jensen Takyi","Biskop Nikolas"],["Per Bogstad Gulliksen", "Gregorius Jonssonn"],
                                ["Isak Holmen Sorensen","Paal Flida / Tronder"],["Fabian Heidelberg Lunde","Baard Bratte / Tronder"],
                                ["Emil Olafsson", "Jatgeir Skald / Dagfinn Bonde"],["Snorre Ryen Tondel","Peter (prest og Ingebjorgs sonn)"]]

skuespillereKjærlighet = ["Sunniva Du Mond Nordal","Jo Saberniak","Marte M. Steinholt","Tor Ivar Hagen","Trond-Ove Skrodal","Natalie Grondahl Tangen", "aasmund Flaten"]

    
    
    
    
    
    
    
    
    
    



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