# author: Jan Kwiatkowski

import random
from initialPopulationGenerator import generate_population

num_vertices = 7
# population_size = 100
# random.seed(123)

edges = [(0, 2), (0, 4), (0, 7), (1, 3), (1, 5), (1, 7), (2, 4), (2, 5), (3, 6), (5, 7)]
nodes = [0,1,2,3,4,5,6,7]


'''
Ocena populacji (Funkcja przystosowania): 
dla każdego zbioru wierzchołków z populacji oblicz liczbę krawędzi grafu, 
które są pokryte przez ten zbiór wierzchołków.
'''
def calculate_fitness(individual, graph):
    '''
    # Obliczanie liczby pokrytych krawędzi
    # Iteracja po krawędziach grafu
    '''

    fitness = sum(1 for edge in graph if individual[edge[0]] or individual[edge[1]])
    return fitness


'''
Selekcja: wybierz najlepsze rozwiązania z populacji (np. najlepsze K osobników według wartości funkcji celu dlatego wywolujemy N razy).
'''
# def tournament_selection(population, fitness, tournament_size):
#     indices = random.sample(range(len(population)), tournament_size)
#     tournament_population = [population[i] for i in indices]
#     tournament_fitness = [fitness[i] for i in indices]
#     index = tournament_fitness.index(min(tournament_fitness))
#     return tournament_population[index]

def tournament_selection(population, fitness_scores, tournament_size, selection_size):
    selected_indices = []
    for i in range(selection_size):
        tournament_indices = random.sample(range(len(population)), tournament_size)
        tournament_fitnesses = [fitness_scores[index] for index in tournament_indices]
        best_index = tournament_indices[tournament_fitnesses.index(max(tournament_fitnesses))]
        selected_indices.append(best_index)
    selected_population = [population[i] for i in selected_indices]
    return selected_population
'''
 Selekcja turniejowa polega na losowym wyborze kilku osobników z populacji i wybraniu z nich najlepszego jako jednego z rodziców do utworzenia nowego osobnika. Ten proces jest powtarzany kilka razy, aby wybrać drugiego rodzica.
Funkcja ta przyjmuje cztery argumenty: populację, wyniki funkcji przystosowania dla każdego osobnika w populacji, rozmiar turnieju oraz rozmiar docelowej populacji selekcji. 
Zwraca populację wybranych osobników, którzy zostaną przekazani do kolejnego etapu algorytmu ewolucyjnego.
W każdej iteracji pętli for, wybieramy losowo kilka osobników z populacji (liczbę określoną przez argument tournament_size), a następnie wybieramy spośród nich osobnika o najlepszym wyniku funkcji przystosowania. 
Taki proces jest powtarzany selection_size razy, a każdorazowo wybrany osobnik zostaje dodany do listy wybranych indeksów, a następnie zwracany jest zbiór osobników odpowiadający tym indeksom.
Selekcja turniejowa jest jednym z popularnych sposobów selekcji w algorytmach ewolucyjnych i często daje dobre wyniki w różnych problemach. 
'''

'''
def tournament_selection(population, fitness_fn, tournament_size):
    """Selekcja turniejowa"""
    tournament = random.sample(population, tournament_size)
    return max(tournament, key=fitness_fn)
'''

'''
Mutacja: wykonaj operację mutacji na każdym z potomków. 
Mutacja polega na dodaniu lub usunięciu losowego wierzchołka z potomka.
'''

def mutation(individual, mutation_rate):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = 1 - individual[i]  # zmiana 0 na 1 lub 1 na 0 z zadanym prawdopodobieństwem
    return individual



# Generowanie populacji o rozmiarze population_size
population_size = 5
population = generate_population(population_size, nodes)

# Obliczanie wartości funkcji przystosowania dla każdego osobnika w populacji
for individual in population:
    fitness = calculate_fitness(individual, edges)
    individual.append(fitness)
    print(individual)


fitness_scores = [calculate_fitness(individual, edges) for individual in population]
# Wybór najlepszych osobników do kolejnej generacji SELEKCJA ELITARNA
elite_indices = sorted(range(len(population)), key=lambda i: fitness_scores[i], reverse=True)[:2]
next_generation = [population[i] for i in elite_indices]

print(next_generation)
#SELEKCJA TURNIEJOWA ta teraz dziala dobrze
print(tournament_selection(population, fitness_scores, 2,2))

'''
Poniżej opisuję poszczególne kroki w tym fragmencie kodu:

elite_indices = sorted(range(len(population)), key=lambda i: fitness_scores[i], reverse=True)[:elite_size]
range(len(population)) tworzy listę liczb całkowitych od 0 do len(population)-1.
key=lambda i: fitness_scores[i] określa, że porównywane będą elementy listy fitness_scores odpowiadające indeksom z listy utworzonej w poprzednim kroku.
sorted() sortuje elementy na podstawie klucza (czyli wartości funkcji fitness) w kolejności malejącej (reverse=True).
[:elite_size] wybiera pierwsze elite_size elementów z posortowanej listy, czyli indeksy osobników o najlepszych wynikach.
next_generation = [population[i] for i in elite_indices]
population[i] wybiera osobnika z populacji o indeksie i.
for i in elite_indices iteruje po indeksach osobników o najlepszych wynikach wybranych w poprzednim kroku.
[population[i] for i in elite_indices] tworzy listę osobników o najlepszych wynikach, którzy zostaną przekazani do następnej generacji.
Ostatecznie, next_generation będzie zawierać kopie kilku najlepszych osobników z populacji population, zgodnie z wynikami funkcji fitness. Dzięki temu, najlepsze rozwiązania zostaną zachowane i będą mogły przekazać swoje geny dalej, a więc wpłynąć na kolejne generacje.'
'''

def genetic_algorithm(num_generations = 1000, mutation_probability = 0.01, elite_size = 2):
    for generation in range(num_generations):
        # Ocena fitness dla każdego osobnika
        fitness_scores = [calculate_fitness(individual,edges) for individual in population]

        # Wybór najlepszych osobników do kolejnej generacji
        elite_indices = sorted(range(len(population)), key=lambda i: fitness_scores[i], reverse=True)[:elite_size]
        next_generation = [population[i] for i in elite_indices]

        # Reprodukcja i mutacja
        while len(next_generation) < population_size:


            # Mutacja
            for individual in population:
                if random.random() < mutation_probability:
                    child = mutation(individual,mutation_probability)
                    next_generation.append(child)



        # Aktualizacja populacji
        population = next_generation

    # Wybór najlepszego osobnika
    best_individual = max(population, key=lambda individual: calculate_fitness(individual,edges))
    return best_individual, calculate_fitness(best_individual, edges)