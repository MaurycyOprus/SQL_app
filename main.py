import pygame
from tkinter import *
import cx_Oracle
import datetime
from tkinter import messagebox
cx_Oracle.init_oracle_client(lib_dir=r"C:\Users\MaurycyOprus\Desktop\instantclient-basic-windows.x64-21.3.0.0.0\instantclient_21_3")
connection = cx_Oracle.connect(user="*******", password="*******",
                               dsn="admlab2.cs.put.poznan.pl/dblab02_students.cs.put.poznan.pl",
                               encoding="UTF-8")
cur = connection.cursor()

pygame.init()
screen_h = 700
screen_w = 1200
screen = pygame.display.set_mode((screen_w, screen_h))

color_buttons = (80, 120, 250)
cofnij_rect = pygame.Rect(1000, 20, 140, 32)
#menu
input_rect = pygame.Rect(100, 400, 140, 32)
atrakcje_rect = pygame.Rect(50, 250, 300, 120)
budynki_rect = pygame.Rect(450, 250, 300, 120)
klienci_rect = pygame.Rect(850, 250, 300, 120)
parking_rect = pygame.Rect(50, 400, 300, 120)
pokoje_rect = pygame.Rect(450, 400, 300, 120)
pracownicy_rect = pygame.Rect(850, 400, 300, 120)
rachunki_rect = pygame.Rect(50, 550, 300, 120)
show_rachunki_rect = pygame.Rect(251, 550, 300, 120)
rezerwacje_rect = pygame.Rect(450, 550, 300, 120)
show_rezerwacje_rect = pygame.Rect(651, 550, 300, 120)
wyswietl_rect = pygame.Rect(850, 550, 300, 120)
#atrakcje
dodaj_atr = pygame.Rect(50, 400, 300, 120)
edytuj_atr = pygame.Rect(450, 400, 300, 120)
usun_atr = pygame.Rect(850, 400, 300, 120)
#dodaj atrakcje
nazwa_atr = pygame.Rect(450, 400, 300, 120)
input_nazwa_atr = pygame.Rect(300, 560, 600, 40)
#edytuj atrakcje
id_atr = pygame.Rect(250, 400, 300, 120)
nazwa_atr2 = pygame.Rect(650, 400, 300, 120)
input_nazwa_atr2 = pygame.Rect(650, 560, 300, 40)
input_id_atr = pygame.Rect(250, 560, 300, 40)
#usun atrakcje
id_atr2 = pygame.Rect(450, 400, 300, 120)
input_id_atr2 = pygame.Rect(450, 560, 300, 40)
#budynki
dodaj_bud = pygame.Rect(50, 401, 300, 120)
edytuj_bud = pygame.Rect(450, 400, 300, 120)
usun_bud = pygame.Rect(850, 400, 300, 120)
#dodaj budynek
nazwa_bud = pygame.Rect(251, 400, 300, 120)
input_nazwa_bud = pygame.Rect(251, 560, 300, 40)
ilosc_pieter_bud = pygame.Rect(650, 401, 300, 120)
input_ilosc_pieter_bud = pygame.Rect(650, 559, 300, 40)
#edytuj budynek
nazwa_bud2 = pygame.Rect(250, 399, 300, 120)
input_nazwa_bud2 = pygame.Rect(250, 559, 300, 40)
ilosc_pieter_bud2 = pygame.Rect(650, 399, 300, 120)
input_ilosc_pieter_bud2 = pygame.Rect(650, 559, 300, 40)
#usun budynek
nazwa_bud3 = pygame.Rect(450, 400, 301, 120)
input_nazwa_bud3 = pygame.Rect(451, 560, 300, 40)
#klienci
dodaj_kl = pygame.Rect(50, 400, 300, 120)
edytuj_kl = pygame.Rect(450, 400, 300, 120)
usun_kl = pygame.Rect(850, 401, 300, 120)
#dodaj klienta
imie_kl = pygame.Rect(50, 250, 300, 80)
input_imie_kl = pygame.Rect(50, 350, 300, 40)
nazwisko_kl = pygame.Rect(450, 250, 350, 80)
input_nazwisko_kl = pygame.Rect(450, 350, 350, 40)
nazwa_typ_dok = pygame.Rect(850, 250, 300, 80)
input_nazwa_typ_dok = pygame.Rect(850, 350, 300, 40)
id_dok_toz = pygame.Rect(251, 420, 300, 80)
input_id_dok_toz = pygame.Rect(251, 521, 300, 40)
data_waz_dok_toz = pygame.Rect(650, 420, 300, 80)
input_data_waz_dok_toz = pygame.Rect(651, 520, 300, 40)
#edytuj klienta
imie_kl2 = pygame.Rect(51, 250, 350, 80)
input_imie_kl2 = pygame.Rect(50, 351, 350, 40)
nazwisko_kl2 = pygame.Rect(450, 250, 370, 80)
input_nazwisko_kl2 = pygame.Rect(450, 350, 370, 40)
nazwa_typ_dok2 = pygame.Rect(850, 250, 340, 80)
input_nazwa_typ_dok2 = pygame.Rect(851, 350, 340, 40)
id_dok_toz2 = pygame.Rect(251, 420, 300, 80)
input_id_dok_toz2 = pygame.Rect(251, 521, 300, 40)
data_waz_dok_toz2 = pygame.Rect(650, 420, 300, 80)
input_data_waz_dok_toz2 = pygame.Rect(651, 520, 300, 40)
#usun klienta
id_klienta = pygame.Rect(450, 401, 301, 120)
input_id_klienta = pygame.Rect(450, 559, 300, 40)
#parking
dodaj_park = pygame.Rect(251, 400, 300, 120)
# edytuj_park = pygame.Rect(450, 401, 300, 120)
usun_park = pygame.Rect(650, 401, 300, 120)
#dodaj miejsce
budynek = pygame.Rect(449, 299, 300, 120)
input_budynek = pygame.Rect(450, 460, 300, 40)
#usun miejsce
budynek2 = pygame.Rect(451, 299, 300, 120)
input_budynek2 = pygame.Rect(451, 459, 300, 40)
#pokoje
dodaj_pok = pygame.Rect(50, 401, 300, 120)
edytuj_pok = pygame.Rect(450, 400, 300, 120)
usun_pok = pygame.Rect(850, 401, 300, 120)
#dodaj pokoj
budynek_pok = pygame.Rect(50, 399, 300, 120)
input_budynek_pok = pygame.Rect(49, 559, 300, 40)
pojemnosc_pok = pygame.Rect(451, 400, 300, 120)
input_pojemnosc_pok = pygame.Rect(451, 559, 300, 40)
pietro_pok = pygame.Rect(851, 399, 300, 120)
input_pietro_pok = pygame.Rect(851, 559, 300, 40)
#edytuj pokoj
budynek_pok2 = pygame.Rect(251, 249, 320, 80)
input_budynek_pok2 = pygame.Rect(251, 349, 320, 40)
nr_pok2 = pygame.Rect(651, 249, 320, 80)
input_nr_pok2 = pygame.Rect(651, 350, 320, 40)
pojemnosc_pok2 = pygame.Rect(251, 420, 320, 80)
input_pojemnosc_pok2 = pygame.Rect(251, 519, 320, 40)
pietro_pok2 = pygame.Rect(651, 420, 320, 80)
input_pietro_pok2 = pygame.Rect(651, 519, 320, 40)
#usun pokoj
budynek_pok3 = pygame.Rect(249, 399, 300, 120)
input_budynek_pok3 = pygame.Rect(249, 559, 300, 40)
nr_pok3 = pygame.Rect(651, 399, 300, 120)
input_nr_pok3 = pygame.Rect(651, 559, 300, 40)
#pracowicy
dodaj_prac = pygame.Rect(50, 401, 300, 120)
edytuj_prac = pygame.Rect(450, 401, 300, 120)
usun_prac= pygame.Rect(850, 400, 300, 120)
#dodaj pracownika
imie_prac = pygame.Rect(251, 249, 300, 81)
input_imie_prac = pygame.Rect(251, 349, 300, 41)
nazwisko_prac = pygame.Rect(651, 249, 370, 81)
input_nazwisko_prac = pygame.Rect(651, 350, 370, 41)
stanowisko_prac = pygame.Rect(251, 420, 300, 81)
input_stanowisko_prac = pygame.Rect(251, 519, 300, 41)
tel_prac = pygame.Rect(651, 420, 370, 81)
input_tel_prac = pygame.Rect(651, 519, 370, 41)
#edytuj pracownika
id_prac2 = pygame.Rect(51, 250, 301, 80)
input_id_prac2 = pygame.Rect(51, 350, 301, 40)
imie_prac2 = pygame.Rect(451, 250, 301, 80)
input_imie_prac2 = pygame.Rect(451, 350, 301, 40)
nazwisko_prac2 = pygame.Rect(851, 250, 301, 80)
input_nazwisko_prac2 = pygame.Rect(851, 350, 301, 40)
stanowisko_prac2 = pygame.Rect(249, 420, 371, 80)
input_stanowisko_prac2 = pygame.Rect(249, 521, 371, 40)
tel_prac2 = pygame.Rect(651, 420, 371, 80)
input_tel_prac2 = pygame.Rect(650, 520, 371, 40)
#usun pracownika
id_prac3 = pygame.Rect(449, 298, 300, 120)
input_id_prac3 = pygame.Rect(449, 458, 300, 40)
#rachunki
dodaj_rach = pygame.Rect(450, 400, 300, 120)
#dodaj rachunek
data_rach = pygame.Rect(51, 398, 300, 120)
input_data_rach = pygame.Rect(51, 558, 300, 40)
kwota_rach = pygame.Rect(451, 398, 300, 120)
input_kwota_rach = pygame.Rect(451, 558, 300, 40)
rezerwacja_rach = pygame.Rect(851, 398, 300, 120)
input_rezerwacja_rach = pygame.Rect(851, 558, 300, 40)
id_klienta_rach = pygame.Rect(450, 251, 300, 80)
input_id_klienta_rach = pygame.Rect(450, 352, 300, 40)
#rezerwacje
dodaj_rez = pygame.Rect(50, 401, 300, 120)
edytuj_rez = pygame.Rect(450, 401, 300, 120)
usun_rez = pygame.Rect(850, 401, 300, 120)
#dodaj rezerwacje
id_kl_rez = pygame.Rect(50, 250, 301, 80)
input_id_kl_rez = pygame.Rect(50, 350, 301, 40)
nr_pok_rez = pygame.Rect(450, 250, 301, 80)
input_nr_pok_rez = pygame.Rect(450, 350, 301, 40)
budynek_rez = pygame.Rect(850, 250, 301, 80)
input_budynek_rez = pygame.Rect(850, 350, 301, 40)
poczatek_rez = pygame.Rect(251, 420, 301, 80)
input_poczatek_rez = pygame.Rect(251, 521, 301, 40)
koniec_rez = pygame.Rect(650, 420, 301, 80)
input_koniec_rez = pygame.Rect(651, 520, 301, 40)
#edytuj rezerwacje
id_rez2 = pygame.Rect(49, 250, 361, 80)
input_id_rez2 = pygame.Rect(49, 350, 361, 40)
nr_pok_rez2 = pygame.Rect(449, 250, 361, 80)
input_nr_pok_rez2 = pygame.Rect(449, 350, 361, 40)
budynek_rez2 = pygame.Rect(849, 250, 348, 80)
input_budynek_rez2 = pygame.Rect(849, 350, 348, 40)
poczatek_rez2 = pygame.Rect(249, 420, 361, 80)
input_poczatek_rez2 = pygame.Rect(249, 521, 361, 40)
koniec_rez2 = pygame.Rect(649, 420, 361, 80)
input_koniec_rez2 = pygame.Rect(649, 520, 361, 40)
#usun rezerwacje
id_rez3 = pygame.Rect(450, 300, 301, 120)
input_id_rez3 = pygame.Rect(450, 460, 301, 40)

