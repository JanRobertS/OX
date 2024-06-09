from typing import Union, Tuple
from Silnik_OX import Silnik
from Znaki import O, X
import Wyswietlanie_OX



def ustawienia() -> Tuple[int,bool, Union[X,O]]:

    while True:
        wielkosc_planszy = input("Podaj wielkość planszy (plansza nxn, podaj n):")
        if wielkosc_planszy.isdigit():
            if int(wielkosc_planszy) > 2:
                break

        print("Błędna liczba\nSpróbuj ponownie\n")

    while True:
        print("\nKolory\n1.Zwykły\n2.Tryb nocny\n")
        kolor = input("Wybierz który kolor: ")
        if kolor.isdigit():
            if int(kolor) > 0 and int(kolor) < 3:
                break

        print("Błędna liczba\nSpróbuj ponownie\n")

    if int(kolor) == 1:
        tryb_nocny = False
    tryb_nocny = True

    while True:
        print("\nJakim znakiem chesz zaczynać O czy X?")
        znak = input("Wybierz znak: ")
        if znak == "o" or znak == "O"  or znak == "x" or znak == "X":   
            break

        print("Błędny znak\nSpróbuj ponownie\n")

    if znak == "o" or znak == "O":
        znak = O
    elif znak == "x" or znak == "X":
        znak = X



    return int(wielkosc_planszy), tryb_nocny, znak

def ustawienia2():
    return 5, True, O


def OX():

    print("\nGra rozpoczyna się\n")
    wielkosc_planszy, tryb_nocny, znak_rozpoczynający = ustawienia2()

    silnik = Silnik([500,500],tryb_nocny,wielkosc_planszy)

    aktualny_znak, poprzedni = znak_rozpoczynający, znak_rozpoczynający

    while True:
        wygrana, start, end = silnik.spr_wygrana(poprzedni, wielkosc_planszy)

        if not wygrana:
            if silnik.spr_remis():
                print("Remis!!!")
                pass

        kolumna, wiersz = Wyswietlanie_OX.wyswietlanie_caloci(silnik.Tablica, silnik.tablica_gry,wygrana, start, end)

        if wygrana:
            print("Wygrał: ", poprzedni)
            break

        if silnik.spr_ruchu(kolumna, wiersz):
            silnik.ruch(kolumna, wiersz, aktualny_znak)

            if aktualny_znak is O:
                aktualny_znak = X
                poprzedni = O
            else:
                aktualny_znak = O
                poprzedni = X



OX()




