from typing import Union, Tuple
import numpy as np

from Znaki import O,X
from Tablica_OX import Tablica

class Silnik:
    def __init__(self, wymiary: Tuple[int,int], tryb_nocny: bool = False, ilosc_rzedow_wierszow: int = 3, kolor_tla: Tuple[int,int] = None, kolor: Tuple[int,int] = None) -> None:
        self.Tablica = Tablica(wymiary,tryb_nocny,ilosc_rzedow_wierszow,kolor_tla,kolor)

        self.tablica_gry = np.full((ilosc_rzedow_wierszow, ilosc_rzedow_wierszow), None)

    def ruch(self, kolumna: int, rzad: int, znak: Union[O,X]):
        self.tablica_gry[rzad, kolumna] = znak(self.Tablica.wymiar,self.Tablica.ilosc_rzedow_wierszow,(rzad,kolumna),self.Tablica.kolor)

    def spr_ruchu(self, kolumna: int, wiersz: int) -> bool:
        if self.tablica_gry[wiersz][kolumna] is None:
            return True
        return False
    
    def spr_wygrana(self, znak_wygrywajacy: Union[X, O] ,liczba_do_wygrania: int):
        for sprawdz in [self.spr_poziom(znak_wygrywajacy,liczba_do_wygrania), self.spr_pion(znak_wygrywajacy,liczba_do_wygrania), 
                        self.spr_skos_LG(znak_wygrywajacy,liczba_do_wygrania), self.spr_skos_PG(znak_wygrywajacy,liczba_do_wygrania)]:
            if sprawdz[0] is True:
                return True ,sprawdz[1], sprawdz[2]
            
            
        return False, (None), (None) 
    
    def spr_remis(self):
        for i in range(len(self.tablica_gry)):
            for j in range(len(self.tablica_gry)):
                if self.tablica_gry[i][j] is None:
                    return False
            
        return True

    def spr_poziom(self, znak_wygrywajacy: Union[X, O] ,liczba_do_wygrania: int):
        # Poziom
        for rzad in range(self.Tablica.ilosc_rzedow_wierszow):
            for pierwszy in range(self.Tablica.ilosc_rzedow_wierszow - (liczba_do_wygrania - 1)): #tutaj pierwszy może być tylko znak który po sobie ma więcej niż liczba wygranych
                wygrane = 1
                if not (isinstance(self.tablica_gry[rzad][pierwszy], znak_wygrywajacy)):
                    continue

                for kolejne in range(pierwszy + 1, self.Tablica.ilosc_rzedow_wierszow):
                        if not (isinstance(self.tablica_gry[rzad][kolejne], znak_wygrywajacy)):
                            break
                        
                        wygrane += 1

                        if wygrane == liczba_do_wygrania:
                             return True, (rzad, pierwszy), (rzad, kolejne)
                        
        return False, (None), (None) 
                        
    def spr_pion(self, znak_wygrywajacy: Union[X, O] ,liczba_do_wygrania: int):
        # Pion
        for kolumna in range(self.Tablica.ilosc_rzedow_wierszow):
            for pierwszy in range(self.Tablica.ilosc_rzedow_wierszow - (liczba_do_wygrania - 1)): #tutaj pierwszy może być tylko znak który po sobie ma więcej niż liczba wygranych
                wygrane = 1

                if not (isinstance(self.tablica_gry[pierwszy][kolumna], znak_wygrywajacy)):
                    continue

                for kolejne in range(pierwszy + 1, self.Tablica.ilosc_rzedow_wierszow):
                        if not (isinstance(self.tablica_gry[kolejne][kolumna], znak_wygrywajacy)):
                            break

                        wygrane += 1
                    
                        if wygrane == liczba_do_wygrania:
                             return True, (pierwszy, kolumna), (kolejne, kolumna)
        
        return False, (None), (None)
    
    def spr_skos_LG(self, znak_wygrywajacy: Union[X, O] ,liczba_do_wygrania: int):
        # skos zaczynamy lewa góra i w prawy dół 
        n = self.Tablica.ilosc_rzedow_wierszow - liczba_do_wygrania + 1 #n=1,2,3,4....

        for wiersz in range(n):
            for kolumna in range(n):
                wygrane = 1

                if not (isinstance(self.tablica_gry[wiersz][kolumna], znak_wygrywajacy)):
                    continue

                for i in range(1, liczba_do_wygrania):
                    if not (isinstance(self.tablica_gry[wiersz + i][kolumna + i], znak_wygrywajacy)):
                        break
                
                    wygrane += 1
                    if wygrane == liczba_do_wygrania:
                            return True, (wiersz, kolumna), (wiersz + i, kolumna + i)
        
        return False, (None), (None)
    
    def spr_skos_PG(self, znak_wygrywajacy: Union[X, O] ,liczba_do_wygrania: int):
        # skos zaczynamy Prawa góra i w lewy dół 
        n = self.Tablica.ilosc_rzedow_wierszow - liczba_do_wygrania + 1 #n=1,2,3,4....

        for wiersz in range(n):
            for kolumna in range(self.Tablica.ilosc_rzedow_wierszow - n, self.Tablica.ilosc_rzedow_wierszow): 
                wygrane = 1

                if not (isinstance(self.tablica_gry[wiersz][kolumna], znak_wygrywajacy)):
                    continue

                for i in range(1, liczba_do_wygrania):
                    if not (isinstance(self.tablica_gry[wiersz + i][kolumna - i],znak_wygrywajacy)):
                        break
                
                    wygrane += 1
                    if wygrane == liczba_do_wygrania:
                            return True, (wiersz, kolumna), (wiersz + i, kolumna - i)
               
        return False, (None), (None)
