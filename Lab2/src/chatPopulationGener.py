import random

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
    # Obliczanie liczby pokrytych krawędzi
    fitness = sum(1 for edge in graph.edges() if individual[edge[0]] or individual[edge[1]])
    return fitness

# Przykładowe użycie:
import networkx as nx

# Tworzenie grafu losowego
G = nx.erdos_renyi_graph(25, 0.3)

# Generowanie populacji o rozmiarze 50
population_size = 25
population = generate_population(population_size, len(G.nodes()))

# Obliczanie wartości funkcji przystosowania dla każdego osobnika w populacji
for individual in population:
    fitness = calculate_fitness(individual, G)
    individual.append(fitness)
    print(individual)

print(G)