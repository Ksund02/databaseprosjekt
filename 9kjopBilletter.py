import sqlite3

con = sqlite3.connect('teater.db')

cursor = con.cursor()

# Finner rad med 9+ ledige stoler
cursor.execute('''
               SELECT Total.Radnummer, Total.Omraadenavn, (Total.AntallStoler - IFNULL(Kjopt.AntallKjopteStoler, 0)) AS LedigeStoler
               FROM
                (SELECT Billett.Radnummer, Billett.Omraadenavn, COUNT(*) AS "AntallKjopteStoler"
                FROM Billett 
                WHERE Billett.Salnavn = "gamle scene"
                GROUP BY Billett.Radnummer, Billett.Omraadenavn) AS Kjopt
                RIGHT JOIN
                (SELECT Stol.Radnummer, Stol.Omraadenavn, COUNT(*) AS "AntallStoler"
                FROM Stol
                WHERE Stol.Sesong="vår/vinter 2024" AND Stol.Salnavn = "gamle scene"
                GROUP BY Stol.Radnummer, Stol.Omraadenavn) AS Total
               ON Kjopt.Radnummer = Total.Radnummer AND Kjopt.Omraadenavn=Total.Omraadenavn
               WHERE LedigeStoler > 8
               ''')

radMed9LedigeStoler = cursor.fetchall()

# Sjekker om det var en rad med 9 ledige stoler igjen
if len(radMed9LedigeStoler) < 1:
    print("Det er ingen rader med 9 ledige stoler igjen")
else:
    # Finner ni ledige stoler i samme rad, som blir koblet til billettene i applikasjonsnivået
    cursor.execute(f'''
                   SELECT Stol.Sesong, Stol.Salnavn, Stol.Stolnummer, Stol.Radnummer, Stol.Omraadenavn
                   FROM Stol
                   WHERE Stol.Radnummer={radMed9LedigeStoler[0][0]} 
                    AND Stol.Omraadenavn="{radMed9LedigeStoler[0][1]}"
                    AND Stol.Sesong="vår/vinter 2024"
                    AND Stol.Salnavn = "gamle scene"
                    AND (Stol.Sesong, Stol.Salnavn, Stol.Stolnummer, Stol.Radnummer, Stol.Omraadenavn) NOT IN (
                        SELECT Stol.Sesong, Stol.Salnavn, Stol.Stolnummer, Stol.Radnummer, Stol.Omraadenavn
                        FROM Stol INNER JOIN Billett
                        ON Stol.Sesong=Billett.Sesong 
                            AND Stol.Salnavn=Billett.Salnavn 
                            AND Stol.Stolnummer=Billett.Stolnummer
                            AND Stol.Radnummer=Billett.Radnummer
                            AND Stol.Omraadenavn=Billett.Omraadenavn 
                        )
                   LIMIT 9
                   ''')
    Stoler = cursor.fetchall()

    # Finner neste genererte billetID
    cursor.execute(f'''
                   SELECT max(Billett.BillettID)
                   FROM Billett
                   ''')
    NesteBillettID = cursor.fetchall()[0][0]+1
    
    # Lager en ny kunde som skal kjøpe disse 9 billettene for de 9 ulike stolene
    cursor.execute(f'''
                   SELECT max(KundeProfil.KundeProfilID)
                   FROM KundeProfil
                   ''')
    NesteKundeProfilID = cursor.fetchall()[0][0]+1
    cursor.execute(f'''
                INSERT INTO KundeProfil (KundeProfilID, MobilNummer, Navn, Adresse)
                VALUES ({NesteKundeProfilID}, NULL, "{"Sensor "+str(NesteKundeProfilID)}", NULL)
                ''')

    # Genererer Billett for Stolene
    for stol in Stoler:
        # Setter inn Billett for stol
        cursor.execute(f'''
                    INSERT INTO Billett (BillettID, Sesong, Salnavn, Stolnummer, Radnummer, Omraadenavn)
                    VALUES ({NesteBillettID}, "{stol[0]}", "{stol[1]}", "{stol[2]}", "{stol[3]}", "{stol[4]}")
                    ''')
        # Oppdaterer Billettrelasjon med ForestillingBillett
        cursor.execute(f'''
                       INSERT INTO ForestillingBillett (BillettID, ForestillingID)
                       VALUES ({NesteBillettID}, 5)
                    ''')
        # Oppdaterer Billettrelasjon med Billettgruppe
        cursor.execute(f'''
                       INSERT INTO Billettgruppe (BillettID, TeaterstykkeID, Prisgruppenavn)
                       VALUES ({NesteBillettID}, 1, "Ordinær")
                    ''')
        # Oppdaterer Billettrelasjon med Billetkjop
        cursor.execute(f'''
                       INSERT INTO Billettkjop (BillettID, KundeProfilID, Dato, Tid)
                       VALUES ({NesteBillettID}, {NesteKundeProfilID}, "Nå", "Nå")
                    ''')
        
        NesteBillettID+=1
        con.commit()

    print("Du kjøper disse ni ledige stolene i samme rad i gamle scenen vår/vinter2024:")
    for stol in Stoler:
        print(f" {stol}")
    # Finner pris på ni billetter
    cursor.execute(f'''
                SELECT Teaterstykke.TeaterstykkeID, Prisgruppe.PrisgruppeNavn, Prisgruppe.Pris
                FROM Teaterstykke INNER JOIN Prisgruppe
                   ON Teaterstykke.TeaterstykkeID = Prisgruppe.TeaterstykkeID
                WHERE Teaterstykke.Name = "Størst av alt er kjærligheten" AND PrisGruppeNavn="Ordinær"
                ''')
    prisForEn = cursor.fetchall()[0][2]
    prisForNi = prisForEn*9
    print("Takk for at du kjøpte ni billetter!")
    print(f"Du brukte til sammen {prisForNi} kr for å kjøpe ni billetter i samme rad i gamle scenen vår/vinter2024 for Størst av alt er kjærligheten 3.februar")