menu_windows = [atrakcje_rect, budynki_rect, klienci_rect, parking_rect, pokoje_rect, pracownicy_rect, rachunki_rect, rezerwacje_rect, wyswietl_rect]
atrakcje_opcje = [dodaj_atr, edytuj_atr, usun_atr, cofnij_rect]
nowa_atr = [nazwa_atr, input_nazwa_atr, cofnij_rect]
ed_atr = [id_atr, input_id_atr, nazwa_atr2, input_nazwa_atr2,  cofnij_rect]
del_atr = [id_atr2, input_id_atr2, cofnij_rect]
budynki_opcje = [dodaj_bud, edytuj_bud, usun_bud, cofnij_rect]
nowy_bud = [nazwa_bud, input_nazwa_bud, ilosc_pieter_bud, input_ilosc_pieter_bud, cofnij_rect]
ed_bud = [nazwa_bud2, input_nazwa_bud2, ilosc_pieter_bud2, input_ilosc_pieter_bud2, cofnij_rect]
del_bud = [nazwa_bud3, input_nazwa_bud3, cofnij_rect]
klienci_opcje = [dodaj_kl, edytuj_kl, usun_kl, cofnij_rect]
nowy_kl = [imie_kl, input_imie_kl, nazwisko_kl, input_nazwisko_kl, nazwa_typ_dok, input_nazwa_typ_dok, id_dok_toz, input_id_dok_toz, data_waz_dok_toz, input_data_waz_dok_toz, cofnij_rect]
ed_kl = [imie_kl2, input_imie_kl2, nazwisko_kl2, input_nazwisko_kl2, nazwa_typ_dok2, input_nazwa_typ_dok2, id_dok_toz2, input_id_dok_toz2, data_waz_dok_toz2, input_data_waz_dok_toz2, cofnij_rect]
del_kl = [id_klienta, input_id_klienta, cofnij_rect]
parking_opcje = [dodaj_park, usun_park, cofnij_rect]    #usuniety edytuj_park
nowe_miejsce = [budynek, input_budynek, cofnij_rect]
del_miejsce = [budynek2, input_budynek2, cofnij_rect]
pokoje_opcje = [dodaj_pok, edytuj_pok, usun_pok, cofnij_rect]
nowy_pok = [budynek_pok, input_budynek_pok, pojemnosc_pok, input_pojemnosc_pok, pietro_pok, input_pietro_pok, cofnij_rect]
ed_pok = [budynek_pok2, input_budynek_pok2, nr_pok2, input_nr_pok2, pojemnosc_pok2, input_pojemnosc_pok2, pietro_pok2, input_pietro_pok2, cofnij_rect]
del_pok = [budynek_pok3, input_budynek_pok3, nr_pok3, input_nr_pok3, cofnij_rect]
pracownicy_opcje = [dodaj_prac, edytuj_prac, usun_prac, cofnij_rect]
nowy_prac = [imie_prac, input_imie_prac, nazwisko_prac, input_nazwisko_prac, stanowisko_prac, input_stanowisko_prac, tel_prac, input_tel_prac, cofnij_rect]
ed_prac = [id_prac2, input_id_prac2, imie_prac2, input_imie_prac2, nazwisko_prac2, input_nazwisko_prac2, stanowisko_prac2, input_stanowisko_prac2, tel_prac2, input_tel_prac2, cofnij_rect]
del_prac = [id_prac3, input_id_prac3, cofnij_rect]
rachunki_opcje = [dodaj_rach, cofnij_rect]
nowy_rach = [data_rach, input_data_rach, kwota_rach, input_kwota_rach, rezerwacja_rach, input_rezerwacja_rach, id_klienta_rach, input_id_klienta_rach, cofnij_rect]
rezerwacje_opcje = [dodaj_rez, edytuj_rez, usun_rez, cofnij_rect]
nowa_rez = [id_kl_rez, input_id_kl_rez, nr_pok_rez, input_nr_pok_rez, budynek_rez, input_budynek_rez, poczatek_rez, input_poczatek_rez, koniec_rez, input_koniec_rez, cofnij_rect]
ed_rez = [id_rez2, input_id_rez2, nr_pok_rez2, input_nr_pok_rez2, budynek_rez2, input_budynek_rez2, poczatek_rez2, input_poczatek_rez2, koniec_rez2, input_koniec_rez2, cofnij_rect]
del_rez = [id_rez3, input_id_rez3, cofnij_rect]
wyswietl_opcje = [atrakcje_rect, budynki_rect, klienci_rect, parking_rect, pokoje_rect, pracownicy_rect, show_rachunki_rect, show_rezerwacje_rect, cofnij_rect]
opcje = [menu_windows, atrakcje_opcje, budynki_opcje, klienci_opcje, parking_opcje, pokoje_opcje, pracownicy_opcje, rachunki_opcje, rezerwacje_opcje,
         nowa_atr, ed_atr, del_atr, nowy_bud, ed_bud, del_bud, nowy_kl, ed_kl, del_kl, nowe_miejsce, del_miejsce, nowy_pok, ed_pok, del_pok,
         nowy_prac, ed_prac, del_prac, nowy_rach, nowa_rez, ed_rez, del_rez, wyswietl_opcje]
widoczne = opcje[0]
aktualne_okno = menu_windows

color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('chartreuse4')
color = color_passive
wielka = pygame.font.SysFont('Arial', 60)
duza = pygame.font.SysFont('Arial', 30)
srednia = pygame.font.SysFont('Arial', 25)
mala = pygame.font.SysFont('Arial', 20)

user_text1 = ''
user_text2 = ''
user_text3 = ''
user_text4 = ''
user_text5 = ''
status1 = False
status2 = False
status3 = False
status4 = False
status5 = False
selected = False
i = 0

class Table:
    def __init__(self, root):
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(root, width=20, fg='blue',
                               font=('Arial', 16, 'bold'))

                self.e.grid(row=i, column=j)
                self.e.insert(END, str(data[i][j]))

def okienko(text, x, y, rect, font):
    pygame.draw.rect(screen, (80, 120, 250), rect)
    txt = font.render(text, True, (255, 255, 255))
    screen.blit(txt, (rect.x + x, rect.y + y))

def okienko_input(rect, color):
    pygame.draw.rect(screen, color, rect)

def menu():
    screen.fill((130, 230, 150))
    txt = wielka.render("WYBIERZ OPCJĘ", True, (255, 255, 255))
    screen.blit(txt, (400, 100))
    okienko("ATRAKCJE", 80, 40, atrakcje_rect, duza)
    okienko("BUDYNKI", 90, 40, budynki_rect, duza)
    okienko("PARKING", 90, 40, parking_rect, duza)
    okienko("KLIENCI", 90, 40, klienci_rect, duza)
    okienko("POKOJE", 90, 40, pokoje_rect, duza)
    okienko("PRACOWNICY", 80, 40, pracownicy_rect, srednia)
    okienko("RACHUNKI", 90, 40, rachunki_rect, duza)
    okienko("REZERWACJE", 80, 40, rezerwacje_rect, srednia)
    okienko("WYŚWIETL", 80, 40, wyswietl_rect, duza)

def atrakcje():
    screen.fill((130, 230, 150))
    txt = wielka.render("WYBIERZ OPCJĘ", True, (255, 255, 255))
    screen.blit(txt, (400, 100))
    okienko("DODAJ ATRAKCJĘ", 50, 40, dodaj_atr, mala)
    okienko("USUŃ ATRAKCJĘ", 65, 40, usun_atr, mala)
    okienko("EDYTUJ ATRAKCJĘ", 57, 40, edytuj_atr, mala)
    okienko("COFNIJ", 40, 5, cofnij_rect, mala)

def dodaj_atrakcje():
    screen.fill((130, 230, 150))
    okienko("COFNIJ", 40, 5, cofnij_rect, mala)
    okienko("PODAJ NAZWE ATRAKCJI", 50, 40, nazwa_atr, mala)
    if status1:
        okienko_input(input_nazwa_atr, color_active)
    else:
        okienko_input(input_nazwa_atr, color_passive)

