CREATE TABLE IF NOT EXISTS Teatersal (
    Sesong TEXT NOT NULL,
    Salnavn TEXT NOT NULL,
    TeaterstykkeID INTEGER,
    PRIMARY KEY(Sesong, Salnavn),
    FOREIGN KEY(TeaterstykkeID)
        REFERENCES Teaterstykke(TeaterstykkeID)
            ON UPDATE CASCADE
            ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS Stol (
    Sesong TEXT NOT NULL,
    Salnavn TEXT NOT NULL,
    Stolnummer INTEGER NOT NULL,
    Radnummer INTEGER NOT NULL,
    Omraadenavn TEXT NOT NULL,
    FOREIGN KEY(Sesong, Salnavn) 
        REFERENCES Teatersal(Sesong, Salnavn)
            ON UPDATE CASCADE
            ON DELETE CASCADE,
    PRIMARY KEY(Sesong, Salnavn, Stolnummer, Radnummer, Omraadenavn)
);

CREATE TABLE IF NOT EXISTS Forestilling (
    ForestillingID INTEGER PRIMARY KEY NOT NULL, -- Kan bruke AUTOINCREMENT mellom PRIMARY KEY og NOT NULL
    Dato TEXT,
    Klokkeslett TEXT, -- TIMESTAMP
    TeaterstykkeID INTEGER NOT NULL,
    FOREIGN KEY(TeaterstykkeID) 
        REFERENCES Teaterstykke(TeaterstykkeID)
            ON UPDATE CASCADE
            ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Billett (
    BillettID INTEGER PRIMARY KEY NOT NULL, -- Kan bruke AUTOINCREMENT mellom PRIMARY KEY og NOT NULL
    Sesong TEXT NOT NULL,
    Salnavn TEXT NOT NULL,
    Stolnummer INTEGER NOT NULL,
    Radnummer INTEGER NOT NULL,
    Omraadenavn TEXT NOT NULL,
    FOREIGN KEY(Sesong, Salnavn, Stolnummer, Radnummer, Omraadenavn) 
        REFERENCES Stol(Sesong, Salnavn, Stolnummer, Radnummer, Omraadenavn)
            ON UPDATE CASCADE
            ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS ForestillingBillett (
    BillettID INTEGER PRIMARY KEY NOT NULL,
    ForestillingID INTEGER NOT NULL, 
    FOREIGN KEY(ForestillingID) 
        REFERENCES Forestilling(ForestillingID)
            ON UPDATE CASCADE
            ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Billettgruppe (
    BillettID INTEGER PRIMARY KEY NOT NULL,
    TeaterstykkeID INTEGER NOT NULL,
    Prisgruppenavn TEXT,
    FOREIGN KEY(TeaterstykkeID, Prisgruppenavn) 
        REFERENCES Prisgruppe(TeaterstykkeID, Prisgruppenavn)
            ON UPDATE CASCADE
            ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS BillettKjop (
    BillettID INTEGER NOT NULL,
    KundeProfilID INTEGER NOT NULL,
    Dato TEXT,
    Tid TEXT, -- TIMESTAMP
    PRIMARY KEY(BillettID, KundeProfilID),
    FOREIGN KEY(BillettID) 
        REFERENCES Billett(BillettID)
            ON UPDATE CASCADE
            ON DELETE CASCADE,
    FOREIGN KEY(KundeProfilID) 
        REFERENCES KundeProfil(KundeProfilID)
            ON UPDATE CASCADE
            ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS KundeProfil (
    KundeProfilID INTEGER PRIMARY KEY NOT NULL, -- Kan bruke AUTOINCREMENT mellom PRIMARY KEY og NOT NULL
    Mobilnummer INTEGER,
    Navn TEXT,
    Adresse TEXT
);

CREATE TABLE IF NOT EXISTS Teaterstykke (
    TeaterstykkeID INTEGER PRIMARY KEY NOT NULL, -- Kan bruke AUTOINCREMENT mellom PRIMARY KEY og NOT NULL
    Name TEXT
);

CREATE TABLE IF NOT EXISTS Prisgruppe (
    TeaterstykkeID INTEGER NOT NULL,
    PrisgruppeNavn TEXT NOT NULL,
    Pris INTEGER,
    PRIMARY KEY(TeaterstykkeID, PrisgruppeNavn),
    FOREIGN KEY(TeaterstykkeID) 
        REFERENCES Teaterstykke(TeaterstykkeID)
            ON UPDATE CASCADE
            ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Rolle (
    TeaterstykkeID INTEGER NOT NULL,
    Rollenavn TEXT,
    PRIMARY KEY(Rollenavn, TeaterstykkeID),
    FOREIGN KEY(TeaterstykkeID) 
        REFERENCES Teaterstykke(TeaterstykkeID)
            ON UPDATE CASCADE
            ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Akt (
    Aktnummer INTEGER NOT NULL,
    TeaterstykkeID INTEGER NOT NULL,
    Aktnavn TEXT,
    PRIMARY KEY(Aktnummer, TeaterstykkeID),
    FOREIGN KEY(TeaterstykkeID) 
        REFERENCES Teaterstykke(TeaterstykkeID)
            ON UPDATE CASCADE
            ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS SkuespillerAnsatt (
    TeaterstykkeID INTEGER NOT NULL,
    Rollenavn TEXT NOT NULL,
    AnsattID INTEGER NOT NULL,
    PRIMARY KEY(TeaterstykkeID, Rollenavn, AnsattID),
    FOREIGN KEY(TeaterstykkeID) 
        REFERENCES Teaterstykke(TeaterstykkeID)
            ON UPDATE CASCADE
            ON DELETE CASCADE,
    FOREIGN KEY(TeaterstykkeID, Rollenavn) 
        REFERENCES Rolle(TeaterstykkeID, Rollenavn)
            ON UPDATE CASCADE
            ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS RolleIAkt (
    Rollenavn TEXT NOT NULL,
    Aktnummer INTEGER NOT NULL,
    TeaterstykkeID INTEGER NOT NULL,
    PRIMARY KEY(Rollenavn, Aktnummer, TeaterstykkeID),
    FOREIGN KEY(TeaterstykkeID, Rollenavn) 
        REFERENCES Rolle(TeaterstykkeID, Rollenavn)
            ON UPDATE CASCADE
            ON DELETE CASCADE,
    FOREIGN KEY(TeaterstykkeID, Aktnummer) 
        REFERENCES Akt(TeaterstykkeID, Aktnummer)
            ON UPDATE CASCADE
            ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Ansatt (
    AnsattID INTEGER PRIMARY KEY NOT NULL, -- Kan bruke AUTOINCREMENT mellom PRIMARY KEY og NOT NULL
    Navn TEXT,
    Epost TEXT,
    AnsattStatus TEXT,
    TeaterStykkeID INTEGER NOT NULL,
    FOREIGN KEY(TeaterStykkeID) 
        REFERENCES Teaterstykke(TeaterstykkeID)
            ON UPDATE CASCADE
            ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Oppgave (
    TeaterStykkeID INTEGER NOT NULL,
    Oppgavetype TEXT NOT NULL,
    PRIMARY KEY(TeaterStykkeID, Oppgavetype),
    FOREIGN KEY(TeaterStykkeID) 
        REFERENCES Teaterstykke(TeaterStykkeID)
            ON UPDATE CASCADE
            ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS AnsattiOppgave (
    AnsattID INTEGER NOT NULL,
    TeaterStykkeID INTEGER NOT NULL,
    Oppgavetype TEXT NOT NULL,
    PRIMARY KEY(AnsattID, TeaterStykkeID, Oppgavetype),
    FOREIGN KEY(TeaterStykkeID, Oppgavetype) 
        REFERENCES Oppgave(TeaterStykkeID, Oppgavetype)
            ON UPDATE CASCADE
            ON DELETE CASCADE,
    FOREIGN KEY(AnsattID) 
        REFERENCES Ansatt(AnsattID)
            ON UPDATE CASCADE
            ON DELETE CASCADE
);
