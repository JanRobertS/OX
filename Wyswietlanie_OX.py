import cv2
import numpy as np
from typing import List, Tuple, Union

from Tablica_OX import Tablica

from Znaki import X, O

clicked_point, clicked_point_previous = None, None


def __click_event(event, x, y, flags, param):
    global clicked_point

    if event == cv2.EVENT_LBUTTONDOWN:
        clicked_point = (x, y)

def wyswietlanie_caloci(Tablica: Tablica, tablica_gry: List[List[Union[None, O, X]]], wygrana: bool = False, start: Tuple[int,int] = None, end: Tuple[int,int] = None, kratki: bool = True):
    global clicked_point_previous
    global clicked_point

    image = np.array(Tablica.plasza, dtype=np.uint8)

    cv2.namedWindow('image')
    cv2.setMouseCallback('image', __click_event)

    if kratki:
        wyswielenie_kratki(image, Tablica)

    kolko_kros(image, tablica_gry)
    
    if wygrana:
        wyswietl_wygrana(image, Tablica, start, end)
    
    resized_image = cv2.resize(image, (Tablica.x, Tablica.y), interpolation=cv2.INTER_NEAREST)
        
    while clicked_point == clicked_point_previous:
        cv2.imshow('image', resized_image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
        
    clicked_point_previous = clicked_point
    return __ktoy_KW(clicked_point,Tablica)

def kolko_kros(image, tablica_gry: List[List[int]]) -> Tuple[int,int]:  
    for i in range(len(tablica_gry)):
        for j in range(len(tablica_gry[i])):
            if tablica_gry[i][j] is not None:
                tablica_gry[i][j].wyswietlenie(image)

def __ktoy_KW(xy: Tuple[int,int], Tablica: Tablica):
    ktora_kolumna_x = np.floor(xy[0]/(Tablica.wymiar/Tablica.ilosc_rzedow_wierszow))
    ktory_wyiersz_y = np.floor(xy[1]/(Tablica.wymiar/Tablica.ilosc_rzedow_wierszow))

    return int(ktora_kolumna_x), int(ktory_wyiersz_y)
    
def wyswielenie_kratki(image, Tablica: Tablica, thickness: int = 1):
    start_point1, end_point1 = Tablica.tworzenie_kratek_XY()
        
    for i, j in zip(start_point1,end_point1):
        cv2.line(image, i, j, Tablica.kolor, thickness=thickness)

def wyswietl_wygrana(image, Tablica: Tablica, start: Tuple[int,int], end: Tuple[int,int]):
    odleglosc_kratki = int(np.round((Tablica.wymiar/Tablica.ilosc_rzedow_wierszow)))

    wiersz, rzad = start
    start = rzad * odleglosc_kratki, wiersz * odleglosc_kratki 

    wiersz, rzad = end
    end = rzad * odleglosc_kratki, wiersz * odleglosc_kratki
        
    polowa_odleglosci = int(np.round((Tablica.wymiar/Tablica.ilosc_rzedow_wierszow)/2))    

    if start[0] == end[0]:
        start = start[0] + polowa_odleglosci, start[1]

        end = end[0] + polowa_odleglosci, end[1] + 2*polowa_odleglosci

    elif start[1] == end[1]:
        end = end[0] + 2*polowa_odleglosci, end[1] + polowa_odleglosci

        start = start[0], start[1] + polowa_odleglosci

    elif start[0] < end[0]:
        end = end[0] + 2*polowa_odleglosci, end[1] + 2*polowa_odleglosci

    elif start[0] > end[0]:
        start = start[0] + 2*polowa_odleglosci, start[1]

        end = end[0], end[1] + 2*polowa_odleglosci

    print(start,end)

    cv2.line(image, start, end, Tablica.kolor, thickness=4)