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

# Insert teaterstykker
if(con.execute('''SELECT * FROM Teaterstykke''').fetchone() == None):
    con.execute('''INSERT INTO Teaterstykke (TeaterstykkeID, Name) VALUES (0, 'Kongsemnene')''')
    con.execute('''INSERT INTO Teaterstykke (TeaterstykkeID, Name) VALUES (1, 'Størst av alt er kjærligheten')''')

# Insert Saler
if(con.execute('''SELECT * FROM Teatersal''').fetchone() == None):
    con.execute('''INSERT INTO Teatersal (Sesong, SalNavn, TeaterstykkeID) VALUES ('vinter2024', 'gamle scene', 0)''')
    con.execute('''INSERT INTO Teatersal (Sesong, SalNavn, TeaterstykkeID) VALUES ('vinter2024', 'hovedscene', 1)''')
    con.execute('''INSERT INTO Teatersal (Sesong, SalNavn, TeaterstykkeID) VALUES ('vår2024', 'gamle scene', 0)''')
    con.execute('''INSERT INTO Teatersal (Sesong, SalNavn, TeaterstykkeID) VALUES ('vår2024', 'hovedscene', 1)''')

# Insert forestillinger
forestillinger = [
    ['2024-02-01', '2024-02-02', '2024-02-03', '2024-02-05', '2024-02-06'], # TeaterstykkeID 0 Hovedscenen
    ['2024-02-03', '2024-02-06', '2024-02-07', '2024-02-12', '2024-02-13', '2024-02-14'] # TeaterstykkeID 1 Gamle scene
]
klokkeslett = ['19:00', '18:30']

if(con.execute('''SELECT * FROM Forestilling''').fetchone() == None):
    teaterstykkeID, forestillingID = 0, 0
    for tid in klokkeslett:
        for dato in forestillinger[teaterstykkeID]:
            con.execute(f"INSERT INTO forestilling (ForestillingID, Dato, Klokkeslett, TeaterstykkeID) VALUES ({forestillingID}, '{dato}', '{tid}', {teaterstykkeID})")
            forestillingID += 1
        teaterstykkeID += 1
    con.commit()

"""
kongesemneneForestillinger = ['2024-02-01', '2024-02-02', '2024-02-03', '2024-02-05', '2024-02-06']
storstAvAltErKjærlighetenForestillinger = ['2024-02-03', '2024-02-06', '2024-02-07', '2024-02-12', '2024-02-13', '2024-02-14']
if(con.execute('''SELECT * FROM Forestilling''').fetchone() == None):
    id = 0
    for i in kongesemneneForestillinger:
        con.execute(f"INSERT INTO forestilling (ForestillingID, Dato, Klokkeslett, TeaterstykkeID) VALUES ({id}, '{i}', '19:00', 0)")
        id += 1
    for i in storstAvAltErKjærlighetenForestillinger:
        con.execute(f"INSERT INTO forestilling (ForestillingID, Dato, Klokkeslett, TeaterstykkeID) VALUES ({id}, '{i}', '18:30', 1)")
        id += 1
    con.commit()
"""
"""
kongesemnene = [0, 1, 2, 4, 5]
storstAvAltErKjærligheten = [0, 1, 2, 3, 4, 5]
prisgruppeNavnListe = ["Ordinær","Honnor","Student","Barn","Gruppe 10","Gruppe Honnor 10"]
kongesemnenePriser = [450, 380, 280, 420, 360]
storstAvAltErKjærlighetenPriser = [350, 300, 220, 220, 320, 270]

# insert prisgrupper
if(con.execute('''SELECT * FROM Prisgruppe''').fetchone() == None):
    for i in range(len(kongesemnene)):
        con.execute(f"INSERT INTO Prisgruppe (TeaterstykkeID, PrisgruppeNavn, Pris) VALUES (0, '{prisgruppeNavnListe[kongesemnene[i]]}', {kongesemnenePriser[i]})")
    for i in range(len(storstAvAltErKjærligheten)):
        con.execute(f"INSERT INTO Prisgruppe (TeaterstykkeID, PrisgruppeNavn, Pris) VALUES (1, '{prisgruppeNavnListe[storstAvAltErKjærligheten[i]]}', {storstAvAltErKjærlighetenPriser[i]})")
    con.commit()
"""

