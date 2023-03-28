# Zadanie 1 - zagadnienie przeszukiwania i związane z tym podejścia

Dokumentacja do projektu: https://github.com/jkwiatk1/WSI-lab/blob/main/Lab1/doc/wsi_1_Jan_Kwiatkowski.pdf

# Polecenie
Zadaniem była minimalizacja funkcji celu i porównanie wyników dla `metody najszybszego spadku gradientu` i `metody Newtona`. Zbadano różnice w działaniu tych metod dla różnych punktów początkowych z zadanego zakresu.

Badaną funkcją celu jest funkcja Bootha w postaci:  
`f(x,y) = (x+2*y-7)^2 + (2*x+y-5)^2, -5 <= x <= 5, -5 <= y <= 5`

Dla zadanej funkcji należało znaleźć minima lokalne i globalne lub w przypadku braku minimum wykazania, że posiada ona punkt siodłowy.

## Zaimplementowane metody
* Steepest Gradient Descent
```python
    x <- x_0
    while !stop
        d <- grad_q(x)
        x <- x+B_t * d
```

* Newton Method
```python
    x <- x_0
    while !stop
        d <-  inv_hess_q(x) * grad_q(x)
        x <- x+B_t * d  
        inv_hess - odwrotność hesjanu 
        grad - gradient 

```

## Rozwiązanie
Dla wybranego punktu początkowego szukany jest taki punkt z dziedziny problemu (w naszym przypadku liczby rzeczywiste), który najlepiej minimalizuje wartość zadanej funkcji celu. W kolejnych iteracjach wyznaczane są kolejne punkty, które dążą do rozwiązania. 