def edytuj_atrakcje():
    screen.fill((130, 230, 150))
    okienko("COFNIJ", 40, 5, cofnij_rect, mala)
    okienko("PODAJ ID ATRAKCJI", 50, 40, id_atr, mala)
    okienko("PODAJ NOWĄ NAZWE", 50, 40, nazwa_atr2, mala)
    if status2:
        okienko_input(input_nazwa_atr2, color_active)
    else:
        okienko_input(input_nazwa_atr2, color_passive)

    if status1:
        okienko_input(input_id_atr, color_active)
    else:
        okienko_input(input_id_atr, color_passive)

def usun_atrakcje():
    screen.fill((130, 230, 150))
    okienko("COFNIJ", 40, 5, cofnij_rect, mala)
    okienko("PODAJ ID ATRAKCJI", 60, 40, id_atr2, mala)
    if status1:
        okienko_input(input_id_atr2, color_active)
    else:
        okienko_input(input_id_atr2, color_passive)

def budynki():
    screen.fill((130, 230, 150))
    txt = wielka.render("WYBIERZ OPCJĘ", True, (255, 255, 255))
    screen.blit(txt, (400, 100))
    okienko("DODAJ BUDYNEK", 50, 40, dodaj_bud, mala)
    okienko("USUŃ BUDYNEK", 55, 40, usun_bud, mala)
    okienko("EDYTUJ BUDYNEK", 57, 40, edytuj_bud, mala)
    okienko("COFNIJ", 40, 5, cofnij_rect, mala)

def dodaj_budynek():
    screen.fill((130, 230, 150))
    okienko("COFNIJ", 40, 5, cofnij_rect, mala)
    okienko("PODAJ NAZWE BUDYNKU", 50, 40, nazwa_bud, mala)
    okienko("PODAJ ILOŚĆ PIĘTER", 50, 40, ilosc_pieter_bud, mala)
    if status1:
        okienko_input(input_nazwa_bud, color_active)
    else:
        okienko_input(input_nazwa_bud, color_passive)

    if status2:
        okienko_input(input_ilosc_pieter_bud, color_active)
    else:
        okienko_input(input_ilosc_pieter_bud, color_passive)

def edytuj_budynek():
    screen.fill((130, 230, 150))
    okienko("COFNIJ", 40, 5, cofnij_rect, mala)
    okienko("PODAJ NAZWĘ", 60, 40, nazwa_bud2, mala)
    okienko("PODAJ ILOŚĆ PIĘTER", 40, 40, ilosc_pieter_bud2, mala)
    if status1:
        okienko_input(input_nazwa_bud2, color_active)
    else:
        okienko_input(input_nazwa_bud2, color_passive)

    if status2:
        okienko_input(input_ilosc_pieter_bud2, color_active)
    else:
        okienko_input(input_ilosc_pieter_bud2, color_passive)

def usun_budynek():
    screen.fill((130, 230, 150))
    okienko("COFNIJ", 40, 5, cofnij_rect, mala)
    okienko("PODAJ NAZWĘ", 80, 40, id_atr2, mala)
    if status1:
        okienko_input(input_nazwa_bud3, color_active)
    else:
        okienko_input(input_nazwa_bud3, color_passive)

def klienci():
    screen.fill((130, 230, 150))
    txt = wielka.render("WYBIERZ OPCJĘ", True, (255, 255, 255))
    screen.blit(txt, (400, 100))
    okienko("DODAJ KLIENTA", 50, 40, dodaj_kl, srednia)
    okienko("USUŃ KLIENTA", 55, 40, usun_kl, srednia)
    okienko("EDYTUJ KLIENTA", 57, 40, edytuj_kl, srednia)
    okienko("COFNIJ", 40, 5, cofnij_rect, mala)

def dodaj_klienta():
    screen.fill((130, 230, 150))
    okienko("COFNIJ", 40, 5, cofnij_rect, mala)
    okienko("PODAJ IMIE KLIENTA", 50, 25, imie_kl, mala)
    okienko("PODAJ NAZWISKO KLIENTA", 50, 25, nazwisko_kl, mala)
    okienko("PODAJ TYP DOKUMENTU", 50, 25, nazwa_typ_dok, mala)
    okienko("PODAJ ID DOKUMENTU", 50, 25, id_dok_toz, mala)
    okienko("PODAJ DATE WAŻNOŚCI", 50, 25, data_waz_dok_toz, mala)
    if status1:
        okienko_input(input_imie_kl, color_active)
    else:
        okienko_input(input_imie_kl, color_passive)

    if status2:
        okienko_input(input_nazwisko_kl, color_active)
    else:
        okienko_input(input_nazwisko_kl, color_passive)

    if status3:
        okienko_input(input_nazwa_typ_dok, color_active)
    else:
        okienko_input(input_nazwa_typ_dok, color_passive)

    if status4:
        okienko_input(input_id_dok_toz, color_active)
    else:
        okienko_input(input_id_dok_toz, color_passive)

    if status5:
        okienko_input(input_data_waz_dok_toz, color_active)
    else:
        okienko_input(input_data_waz_dok_toz, color_passive)

def edytuj_klienta():                                                           #zmienić położenie - 2x2
    screen.fill((130, 230, 150))
    okienko("COFNIJ", 40, 5, cofnij_rect, mala)
    okienko("PODAJ NOWE IMIE KLIENTA", 40, 25, imie_kl2, mala)
    okienko("PODAJ NOWE NAZWISKO KLIENTA", 15, 25, nazwisko_kl2, mala)
    okienko("PODAJ NOWY TYP DOKUMENTU", 20, 25, nazwa_typ_dok2, mala)
    okienko("PODAJ ID KLIENTA", 50, 25, id_dok_toz2, mala)
    if status1:
        okienko_input(input_imie_kl2, color_active)
    else:
        okienko_input(input_imie_kl2, color_passive)

    if status2:
        okienko_input(input_nazwisko_kl2, color_active)
    else:
        okienko_input(input_nazwisko_kl2, color_passive)

    if status3:
        okienko_input(input_nazwa_typ_dok2, color_active)
    else:
        okienko_input(input_nazwa_typ_dok2, color_passive)

    if status4:
        okienko_input(input_id_dok_toz2, color_active)
    else:
        okienko_input(input_id_dok_toz2, color_passive)

def usun_klienta():
    screen.fill((130, 230, 150))
    okienko("COFNIJ", 40, 5, cofnij_rect, mala)
    okienko("PODAJ ID KLIENTA", 50, 40, id_klienta, mala)
    if status1:
        okienko_input(input_id_klienta, color_active)
    else:
        okienko_input(input_id_klienta, color_passive)

def parking():
    screen.fill((130, 230, 150))
    txt = wielka.render("WYBIERZ OPCJĘ", True, (255, 255, 255))
    screen.blit(txt, (400, 100))
    okienko("DODAJ MIEJSCE", 60, 40, dodaj_park, mala)
    okienko("USUŃ MIEJSCE", 70, 40, usun_park, mala)
    # okienko("EDYTUJ MIEJSCE", 27, 40, edytuj_park, mala)
    okienko("COFNIJ", 40, 5, cofnij_rect, mala)

def dodaj_miejsce():
    screen.fill((130, 230, 150))
    okienko("COFNIJ", 40, 5, cofnij_rect, mala)
    okienko("PODAJ NAZWĘ BUDYNKU", 50, 40, budynek, mala)
    if status1:
        okienko_input(input_budynek, color_active)
    else:
        okienko_input(input_budynek, color_passive)

def usun_miejsce():
    screen.fill((130, 230, 150))
    okienko("COFNIJ", 40, 5, cofnij_rect, mala)
    okienko("PODAJ NUMER MIEJSCA", 50, 40, budynek, mala)
    if status1:
        okienko_input(input_budynek2, color_active)
    else:
        okienko_input(input_budynek2, color_passive)

def pokoje():
    screen.fill((130, 230, 150))
    txt = wielka.render("WYBIERZ OPCJĘ", True, (255, 255, 255))
    screen.blit(txt, (400, 100))
    okienko("DODAJ POKÓJ", 70, 40, dodaj_pok, srednia)
    okienko("USUŃ POKÓJ", 75, 40, usun_pok, srednia)
    okienko("EDYTUJ POKÓJ", 62, 40, edytuj_pok, srednia)
    okienko("COFNIJ", 40, 5, cofnij_rect, mala)

def dodaj_pokoj():
    screen.fill((130, 230, 150))
    okienko("NAZWA BUDYNKU", 50, 40, budynek_pok, srednia)
    okienko("POJEMNOŚĆ POKOJU", 50, 40, pojemnosc_pok, mala)
    okienko("PIĘTRO POKOJU", 50, 40, pietro_pok, srednia)
    okienko("COFNIJ", 40, 5, cofnij_rect, mala)
    if status1:
        okienko_input(input_budynek_pok, color_active)
    else:
        okienko_input(input_budynek_pok, color_passive)

    if status2:
        okienko_input(input_pojemnosc_pok, color_active)
    else:
        okienko_input(input_pojemnosc_pok, color_passive)

    if status3:
        okienko_input(input_pietro_pok, color_active)
    else:
        okienko_input(input_pietro_pok, color_passive)

def edytuj_pokoj():
    screen.fill((130, 230, 150))
    okienko("NAZWA BUDYNKU", 30, 40, budynek_pok2, srednia)
    okienko("NUMER POKOJU", 30, 40, nr_pok2, srednia)
    okienko("NOWA POJEMNOŚĆ POKOJU", 30, 40, pojemnosc_pok2, mala)
    okienko("NOWE PIĘTRO POKOJU", 30, 40, pietro_pok2, srednia)
    okienko("COFNIJ", 40, 5, cofnij_rect, mala)
    if status1:
        okienko_input(input_budynek_pok2, color_active)
    else:
        okienko_input(input_budynek_pok2, color_passive)

    if status2:
        okienko_input(input_nr_pok2, color_active)
    else:
        okienko_input(input_nr_pok2, color_passive)

    if status3:
        okienko_input(input_pojemnosc_pok2, color_active)
    else:
        okienko_input(input_pojemnosc_pok2, color_passive)

    if status4:
        okienko_input(input_pietro_pok2, color_active)
    else:
        okienko_input(input_pietro_pok2, color_passive)