lovligePrisgrupper = {
        "Ordinær": [450, 350],
        "Honnør": [380, 300],
        "Student": [280, 220],
        "Barn": [None, 220],
        "Gruppe 10": [420, 320],
        "Gruppe Honnør 10": [360, 270]
    }

if(con.execute('''SELECT * FROM Prisgruppe''').fetchone() == None):
    for teaterstykkeID in range(2):
        for prisgruppeNavn in lovligePrisgrupper.keys():
            if (pris := lovligePrisgrupper[prisgruppeNavn][teaterstykkeID]) is not None:
                con.execute(f"INSERT INTO Prisgruppe (TeaterstykkeID, PrisgruppeNavn, Pris) VALUES ({teaterstykkeID}, '{prisgruppeNavn}', {pris})")
    con.commit()

"""
sesonger = ["vinter2024", "vaar2024"]
gamleSceneOppsett = ["galleri", "balkong", "parkett"]
gamleSceneStolerGalleri = [[33,18,17], [28,27,22,17], [18,16,17,18,18,17,18,17,17,14]]

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
"""

sesonger = ["vinter2024", "vaar2024"]
gamleSceneStruktur = {
    "galleri": [33,18,17],
    "balkong": [28,27,22,17],
    "parkett": [18,16,17,18,18,17,18,17,17,14]
}

# insert stoler gamle scene og hovedscene
if(con.execute('''SELECT * FROM Stol''').fetchone() == None):
    for sesong in sesonger:
        for omraade in gamleSceneStruktur.keys():
            for rad in range(len(gamleSceneStruktur[omraade])):
                for stol in range(gamleSceneStruktur[omraade][rad]):
                    con.execute(f"INSERT INTO Stol (Sesong, Salnavn, Stolnummer, Radnummer, Omraadenavn) VALUES ('{sesong}', 'gamle scene', {stol + 1}, {rad + 1}, '{omraade}')")
    con.commit()
    for sesong in sesonger:
        for stol in range(524):
            if stol < 504:
                con.execute(f"INSERT INTO Stol (Sesong, Salnavn, Stolnummer, Radnummer, Omraadenavn) VALUES ('{sesong}', 'hovedscene', {stol + 1}, {(stol)//28 + 1}, 'parkett')")
            elif (stol < 514 and stol > 503):
                con.execute(f"INSERT INTO Stol (Sesong, Salnavn, Stolnummer, Radnummer, Omraadenavn) VALUES ('{sesong}', 'hovedscene', {stol + 1}, {(stol - 504)//5 + 1}, 'nedre galleri')")
            elif (stol < 524 and stol > 513):
                con.execute(f"INSERT INTO Stol (Sesong, Salnavn, Stolnummer, Radnummer, Omraadenavn) VALUES ('{sesong}', 'hovedscene', {stol + 1}, {(stol - 514)//5 + 1}, 'ovre galleri')")
    con.commit()
    for i in range(495,499):
        con.execute(f"DELETE FROM Stol WHERE Stolnummer = {i} AND Salnavn = 'hovedscene' AND Sesong = 'vaar2024'")
        con.execute(f"DELETE FROM Stol WHERE Stolnummer = {i} AND Salnavn = 'hovedscene' AND Sesong = 'vinter2024'")
    for i in range(467,471):
        con.execute(f"DELETE FROM Stol WHERE Stolnummer = {i} AND Salnavn = 'hovedscene' AND Sesong = 'vaar2024'")
        con.execute(f"DELETE FROM Stol WHERE Stolnummer = {i} AND Salnavn = 'hovedscene' AND Sesong = 'vinter2024'")
    con.commit()


