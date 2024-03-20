# DB2: Realisert databasesystem

Utfør brukstilfellene i dette dokumentet i kronologisk rekkefølge. Alle brukstilfeller har en kommando som skal kjøres i terminalen og tilhørende forventet output. Der hvor det er argumentverdier i kommandoen, er disse bare eksempler, og andre verdier vil også fungere.

## Innholdsfortegnelse

- [Gruppe 4 medlemmer](#gruppe-4-medlemmer)
- [Brukstilfelle 1 og 2](#brukstilfelle-1-og-2)
- [Brukstilfelle 3](#brukstilfelle-3)
- [Brukstilfelle 4](#brukstilfelle-4)
- [Brukstilfelle 5](#brukstilfelle-5)
- [Brukstilfelle 6](#brukstilfelle-6)
- [Brukstilfelle 7](#brukstilfelle-7)
- [Endringer fra DB1](#endringer-fra-db1)

## Gruppe 4 medlemmer

- Mikkel Bakken Eggen
- David Tuan Kiet Tran
- Kristian Underdal

# Brukstilfelle 1 og 2

Vi setter opp databasen via terminalen.
Kjør følgende kommando for å opprette tabellene:

```py
python .\dbInsertScript.py
```

Her er et eksempel på insatt data i Forestilling-tabellen etter å ha kjørt kommandoen ovenfor:

| ForestillingID | Dato       | Klokkeslett | TeaterstykkeID |
| -------------- | ---------- | ----------- | -------------- |
| 0              | 2024-02-01 | 19:00       | 0              |
| 1              | 2024-02-02 | 19:00       | 0              |
| 2              | 2024-02-03 | 19:00       | 0              |
| 3              | 2024-02-05 | 19:00       | 0              |
| 4              | 2024-02-06 | 19:00       | 0              |
| 5              | 2024-02-03 | 18:30       | 1              |
| 6              | 2024-02-06 | 18:30       | 1              |
| 7              | 2024-02-07 | 18:30       | 1              |
| 8              | 2024-02-12 | 18:30       | 1              |
| 9              | 2024-02-13 | 18:30       | 1              |
| 10             | 2024-02-14 | 18:30       | 1              |

Alle solgte billetter er også blitt lagt til i databasen og ligger i tabellen Billettkjop (brukstilfelle 2). Det er totalt 92 solgte billetter:

| BillettID | KundeProfilID | Dato       | Tid   |
| --------- | ------------- | ---------- | ----- |
| 0         | 0             | 2024-02-03 | 00:00 |
| 1         | 0             | 2024-02-03 | 00:00 |
| 2         | 0             | 2024-02-03 | 00:00 |
| 3         | 0             | 2024-02-03 | 00:00 |
| 4         | 0             | 2024-02-03 | 00:00 |
| 5         | 0             | 2024-02-03 | 00:00 |
|           | ...           |            |       |
| 86        | 0             | 2024-02-03 | 00:00 |
| 87        | 0             | 2024-02-03 | 00:00 |
| 88        | 0             | 2024-02-03 | 00:00 |
| 89        | 0             | 2024-02-03 | 00:00 |
| 90        | 0             | 2024-02-03 | 00:00 |
| 91        | 0             | 2024-02-03 | 00:00 |

Da vil dataene bli laget som tabeller i "teater.db". Tabellene er definert i "tabeller.sql". Åpne databasefila for å direkte se hva som ligger i databasen. All informasjon for de to teaterstykkene er nå lagt inn, sammen med informasjon om selve Trøndelag Teater og dets saler/stoler, med andre ord er brukstilfelle 1 og 2 oppfylt her.

# Brukstilfelle 3

For å teste brukstilfelle 3 kjører man kommandoen nedenfor:

```py
python .\3kjopNiBilletter.py
```

Etter å ha kjørt filen vil du i terminalen få opp hvilke stoler du har kjøpt for, og hvor mye disse ni billetene koster til sammen. All informasjon om billettene blir oppdatert i databasen samtidig med alle relasjonene for billett. Vi har nemlig laget et system der billettene bare blir laget når noen kjøper en ledig stolplass. Kundeprofilen som kjøper disse billettene vil da bli lagret som "Sensor{nummer}", der nummer avhenger av hvor mange ganger programmet er kjørt. Du kan kjøre programmet så mange ganger du vil. Til slutt vil det ikke være rader med ni ledige stoler igjen, så output blir da "Det er ingen rader med 9 ledige stoler igjen" (Om du vil ha tilbake den opprinnelige databasen, så sletter du "teater.db" og kjører "dbInsertScript.py" igjen).

| BillettID | Sesong           | Salnavn     | Stolnummer | Radnummer | Omraadenavn |
| --------- | ---------------- | ----------- | ---------- | --------- | ----------- |
| 92        | vaar/vinter 2024 | gamle scene | 1          | 1         | Galleri     |
| 93        | vaar/vinter 2024 | gamle scene | 2          | 1         | Galleri     |
| 94        | vaar/vinter 2024 | gamle scene | 3          | 1         | Galleri     |
| 95        | vaar/vinter 2024 | gamle scene | 4          | 1         | Galleri     |
| 96        | vaar/vinter 2024 | gamle scene | 5          | 1         | Galleri     |
| 97        | vaar/vinter 2024 | gamle scene | 8          | 1         | Galleri     |
| 98        | vaar/vinter 2024 | gamle scene | 9          | 1         | Galleri     |
| 99        | vaar/vinter 2024 | gamle scene | 10         | 1         | Galleri     |
| 100       | vaar/vinter 2024 | gamle scene | 11         | 1         | Galleri     |

# Brukstilfelle 4

Fra terminalen kan man kjøre fila "4totaltSolgteBilletter.py". Denne tar inn en dato på formatett 'YYYY-MM-DD' og retunerer navnet på forestillingen sammen med antalll solgte billetter på denne forestillingen. Et eksempel på hva man kan skrive i terminalen er:

```py
python .\4totaltSolgteBilletter.py "2024-02-03"
```

Output:

```py
('Kongsemnene', 65)
('Størst av alt er kjærligheten', 27)
```

Her er andre argumenter også gyldige bare de følger det samme formatet på dato ('YYYY-MM-DD')

# Brukstilfelle 5

For å teste brukstilfelle 5, kjører man kommandoen:

```py
python .\5skuespillereIStykke.py
```

Da skal terminalen fylles med tupler etter dette formatet: ('teaterstykke', 'skuespiller', 'rolle')

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

(All kode her er skrevet i en SQL query, men vi bruker bare pythonfilen for å enkelt kjøre SQL queryen
Om du vil se SQL queryen åpner du "./skuespillereIStykke.sql")

# Brukstilfelle 6

For å teste brukstilfelle 6, kjører man kommandoen:

```py
python .\6bestSolgteForestillinger.py
```

Deretter vil du få opp tupler etter dette formatet: ('teaterstykke', 'dato', 'antall solgte billetter'). Disse fremstiller alle de forskjellige forestillingene i synkende rekkefølge etter hvor mange solgte billetter hver forestilling har solgt.

Output:

```py
('Kongsemnene', '2024-02-03', 65)
('Størst av alt er kjærligheten', '2024-02-03', 27)
('Kongsemnene', '2024-02-01', 0)
('Kongsemnene', '2024-02-02', 0)
('Kongsemnene', '2024-02-05', 0)
('Kongsemnene', '2024-02-06', 0)
('Størst av alt er kjærligheten', '2024-02-06', 0)
('Størst av alt er kjærligheten', '2024-02-07', 0)
('Størst av alt er kjærligheten', '2024-02-12', 0)
('Størst av alt er kjærligheten', '2024-02-13', 0)
('Størst av alt er kjærligheten', '2024-02-14', 0)
```

(All kode her er skrevet i en SQL query, men vi bruker bare pythonfilen for å enkelt kjøre SQL queryen
Om du vil se SQL queryen åpner du "./bestSolgteForestillinger.sql")

# Brukstilfelle 7

For å teste brukstilfelle 7, må man skrive inn navnet på filen som før sammen med navnet på en skuespiller. Deretter vil du få opp en oversikt i terminalen over hvilke andre skuespillere de har spilt med i samme akt i formatet ("skuespiller søkt på" | "annen skuespiller som har spilt med den søkte skuespilleren" | "skuespill")

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

# Endringer fra DB1

Endringer i ER-modellen:

- Endret kardinaliteten mellom Billett og Kundeprofil fra (0,1) til (1,1), altså at Billett må ha en relasjon til en Kundeprofil. Siden vi alltid holder styr på kjøpte Billett-er, må nødvendigvis disse alltid være koblet til en Kundeprofil.

- Endret kardinaliteten mellom Oppgave og Ansatt fra (0,1) til (0,n), altså kan en Oppgave bli gjort av flere Ansatte. Det må ikke nødvendigvis bare være én ansatt på hver oppgave, de kan ha samme oppgave.

- Endret kardinaliteten mellom Ansatt og Teaterstykke fra (1,1) til (1,n), altså kan en Ansatt være ansatt på flere Teaterstykker. Dette gjelder blant annet direktøren for Trøndelag Teater som kan anses som ansatt i alle teaterstykker.

Disse endringene er tatt hensyn til under opprettelsen av tabellene i **tables.sql**.