def usun_pokoj():
    screen.fill((130, 230, 150))
    okienko("COFNIJ", 40, 5, cofnij_rect, mala)
    okienko("PODAJ NAZWĘ BUDYNKU", 50, 40, budynek_pok3, mala)
    okienko("PODAJ NUMER POKOJU", 50, 40, nr_pok3, mala)
    if status1:
        okienko_input(input_budynek_pok3, color_active)
    else:
        okienko_input(input_budynek_pok3, color_passive)

    if status2:
        okienko_input(input_nr_pok3, color_active)
    else:
        okienko_input(input_nr_pok3, color_passive)

def pracownicy():
    screen.fill((130, 230, 150))
    txt = wielka.render("WYBIERZ OPCJĘ", True, (255, 255, 255))
    screen.blit(txt, (400, 100))
    okienko("DODAJ PRACOWNIKA", 50, 40, dodaj_prac, mala)
    okienko("USUŃ PRACOWNIKA", 55, 40, usun_prac, mala)
    okienko("EDYTUJ PRACOWNIKA", 67, 40, edytuj_prac, mala)
    okienko("COFNIJ", 40, 5, cofnij_rect, mala)

def dodaj_pracownika():
    screen.fill((130, 230, 150))
    okienko("COFNIJ", 40, 5, cofnij_rect, mala)
    okienko("PODAJ IMIE PRACOWNIKA", 35, 25, imie_prac, mala)
    okienko("PODAJ NAZWISKO PRACOWNIKA", 15, 25, nazwisko_prac, mala)
    okienko("PODAJ STANOWISKO", 60, 25, stanowisko_prac, mala)
    okienko("PODAJ NUMER TELEFONU", 20, 25, tel_prac, mala)
    if status1:
        okienko_input(input_imie_prac, color_active)
    else:
        okienko_input(input_imie_prac, color_passive)

    if status2:
        okienko_input(input_nazwisko_prac, color_active)
    else:
        okienko_input(input_nazwisko_prac, color_passive)

    if status3:
        okienko_input(input_stanowisko_prac, color_active)
    else:
        okienko_input(input_stanowisko_prac, color_passive)

    if status4:
        okienko_input(input_tel_prac, color_active)
    else:
        okienko_input(input_tel_prac, color_passive)

def edytuj_pracownika():
    screen.fill((130, 230, 150))
    okienko("COFNIJ", 40, 5, cofnij_rect, mala)
    okienko("PODAJ ID PRACOWNIKA", 50, 25, id_prac2, mala)
    okienko("PODAJ NOWE IMIE", 50, 25, imie_prac2, mala)
    okienko("PODAJ NOWE NAZWISKO", 40, 25, nazwisko_prac2, mala)
    okienko("PODAJ NOWE STANOWISKO", 35, 25, stanowisko_prac2, mala)
    okienko("PODAJ NOWY NUMER TELEFONU", 20, 25, tel_prac, mala)
    if status1:
        okienko_input(input_id_prac2, color_active)
    else:
        okienko_input(input_id_prac2, color_passive)

    if status2:
        okienko_input(input_imie_prac2, color_active)
    else:
        okienko_input(input_imie_prac2, color_passive)

    if status3:
        okienko_input(input_nazwisko_prac2, color_active)
    else:
        okienko_input(input_nazwisko_prac2, color_passive)

    if status4:
        okienko_input(input_stanowisko_prac2, color_active)
    else:
        okienko_input(input_stanowisko_prac2, color_passive)

    if status5:
        okienko_input(input_tel_prac2, color_active)
    else:
        okienko_input(input_tel_prac2, color_passive)


def usun_pracownika():
    screen.fill((130, 230, 150))
    okienko("COFNIJ", 40, 5, cofnij_rect, mala)
    okienko("PODAJ ID PRACOWNIKA", 50, 40, id_prac3, mala)
    if status1:
        okienko_input(input_id_prac3, color_active)
    else:
        okienko_input(input_id_prac3, color_passive)

def rachunki():
    screen.fill((130, 230, 150))
    txt = wielka.render("WYBIERZ OPCJĘ", True, (255, 255, 255))
    screen.blit(txt, (400, 100))
    okienko("DODAJ RACHUNEK", 70, 40, dodaj_rach, mala)
    okienko("COFNIJ", 40, 5, cofnij_rect, mala)

def dodaj_rachunek():
    screen.fill((130, 230, 150))
    okienko("COFNIJ", 40, 5, cofnij_rect, mala)
    okienko("PODAJ DATĘ WYSTAWIENIA", 30, 35, data_rach, mala)
    okienko("PODAJ KWOTĘ RACHUNKU", 30, 35, kwota_rach, mala)
    okienko("PODAJ ID REZERWACJI", 30, 35, rezerwacja_rach, mala)
    okienko("PODAJ ID KLIENTA", 30, 35, id_klienta_rach, mala)
    if status1:
        okienko_input(input_data_rach, color_active)
    else:
        okienko_input(input_data_rach, color_passive)

    if status2:
        okienko_input(input_kwota_rach, color_active)
    else:
        okienko_input(input_kwota_rach, color_passive)

    if status3:
        okienko_input(input_rezerwacja_rach, color_active)
    else:
        okienko_input(input_rezerwacja_rach, color_passive)

    if status4:
        okienko_input(input_id_klienta_rach, color_active)
    else:
        okienko_input(input_id_klienta_rach, color_passive)

def rezerwacje():
    screen.fill((130, 230, 150))
    txt = wielka.render("WYBIERZ OPCJĘ", True, (255, 255, 255))
    screen.blit(txt, (400, 100))
    okienko("DODAJ REZERWACJĘ", 50, 40, dodaj_rez, mala)
    okienko("USUŃ REZERWACJĘ", 55, 40, usun_rez, mala)
    okienko("EDYTUJ REZERWACJĘ", 57, 40, edytuj_rez, mala)
    okienko("COFNIJ", 40, 5, cofnij_rect, mala)

def dodaj_rezerwacje():
    screen.fill((130, 230, 150))
    okienko("COFNIJ", 40, 5, cofnij_rect, mala)
    okienko("PODAJ ID KLIENTA", 50, 25, id_kl_rez, mala)
    okienko("PODAJ NUMER POKOJU", 50, 25, nr_pok_rez, mala)
    okienko("PODAJ NAZWE BUDYNKU", 50, 25, budynek_rez, mala)
    okienko("PODAJ DATĘ POCZĄTKU", 50, 25, poczatek_rez, mala)
    okienko("PODAJ DATE KOŃCA", 50, 25, koniec_rez, mala)
    if status1:
        okienko_input(input_id_kl_rez, color_active)
    else:
        okienko_input(input_id_kl_rez, color_passive)

    if status2:
        okienko_input(input_nr_pok_rez, color_active)
    else:
        okienko_input(input_nr_pok_rez, color_passive)

    if status3:
        okienko_input(input_budynek_rez, color_active)
    else:
        okienko_input(input_budynek_rez, color_passive)

    if status4:
        okienko_input(input_poczatek_rez, color_active)
    else:
        okienko_input(input_poczatek_rez, color_passive)

    if status5:
        okienko_input(input_koniec_rez, color_active)
    else:
        okienko_input(input_koniec_rez, color_passive)

def edytuj_rezerwacje():
    screen.fill((130, 230, 150))
    okienko("COFNIJ", 40, 5, cofnij_rect, mala)
    okienko("PODAJ ID REZERWACJE", 50, 25, id_kl_rez, mala)
    okienko("PODAJ NOWY NUMER POKOJU", 30, 25, nr_pok_rez, mala)
    okienko("PODAJ NOWĄ NAZWĘ BUDYNKU", 30, 25, budynek_rez, mala)
    okienko("PODAJ NOWĄ DATĘ POCZĄTKU", 30, 25, poczatek_rez, mala)
    okienko("PODAJ NOWĄ DATĘ KOŃCA", 40, 25, koniec_rez, mala)
    if status1:
        okienko_input(input_id_rez2, color_active)
    else:
        okienko_input(input_id_rez2, color_passive)

    if status2:
        okienko_input(input_nr_pok_rez2, color_active)
    else:
        okienko_input(input_nr_pok_rez2, color_passive)

    if status3:
        okienko_input(input_budynek_rez2, color_active)
    else:
        okienko_input(input_budynek_rez2, color_passive)

    if status4:
        okienko_input(input_poczatek_rez2, color_active)
    else:
        okienko_input(input_poczatek_rez2, color_passive)

    if status5:
        okienko_input(input_koniec_rez2, color_active)
    else:
        okienko_input(input_koniec_rez2, color_passive)

def usun_rezerwacje():
    screen.fill((130, 230, 150))
    okienko("COFNIJ", 40, 5, cofnij_rect, mala)
    okienko("PODAJ ID REZERWACJI", 50, 40, id_rez3, mala)
    if status1:
        okienko_input(input_id_rez3, color_active)
    else:
        okienko_input(input_id_rez3, color_passive)

def co_wyswietl():
    screen.fill((130, 230, 150))
    txt = wielka.render("WYBIERZ OPCJĘ", True, (255, 255, 255))
    screen.blit(txt, (400, 100))
    okienko("COFNIJ", 40, 5, cofnij_rect, mala)
    okienko("ATRAKCJE", 80, 40, atrakcje_rect, duza)
    okienko("BUDYNKI", 90, 40, budynki_rect, duza)
    okienko("PARKING", 90, 40, parking_rect, duza)
    okienko("KLIENCI", 90, 40, klienci_rect, duza)
    okienko("POKOJE", 90, 40, pokoje_rect, duza)
    okienko("PRACOWNICY", 80, 40, pracownicy_rect, srednia)
    okienko("RACHUNKI", 90, 40, show_rachunki_rect, duza)
    okienko("REZERWACJE", 80, 40, show_rezerwacje_rect, srednia)

