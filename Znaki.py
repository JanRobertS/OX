from typing import List, Tuple
from abc import ABC, abstractmethod
import numpy as np
import cv2

class Znak(ABC):
    def __init__(self, wymiar_wyswietlania: int, ilosc_rzedow_wierszow: int, wiersz_rzad: Tuple[int,int], kolor: Tuple[int,int,int]):
        self.wymiar = wymiar_wyswietlania 
        self.ilosc_rzedow_wierszow = ilosc_rzedow_wierszow

        self.dlugosc = int(self.wymiar/(self.ilosc_rzedow_wierszow))

        self.kolor = kolor

        self.wspolrzedne_xy = self.okresl_wsp(wiersz_rzad)

        self.znak = "Znak"


    def okresl_wsp(self, wiersz_kol: Tuple[int,int]):
        wiersz, kolumna = wiersz_kol

        x = kolumna * self.dlugosc
        y = wiersz * self.dlugosc 

        return x,y
    
    def __str__(self):
        return self.znak
    
    @abstractmethod
    def wyswietlenie(self, image):
        pass
    
class O(Znak):
    def __init__(self, wymiar_wyswietlania: int, ilosc_rzedow_wierszow: int, wiersz_kol: Tuple[int,int], kolor: Tuple[int,int,int]):
        super().__init__(wymiar_wyswietlania, ilosc_rzedow_wierszow, wiersz_kol, kolor)

        self.znak = "O"

        self.r = int(np.round(2*self.dlugosc/5))

        self.srodek_xy = int(np.round(self.wspolrzedne_xy[0] + self.dlugosc/2)), int(np.round(self.wspolrzedne_xy[1] + self.dlugosc/2))

    def wyswietlenie(self, image):
        cv2.circle(image, self.srodek_xy, self.r, self.kolor, thickness=4)

class X(Znak):
    def __init__(self, wymiar_wyswietlania: int, ilosc_rzedow_wierszow: int, wiersz_kol: Tuple[int,int], kolor: Tuple[int,int,int]):
        super().__init__(wymiar_wyswietlania, ilosc_rzedow_wierszow, wiersz_kol, kolor)

        self.znak = "X"

    def wyswietlenie(self, image):

        start_point1 = self.wspolrzedne_xy[0] + int(self.dlugosc/7), self.wspolrzedne_xy[1] + int(self.dlugosc/7)
        end_point1 =  self.wspolrzedne_xy[0] + int((6*self.dlugosc)/7), self.wspolrzedne_xy[1] + int((6*self.dlugosc)/7)
        start_point2 = self.wspolrzedne_xy[0] + int(self.dlugosc/7), self.wspolrzedne_xy[1] + int((6*self.dlugosc)/7)
        end_point2 = self.wspolrzedne_xy[0] + int((6*self.dlugosc)/7), self.wspolrzedne_xy[1] + int(self.dlugosc/7)

        cv2.line(image, start_point1, end_point1, self.kolor, thickness=4)
        cv2.line(image, start_point2, end_point2, self.kolor, thickness=4)
