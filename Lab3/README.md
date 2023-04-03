# Zadanie 3 - Dwuosobowe gry deterministyczne

Dokumentacja do projektu: 

## Polecenie

Zadaniem będzie napisanie programu, który buduje drzewo zadanej gry a następnie gra sam ze sobą wykorzystując do tego `algorytm minimax`. Należało sprawdzić dwa przypadki: 
1.	Jeden z graczy gra w sposób losowy (tzn. nie używa tego algorytmu) a drugi stara się optymalizować swoje ruchy (random vs minimax).
2.	Obaj gracze podejmują optymalne decyzje (minimax vs minimax).

Aktualny stan planszy powinien być wyświetlany w konsoli, ale można użyć dodatkowych bibliotek do pisania i wyświetlania gier w Pythonie takich jak `pygame`.
W raporcie należy przedstawić przykład wykonania programu wraz z odpowiadającymi stanami drzewa gry i wyborami algorytmu minimax. Zastosowanie przycinania alfa-beta nie jest wymagane, ale może okazać się potrzebne. W raporcie należy pokazać wygraną każdej ze stron, czyli że gra nie jest ustawiona (przeprowadzić 100 testów i zliczyć sumy wyników każdej ze stron).

## Problem

Program buduje drzewo gry w `Czwórki (Connect four)`. Wejściem są wymiary planszy NxM (N>= 5,M >=4) oraz maksymalna głębokość drzewa.
Zasady:
* gracze co turę wrzucają 1 kolorowy token (kolor odpowiada kolorowi danego gracza) do jednej z kolumn na planszy (token opada na spód kolumny – to nie jest kółko i krzyżyk!),
* jeżeli w pionie, poziomie lub na ukos znajdą się 4 tokeny gracza to ten gracz wygrywa,
* jeżeli plansza się zapełni to dochodzi do remisu.


## Zaimplementowany algorytm
```python
def minMax():
    pass 
```


## Rozwiązanie
* pass
 
## Dodatkowe uwagi:  
* Kiedy budujemy drzewo minimax o głębokości D to warto sprawdzić różne wartości tego D<=D_Max.
* Należałoby sprawdzić czy gra nie faworyzuje, któregoś z graczy i wykazać w raporcie wygraną obu stron. Jeżeli istnieje możliwość remisu to też warto byłoby to pokazać.
* Wybór następnego ruchu przez algorytm dla zbioru tak samo ocenionych stanów powinien wykonywać się w sposób losowy (tzn. jeżeli mamy do wyboru pole 1,2 i 5 o tej samej wartości funkcji heurystycznej to każde z nich powinno mieć szansę wyboru a nie tylko pole nr 1).
* Rozwiązanie powinno być w miarę ogólne tzn. proszę nie robić 12 zagnieżdżonych pętli `for` jeśli da się to zadanie rozwiązać brutalnie tylko zaimplementować wskazany algorytm. 