kundeProfilEksempel = [12345678, 'Ola Nordmann', 'Verden']

# insert Kundeprofil
if(con.execute('''SELECT * FROM KundeProfil''').fetchone() == None):
    con.execute(f'''INSERT INTO KundeProfil (KundeProfilID, Mobilnummer, Navn, Adresse) VALUES (1, {kundeProfilEksempel[0]}, '{kundeProfilEksempel[1]}', '{kundeProfilEksempel[2]}')''')
    con.commit()

#TODO: insert Billett
# Insert data
GenBillettID = 0
gamleScene = './gamle-scene.txt'
hovedScene = './hovedscenen.txt'

# les gamle scene data

with open(gamleScene, 'r') as openFile:
    lines = [line.strip() for line in openFile.readlines()]
    # for line in lines:
    dato = lines[0]
    lines = lines[1:]
    lines.reverse()
    områder = []
    temp = []
    for line in lines:
        if line not in ["Galleri", "Balkong", "Parkett"]:
            temp.append(line)
        else:
            temp = [line] + temp
            områder.append(temp)
            temp = []

Billetter = []
BillettKjøp = []
#Billetter = [[BillettID, Stolnummer, Radnummer, Omraadenavn],...]
#Billettkjøp = [BillettID,...]

for i in områder:
    for j in range(len(i)):
        if j>0:
            temp = list(i[j])
            for k in range(len(temp)):
                if temp[k] == "1":
                    Billetter.append([GenBillettID, k+1,j,i[0]])
                    BillettKjøp.append(GenBillettID)
                    GenBillettID += 1
                elif temp[k] == "0":
                    Billetter.append([GenBillettID, k+1,j,i[0]])
                    GenBillettID += 1

# Les hovedscene data
openFile = open(hovedScene, 'r')
lines = openFile.readlines()
openFile.close()
lines = [line.strip() for line in lines]
# for line in lines:
datoHoved = lines[0]
lines = lines[1:]
lines.reverse()
områder = []
temp = []
for line in lines:
    if line not in ["Galleri", "Parkett"]:
        temp.append(line)
    else:
        temp = [line] + temp
        områder.append(temp)
        temp = []
BilletterHoved = []
BillettKjøpHoved = []

for i in range(0,2):
    for radIndex, radValues in enumerate(områder[i][1:]):
        for numIndex, numValue in enumerate(list(radValues)): 
            if i == 0: # Om område er Parkett
                #BilletterHoved = [[BillettID, Stolnummer, Radnummer, Omraadenavn],...]
                #BillettkjøpHoved = [BillettID,...]
                if numValue == "1":
                    BilletterHoved.append([GenBillettID, numIndex+1+(28*radIndex), radIndex+1, områder[i][0]])
                    BillettKjøpHoved.append(GenBillettID)
                    GenBillettID+=1
                elif numValue == "0":
                    BilletterHoved.append([GenBillettID, numIndex+1+(28*radIndex), radIndex+1, områder[i][0]])
                    GenBillettID+=1
            elif i == 1: # Om område er Galleri
                if numValue == "1":
                    BilletterHoved.append([GenBillettID, numIndex+1+504+(5*radIndex), radIndex+1, områder[i][0]])
                    BillettKjøpHoved.append(GenBillettID)
                    GenBillettID+=1
                elif numValue == "0":
                    BilletterHoved.append([GenBillettID, numIndex+1+504+(5*radIndex), radIndex+1, områder[i][0]])
                    GenBillettID+=1

                    

# insert billetter
if(con.execute('''SELECT * FROM Billett''').fetchone() == None):
    for Billett in Billetter:
        con.execute(f"INSERT INTO Billett (BillettID, Sesong, Salnavn, Stolnummer, Radnummer, Omraadenavn) VALUES ({Billett[0]}, 'vinter2024', 'gamle scene', {Billett[1]}, {Billett[2]}, '{Billett[3]}')")
    for Billett in BilletterHoved:
        con.execute(f"INSERT INTO Billett (BillettID, Sesong, Salnavn, Stolnummer, Radnummer, Omraadenavn) VALUES ({Billett[0]}, 'vinter2024', 'hovedscene', {Billett[1]}, {Billett[2]}, '{Billett[3]}')")
    con.commit()

