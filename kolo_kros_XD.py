import numpy as np
import cv2
from typing import List, Tuple


class Tablica:
    def __init__(self, wymiary: Tuple[int,int], tryb_nocny: bool = False, ilosc_miejsc_w_grze: int = 9, kolor_tla: Tuple[int,int] = None, kolor: Tuple[int,int] = None):
        self.wymiar = max(wymiary)
        self.x, self.y = wymiary[0], wymiary[1]

        self.tlo, self.kolor = self.kolory(kolor_tla,kolor, tryb_nocny)

        self.plasza = self.tworzenie_planszy

        self.ilosc_miejsc_w_grze = ilosc_miejsc_w_grze

    
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
        # for i in range(self.wymiar):             
        #     plansza[i][0] = self.kolor
        #     plansza[-1][0] = self.kolor
        #     plansza[0][i] = self.kolor
        #     plansza[0][-1] = self.kolor

        return plansza
    
    def tworzenie_kratek(self) -> Tuple[List[int],List[int]]:

        sqrt_ilosc = int(np.sqrt(self.ilosc_miejsc_w_grze))

        odstep = int((self.wymiar/sqrt_ilosc)/10)

        start_point1 = []
        end_point1 = []
        for i in range(1,sqrt_ilosc):
            start_point1.append([int((self.wymiar/sqrt_ilosc)*i), odstep])
            end_point1.append([int((self.wymiar/sqrt_ilosc)*i), self.wymiar - odstep])

            start_point1.append([odstep, int((self.wymiar/sqrt_ilosc)*i)])
            end_point1.append([self.wymiar - odstep, int((self.wymiar/sqrt_ilosc)*i)])

        return start_point1, end_point1
 
class Kolo:
    def __init__(self, Obiekt_tablica: Tablica, miejsce: int,  kolor: Tuple[int,int,int] = None):
        self.wymiar = Obiekt_tablica.wymiar
        self.sqrt_ilosci = int(np.sqrt(Obiekt_tablica.ilosc_miejsc_w_grze))

        self.r = int(Obiekt_tablica.wymiar/((self.sqrt_ilosci+1)*2))
        self.dlugosc = int(Obiekt_tablica.wymiar/(self.sqrt_ilosci))
        if kolor is None:
            kolor = Obiekt_tablica.kolor
        self.kolor = kolor

        self.wspolrzedne_xy = self.okresl_wsp(miejsce)
        self.srodek_xy = self.wspolrzedne_xy[0] + int(self.dlugosc/2), self.wspolrzedne_xy[1] + int(self.dlugosc/2)


    def okresl_wsp(self, miejsce: int):
        ile_w_lini = int(self.sqrt_ilosci)

        dlugosc = int(np.ceil(self.wymiar/ile_w_lini))

        #miejsce musi być numerowane od 0 do ...
        x = (miejsce)*dlugosc

        jaka_linijka = int(np.floor(x/self.wymiar))
        x = x-(jaka_linijka*self.wymiar)
        y = jaka_linijka*dlugosc

        return x,y

    def wyswietlenie(self, image):
        cv2.circle(image, self.srodek_xy, self.r, self.kolor, thickness=4)

