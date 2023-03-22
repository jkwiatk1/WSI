# author: Jan Kwiatkowski

import random

num_vertices = 7
population_size = 100
random.seed(123)

edges = [(0, 2), (0, 4), (0, 7), (1, 3), (1, 5), (1, 7), (2, 4), (2, 5), (3, 6), (5, 7)]

'''
Tworzy losową populację początkową
Każdy chromosom reprezentuje potencjalne pokrycie wierzchołkowe grafu
'''

def generate_individual(n, min_lights=1, max_lights=None):
    # Generowanie losowego wektora binarnego reprezentującego pojedyncze rozwiązanie
    if max_lights is None:
        max_lights = n
    num_lights = random.randint(min_lights, max_lights)
    lights = random.sample(range(n), num_lights)
    individual = [1 if i in lights else 0 for i in range(n)]
    return individual

def generate_population(population_size, n, min_lights=1, max_lights=None):
    # Generowanie populacji losowych wektorów binarnych
    population = [generate_individual(n, min_lights, max_lights) for i in range(population_size)]
    return population

def calculate_fitness(individual, graph):
    # Inicjalizacja licznika pokrytych krawędzi
    fitness = 0

    # Obliczanie liczby pokrytych krawędzi
    # Iteracja po krawędziach grafu
    for edge in graph:
        # Sprawdzenie, czy co najmniej jeden z końców krawędzi jest pokryty przez wierzchołek reprezentowany przez wartość 1 na odpowiedniej pozycji w wektorze individual
        if individual[edge[0]] == 1 or individual[edge[1]] == 1:
            # Inkrementacja licznika pokrytych krawędzi
            fitness += 1


    # fitness = sum(1 for edge in graph if individual[edge[0]] or individual[edge[1]])
    return fitness


# Generowanie populacji o rozmiarze 25
population_size = 5
nodesLenght = max(max(edges))
population = generate_population(population_size, nodesLenght)

# Obliczanie wartości funkcji przystosowania dla każdego osobnika w populacji
for individual in population:
    fitness = calculate_fitness(individual, edges)
    individual.append(fitness)
    print(individual)
