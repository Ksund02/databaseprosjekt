SELECT Teaterstykke.Name, Forestilling.Dato, COUNT(ForestillingBillett.BillettID) AS Ticket_count 
FROM Forestilling
    LEFT JOIN ForestillingBillett
        ON Forestilling.ForestillingID = ForestillingBillett.ForestillingID
    INNER JOIN Teaterstykke
        ON Forestilling.TeaterstykkeID = Teaterstykke.TeaterstykkeID
GROUP BY Forestilling.ForestillingID
ORDER BY Ticket_count DESC