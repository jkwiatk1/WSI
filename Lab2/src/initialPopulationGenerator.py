# author: Jan Kwiatkowski

import random


# random.seed(123)
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

def generate_population(population_size, nodes, min_lights=1, max_lights=None):
    # Generowanie populacji losowych wektorów binarnych
    nodesLenght = len(nodes)
    population = [generate_individual(nodesLenght, min_lights, max_lights) for i in range(population_size)]
    return population