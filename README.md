# Brukstilfelle 1 og 2:

Vi setter opp databasen via terminalen.
Kjør følgende kommando for å opprette tabellene:

```py
python .\dbInsertScript.py
```

Da vil databasen bli laget i "teater.db"
Åpne "teater.db" for å direkte se hva som ligger i databasen
(All informasjon for de to teaterstykkene er nå lagt inn,
sammen med informasjon om selve Trøndelag Teater og dets saler/stoler,
med andre ord er brukstilfelle 1 og 2 oppfylt her).

# Brukstilfelle 3:

For å teste brukstilfelle 3 må du kjøre filen "9kjopNiBilletter.py".

Etter å ha kjørt filen vil du i terminalen få opp hvilke stoler du
har kjøpt for, og hvor mye disse ni billetene koster til sammen. All
informasjon om billettene blir oppdatert i databasen samtidig med
alle relasjonene for billett. Vi har nemlig laget et system der
billettene bare blir laget når noen kjøper en ledig stolplass. Kundeprofilen
som kjøper disse billettene vil da bli lagret som "Sensor {nummer}", der nummer avhenger av hvor mange ganger programmet er kjørt. Du kan kjøre
programmet så mange ganger du vil.
(Om du vil ha tilbake den opprinnelige databasen
så sletter du "teater.db" og kjører "dbInsertScript.py" igjen)

# Brukstilfelle 4

For å teste brukstilfelle 4:

Fra terminalen kan man kjøre fila "4totaltSolgteBilletter.py". Denne tar inn en dato på formatett 'YYYY-MM-DD' og retunerer navnet på forestillingen sammen med antalll solgte billetter på denne forestillingen. Et eksempel på hva man kan skrive i terminalen er:

```py
python .\4totaltSolgteBilletter.py "2024-02-03"
```

Output:

```py
('Kongsemnene', 65)
('Størst av alt er kjærligheten', 27)
```

# Brukstilfelle 5:

For å teste brukstilfelle 5
kjør:

```py
python .\5skuespillereIStykke.py
```

Da skal terminalen fylles med tupler etter dette formatet: ('teaterstykke', 'skuespiller', 'rolle')

(All kode her er skrevet i en SQL query, men vi bruker bare pythonfilen for å enkelt kjøre SQL queryen
Om du vil se SQL queryen åpner du "./skuespillereIStykke.sql")

Output:

```py
('Kongsemnene', 'Arturo Scotti', 'Haakon Haakonssonn')
('Kongsemnene', 'Ingunn Beate Strige Oyen', 'Inga fra Vartejg (Haakons mor)')
('Kongsemnene', 'Hans Petter Nilsen', 'Skule Jarl')
('Kongsemnene', 'Madeleine Brandtzæg Nilsen', 'Fru Ragnhild (Skules hustru)')
('Kongsemnene', 'Synnove Fossum Eriksen', 'Margrete (Skules datter)')
('Kongsemnene', 'Emma Caroline Deichmann', 'Sigrid (Skules soster)')
('Kongsemnene', 'Emma Caroline Deichmann', 'Ingebjorg')
('Kongsemnene', 'Thomas Jensen Takyi', 'Biskop Nikolas')
('Kongsemnene', 'Per Bogstad Gulliksen', 'Gregorius Jonssonn')
('Kongsemnene', 'Isak Holmen Sorensen', 'Paal Flida')
('Kongsemnene', 'Isak Holmen Sorensen', 'Tronder 1')
('Kongsemnene', 'Fabian Heidelberg Lunde', 'Baard Bratte')
('Kongsemnene', 'Fabian Heidelberg Lunde', 'Tronder 2')
('Kongsemnene', 'Emil Olafsson', 'Jatgeir Skald')
('Kongsemnene', 'Emil Olafsson', 'Dagfinn Bonde')
('Kongsemnene', 'Snorre Ryen Tondel', 'Peter (prest og Ingebjorgs sonn)')
('Størst av alt er kjærligheten', 'Sunniva Du Mond Nordal', 'Sunniva Du Mond Nordal')
('Størst av alt er kjærligheten', 'Jo Saberniak', 'Jo Saberniak')
('Størst av alt er kjærligheten', 'Marte M. Steinholt', 'Marte M. Steinholt')
('Størst av alt er kjærligheten', 'Tor Ivar Hagen', 'Tor Ivar Hagen')
('Størst av alt er kjærligheten', 'Trond-Ove Skrodal', 'Trond-Ove Skrodal')
('Størst av alt er kjærligheten', 'Natalie Grondahl Tangen', 'Natalie Grondahl Tangen')
('Størst av alt er kjærligheten', 'Aasmund Flaten', 'Aasmund Flaten')
```

# Brukstilfelle 6:

For å teste brukstilfelle 6
kjør:

```py
python .\6bestSolgteForestillinger.py
```

Deretter vil du få opp tupler etter dette formatet: ('teaterstykke', 'dato', 'antall solgte billetter')
Disse fremstiller alle de forskjellige forestillingene i synkende rekkefølge etter hvor mange solgte
billetter hver forestilling har solgt.

Output:

```

```

(All kode her er skrevet i en SQL query, men vi bruker bare pythonfilen for å enkelt kjøre SQL queryen
Om du vil se SQL queryen åpner du "./bestSolgteForestillinger.sql")

# Brukstilfelle 7:

For å teste brukstilfelle 7, må man skrive inn navnet på filen som før sammen med navnet på en skuespiller.

Format:

```py
python .\7skuespillereISammeAkt.py <skuespillernavn>
```

Deretter vil du få opp en oversikt i terminalen over hvilke andre skuespillere de har spilt med i samme akt
i formatet ("skuespiller søkt på" | "annen skuespiller som har spilt med den søkte skuespilleren" | "skuespill")

Kjør for eksempel:

```py
python .\7skuespillereISammeAkt.py "Arturo Scotti"
```

Output:

```py
Arturo Scotti | Ingunn Beate Strige Oyen | Kongsemnene
Arturo Scotti | Hans Petter Nilsen | Kongsemnene
Arturo Scotti | Madeleine Brandtzæg Nilsen | Kongsemnene
Arturo Scotti | Synnove Fossum Eriksen | Kongsemnene
Arturo Scotti | Emma Caroline Deichmann | Kongsemnene
Arturo Scotti | Thomas Jensen Takyi | Kongsemnene
Arturo Scotti | Per Bogstad Gulliksen | Kongsemnene
Arturo Scotti | Isak Holmen Sorensen | Kongsemnene
Arturo Scotti | Fabian Heidelberg Lunde | Kongsemnene
Arturo Scotti | Emil Olafsson | Kongsemnene
Arturo Scotti | Snorre Ryen Tondel | Kongsemnene
```
