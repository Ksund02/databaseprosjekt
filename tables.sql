CREATE TABLE IF NOT EXISTS Teatersal (
    Sesong TEXT NOT NULL,
    Salnavn TEXT NOT NULL,
    TeaterstykkeID INTEGER,
    PRIMARY KEY(Sesong, Salnavn),
    FOREIGN KEY(TeaterstykkeID) 
        REFERENCES Teaterstykke(TeaterstykkeID)
            ON UPDATE CASCADE
            ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Stol (
    Sesong TEXT NOT NULL,
    Salnavn TEXT NOT NULL,
    Stolnummer INTEGER NOT NULL,
    Radnummer INTEGER NOT NULL,
    Områdenavn TEXT NOT NULL,
    FOREIGN KEY(Sesong, Salnavn) REFERENCES Teatersal(Sesong, Salnavn),
    PRIMARY KEY(Sesong, Salnavn, Stolnummer, Radnummer, Områdenavn)
);

CREATE TABLE IF NOT EXISTS Forestilling (
    ForestillingID INTEGER PRIMARY KEY,
    Dato TEXT,
    Klokkeslett TEXT,
    TeaterstykkeID INTEGER NOT NULL,
    FOREIGN KEY(TeaterstykkeID) REFERENCES Teaterstykke(TeaterstykkeID)
);

CREATE TABLE IF NOT EXISTS Billett (
    BillettID INTEGER PRIMARY KEY,
    Sesong TEXT NOT NULL,
    Salnavn TEXT NOT NULL,
    Stolnummer INTEGER NOT NULL,
    Radnummer INTEGER NOT NULL,
    Områdenavn TEXT NOT NULL,
    FOREIGN KEY(Sesong, Salnavn, Stolnummer, Radnummer, Områdenavn) REFERENCES Stol(Sesong, Salnavn, Stolnummer, Radnummer, Områdenavn)
);

CREATE TABLE IF NOT EXISTS ForestillingBillett (
    BillettID INTEGER PRIMARY KEY,
    ForestillingID INTEGER NOT NULL,
    FOREIGN KEY(ForestillingID) REFERENCES Forestilling(ForestillingID)
);

CREATE TABLE IF NOT EXISTS Billettgruppe (
    BillettID INTEGER PRIMARY KEY,
    TeaterstykkeID INTEGER NOT NULL,
    Prisgruppenavn TEXT,
    FOREIGN KEY(TeaterstykkeID, Prisgruppenavn) REFERENCES Prisgruppe(TeaterstykkeID, Prisgruppenavn)
);

CREATE TABLE IF NOT EXISTS BillettKjøp (
    BillettID INTEGER NOT NULL,
    KundeProfilID INTEGER NOT NULL,
    Dato TEXT,
    Tid TEXT,
    PRIMARY KEY(BillettID, KundeProfilID),
    FOREIGN KEY(BillettID) REFERENCES Billett(BillettID),
    FOREIGN KEY(KundeProfilID) REFERENCES KundeProfil(KundeProfilID)
);

CREATE TABLE IF NOT EXISTS KundeProfil (
    KundeProfilID INTEGER PRIMARY KEY,
    Mobilnummer INTEGER,
    Navn TEXT,
    Adresse TEXT
);

CREATE TABLE IF NOT EXISTS Teaterstykke (
    TeaterstykkeID INTEGER PRIMARY KEY,
    Name TEXT
);

CREATE TABLE IF NOT EXISTS Prisgruppe (
    TeaterstykkeID INTEGER NOT NULL,
    PrisgruppeNavn TEXT NOT NULL,
    Pris INTEGER,
    PRIMARY KEY(TeaterstykkeID, PrisgruppeNavn),
    FOREIGN KEY(TeaterstykkeID) REFERENCES Teaterstykke(TeaterstykkeID)
);

CREATE TABLE IF NOT EXISTS Rolle (
    TeaterstykkeID INTEGER NOT NULL,
    Rollenavn TEXT,
    PRIMARY KEY(Rollenavn, TeaterstykkeID),
    FOREIGN KEY(TeaterstykkeID) REFERENCES Teaterstykke(TeaterstykkeID)
);

CREATE TABLE IF NOT EXISTS Akt (
    Aktnummer INTEGER NOT NULL,
    TeaterstykkeID INTEGER NOT NULL,
    Aktnavn TEXT,
    PRIMARY KEY(Aktnummer, TeaterstykkeID),
    FOREIGN KEY(TeaterstykkeID) REFERENCES Teaterstykke(TeaterstykkeID)
);

CREATE TABLE IF NOT EXISTS SkuespillerAnsatt (
    TeaterstykkeID INTEGER NOT NULL,
    Rollenavn TEXT NOT NULL,
    AnsattID INTEGER NOT NULL,
    PRIMARY KEY(TeaterstykkeID, Rollenavn, AnsattID),
    FOREIGN KEY(TeaterstykkeID) REFERENCES Teaterstykke(TeaterstykkeID),
    FOREIGN KEY(TeaterstykkeID, Rollenavn) REFERENCES Rolle(TeaterstykkeID, Rollenavn)
);

CREATE TABLE IF NOT EXISTS RolleIAkt (
    Rollenavn TEXT NOT NULL,
    Aktnummer INTEGER NOT NULL,
    TeaterstykkeID INTEGER NOT NULL,
    PRIMARY KEY(Rollenavn, Aktnummer, TeaterstykkeID),
    FOREIGN KEY(TeaterstykkeID, Rollenavn) REFERENCES Rolle(TeaterstykkeID, Rollenavn),
    FOREIGN KEY(TeaterstykkeID, Aktnummer) REFERENCES Akt(TeaterstykkeID, Aktnummer)
);

CREATE TABLE IF NOT EXISTS Ansatt (
    AnsattID INTEGER PRIMARY KEY,
    Navn TEXT,
    Epost TEXT,
    AnsattStatus TEXT,
    TeaterStykkeID INTEGER NOT NULL,
    FOREIGN KEY(TeaterStykkeID) REFERENCES Teaterstykke(TeaterstykkeID)
);

CREATE TABLE IF NOT EXISTS Oppgave (
    TeaterStykkeID INTEGER NOT NULL,
    Oppgavetype TEXT NOT NULL,
    AnsattID INTEGER NOT NULL,
    PRIMARY KEY(TeaterStykkeID, Oppgavetype),
    FOREIGN KEY(TeaterStykkeID, Oppgavetype) REFERENCES Oppgave(TeaterStykkeID, Oppgavetype),
    FOREIGN KEY(AnsattID) REFERENCES Ansatt(AnsattID)
);
