from typing import Union, Tuple
import numpy as np

from kolo_kros_XD import Tablica, O, X, Wyswietlanie

class Silnik:
    def __init__(self, Tablica: Tablica) -> None:
        self.plansza = Tablica

        self.tablica_gry = np.full((self.plansza.sqrt_miejsc_w_grze,self.plansza.sqrt_miejsc_w_grze), None)


    def spr_ruchu(self, pozycja: int) -> bool:
        #czy wolne?
        
        if self.tablica_gry[pozycja] is None:
            return True
        return False
    
    def spr_wygrana(self, znak_wygrywajacy: Union[X, O] ,liczba_do_wygrania: int):
        
        for sprawdz in [self.spr_poziom(znak_wygrywajacy,liczba_do_wygrania), self.spr_poziom(znak_wygrywajacy,liczba_do_wygrania), 
                        self.spr_skos_LG(znak_wygrywajacy,liczba_do_wygrania), self.spr_skos_PG(znak_wygrywajacy,liczba_do_wygrania)]:
            if sprawdz[0] is True:
                return True ,sprawdz[1], sprawdz[2]
            
        return False, (None), (None) 

    def spr_poziom(self, znak_wygrywajacy: Union[X, O] ,liczba_do_wygrania: int):
        # Poziom
        for rzad in range(self.plansza.sqrt_miejsc_w_grze):
            for pierwszy in range(self.plansza.sqrt_miejsc_w_grze - (liczba_do_wygrania - 1)): #tutaj pierwszy może być tylko znak który po sobie ma więcej niż liczba wygranych
                wygrane = 1

                if not (self.tablica_gry[rzad][pierwszy] is znak_wygrywajacy):
                    continue

                for kolejne in range(pierwszy + 1, self.plansza.sqrt_miejsc_w_grze):
                        if not (self.tablica_gry[rzad][kolejne] is znak_wygrywajacy):
                            break

                        wygrane += 1

                        if wygrane == liczba_do_wygrania:
                             return True, (rzad, pierwszy), (rzad, kolejne)
                        
        return False, (None), (None) 
                        
    def spr_pion(self, znak_wygrywajacy: Union[X, O] ,liczba_do_wygrania: int):
        # Pion

        for kolumna in range(self.plansza.sqrt_miejsc_w_grze):
            for pierwszy in range(self.plansza.sqrt_miejsc_w_grze - (liczba_do_wygrania - 1)): #tutaj pierwszy może być tylko znak który po sobie ma więcej niż liczba wygranych
                wygrane = 1

                if not (self.tablica_gry[pierwszy][kolumna] is znak_wygrywajacy):
                    continue

                for kolejne in range(pierwszy + 1, self.plansza.sqrt_miejsc_w_grze):
                        if not (self.tablica_gry[kolejne][kolumna] is znak_wygrywajacy):
                            break

                        wygrane += 1
                    
                        if wygrane == liczba_do_wygrania:
                             return True, (pierwszy, kolumna), (kolejne, kolumna)
        
        return False, (None), (None)
    
    def spr_skos_LG(self, znak_wygrywajacy: Union[X, O] ,liczba_do_wygrania: int):
        # skos zaczynamy lewa góra i w prawy dół 
        n = self.plansza.sqrt_miejsc_w_grze - liczba_do_wygrania + 1 #n=1,2,3,4....

        for wiersz in range(n):
            for kolumna in range(n):
                wygrane = 1

                if not (self.tablica_gry[wiersz][kolumna] is znak_wygrywajacy):
                    continue

                for i in range(1, liczba_do_wygrania):
                    if not (self.tablica_gry[wiersz + i][kolumna + i] is znak_wygrywajacy):
                        break
                
                    wygrane += 1
                    if wygrane == liczba_do_wygrania:
                            return True, (wiersz, kolumna), (wiersz + i, kolumna + i)
        
        return False, (None), (None)
    
    def spr_skos_PG(self, znak_wygrywajacy: Union[X, O] ,liczba_do_wygrania: int):
        # skos zaczynamy Prawa góra i w lewy dół 
        n = self.plansza.sqrt_miejsc_w_grze - liczba_do_wygrania + 1 #n=1,2,3,4....

        for wiersz in range(n):
            for kolumna in range(self.plansza.sqrt_miejsc_w_grze - n, self.plansza.sqrt_miejsc_w_grze): 
                wygrane = 1

                if not (self.tablica_gry[wiersz][kolumna] is znak_wygrywajacy):
                    continue

                for i in range(1, liczba_do_wygrania):
                    if not (self.tablica_gry[wiersz + i][kolumna - i] is znak_wygrywajacy):
                        break
                
                    wygrane += 1
                    if wygrane == liczba_do_wygrania:
                            return True, (wiersz, kolumna), (wiersz + i, kolumna - i)
               
        return False, (None), (None)



                  





        # for kolumna in range(self.plansza.sqrt_miejsc_w_grze):
        #     for pierwszy in range(self.plansza.sqrt_miejsc_w_grze - (liczba_do_wygrania - 1)): #tutaj pierwszy może być tylko znak który po sobie ma więcej niż liczba wygranych
        #         wygrane = 1

        #         if not (self.tablica_gry[pierwszy][kolumna] is znak_wygrywajacy):
        #             continue

        #         for kolejne in range(pierwszy + 1, self.plansza.sqrt_miejsc_w_grze):
        #                 if not (self.tablica_gry[kolejne][kolumna] is znak_wygrywajacy):
        #                     break

        #                 wygrane += 1

        #                 if wygrane == liczba_do_wygrania:
        #                      return True, (kolumna,pierwszy,kolejne)
                        
        # return False, (None)



                
    



        