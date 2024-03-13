import sqlite3

con = sqlite3.connect('teater.db')

cursor = con.cursor()
#Du skal lage et Pythonprogram (og SQL) som tar et skuespillernavn og finner
#hvilke skuespilllere de har spilt med i samme akt. Skriv ut navn på begge og
#hvilket skuespill det skjedde.


#SkuespillerAnsatt
#(TeaterstykkeID, Rollenavn, AnsattID)

#Ansatt
#(AnsattID, Navn, Epost, AnsattStatus, TeaterstykkeID)

# FINNER Rollenavn TIL Skuespilleren
cursor.execute('''
               SELECT SkuespillerAnsatt.AnsattID, Ansatt.Navn, SkuespillerAnsatt.TeaterstykkeID, SkuespillerAnsatt.Rollenavn
               FROM SkuespillerAnsatt 
                INNER JOIN Ansatt 
                ON SkuespillerAnsatt.AnsattID=Ansatt.AnsattID
               WHERE Ansatt.Navn="Sunniva Du Mond Nordal"
               ''')
skuespiller = cursor.fetchall()
#Rolle (TeaterstykkeID, Rollenavn)

# Finner Rolle til Skuespilleren
cursor.execute(f'''
               SELECT *
               FROM Rolle
               WHERE Rolle.TeaterstykkeID={skuespiller[0][2]} AND Rolle.Rollenavn="{skuespiller[0][3]}"
               ''')

rolle = cursor.fetchall()

#RolleIAkt (Rollenavn, Aktnummer, TeaterstykkeID)
#Akt (Aktnummer, TeaterstykkeID, Aktnavn)

# Finner Akter rollen er i
cursor.execute(f'''
               SELECT RolleIAkt.Aktnummer, RolleIAkt.TeaterstykkeID
               FROM RolleIAkt 
               WHERE RolleIAkt.TeaterstykkeID={rolle[0][0]} AND RolleIAkt.Rollenavn="{rolle[0][1]}" 
               ''')

akterRollenErI = cursor.fetchall()

# Finner andre roller i samme akt
andre_roller = {}
for akt in akterRollenErI:
    aktNummer= akt[0]
    tID = akt[1]
    cursor.execute(f'''
               SELECT Rollenavn
               FROM RolleIAkt 
               WHERE RolleIAkt.TeaterstykkeID={tID} AND RolleIAkt.Aktnummer={aktNummer} 
               ''')
    temp = cursor.fetchall()
    andre_roller[aktNummer]=temp

# Mapper Rollenavn og TeaterstykkeID til SkuespillerAnsatt
andre_skuespillere = {}

for akt in andre_roller.keys():
    rollerIsammeAkt = andre_roller[akt]
    for rolle in rollerIsammeAkt:
        cursor.execute(f'''
                       SELECT SkuespillerAnsatt.AnsattID, Ansatt.Navn
                       FROM SkuespillerAnsatt 
                        INNER JOIN Ansatt 
                        ON SkuespillerAnsatt.AnsattID=Ansatt.AnsattID
                       WHERE SkuespillerAnsatt.Rollenavn = "{rolle[0]}" AND SkuespillerAnsatt.TeaterstykkeID = {akterRollenErI[0][1]}     
                       ''')
        temp = cursor.fetchall()[0][1]
        if akt not in andre_skuespillere.keys():
            andre_skuespillere[akt] = []
        andre_skuespillere[akt].append(temp)



print(andre_skuespillere)