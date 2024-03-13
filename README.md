sett opp db via terminalen:

- python .\dbInsertScript.py

Da vil databasen bli laget i "teater.db"
Åpne "teater.db" for å direkte se hva som ligger i databasen
(All informasjon for de to teaterstykkene er nå lagt inn,
sammen med informasjon om selve Trøndelag Teater og dets saler/stoler)
(Med andre ord er Brukerhistorie 1 og 2 oppfylt her)

For å teste brukerhistorie 3 må du kjøre filen "9kjopBilletter.py".
Etter å ha kjørt filen vil du i terminalen få opp hvilke stoler du
har kjøpt for, og hvor mye disse ni billetene koster til sammen. All
informasjon om billettene blir oppdatert i databasen samtidig med
alle relasjonene for billett. Vi har nemlig laget et system der
billettene bare blir laget når noen kjøper billetten. Kundeprofilen
som kjøper disse billettene vil da bli lagret som "Sensor {nummer}", der
nummer avhenger av hvor mange ganger programmet er kjørt. Du kan kjøre
programmet så mange ganger du vil.
(Om du vil ha tilbake den opprinnelige databasen
så sletter du "teater.db" og kjører "dbInsertScript.py" igjen)

For å teste brukerhistorie 4 m