running = True
while running:
    if aktualne_okno == menu_windows:
        menu()
    elif aktualne_okno == atrakcje_opcje:
        atrakcje()
    elif aktualne_okno == nowa_atr:
        dodaj_atrakcje()
    elif aktualne_okno == ed_atr:
        edytuj_atrakcje()
    elif aktualne_okno == del_atr:
        usun_atrakcje()
    elif aktualne_okno == budynki_opcje:
        budynki()
    elif aktualne_okno == nowy_bud:
        dodaj_budynek()
    elif aktualne_okno == ed_bud:
        edytuj_budynek()
    elif aktualne_okno == del_bud:
        usun_budynek()
    elif aktualne_okno == klienci_opcje:
        klienci()
    elif aktualne_okno == nowy_kl:
        dodaj_klienta()
    elif aktualne_okno == ed_kl:
        edytuj_klienta()
    elif aktualne_okno == del_kl:
        usun_klienta()
    elif aktualne_okno == parking_opcje:
        parking()
    elif aktualne_okno == nowe_miejsce:
        dodaj_miejsce()
    elif aktualne_okno == del_miejsce:
        usun_miejsce()
    elif aktualne_okno == pokoje_opcje:
        pokoje()
    elif aktualne_okno == nowy_pok:
        dodaj_pokoj()
    elif aktualne_okno == ed_pok:
        edytuj_pokoj()
    elif aktualne_okno == del_pok:
        usun_pokoj()
    elif aktualne_okno == pracownicy_opcje:
        pracownicy()
    elif aktualne_okno == nowy_prac:
        dodaj_pracownika()
    elif aktualne_okno == ed_prac:
        edytuj_pracownika()
    elif aktualne_okno == del_prac:
        usun_pracownika()
    elif aktualne_okno == rachunki_opcje:
        rachunki()
    elif aktualne_okno == nowy_rach:
        dodaj_rachunek()
    elif aktualne_okno == rezerwacje_opcje:
        rezerwacje()
    elif aktualne_okno == nowa_rez:
        dodaj_rezerwacje()
    elif aktualne_okno == ed_rez:
        edytuj_rezerwacje()
    elif aktualne_okno == del_rez:
        usun_rezerwacje()
    elif aktualne_okno == wyswietl_opcje:
        co_wyswietl()

    selected = False

    text_surface1 = duza.render(user_text1, True, (255, 255, 255))
    text_surface2 = duza.render(user_text2, True, (255, 255, 255))
    text_surface3 = duza.render(user_text3, True, (255, 255, 255))
    text_surface4 = duza.render(user_text4, True, (255, 255, 255))
    text_surface5 = duza.render(user_text5, True, (255, 255, 255))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            status1 = False
            status2 = False
            status3 = False
            status4 = False
            status5 = False
            for i in range(len (widoczne)):
                if widoczne[i].collidepoint(event.pos):
                    selected = True
                    break

            if selected:
                if widoczne[i] == cofnij_rect:                                                                                                                              #cofanie
                    user_text1 = ''
                    user_text2 = ''
                    user_text3 = ''
                    user_text4 = ''
                    user_text5 = ''
                    if aktualne_okno == atrakcje_opcje or aktualne_okno == budynki_opcje or aktualne_okno == klienci_opcje or aktualne_okno == parking_opcje or aktualne_okno == rezerwacje_opcje or aktualne_okno == pokoje_opcje or aktualne_okno == pracownicy_opcje or aktualne_okno == rachunki_opcje or aktualne_okno == wyswietl_opcje:
                        aktualne_okno = menu_windows
                        widoczne = opcje[0]
                    elif aktualne_okno == nowa_atr or aktualne_okno == ed_atr or aktualne_okno == del_atr:
                        aktualne_okno = atrakcje_opcje
                        widoczne = opcje[1]
                    elif aktualne_okno == nowy_bud or aktualne_okno == ed_bud or aktualne_okno == del_bud:
                        aktualne_okno = budynki_opcje
                        widoczne = opcje[2]
                    elif aktualne_okno == nowy_kl or aktualne_okno == ed_kl or aktualne_okno == del_kl:
                        aktualne_okno = klienci_opcje
                        widoczne = opcje[3]
                    elif aktualne_okno == nowe_miejsce or aktualne_okno == del_miejsce:
                        aktualne_okno = parking_opcje
                        widoczne = opcje[4]
                    elif aktualne_okno == nowy_pok or aktualne_okno == ed_pok or aktualne_okno == del_pok:
                        aktualne_okno = pokoje_opcje
                        widoczne = opcje[5]
                    elif aktualne_okno == nowy_prac or aktualne_okno == ed_prac or aktualne_okno == del_prac:
                        aktualne_okno = pracownicy_opcje
                        widoczne = opcje[6]
                    elif aktualne_okno == nowy_rach:
                        aktualne_okno = rachunki_opcje
                        widoczne = opcje[7]
                    elif aktualne_okno == nowa_rez or aktualne_okno == ed_rez or aktualne_okno == del_rez:
                        aktualne_okno = rezerwacje_opcje
                        widoczne = opcje[8]
#-------------------------------------------------------------------
                elif i == 0 and aktualne_okno == menu_windows:
                    aktualne_okno = atrakcje_opcje
                    widoczne = opcje[1]

                elif i == 0 and aktualne_okno == atrakcje_opcje:
                    aktualne_okno = nowa_atr
                    widoczne = opcje[9]

                elif i == 1 and aktualne_okno == nowa_atr:
                    status1 = True

                elif i == 1 and aktualne_okno == atrakcje_opcje:
                    aktualne_okno = ed_atr
                    widoczne = opcje[10]

                elif i == 1 and aktualne_okno == ed_atr:
                    status1 = True
                    status2 = False

                elif i == 3 and aktualne_okno == ed_atr:
                    status1 = False
                    status2 = True

                elif i == 2 and aktualne_okno == atrakcje_opcje:
                    aktualne_okno = del_atr
                    widoczne = opcje[11]

                elif i == 1 and aktualne_okno == del_atr:
                    status1 = True
#----------------------------------------------------------------
                elif i == 1 and aktualne_okno == menu_windows:
                    aktualne_okno = budynki_opcje
                    widoczne = opcje[2]

                elif i == 0 and aktualne_okno == budynki_opcje:
                    aktualne_okno = nowy_bud
                    widoczne = opcje[12]

                elif i == 1 and aktualne_okno == nowy_bud:
                    status1 = True
                    status2 = False

                elif i == 3 and aktualne_okno == nowy_bud:
                    status1 = False
                    status2 = True

                elif i == 1 and aktualne_okno == budynki_opcje:
                    aktualne_okno = ed_bud
                    widoczne = opcje[13]

                elif i == 1 and aktualne_okno == ed_bud:
                    status1 = True
                    status2 = False

                elif i == 3 and aktualne_okno == ed_bud:
                    status1 = False
                    status2 = True

                elif i == 2 and aktualne_okno == budynki_opcje:
                    aktualne_okno = del_bud
                    widoczne = opcje[14]

                elif i == 1 and aktualne_okno == del_bud:
                    status1 = True
#----------------------------------------------------------------
                elif i == 2 and aktualne_okno == menu_windows:
                    aktualne_okno = klienci_opcje
                    widoczne = opcje[3]

                elif i == 0 and aktualne_okno == klienci_opcje:
                    aktualne_okno = nowy_kl
                    widoczne = opcje[15]

                elif i == 1 and aktualne_okno == nowy_kl:
                    status1 = True
                    status2 = False
                    status3 = False
                    status4 = False
                    status5 = False

                elif i == 3 and aktualne_okno == nowy_kl:
                    status1 = False
                    status2 = True
                    status3 = False
                    status4 = False
                    status5 = False

                elif i == 5 and aktualne_okno == nowy_kl:
                    status1 = False
                    status2 = False
                    status3 = True
                    status4 = False
                    status5 = False

                elif i == 7 and aktualne_okno == nowy_kl:
                    status1 = False
                    status2 = False
                    status3 = False
                    status4 = True
                    status5 = False

                elif i == 9 and aktualne_okno == nowy_kl:
                    status1 = False
                    status2 = False
                    status3 = False
                    status4 = False
                    status5 = True

                elif i == 1 and aktualne_okno == klienci_opcje:
                    aktualne_okno = ed_kl
                    widoczne = opcje[16]

                elif i == 1 and aktualne_okno == ed_kl:
                    status1 = True
                    status2 = False
                    status3 = False
                    status4 = False

                elif i == 3 and aktualne_okno == ed_kl:
                    status1 = False
                    status2 = True
                    status3 = False
                    status4 = False

                elif i == 5 and aktualne_okno == ed_kl:
                    status1 = False
                    status2 = False
                    status3 = True
                    status4 = False

                elif i == 7 and aktualne_okno == ed_kl:
                    status1 = False
                    status2 = False
                    status3 = False
                    status4 = True

                elif i == 2 and aktualne_okno == klienci_opcje:
                    aktualne_okno = del_kl
                    widoczne = opcje[17]

                elif i == 1 and aktualne_okno == del_kl:
                    status1 = True
# ----------------------------------------------------------------
                elif i == 3 and aktualne_okno == menu_windows:
                    aktualne_okno = parking_opcje
                    widoczne = opcje[4]

                elif i == 0 and aktualne_okno == parking_opcje:
                    aktualne_okno = nowe_miejsce
                    widoczne = opcje[18]

                elif i == 1 and aktualne_okno == nowe_miejsce:
                    status1 = True

                elif i == 1 and aktualne_okno == parking_opcje:
                    aktualne_okno = del_miejsce
                    widoczne = opcje[19]

                elif i == 1 and aktualne_okno == del_miejsce:
                    status1 = True
