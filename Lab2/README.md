# Zadanie 2 - Algorytmy genetyczne i ewolucyjne

Dokumentacja do projektu: https://github.com/jkwiatk1/WSI-lab/blob/main/Lab2/doc/wsi_2_Jan_Kwiatkowski.pdf

## Polecenie

Tematem ćwiczeń są algorytmy genetyczne i ewolucyjne. Zadaniem jest zaimplementowanie klasycznego `algorytmu ewolucyjnego bez krzyżowania, z selekcją turniejową i sukcesją generacyjną`. Należy wskazać jak zmiana liczby osobników w populacji wpływa na jakość uzyskanych rozwiązań przy ograniczonym budżecie. Dodatkowo należy opisać zachowanie algorytmu dla różnych rodzajów danych wejściowych oraz wpływ zmiany parametrów. Przykładowe zbiory danych i/lub ich generatory należy samemu skonstruować na potrzebę zadania.   

## Problem

Z powodu podwyżek cen prądu w mieście, zmniejszono nakłady na oświetlenie ulic. W mieście znajduje się n=25 placów (wierzchołki w grafie), z których można dotrzeć do sąsiadujących placów (istnieje krawędź w grafie). Latarnia stojąca na placu jest w stanie pokryć wszystkie krawędzie biegnące od tego placu do wszystkich jego sąsiadów. Które lampy powinniśmy włączyć na noc by uzyskać jak największe pokrycie wszystkich ulic. (vertex cover problem) 
Sugerowane grafy: graf pełny, graf dwudzielny, graf losowy (graf pełny z usuniętymi 50-70% krawędzi)  

## Zaimplementowany algorytm
```python
P_t = init()
t = 0
ocena(P_t)
while !stop
    Tt = selekcja(Pt)
    Ot = mutacja(Tt)
    ocena(Ot)
    Pt = Ot
    t=t+1  
```


## Rozwiązanie
* `Selekcja turniejowa` polega na tym, że losowo bez zwracania wybieramy grupę elementów i z nich wybieramy element najlepszy. Przeprowadzane jest N turniejów, co oznacza to, że wybrane wcześniej elementy, wciąż mają szansę na wystąpienie w innym turnieju. Na slajdach wykładowych mowa jest o tym, że zazwyczaj stosuje się turnieje 2 osobnikowe. Słowo klucz „zazwyczaj”. Warto wspomnieć w raporcie, że przyjmują Państwo założenie o turnieju o stałym rozmiarze, gdyż w przeciwnym wypadku spodziewałbym się od Państwa turnieju k-elementowego, gdzie wartość k również zostanie przebadana w ramach eksperymentów.   
 
* `Mutacja` stanowi element pomocniczy ułatwiający opuszczenie ekstremum lokalnego, zwiększający różnorodność populacji za pomocą generowania punktów w otoczeniu punktu mutowanego.  W przypadku mutacji należy pamiętać o tym, że występują tam 2 różne prawdopodobieństwa. Po pierwsze czy dany element ulegnie mutacji (nie wszystkie dzieci powinny być mutantami rodziców!). Po drugie, który fragment dziecka należy zmutować (np. dla sekwencji miast, które i ile miast zmienić). Oczywiście można to dodatkowo komplikować o prawdopodobieństwo siły samej mutacji, ale nie to jest celem tego zadania.  
 
* `Sukcesja generacyjna` jest najprostszym przykładem sukcesji, gdzie wszystkie elementy pochodne stają się nową generacją bazową. Uwaga, liczność populacji nie powinna ulec zmianie, dlatego na etapie mutacji (generacja sąsiadów) lub selekcji (liczba turniejów) musimy o to zadbać. Dodatkowo startowa liczność populacji powinna być znacznie większa od rozmiaru problemu, którym się zajmujemy.  
 

* Jeżeli chodzi zaś o same zadania to są to historyjki dopisane do realnych problemów NP-zupełnych dotyczących zadań grafowych. Nie zależy nam na znalezieniu idealnego rozwiązania tylko na znalezieniu najlepszego z nich przy ograniczonym budżecie. Na potrzebę tego zadania warto zastanowić się co stanowi element populacji i w jaki sposób będziemy modyfikować jego strukturę w kolejnych iteracjach. Dla problemu podzbioru wierzchołków grafu może to być sekwencja punktów z wartościami 0 i 1, gdzie 1 oznacza użycie danego wierzchołka a 0 jego zignorowanie. Wtedy mutacją będzie przełączenie wartości z 0->1 i 1->0. Np. dla wierzchołków 1234 użyjemy sekwencji 0110, gdzie tylko wierzchołki 2 i 3 zostaną użyte.
 
* Wszystkie grafy są nieskierowane, chyba że treść zadania przewiduje inaczej. Problem najmniejszego pokrycia wierzchołkowego – minimalny podzbiór wierzchołków, który pokrywa cały graf 
 
## Dodatkowe uwagi:  
* Dostali Państwo zadania grafowe, dlatego warto jest zwizualizować sobie końcowy wynik działania algorytmu.  
* nie można wyciągać wniosków po jednym wykonaniu algorytmu. Jeśli generują Państwo losowe wyniki to niezbędne jest przeprowadzenie kilkunastu pomiarów i wyznaczenie miar takich jak średnia czy odchylenie standardowe (nie zapominajmy o pomiarach czasowych, gdyż sama jakość wyniku nie daje pełnego obrazu). Warto również mieć wpływ na losowość algorytmu i pamiętać ziarno generatora do testów.  
