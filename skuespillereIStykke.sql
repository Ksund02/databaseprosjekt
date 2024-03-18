SELECT Teaterstykke.Name, Ansatt.Navn, SkuespillerAnsatt.Rollenavn
FROM SkuespillerAnsatt
    NATURAL JOIN Ansatt
    NATURAL JOIN Teaterstykke
WHERE SkuespillerAnsatt.AnsattID = Ansatt.AnsattID