# ----------------------------------------------------------------
                elif i == 4 and aktualne_okno == menu_windows:
                    aktualne_okno = pokoje_opcje
                    widoczne = opcje[5]
                elif i == 0 and aktualne_okno == pokoje_opcje:
                    aktualne_okno = nowy_pok
                    widoczne = opcje[20]

                elif i == 1 and aktualne_okno == nowy_pok:
                    status1 = True
                    status2 = False
                    status3 = False

                elif i == 3 and aktualne_okno == nowy_pok:
                    status1 = False
                    status2 = True
                    status3 = False

                elif i == 5 and aktualne_okno == nowy_pok:
                    status1 = False
                    status2 = False
                    status3 = True

                elif i == 1 and aktualne_okno == pokoje_opcje:
                    aktualne_okno = ed_pok
                    widoczne = opcje[21]

                elif i == 1 and aktualne_okno == ed_pok:
                    status1 = True
                    status2 = False
                    status3 = False
                    status4 = False

                elif i == 3 and aktualne_okno == ed_pok:
                    status1 = False
                    status2 = True
                    status3 = False
                    status4 = False

                elif i == 5 and aktualne_okno == ed_pok:
                    status1 = False
                    status2 = False
                    status3 = True
                    status4 = False

                elif i == 7 and aktualne_okno == ed_pok:
                    status1 = False
                    status2 = False
                    status3 = False
                    status4 = True

                elif i == 2 and aktualne_okno == pokoje_opcje:
                    aktualne_okno = del_pok
                    widoczne = opcje[22]
                elif i == 1 and aktualne_okno == del_pok:
                    status1 = True
                    status2 = False
                elif i == 3 and aktualne_okno == del_pok:
                    status1 = False
                    status2 = True
# ----------------------------------------------------------------
                elif i == 5 and aktualne_okno == menu_windows:
                    aktualne_okno = pracownicy_opcje
                    widoczne = opcje[6]

                elif i == 0 and aktualne_okno == pracownicy_opcje:
                    aktualne_okno = nowy_prac
                    widoczne = opcje[23]

                elif i == 1 and aktualne_okno == nowy_prac:
                    status1 = True
                    status2 = False
                    status3 = False
                    status4 = False

                elif i == 3 and aktualne_okno == nowy_prac:
                    status1 = False
                    status2 = True
                    status3 = False
                    status4 = False

                elif i == 5 and aktualne_okno == nowy_prac:
                    status1 = False
                    status2 = False
                    status3 = True
                    status4 = False

                elif i == 7 and aktualne_okno == nowy_prac:
                    status1 = False
                    status2 = False
                    status3 = False
                    status4 = True

                elif i == 1 and aktualne_okno == pracownicy_opcje:
                    aktualne_okno = ed_prac
                    widoczne = opcje[24]

                elif i == 1 and aktualne_okno == ed_prac:
                    status1 = True
                    status2 = False
                    status3 = False
                    status4 = False
                    status5 = False

                elif i == 3 and aktualne_okno == ed_prac:
                    status1 = False
                    status2 = True
                    status3 = False
                    status4 = False
                    status5 = False

                elif i == 5 and aktualne_okno == ed_prac:
                    status1 = False
                    status2 = False
                    status3 = True
                    status4 = False
                    status5 = False

                elif i == 7 and aktualne_okno == ed_prac:
                    status1 = False
                    status2 = False
                    status3 = False
                    status4 = True
                    status5 = False

                elif i == 9 and aktualne_okno == ed_prac:
                    status1 = False
                    status2 = False
                    status3 = False
                    status4 = False
                    status5 = True

                elif i == 2 and aktualne_okno == pracownicy_opcje:
                    aktualne_okno = del_prac
                    widoczne = opcje[25]

                elif i == 1 and aktualne_okno == del_prac:
                    status1 = True
# ----------------------------------------------------------------
                elif i == 6 and aktualne_okno == menu_windows:
                    aktualne_okno = rachunki_opcje
                    widoczne = opcje[7]
                elif i == 0 and aktualne_okno == rachunki_opcje:
                    aktualne_okno = nowy_rach
                    widoczne = opcje[26]
                elif i == 1 and aktualne_okno == nowy_rach:
                    status1 = True
                    status2 = False
                    status3 = False
                    status4 = False
                elif i == 3 and aktualne_okno == nowy_rach:
                    status1 = False
                    status2 = True
                    status3 = False
                    status4 = False

                elif i == 5 and aktualne_okno == nowy_rach:
                    status1 = False
                    status2 = False
                    status3 = True
                    status4 = False

                elif i == 7 and aktualne_okno == nowy_rach:
                    status1 = False
                    status2 = False
                    status3 = False
                    status4 = True
# ----------------------------------------------------------------
                elif i == 7 and aktualne_okno == menu_windows:
                    aktualne_okno = rezerwacje_opcje
                    widoczne = opcje[8]

                elif i == 0 and aktualne_okno == rezerwacje_opcje:
                    aktualne_okno = nowa_rez
                    widoczne = opcje[27]

                elif i == 1 and aktualne_okno == nowa_rez:
                    status1 = True
                    status2 = False
                    status3 = False
                    status4 = False
                    status5 = False

                elif i == 3 and aktualne_okno == nowa_rez:
                    status1 = False
                    status2 = True
                    status3 = False
                    status4 = False
                    status5 = False

                elif i == 5 and aktualne_okno == nowa_rez:
                    status1 = False
                    status2 = False
                    status3 = True
                    status4 = False
                    status5 = False

                elif i == 7 and aktualne_okno == nowa_rez:
                    status1 = False
                    status2 = False
                    status3 = False
                    status4 = True
                    status5 = False

                elif i == 9 and aktualne_okno == nowa_rez:
                    status1 = False
                    status2 = False
                    status3 = False
                    status4 = False
                    status5 = True

                elif i == 1 and aktualne_okno == rezerwacje_opcje:
                    aktualne_okno = ed_rez
                    widoczne = opcje[28]

                elif i == 1 and aktualne_okno == ed_rez:
                    status1 = True
                    status2 = False
                    status3 = False
                    status4 = False
                    status5 = False

                elif i == 3 and aktualne_okno == ed_rez:
                    status1 = False
                    status2 = True
                    status3 = False
                    status4 = False
                    status5 = False

                elif i == 5 and aktualne_okno == ed_rez:
                    status1 = False
                    status2 = False
                    status3 = True
                    status4 = False
                    status5 = False

                elif i == 7 and aktualne_okno == ed_rez:
                    status1 = False
                    status2 = False
                    status3 = False
                    status4 = True
                    status5 = False

                elif i == 9 and aktualne_okno == ed_rez:
                    status1 = False
                    status2 = False
                    status3 = False
                    status4 = False
                    status5 = True

                elif i == 2 and aktualne_okno == rezerwacje_opcje:
                    aktualne_okno = del_rez
                    widoczne = opcje[29]

                elif i == 1 and aktualne_okno == del_rez:
                    status1 = True
# ----------------------------------------------------------------------------------
                elif i == 8 and aktualne_okno == menu_windows:
                    aktualne_okno = wyswietl_opcje
                    widoczne = opcje[30]


                elif i == 0 and aktualne_okno == wyswietl_opcje:
                    cur.execute("select * from atrakcje")
                    data = []
                    for result in cur:
                        print(result)
                        data.append(result)
                    if not data:
                        root = Tk()
                        root.withdraw()
                        messagebox.showwarning(title="WARNING", message="Tabela jest pusta")
                        root.destroy()
                    else:
                        total_rows = len(data)
                        total_columns = len(data[0])
                        root = Tk()
                        root.title("Atrakcje")
                        t = Table(root)
                        root.mainloop()
                    aktualne_okno = menu_windows
                    widoczne = opcje[0]


                elif i == 1 and aktualne_okno == wyswietl_opcje:
                    cur.execute("select * from budynek")
                    data = []
                    for result in cur:
                        print(result)
                        data.append(result)
                    if not data:
                        root = Tk()
                        root.withdraw()
                        messagebox.showwarning(title="WARNING", message="Tabela jest pusta")
                        root.destroy()
                    else:
                        total_rows = len(data)
                        total_columns = len(data[0])
                        root = Tk()
                        root.title("Budynki")
                        t = Table(root)
                        root.mainloop()
                    aktualne_okno = menu_windows
                    widoczne = opcje[0]


                elif i == 2 and aktualne_okno == wyswietl_opcje:
                    cur.execute("select * from klient")
                    data = []
                    for result in cur:
                        print(result)
                        data.append(result)
                    if not data:
                        root = Tk()
                        root.withdraw()
                        messagebox.showwarning(title="WARNING", message="Tabela jest pusta")
                        root.destroy()
                    else:
                        total_rows = len(data)
                        total_columns = len(data[0])
                        root = Tk()
                        root.title("Klienci")
                        t = Table(root)
                        root.mainloop()
                    aktualne_okno = menu_windows
                    widoczne = opcje[0]


                elif i == 3 and aktualne_okno == wyswietl_opcje:
                    cur.execute("select * from miejsce_parkingowe")
                    data = []
                    for result in cur:
                        print(result)
                        data.append(result)
                    if not data:
                        root = Tk()
                        root.withdraw()
                        messagebox.showwarning(title="WARNING", message="Tabela jest pusta")
                        root.destroy()
                    else:
                        total_rows = len(data)
                        total_columns = len(data[0])
                        root = Tk()
                        root.title("Parking")
                        t = Table(root)
                        root.mainloop()
                    aktualne_okno = menu_windows
                    widoczne = opcje[0]


                elif i == 4 and aktualne_okno == wyswietl_opcje:
                    cur.execute("select * from pokoj")
                    data = []
                    for result in cur:
                        print(result)
                        data.append(result)
                    if not data:
                        root = Tk()
                        root.withdraw()
                        messagebox.showwarning(title="WARNING", message="Tabela jest pusta")
                        root.destroy()
                    else:
                        total_rows = len(data)
                        total_columns = len(data[0])
                        root = Tk()
                        root.title("Pokoje")
                        t = Table(root)
                        root.mainloop()
                    aktualne_okno = menu_windows
                    widoczne = opcje[0]


                elif i == 5 and aktualne_okno == wyswietl_opcje:
                    cur.execute("select * from pracownik")
                    data = []
                    for result in cur:
                        print(result)
                        data.append(result)
                    if not data:
                        root = Tk()
                        root.withdraw()
                        messagebox.showwarning(title="WARNING", message="Tabela jest pusta")
                        root.destroy()
                    else:
                        liczba_prac = cur.callfunc("policz", int)
                        total_rows = len(data)
                        total_columns = len(data[0])
                        root = Tk()
                        root.title("Liczba pracowników: " + str(liczba_prac))
                        t = Table(root)
                        root.mainloop()
                    aktualne_okno = menu_windows
                    widoczne = opcje[0]


                elif i == 6 and aktualne_okno == wyswietl_opcje:
                    cur.execute("select * from rachunek")
                    data = []
                    for result in cur:
                        print(result)
                        data.append(result)
                    if not data:
                        root = Tk()
                        root.withdraw()
                        messagebox.showwarning(title="WARNING", message="Tabela jest pusta")
                        root.destroy()
                    else:
                        total_rows = len(data)
                        total_columns = len(data[0])
                        root = Tk()
                        root.title("Rachunki")
                        t = Table(root)
                        root.mainloop()
                    aktualne_okno = menu_windows
                    widoczne = opcje[0]

                elif i == 7 and aktualne_okno == wyswietl_opcje:
                    cur.execute("select * from rezerwacja")
                    data = []
                    for result in cur:
                        print(result)
                        data.append(result)
                    if not data:
                        root = Tk()
                        root.withdraw()
                        messagebox.showwarning(title="WARNING", message="Tabela jest pusta")
                        root.destroy()
                    else:
                        total_rows = len(data)
                        total_columns = len(data[0])
                        root = Tk()
                        root.title("Rezerwacje")
                        t = Table(root)
                        root.mainloop()
                    aktualne_okno = menu_windows
                    widoczne = opcje[0]