# insert BillettKjøp
if(con.execute('''SELECT * FROM BillettKjop''').fetchone() == None):
    for Billett in BillettKjøp:
        con.execute(f"INSERT INTO BillettKjop (BillettID, KundeProfilID, Dato, Tid) VALUES ({Billett},1,'{dato}','00:00')")
    for Billett in BillettKjøpHoved:
        con.execute(f"INSERT INTO BillettKjop (BillettID, KundeProfilID, Dato, Tid) VALUES ({Billett},1, '{datoHoved}', '00:00')")
    con.commit()

#: insert Billetgruppe
if(con.execute('''SELECT * FROM Billettgruppe''').fetchone() == None):
    for Billett in BillettKjøp:
        con.execute(f"INSERT INTO Billettgruppe (BillettID, TeaterstykkeID, Prisgruppenavn) VALUES ({Billett},1,'Gruppe 10')")
    for Billett in BillettKjøpHoved:
        con.execute(f"INSERT INTO Billettgruppe (BillettID, TeaterstykkeID, Prisgruppenavn) VALUES ({Billett},0,'Gruppe 10')")
    con.commit()

#: insert ForestillingBillett
if(con.execute('''SELECT * FROM ForestillingBillett''').fetchone() == None):
    for Billett in BillettKjøp:
        con.execute(f"INSERT INTO ForestillingBillett (BillettID, ForestillingID) VALUES ({Billett},{forestillinger[1].index(dato.split(" ")[1])+len(forestillinger[0])})")
    for Billett in BillettKjøpHoved:
        con.execute(f"INSERT INTO ForestillingBillett (BillettID, ForestillingID) VALUES ({Billett},{forestillinger[0].index(datoHoved.split(" ")[1])})")
    con.commit()

#hovedscenen billetter
kongesemneneOppgaver = [
    ["inspirent", "Randi Andersen Gafseth", "Emily F. Luthentun"],
    ["sufflor", "Ann Eli Aasgaard"],
    [ "maskeansvarlig","Marianne Aunvik"], 
    ["teknisk koordinator", "Martin Didrichsen"],
    ["lysdesign","Eivind Myren"], 
    ["dramaturg", "Mina Rype Stokke"], 
    ["regi og musikkutvelgelse", "Yury Butusov"], 
    ["scenografi og kostymer", "Aleksandr Shishkin-Hokisai"], 
    ["lysmester", "Are Skarra Kvitnes"], 
    ["lysbordoperator", "Roger Indgul", "Oliver Loding","Harald Soltvedt" ], 
    ["lyddesign", "Anders Schille"], 
    ["rekvisittansvarlig", "Karl-Martin Hoddevik"], 
    ["sceneansvarlig", "Geir Dyrdal"], 
    ["stykkeansvarlig kostyme", "Trine Bjorhusdal"], 
    ["stykkeansvarlig paakledere","Renee Desmond"], 
    ["tapetserer", "Charlotta Winger"], 
    ["snekker", "Egil Buseth"], 
    ["metallarbeider", "Per Arne Johansen"], 
    ["malersal","Toril Skipnes","Anita Gundersen"]
]

