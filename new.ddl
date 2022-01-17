-- Generated by Oracle SQL Developer Data Modeler 20.4.0.374.0801
--   at:        2022-01-09 19:06:08 CET
--   site:      Oracle Database 11g
--   type:      Oracle Database 11g



DROP TABLE atrakcje CASCADE CONSTRAINTS;

DROP TABLE atrakcje_w_budynku CASCADE CONSTRAINTS;

DROP TABLE budynek CASCADE CONSTRAINTS;

DROP TABLE dokument CASCADE CONSTRAINTS;

DROP TABLE klient CASCADE CONSTRAINTS;

DROP TABLE miejsce_parkingowe CASCADE CONSTRAINTS;

DROP TABLE obsluguje CASCADE CONSTRAINTS;

DROP TABLE pokoj CASCADE CONSTRAINTS;

DROP TABLE pracownik CASCADE CONSTRAINTS;

DROP TABLE rachunek CASCADE CONSTRAINTS;

DROP TABLE rezerwacja CASCADE CONSTRAINTS;

DROP TABLE typ_dokumentu CASCADE CONSTRAINTS;

-- predefined type, no DDL - MDSYS.SDO_GEOMETRY

-- predefined type, no DDL - XMLTYPE

CREATE TABLE atrakcje (
    id_atrakcji  INTEGER NOT NULL,
    nazwa        VARCHAR2(25 CHAR) NOT NULL
);

ALTER TABLE atrakcje ADD CONSTRAINT atrakcje_pk PRIMARY KEY ( id_atrakcji );

CREATE TABLE atrakcje_w_budynku (
    budynek_nazwa  VARCHAR2(25 CHAR) NOT NULL,
    atrakcje_id    INTEGER NOT NULL
);

ALTER TABLE atrakcje_w_budynku ADD CONSTRAINT atrakcje_w_budynku_pk PRIMARY KEY ( budynek_nazwa,
                                                                                  atrakcje_id );

CREATE TABLE budynek (
    nazwa         VARCHAR2(25 CHAR) NOT NULL,
    ilosc_pieter  SMALLINT NOT NULL
);

ALTER TABLE budynek ADD CONSTRAINT budynek_pk PRIMARY KEY ( nazwa );

CREATE TABLE dokument (
    id_dokumentu         VARCHAR2(25 CHAR) NOT NULL,
    data_waznosci        DATE NOT NULL,
    typ_dokumentu_nazwa  VARCHAR2(25 CHAR) NOT NULL
);

CREATE INDEX dokument_tozsamosci__idx ON
    dokument (
        typ_dokumentu_nazwa
    ASC );

ALTER TABLE dokument ADD CONSTRAINT dokument_tozsamosci_pk PRIMARY KEY ( id_dokumentu );

CREATE TABLE klient (
    id_klienta           INTEGER NOT NULL,
    imie                 VARCHAR2(25 CHAR) NOT NULL,
    nazwisko             VARCHAR2(25 CHAR) NOT NULL,
    typ_dokumentu_nazwa  VARCHAR2(25 CHAR) NOT NULL
);

CREATE INDEX klient__idx ON
    klient (
        typ_dokumentu_nazwa
    ASC );

ALTER TABLE klient ADD CONSTRAINT klient_pk PRIMARY KEY ( id_klienta );

CREATE TABLE miejsce_parkingowe (
    nr_miejsca     INTEGER NOT NULL,
    budynek_nazwa  VARCHAR2(25 CHAR) NOT NULL
);

ALTER TABLE miejsce_parkingowe ADD CONSTRAINT miejsce_parkingowe_pk PRIMARY KEY ( nr_miejsca );

CREATE TABLE obsluguje (
    pokoj_nr_pokoju  INTEGER NOT NULL,
    pokoj_nazwa      VARCHAR2(25 CHAR) NOT NULL,
    pracownik_id     INTEGER NOT NULL
);

ALTER TABLE obsluguje
    ADD CONSTRAINT obsluguje_pk PRIMARY KEY ( pokoj_nr_pokoju,
                                              pokoj_nazwa,
                                              pracownik_id );

CREATE TABLE pokoj (
    nr_pokoju      INTEGER NOT NULL,
    pojemnosc      SMALLINT NOT NULL,
    pietro         SMALLINT NOT NULL,
    budynek_nazwa  VARCHAR2(25 CHAR) NOT NULL
);

ALTER TABLE pokoj ADD CONSTRAINT pokoj_pk PRIMARY KEY ( nr_pokoju,
                                                        budynek_nazwa );

