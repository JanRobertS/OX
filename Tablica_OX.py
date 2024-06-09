import numpy as np
from typing import List, Tuple


class Tablica:
    def __init__(self, wymiary: Tuple[int,int], tryb_nocny: bool = False, ilosc_rzedow_wierszow: int = 3, kolor_tla: Tuple[int,int] = None, kolor: Tuple[int,int] = None):
        self.wymiar = max(wymiary)
        self.x, self.y = wymiary[0], wymiary[1]

        self.tlo, self.kolor = self.kolory(kolor_tla, kolor, tryb_nocny)

        self.ilosc_rzedow_wierszow = ilosc_rzedow_wierszow

        self.plasza = self.tworzenie_planszy()
    
    def kolory(self, tlo: Tuple[int,int,int], kolor: Tuple[int,int,int], tryb_nocny: bool):
        if kolor is None and tlo is None:
            if tryb_nocny:
                tlo, kolor = [0,0,0], [255,255,255]
                
            else:
                tlo, kolor = [255,255,255], [0,0,0]

        elif kolor is None and not tlo is None:
            tlo, kolor = [tlo[0],tlo[1],tlo[2]], [255-tlo[0],255-tlo[1],255-tlo[2]]

        elif tlo is None:
            tlo, kolor = [255-kolor[0],255-kolor[1],255-kolor[2]], [kolor[0],kolor[1],kolor[2]]
        else:
            tlo, kolor = [tlo[0],tlo[1],tlo[2]], [kolor[0],kolor[1],kolor[2]]

        return tlo, kolor
    
    def tworzenie_planszy(self):
        plansza = [[self.tlo for _ in range(self.wymiar)] for _ in range(self.wymiar)]

        return plansza
    
    def tworzenie_kratek_XY(self) -> Tuple[List[int],List[int]]:
        odstep = int((self.wymiar/self.ilosc_rzedow_wierszow)/10)

        start_point1 = []
        end_point1 = []

        for i in range(1,self.ilosc_rzedow_wierszow):
            start_point1.append([int((self.wymiar/self.ilosc_rzedow_wierszow)*i), odstep])
            end_point1.append([int((self.wymiar/self.ilosc_rzedow_wierszow)*i), self.wymiar - odstep])

            start_point1.append([odstep, int((self.wymiar/self.ilosc_rzedow_wierszow)*i)])
            end_point1.append([self.wymiar - odstep, int((self.wymiar/self.ilosc_rzedow_wierszow)*i)])

        return start_point1, end_point1
 



