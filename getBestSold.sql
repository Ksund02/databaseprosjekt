SELECT stykke.name,Forestilling.dato, COUNT(Forestilling.ForestillingID) as ticket_count FROM Forestilling
               NATURAL JOIN ForestillingBillett
               NATURAL JOIN Teaterstykke as stykke
               GROUP BY Forestilling.ForestillingID
               ORDER BY ticket_count DESC