CREATE TABLE pracownik (
    id_pracownika  INTEGER NOT NULL,
    imie           VARCHAR2(25 CHAR) NOT NULL,
    nazwisko       VARCHAR2(25 CHAR) NOT NULL,
    stanowisko     VARCHAR2(25 CHAR) NOT NULL,
    nr_tel         INTEGER
);

ALTER TABLE pracownik ADD CONSTRAINT pracownik_pk PRIMARY KEY ( id_pracownika );

CREATE TABLE rachunek (
    id_rachunku                   INTEGER NOT NULL,
    data_wystawienia              DATE NOT NULL,
    kwota                         NUMBER NOT NULL,
    rezerwacja_id_rezerwacji      INTEGER NOT NULL,
    rezerwacja_klient_id_klienta  INTEGER NOT NULL
);

CREATE UNIQUE INDEX rachunek__idx ON
    rachunek (
        rezerwacja_id_rezerwacji
    ASC,
        rezerwacja_klient_id_klienta
    ASC );

ALTER TABLE rachunek ADD CONSTRAINT rachunek_pk PRIMARY KEY ( id_rachunku );

CREATE TABLE rezerwacja (
    id_rezerwacji        INTEGER NOT NULL,
    data_poczatku        DATE NOT NULL,
    data_konca           DATE NOT NULL,
    pokoj_nr_pokoju      INTEGER NOT NULL,
    klient_id_klienta    INTEGER NOT NULL,
    pokoj_budynek_nazwa  VARCHAR2(25 CHAR) NOT NULL
);

ALTER TABLE rezerwacja ADD CONSTRAINT rezerwacja_pk PRIMARY KEY ( id_rezerwacji,
                                                                  klient_id_klienta );

CREATE TABLE typ_dokumentu (
    nazwa                  VARCHAR2(25 CHAR) NOT NULL,
    klient_id_klienta      INTEGER NOT NULL,
    dokument_id_dokumentu  VARCHAR2(25 CHAR) NOT NULL
);

CREATE UNIQUE INDEX typ_dokumentu__idx ON
    typ_dokumentu (
        klient_id_klienta
    ASC );

CREATE UNIQUE INDEX typ_dokumentu__idxv1 ON
    typ_dokumentu (
        dokument_id_dokumentu
    ASC );

ALTER TABLE typ_dokumentu ADD CONSTRAINT typ_dokumentu_pk PRIMARY KEY ( nazwa );

ALTER TABLE atrakcje_w_budynku
    ADD CONSTRAINT atrakcje_w_budynku_atrakcje_fk FOREIGN KEY ( atrakcje_id )
        REFERENCES atrakcje ( id_atrakcji );

ALTER TABLE atrakcje_w_budynku
    ADD CONSTRAINT atrakcje_w_budynku_budynek_fk FOREIGN KEY ( budynek_nazwa )
        REFERENCES budynek ( nazwa );

ALTER TABLE miejsce_parkingowe
    ADD CONSTRAINT miejsce_parkingowe_budynek_fk FOREIGN KEY ( budynek_nazwa )
        REFERENCES budynek ( nazwa );

ALTER TABLE obsluguje
    ADD CONSTRAINT obsluguje_pokoj_fk FOREIGN KEY ( pokoj_nr_pokoju,
                                                    pokoj_nazwa )
        REFERENCES pokoj ( nr_pokoju,
                           budynek_nazwa );

ALTER TABLE obsluguje
    ADD CONSTRAINT obsluguje_pracownik_fk FOREIGN KEY ( pracownik_id )
        REFERENCES pracownik ( id_pracownika );

ALTER TABLE pokoj
    ADD CONSTRAINT pokoj_budynek_fk FOREIGN KEY ( budynek_nazwa )
        REFERENCES budynek ( nazwa );

ALTER TABLE rachunek
    ADD CONSTRAINT rachunek_rezerwacja_fk FOREIGN KEY ( rezerwacja_id_rezerwacji,
                                                        rezerwacja_klient_id_klienta )
        REFERENCES rezerwacja ( id_rezerwacji,
                                klient_id_klienta );

ALTER TABLE rezerwacja
    ADD CONSTRAINT rezerwacja_klient_fk FOREIGN KEY ( klient_id_klienta )
        REFERENCES klient ( id_klienta );

ALTER TABLE rezerwacja
    ADD CONSTRAINT rezerwacja_pokoj_fk FOREIGN KEY ( pokoj_nr_pokoju,
                                                     pokoj_budynek_nazwa )
        REFERENCES pokoj ( nr_pokoju,
                           budynek_nazwa );



-- Oracle SQL Developer Data Modeler Summary Report: 
-- 
-- CREATE TABLE                            12
-- CREATE INDEX                             5
-- ALTER TABLE                             21
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           0
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          0
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   0
-- WARNINGS                                 0