storstAvAltErKjærlighetenOppgaver = [
    ["Regi", "Jonas Corell Petersen"], 
    ["scenografi og kostymer", "David Gehrt"], 
    ["musikalsk ansvarlig","Gaute Tonder"], 
    ["lysdesign","Magnus Mikaelsen"], 
    ["dramaturg", "Kristoffer Spender"], 
    ["inspirent", "Line aamil"], 
    ["sufflor", "Lars Magnus Krogh Utne"], 
    ["maskeansvarlig", "Livinger Ferner Diesen"], 
    ["stykkeansvarlig rekvisitt", "Espen Hoyem"], 
    ["stykkeansvarlig kostyme", "Kjersti Eckhoff"], 
    ["stykkeansvarlig paakledere", "Ida Marie Bronstad"], 
    ["lyddesign", "Jan Magne Hoyes","Siril Gaare"], 
    ["videodesign","Stein Jorgen oien"], 
    ["lysbordoperator","Steffen Telstad"], 
    ["sceneansvarlig", "Erik Chan"], 
    ["snekker","Olav Rui"], 
    ["metallarbeider", "Per Arne Johansen"], 
    ["malersal", "Toril Skipnes","Anita Gundersen"]
]

fastAnsatte = [
    'Mira Dyrnes Askelund', 
    'Kine Bendixen', 
    'Ingrid Bergstrom', 
    'Stephen Brandt-Hansen', 
    'oyvind Brandtzæg', 
    'Emma Caroline Deichmann', 
    'Hildegunn Eggen', 
    'Carl Martin Eggesbo', 
    'Christian Eidem', 
    'Synnove Fossum Eriksen', 
    'Ragne Grande', 
    'Per Bogstad Gulliksen', 
    'Tor Ivar Hagen', 
    'Erik J. Hauge', 
    'Hallvard Holmen', 
    'Kenneth Homstad', 
    'Paal Herman Ims', 
    'Haakon Mjaaset Johansen', 
    'Janne Kokkin', 
    'Katja Brita Lindeberg', 
    'Fabian Heidelberg Lunde', 
    'Elisabeth Matheson', 
    'Kari Eline Kristvik Meinhardt', 
    'Marianne Meloy', 
    'Ivar Nergaard', 
    'Hans Petter Nilsen', 
    'Madeleine Brandtzæg Nilsen', 
    'Sunniva Du Mond Nordal', 
    'Emil Olafsson', 
    'Jovan Pavlovic', 
    'Iren Reppen', 
    'Jon Lockert Rohde', 
    'Jo Saberniak', 
    'Arturo Scotti', 
    'Trond-Ove Skrodal', 
    'Haakon Mustafa Akdokur Smestad', 
    'Marte M. Steinholt', 
    'Kathrine Strugstad', 
    'Isak Holmen Sorensen', 
    'Thomas Jensen Takyi', 
    'Natalie Grondahl Tangen', 
    'Snorre Ryen Tondel', 
    'Staale Kvarme Torring', 
    'Anna Ueland', 
    'Ingunn Beate Strige oyen'
]

skuespillereOgDemsRollerKongs = [
    ["Arturo Scotti", "Haakon Haakonssonn"],
    ["Ingunn Beate Strige oyen","Inga fra Vartejg (Haakons mor)"],
    ["Hans Petter Nilsen","Skule jarl"],
    ["Madeleine Brandtzæg Nilsen", "Fru Ragnhild (Skules hustru)"],
    ["Synnove Fossum Eriksen","Margrete (Skules datter)" ], 
    ["Emma Caroline Deichmann","Sigrid (Skules soster) / Ingebjorg"],
    ["Thomas Jensen Takyi","Biskop Nikolas"],
    ["Per Bogstad Gulliksen", "Gregorius Jonssonn"],
    ["Isak Holmen Sorensen","Paal Flida / Tronder"],
    ["Fabian Heidelberg Lunde","Baard Bratte / Tronder"],
    ["Emil Olafsson", "Jatgeir Skald / Dagfinn Bonde"],
    ["Snorre Ryen Tondel","Peter (prest og Ingebjorgs sonn)"]
]

skuespillereKjærlighet = [
    "Sunniva Du Mond Nordal",
    "Jo Saberniak",
    "Marte M. Steinholt",
    "Tor Ivar Hagen",
    "Trond-Ove Skrodal",
    "Natalie Grondahl Tangen",
    "Aasmund Flaten"
]


ansattogOppgaveIKongs = {}
ansattogOppgaveIKjærlighet = {}
ansatteIkonge = []

