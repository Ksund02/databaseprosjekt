SELECT Skuespiller.navn, Teaterstykke.name
    FROM RolleIAkt
    natural join Teaterstykke
    natural join SkuespillerAnsatt
    WHERE RolleIAkt.Aktnummer in
        (SELECT Akt.Aktnummer 
        FROM Akt
        natural join SkuespillerAnsatt as skuespiller
        WHERE skuesopiller.rollenavn in 
                (select rollenavn
                FROM Akt natural join SkuespillerAnsatt as skuespiller
                WHERE skuespiller.navn = '{inputNavn}')