class X:
    def __init__(self, Obiekt_tablica: Tablica, miejsce: int, kolor: Tuple[int,int,int] = None):
        self.wymiar = Obiekt_tablica.wymiar
        self.sqrt_ilosci = int(np.sqrt(Obiekt_tablica.ilosc_miejsc_w_grze))

        self.dlugosc = int(self.wymiar/(self.sqrt_ilosci))
        if kolor is None:
            kolor = Obiekt_tablica.kolor
        self.kolor = kolor

        self.wspolrzedne_xy_poczatku = self.okresl_wsp(miejsce)

    def okresl_wsp(self, miejsce: int):
        ile_w_lini = int(self.sqrt_ilosci)

        dlugosc = int(np.ceil(self.wymiar/ile_w_lini))

        #miejsce musi być numerowane od 0 do ...
        x = (miejsce)*dlugosc

        jaka_linijka = int(np.floor(x/self.wymiar))
        x = x-(jaka_linijka*self.wymiar)
        y = jaka_linijka*dlugosc

        return x,y


    def wyswietlenie(self, image):

        start_point1 = self.wspolrzedne_xy_poczatku[0] + int(self.dlugosc/7), self.wspolrzedne_xy_poczatku[1] + int(self.dlugosc/7)
        end_point1 =  self.wspolrzedne_xy_poczatku[0] + int((6*self.dlugosc)/7), self.wspolrzedne_xy_poczatku[1] + int((6*self.dlugosc)/7)
        start_point2 = self.wspolrzedne_xy_poczatku[0] + int(self.dlugosc/7), self.wspolrzedne_xy_poczatku[1] + int((6*self.dlugosc)/7)
        end_point2 = self.wspolrzedne_xy_poczatku[0] + int((6*self.dlugosc)/7), self.wspolrzedne_xy_poczatku[1] + int(self.dlugosc/7)

    # Rysowanie pierwszej linii "X"
        cv2.line(image, start_point1, end_point1, self.kolor, thickness=4)
    
    # Rysowanie drugiej linii "X"
        cv2.line(image, start_point2, end_point2, self.kolor, thickness=4)

    

class Wyswietlanie:
    def __init__(self, Obiekt_tablica: Tablica, tablica_gry: List[int]):
        self.clicked_point = None
        self.clicked_point_previous = None

        self.Obiekt_tablica = Obiekt_tablica
        self.tablica_gry = tablica_gry
    
    def aktualizacja_tablicy_gry(self, tablica_gry: List[int]):
        self.tablica_gry = tablica_gry

    def click_event(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.clicked_point = (x, y)

    def wyswietlanie_caloci(self):
        image = np.array(self.Obiekt_tablica.plasza(), dtype=np.uint8)

        cv2.namedWindow('image')
        cv2.setMouseCallback('image', self.click_event)
        self.wyswielenie_kratki(image)
        self.__kolko_kros(image)
        resized_image = cv2.resize(image, (self.Obiekt_tablica.x, self.Obiekt_tablica.y), interpolation=cv2.INTER_NEAREST)

        
        while self.clicked_point == self.clicked_point_previous:
            cv2.imshow('image', resized_image)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break

        
        self.clicked_point_previous = self.clicked_point
        return self.__ktora_kratka(self.clicked_point)
    
    def __kolko_kros(self, image):  
        for i in self.tablica_gry:
            if i is not None:
                i.wyswietlenie(image)

    def __ktora_kratka(self, xy: Tuple[int,int]):
        ktora_kolumna_x = np.floor(xy[0]/(self.Obiekt_tablica.wymiar/np.sqrt(self.Obiekt_tablica.ilosc_miejsc_w_grze)))
        ktory_wyiersz_y = np.floor(xy[1]/(self.Obiekt_tablica.wymiar/np.sqrt(self.Obiekt_tablica.ilosc_miejsc_w_grze)))*np.sqrt(self.Obiekt_tablica.ilosc_miejsc_w_grze)

        return int(ktora_kolumna_x + ktory_wyiersz_y)
    
    def wyswielenie_kratki(self, image, thickness: int = 1):
        start_point1, end_point1 = self.Obiekt_tablica.tworzenie_kratek()

        
        for i, j in zip(start_point1,end_point1):
            cv2.line(image, i, j, self.Obiekt_tablica.kolor, thickness=thickness)
        
        

tablica_gry = [None for __ in range(9)]


tablica = Tablica((500,500), ilosc_miejsc_w_grze=100, kolor_tla=(203,192,255))
tablica_gry.append(Kolo(tablica, 0))
tablica_gry.append(X(tablica, 7))
tablica_gry.append(Kolo(tablica, 8))

gra = Wyswietlanie(tablica,tablica_gry)

for __ in range(10):
    aha = gra.wyswietlanie_caloci()
    print(aha)
    tablica_gry.append(X(tablica, aha))
    gra.aktualizacja_tablicy_gry(tablica_gry)