# ----------------------------------------------------------------------------------
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
# #---------------------------------------------------------------------------------
                try:
                    if aktualne_okno == nowa_atr:
                        cur.execute('insert into atrakcje (nazwa) values (\'' + user_text1 + '\')')
                        print("Nazwa nowej atrakcji: ", user_text1)
                        connection.commit()
                    elif aktualne_okno == ed_atr:
                        cur.execute('update atrakcje set nazwa = \'' + user_text2 + '\' where id_atrakcji = \'' + user_text1 + '\'')
                        print("ID edytowaniej atrakcji: ", user_text1)
                        print("Nowa nazwa edytowanej atrakcji: ", user_text2)
                        connection.commit()
                    elif aktualne_okno == del_atr:
                        cur.execute('delete from atrakcje where id_atrakcji =\'' + user_text1 + '\'')
                        print("Usunięto atrakcję: ", user_text1)
                        connection.commit()
                    # ---------------------------------------------------------------------------------
                    elif aktualne_okno == nowy_bud:
                        cur.execute("insert into budynek (nazwa, ilosc_pieter) values (\'" + user_text1 + "\', \'" + user_text2 + "\')")
                        print("Nazwa nowego budynku: ", user_text1)
                        print("Ilość pięter budynku: ", user_text2)
                        connection.commit()
                    elif aktualne_okno == ed_bud:
                        cur.execute("update budynek set ilosc_pieter =\'" + user_text2 + "\' where nazwa =\'" + user_text1 + "\'")
                        print("Nazwa edytowanego budynku: ", user_text1)
                        print("Nowa ilość pięter: ", user_text2)
                        connection.commit()
                    elif aktualne_okno == del_bud:
                        cur.execute("delete from budynek where nazwa =\'" + user_text1 + "\'")
                        print("Usunięto budynek: ", user_text1)
                        connection.commit()
                    # ---------------------------------------------------------------------------------
                    elif aktualne_okno == nowy_kl:
                        cur.execute("insert into klient (imie, nazwisko, typ_dokumentu_nazwa) values ('{0}', '{1}', '{2}')".format(user_text1, user_text2, user_text3))
                        temp = list(map(int, user_text5.split(",")))
                        cur.execute("insert into dokument (id_dokumentu, data_waznosci, typ_dokumentu_nazwa) values ('{0}', '{1}', '{2}')".format(user_text4, datetime.datetime(temp[0], temp[1], temp[2]).date().isoformat(), user_text3))
                        print("Imię nowego klienta: ", user_text1)
                        print("Nazwisko nowego klienta: ", user_text2)
                        print("Typ dokumentu tożsamości: ", user_text3)
                        print("ID dokumentu tożsamości: ", user_text4)
                        print("Data ważności dokumentu tożsamości", user_text5)
                        connection.commit()
                    elif aktualne_okno == ed_kl:
                        cur.execute("update klient set imie =\'" + user_text1 + "\', nazwisko =\'" + user_text2 + "\', typ_dokumentu_nazwa =\'" + user_text3 + "\' where id_klienta =\'" + user_text4 + "\'")
                        print("Nowe imię klienta: ", user_text1)
                        print("Nowe nazwisko klienta: ", user_text2)
                        print("Nowy typ dokumentu tożsamości: ", user_text3)
                        print("ID edytowanego klienta", user_text4)
                        connection.commit()
                    elif aktualne_okno == del_kl:
                        cur.execute("delete from klient where id_klienta =\'" + user_text1 + "\'")
                        print("Usunięto klienta o ID: ", user_text1)
                        connection.commit()
                    # ---------------------------------------------------------------------------------
                    elif aktualne_okno == nowe_miejsce:
                        cur.execute("insert into miejsce_parkingowe (budynek_nazwa) values (\'" + user_text1 + "\')")
                        print("Dodano miejsce przed budynkiem: ", user_text1)
                        connection.commit()
                    elif aktualne_okno == del_miejsce:
                        cur.execute("delete from miejsce_parkingowe where nr_miejsca =\'" + user_text1 + "\'")
                        print("Usunięto miejsce numer:", user_text1)
                        connection.commit()
                    # ---------------------------------------------------------------------------------
                    elif aktualne_okno == nowy_pok:
                        cur.execute("insert into pokoj (budynek_nazwa, pojemnosc, pietro) values (\'" + user_text1 + "\', \'" + user_text2 + "\', \'" + user_text3 + "\')")
                        print("Dodano pokój w budynku: ", user_text1)
                        print("Pojemność pokoju ", user_text2)
                        print("Piętro pokoju: ", user_text3)
                        connection.commit()
                    elif aktualne_okno == ed_pok:
                        cur.execute("update pokoj set pojemnosc =\'" + user_text3 + "\', pietro =\'" + user_text4 + "\' where nr_pokoju =\'" + user_text2 + "\' and budynek_nazwa =\'" + user_text1 + "\'")
                        print("Edytowano pokój w budynku: ", user_text1)
                        print("Numer edytowanego pokoju: ", user_text2)
                        print("Nowa pojemność ", user_text3)
                        print("Nowe piętro ", user_text4)
                        connection.commit()
                    elif aktualne_okno == del_pok:
                        print("Usunięto pokój nr ", user_text2, " z budynku ", user_text1)
                        cur.execute("delete from pokoj where nr_pokoju =\'" + user_text2 + "\' and budynek_nazwa =\'" + user_text1 + "\'")
                        connection.commit()
                    # ---------------------------------------------------------------------------------
                    elif aktualne_okno == nowy_prac:
                        cur.callproc("dodaj_pracownika", [user_text1, user_text2, user_text3, user_text4])
                        print("Imię pracownika: ", user_text1)
                        print("Nazwisko pracownika: ", user_text2)
                        print("Stanowisko pracownika: ", user_text3)
                        print("Telefon do pracownika: ", user_text4)
                        connection.commit()
                    elif aktualne_okno == ed_prac:
                        cur.execute("update pracownik set imie =\'" + user_text2 + "\', nazwisko =\'" + user_text3 + "\', stanowisko =\'" + user_text4 + "\', nr_tel =\'" + user_text5 + "\' where id_pracownika =\'" + user_text1 + "\'")
                        print("ID edytowanego pracownika: ", user_text1)
                        print("Nowe imię pracownika: ", user_text2)
                        print("Nowe nazwisko pracownika: ", user_text3)
                        print("Nowe stanowisko pracownika: ", user_text4)
                        print("Nowy telefon do pracownika: ", user_text5)
                        connection.commit()
                    elif aktualne_okno == del_prac:
                        cur.execute("delete from pracownik where id_pracownika =\'" + user_text1 + "\'")
                        print("Usunięto pracownika od ID ", user_text1)
                        connection.commit()
                    # ---------------------------------------------------------------------------------
                    elif aktualne_okno == nowy_rach:
                        temp = list(map(int, user_text1.split(",")))
                        cur.execute("insert into rachunek (data_wystawienia, kwota, rezerwacja_id_rezerwacji, rezerwacja_klient_id_klienta) values ('{0}', '{1}', '{2}', '{3}')". format(datetime.datetime(temp[0], temp[1], temp[2]).date().isoformat(), user_text2, user_text3, user_text4))
                        print("Data wystawienia: ", user_text1)
                        print("Kwota rachunku: ", user_text2)
                        print("ID rezerwacji: ", user_text3)
                        print("Rachunek na ID klienta: ", user_text4)
                        connection.commit()
                    # ---------------------------------------------------------------------------------
                    elif aktualne_okno == nowa_rez:
                        cur.execute("insert into rezerwacja (data_poczatku, data_konca, pokoj_nr_pokoju, pokoj_budynek_nazwa, klient_id_klienta) values (\'" + user_text4 + "\', \'" + user_text5 + "\', \'" + user_text2 + "\', \'" + user_text3 + "\', \'" + user_text1 + "\')")
                        print("ID klienta: ", user_text1)
                        print("Numer pokoju: ", user_text2)
                        print("Nazwa budynku: ", user_text3)
                        print("Początek rezerwacji: ", user_text4)
                        print("Koniec rezerwacji: ", user_text5)
                        connection.commit()
                    elif aktualne_okno == ed_rez:
                        cur.execute("update rezerwacja set pokoj_nr_pokoju =\'" + user_text2 + "\', pokoj_budynek_nazwa =\'" + user_text3 + "\', data_poczatku =\'" + user_text4 + "\', data_konca =\'" + user_text5 + "\' where id_rezerwacji =\'" + user_text1 + "\'")
                        print("ID rezerwacji: ", user_text1)
                        print("Nowy numer pokoju: ", user_text2)
                        print("Nowy budynek: ", user_text3)
                        print("Nowy początek rezerwacji: ", user_text4)
                        print("Nowy koniec rezerwacji: ", user_text5)
                        connection.commit()
                    elif aktualne_okno == del_rez:
                        cur.execute("delete from rezerwacja where id_rezerwacji =\'" + user_text1 + "\'")
                        print("Usunięto rezerwację o ID: ", user_text1)
                        connection.commit()
                except cx_Oracle.IntegrityError as e:
                    e = str(e)
                    code = e[0:9]
                    print(code) #ORA-02292 - usuwanie związanego obiektu
                    if code == "ORA-01400":
                        root = Tk()
                        root.withdraw()
                        messagebox.showwarning(title="WARNING", message="Pole obowiązkowe zostało puste.")
                    elif code == "ORA-02292":
                        root = Tk()
                        root.withdraw()
                        messagebox.showwarning(title="WARNING", message="Nie można usunąc obiektu.")
                    elif code == "ORA-02291":
                        root = Tk()
                        root.withdraw()
                        messagebox.showwarning(title="WARNING", message="Adnotacja do nieistniejącego obiektu.")
                    elif code == "ORA-01840" or code == "ORA-01861" or code == "ORA-01722":
                        root = Tk()
                        root.withdraw()
                        messagebox.showwarning(title="WARNING", message="Zły format daty. Oczekiwano rok/miesiąc/dzień.")

                except ValueError:
                    root = Tk()
                    root.withdraw()
                    messagebox.showwarning(title="WARNING", message="Wpisano niepoprawne dane")

                aktualne_okno = menu_windows
                widoczne = opcje[0]
                status1 = False
                status2 = False
                status3 = False
                status4 = False
                status5 = False
                user_text1 = ''
                user_text2 = ''
                user_text3 = ''
                user_text4 = ''
                user_text5 = ''

            elif status1:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        user_text1 = user_text1[:-1]
                    else:
                        user_text1 += event.unicode

            elif status2:
                if event.key == pygame.K_BACKSPACE:
                    user_text2 = user_text2[:-1]
                else:
                    user_text2 += event.unicode

            elif status3:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        user_text3 = user_text3[:-1]
                    else:
                        user_text3 += event.unicode

            elif status4:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        user_text4 = user_text4[:-1]
                    else:
                        user_text4 += event.unicode

            elif status5:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        user_text5 = user_text5[:-1]
                    else:
                        user_text5 += event.unicode

    if aktualne_okno == nowa_atr:
        screen.blit(text_surface1, (input_nazwa_atr.x + 5, input_nazwa_atr.y + 1))
    elif aktualne_okno == ed_atr:
        screen.blit(text_surface1, (input_id_atr.x + 5, input_id_atr.y + 1))
        screen.blit(text_surface2, (input_nazwa_atr2.x + 5, input_nazwa_atr2.y + 1))
    elif aktualne_okno == del_atr:
        screen.blit(text_surface1, (input_id_atr2.x + 5, input_id_atr2.y + 1))
    elif aktualne_okno == nowy_bud:
        screen.blit(text_surface1, (input_nazwa_bud.x + 5, input_nazwa_bud.y + 1))
        screen.blit(text_surface2, (input_ilosc_pieter_bud.x + 5, input_ilosc_pieter_bud.y + 1))
    elif aktualne_okno == ed_bud:
        screen.blit(text_surface1, (input_nazwa_bud2.x + 5, input_nazwa_bud2.y + 1))
        screen.blit(text_surface2, (input_ilosc_pieter_bud2.x + 5, input_ilosc_pieter_bud2.y + 1))
    elif aktualne_okno == del_bud:
        screen.blit(text_surface1, (input_nazwa_bud3.x + 5, input_nazwa_bud3.y + 1))
    elif aktualne_okno == nowy_kl:
        screen.blit(text_surface1, (input_imie_kl.x + 5, input_imie_kl.y + 1))
        screen.blit(text_surface2, (input_nazwisko_kl.x + 5, input_nazwisko_kl.y + 1))
        screen.blit(text_surface3, (input_nazwa_typ_dok.x + 5, input_nazwa_typ_dok.y + 1))
        screen.blit(text_surface4, (input_id_dok_toz.x + 5, input_id_dok_toz.y + 1))
        screen.blit(text_surface5, (input_data_waz_dok_toz.x + 5, input_data_waz_dok_toz.y + 1))
    elif aktualne_okno == ed_kl:
        screen.blit(text_surface1, (input_imie_kl2.x + 5, input_imie_kl2.y + 1))
        screen.blit(text_surface2, (input_nazwisko_kl2.x + 5, input_nazwisko_kl2.y + 1))
        screen.blit(text_surface3, (input_nazwa_typ_dok2.x + 5, input_nazwa_typ_dok2.y + 1))
        screen.blit(text_surface4, (input_id_dok_toz2.x + 5, input_id_dok_toz2.y + 1))
        screen.blit(text_surface5, (input_data_waz_dok_toz2.x + 5, input_data_waz_dok_toz2.y + 1))
    elif aktualne_okno == del_kl:
        screen.blit(text_surface1, (input_id_klienta.x + 5, input_id_klienta.y + 1))
    elif aktualne_okno == nowe_miejsce:
        screen.blit(text_surface1, (input_budynek.x + 5, input_budynek.y + 1))
    elif aktualne_okno == del_miejsce:
        screen.blit(text_surface1, (input_budynek2.x + 5, input_budynek2.y + 1))
    elif aktualne_okno == nowy_pok:
        screen.blit(text_surface1, (input_budynek_pok.x + 5, input_budynek_pok.y + 1))
        screen.blit(text_surface2, (input_pojemnosc_pok.x + 5, input_pojemnosc_pok.y + 1))
        screen.blit(text_surface3, (input_pietro_pok.x + 5, input_pietro_pok.y + 1))
    elif aktualne_okno == ed_pok:
        screen.blit(text_surface1, (input_budynek_pok2.x + 5, input_budynek_pok2.y + 1))
        screen.blit(text_surface2, (input_nr_pok2.x + 5, input_nr_pok2.y + 1))
        screen.blit(text_surface3, (input_pojemnosc_pok2.x + 5, input_pojemnosc_pok2.y + 1))
        screen.blit(text_surface4, (input_pietro_pok2.x + 5, input_pietro_pok2.y + 1))
    elif aktualne_okno == del_pok:
        screen.blit(text_surface1, (input_budynek_pok3.x + 5, input_budynek_pok3.y + 1))
        screen.blit(text_surface2, (input_nr_pok3.x + 5, input_nr_pok3.y + 1))
    elif aktualne_okno == nowy_prac:
        screen.blit(text_surface1, (input_imie_prac.x + 5, input_imie_prac.y + 1))
        screen.blit(text_surface2, (input_nazwisko_prac.x + 5, input_nazwisko_prac.y + 1))
        screen.blit(text_surface3, (input_stanowisko_prac.x + 5, input_stanowisko_prac.y + 1))
        screen.blit(text_surface4, (input_tel_prac.x + 5, input_tel_prac.y + 1))
    elif aktualne_okno == ed_prac:
        screen.blit(text_surface1, (input_id_prac2.x + 5, input_id_prac2.y + 1))
        screen.blit(text_surface2, (input_imie_prac2.x + 5, input_imie_prac2.y + 1))
        screen.blit(text_surface3, (input_nazwisko_prac2.x + 5, input_nazwisko_prac2.y + 1))
        screen.blit(text_surface4, (input_stanowisko_prac2.x + 5, input_stanowisko_prac2.y + 1))
        screen.blit(text_surface5, (input_tel_prac2.x + 5, input_tel_prac2.y + 1))
    elif aktualne_okno == del_prac:
        screen.blit(text_surface1, (input_id_prac3.x + 5, input_id_prac3.y + 1))
    elif aktualne_okno == nowy_rach:
        screen.blit(text_surface1, (input_data_rach.x + 5, input_data_rach.y + 1))
        screen.blit(text_surface2, (input_kwota_rach.x + 5, input_kwota_rach.y + 1))
        screen.blit(text_surface3, (input_rezerwacja_rach.x + 5, input_rezerwacja_rach.y + 1))
        screen.blit(text_surface4, (input_id_klienta_rach.x + 5, input_id_klienta_rach.y + 1))
    elif aktualne_okno == nowa_rez:
        screen.blit(text_surface1, (input_id_kl_rez.x + 5, input_id_kl_rez.y + 1))
        screen.blit(text_surface2, (input_nr_pok_rez.x + 5, input_nr_pok_rez.y + 1))
        screen.blit(text_surface3, (input_budynek_rez.x + 5, input_budynek_rez.y + 1))
        screen.blit(text_surface4, (input_poczatek_rez.x + 5, input_poczatek_rez.y + 1))
        screen.blit(text_surface5, (input_koniec_rez.x + 5, input_koniec_rez.y + 1))
    elif aktualne_okno == ed_rez:
        screen.blit(text_surface1, (input_id_rez2.x + 5, input_id_rez2.y + 1))
        screen.blit(text_surface2, (input_nr_pok_rez2.x + 5, input_nr_pok_rez2.y + 1))
        screen.blit(text_surface3, (input_budynek_rez2.x + 5, input_budynek_rez2.y + 1))
        screen.blit(text_surface4, (input_poczatek_rez2.x + 5, input_poczatek_rez2.y + 1))
        screen.blit(text_surface5, (input_koniec_rez2.x + 5, input_koniec_rez2.y + 1))
    elif aktualne_okno == del_rez:
        screen.blit(text_surface1, (input_id_rez3.x + 5, input_id_rez3.y + 1))
    pygame.display.flip()

