from typing import Union
from kolo_kros_XD import Tablica, O, X, Wyswietlanie

class Silnik:
    def __init__(self, Tablica: Tablica) -> None:
        self.plansza = Tablica

        self.tablica_gry = [None for __ in range(self.plansza.ilosc_miejsc_w_grze)]


    def spr_ruchu(self, pozycja: int) -> bool:

        #czy zajęte?

        if self.tablica_gry[pozycja] is None:
            return True
        return False
    
    def spr_wygrana(self, znak_wygrywajacy: Union[X, O] ,liczba_do_wygrania: int):


        for znak in self.tablica_gry:
            if isinstance(znak, znak_wygrywajacy):
                pass
    



        