for i in kongesemneneOppgaver:
    for j in range(len(i)):
        if j>0:
            ansatteIkonge.append(i[j])
            ansattogOppgaveIKongs[i[j]] = i[0]

ansatteIkjærlighet = []
for i in storstAvAltErKjærlighetenOppgaver:
    for j in range(len(i)):
        if j>0:
            ansatteIkjærlighet.append(i[j])
            ansattogOppgaveIKjærlighet[i[j]] = i[0]

for skuespiller in skuespillereOgDemsRollerKongs:
    ansatteIkonge.append(skuespiller[0])
    ansattogOppgaveIKongs[skuespiller[0]] = "Skuespiller"

for skuespiller in skuespillereKjærlighet:
    ansatteIkjærlighet.append(skuespiller)
    ansattogOppgaveIKjærlighet[skuespiller] = "Skuespiller"

fastAnsatteIkonge = []
for i in ansatteIkonge:
    if i in fastAnsatte:
        fastAnsatteIkonge.append(j)
fastAnsatteIkjærlighet = []
for i in fastAnsatteIkjærlighet:
    if i in fastAnsatte:
        fastAnsatteIkjærlighet.append(j)

# insert fast ansatte
#     if(con.execute('''SELECT * FROM Ansatt''').fetchone() == None):
#         id = 0
#         for i in fastAnsatteIkonge:
#             con.execute(f"INSERT INTO Ansatt (AnsattID, Navn, Epost, AnsattStatus, TeaterstykkeID) VALUES ({id}, '{i}', NULL, 'fast', 0)")
#             id+=1
#         for i in fastAnsatteIkjærlighet:
#             con.execute(f"INSERT INTO Ansatt (AnsattID, Navn, Epost, AnsattStatus, TeaterstykkeID) VALUES ({id}, '{i}', NULL, 'fast', 1)")
#             id+=1

# insert ansatte
#TODO: insert direktør og sånt
ansattogid = {}
if(con.execute('''SELECT * FROM Ansatt''').fetchone() == None):
    id = 0
    # kanskje ikke nødvendig:
    # for i in fastAnsatte:
    #     con.execute(f"INSERT INTO Ansatt (AnsattID, Navn, Epost, AnsattStatus, TeaterstykkeID) VALUES ({id}, '{i}', '{i.split(' ')[0]+"@trøndelagteater.no"}', 'fast', NULL)")
    #     id+=1
    for i in ansatteIkonge:
        epost = i.split(' ')[0]+"@trøndelagteater.no"
        ansattogid[i] = id
        con.execute(f"INSERT INTO Ansatt (AnsattID, Navn, Epost, AnsattStatus, TeaterstykkeID) VALUES ({id},'{i}', '{epost}', 'frivillig', 0)")
        id+=1
    for i in ansatteIkjærlighet:
        epost = i.split(' ')[0]+"@trøndelagteater.no"
        ansattogid[i] = id
        con.execute(f"INSERT INTO Ansatt (AnsattID, Navn, Epost, AnsattStatus, TeaterstykkeID) VALUES ({id},'{i}', '{epost}', 'frivillig', 1)")
        id+=1
    con.commit()

# insert oppgaver
if(con.execute('''SELECT * FROM Oppgave''').fetchone() == None):
    for i in kongesemneneOppgaver:
        con.execute(f"INSERT INTO Oppgave (TeaterstykkeID, Oppgavetype) VALUES (0, '{i[0]}')")
    for i in storstAvAltErKjærlighetenOppgaver:
        con.execute(f"INSERT INTO Oppgave (TeaterstykkeID, Oppgavetype) VALUES (1, '{i[0]}')")
    con.commit()

# insert ansattIoppgave
if(con.execute('''SELECT * FROM ansattioppgave''').fetchone() == None):
    for i in ansatteIkonge:
        con.execute(f"INSERT INTO ansattioppgave (TeaterstykkeID, Oppgavetype, AnsattID) VALUES (0, '{ansattogOppgaveIKongs[i]}', {ansattogid[i]})")
    for i in ansatteIkjærlighet:
        con.execute(f"INSERT INTO ansattioppgave (TeaterstykkeID, Oppgavetype, AnsattID) VALUES (1, '{ansattogOppgaveIKjærlighet[i]}', {ansattogid[i]})")
    con.commit()


