import numpy as np


ilosc = 6
tablica_gry = np.full((ilosc,ilosc), None)

tablica_gry[0][5] = " "
tablica_gry[2][4] = "o"
tablica_gry[3][3] = "o"
tablica_gry[4][2] = "o"
tablica_gry[5][1] = "o"

print(tablica_gry)


def spr_wygrana(znak_wygrywajacy, liczba_do_wygrania: int):
    
    # Sprawdzanie wygrane Poziom|Pion|Skos

    # Poziom

    # for rzad in range(ilosc):
    #     for pierwszy in range(ilosc - (liczba_do_wygrania - 1)): #tutaj pierwszy może być tylko znak który po sobie ma więcej niż liczba wygranych
    #         wygrane = 1

    #         if not (tablica_gry[rzad][pierwszy] is znak_wygrywajacy):
    #              continue
            
    #         for kolejne in range(pierwszy + 1, ilosc): 
    #                 if not (tablica_gry[rzad][kolejne] == znak_wygrywajacy):
    #                     break

    #                 wygrane += 1

    #                 if wygrane == liczba_do_wygrania:
    #                     return True, (rzad,pierwszy,kolejne)
                    
    # return False, (None)

    # # Pion
    # for kolumna in range(ilosc):
    #     for pierwszy in range(ilosc - (liczba_do_wygrania - 1)): #tutaj pierwszy może być tylko znak który po sobie ma więcej niż liczba wygranych
    #         wygrane = 1

    #         if not (tablica_gry[pierwszy][kolumna] is znak_wygrywajacy):
    #              continue
            
    #         for kolejne in range(pierwszy + 1, ilosc): 
    #                 if not (tablica_gry[kolejne][kolumna] == znak_wygrywajacy):
    #                     break

    #                 wygrane += 1

    #                 if wygrane == liczba_do_wygrania:
    #                     return True, (kolumna,pierwszy,kolejne)
                    
    # return False, (None)

    # Skos

    # for kolumna in range(ilosc):
    #     for pierwszy in range(ilosc - (liczba_do_wygrania - 1)): #tutaj pierwszy może być tylko znak który po sobie ma więcej niż liczba wygranych
    #         wygrane = 1

    #         if not (tablica_gry[pierwszy][kolumna] is znak_wygrywajacy):
    #              continue
            
    #         for kolejne in range(pierwszy + 1, ilosc): 
    #                 if not (tablica_gry[kolejne][kolumna] == znak_wygrywajacy):
    #                     break

    #                 wygrane += 1

    #                 if wygrane == liczba_do_wygrania:
    #                     return True, (kolumna,pierwszy,kolejne)
                    
    # return False, (None)
        # skos lewy dól 
    n = ilosc - liczba_do_wygrania + 1 #n=1,2,3,4....


    for wiersz in range(n):
        for kolumna in range(ilosc - n, ilosc):
            wygrane = 1

            if not (tablica_gry[wiersz][kolumna] == znak_wygrywajacy):
                continue


            for i in range(1, liczba_do_wygrania):
                if not (tablica_gry[wiersz + i][kolumna - i] == znak_wygrywajacy):
                    break
                
                wygrane += 1

                if wygrane == liczba_do_wygrania:
                        return True, (wiersz, kolumna), (wiersz + i, kolumna - i)
        
                    
    return False, (None), (None)

                    

print(spr_wygrana("o", 4))