# insert akt
if(con.execute('''SELECT * FROM akt''').fetchone() == None):
    # Kongsemnene av Henrik Ibsen (Hovedscenen)
    akterKonge = [1,2,3,4,5]
    for akt in akterKonge:
        con.execute(f"INSERT INTO akt (Aktnummer, TeaterstykkeID, Aktnavn) VALUES ({akt},0,'test')")
    # Størst av alt er kjærligheten av Jonas Corell Petersen(Gamle scene)
    con.execute(f"INSERT INTO akt (Aktnummer, TeaterstykkeID, Aktnavn) VALUES (1,1,'Akt 1')")
    con.commit()



# insert rolleiakt
if(con.execute('''SELECT * FROM rolleiakt''').fetchone() == None):
    # Kongsemnene av Henrik Ibsen (Hovedscenen)
    rolleIaktKonge = {
    "Håkon Håkonson":[1,2,3,4,5],
    "Dagfinn Bonde":[1,2,3,4,5],
    "Jatgeir Skald":[4],
    "Sigrid":[1,2,5],
    "Ingeborg":[4],
    "Guttorm Ingesson":[1],
    "Skule Jarl":[1,2,3,4,5],
    "Inga frå Vartejg":[1,3],
    "Paal Flida":[1,2,3,4,5],
    "Ragnhild":[1,5],
    "Gregorius Jonsson":[1,2,3,4,5],
    "Margrete":[1,2,3,4,5],
    "Biskop Nikolas":[1,2,3],
    "Peter":[3,4,5]         
    }

    for rolle in rolleIaktKonge.keys():
        for akt in rolleIaktKonge[rolle]:
            con.execute(f"INSERT INTO rolleiakt (Rollenavn, Aktnummer, TeaterstykkeID) VALUES ('{rolle}', {akt}, {0})")
            
    # Størst av alt er kjærligheten av Jonas Corell Petersen(Gamle scene)
    for rolle in skuespillereKjærlighet:
        con.execute(f"INSERT INTO rolleiakt (Rollenavn, Aktnummer, TeaterstykkeID) VALUES ('{rolle}', {1} , {1})")
    con.commit()


# Insert roller
if(con.execute('''SELECT * FROM Rolle''').fetchone() == None):
    for rolle in skuespillereOgDemsRollerKongs:
        rollenavn = rolle[1]
        con.execute(f"INSERT INTO Rolle (TeaterstykkeID, Rollenavn) VALUES (0, '{rollenavn}')")
    for rolle in skuespillereKjærlighet:
        con.execute(f"INSERT INTO Rolle (TeaterstykkeID, Rollenavn) VALUES (1, '{rolle}')")
    con.commit()


# Insert skuespillerAnsatt
if(con.execute('''SELECT * FROM SkuespillerAnsatt''').fetchone() == None):
    for rolle in skuespillereOgDemsRollerKongs:
        ansattnavn = rolle[0]
        if (ansattnavn in ansattogid.keys()):
            ansattid = ansattogid[ansattnavn]
            rollenavn = rolle[1]
            con.execute(f"INSERT INTO SkuespillerAnsatt (TeaterstykkeID, Rollenavn, AnsattID) VALUES (0, '{rollenavn}', '{ansattid}')")
    for ansattOgRolle in skuespillereKjærlighet:
        if (ansattOgRolle in ansattogid.keys()):
            ansattid = ansattogid[ansattOgRolle]
            con.execute(f"INSERT INTO SkuespillerAnsatt (TeaterstykkeID, Rollenavn, AnsattID) VALUES (1, '{ansattOgRolle}', '{ansattid}')")
    con.commit()


con.close()
"""
hello

"""