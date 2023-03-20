# author: Jan Kwiatkowski

import random

# class EvolutionaryAlgorithm:
#     def __init__(self, first_population_generator, t_max, mutation_probability):
#         self.first_generation_func = first_population_generator
#         self.t_max = t_max
#         self.mutation_probability = mutation_probability


def fitness(individual, graph):
    """Funkcja przystosowania dla problemu największego pokrycia grafu"""
    return sum([1 for edge in graph if edge[0] in individual or edge[1] in individual])

def tournament_selection(population, fitness_fn, tournament_size):
    """Selekcja turniejowa"""
    tournament = random.sample(population, tournament_size)
    return max(tournament, key=fitness_fn)

def replace_population(parents, children):
    """Sukcesja generacyjna"""
    return children

def evolve(population, fitness_fn, tournament_size, mutation_rate, graph):
    """Algorytm ewolucyjny bez krzyżowania"""
    new_population = []
    for i in range(len(population)):
        parent = tournament_selection(population, fitness_fn, tournament_size)
        child = list(parent)
        for j in range(len(child)):
            if random.random() < mutation_rate:
                child[j] = 1 - child[j]
        new_population.append(child)

    new_population.sort(key=lambda x: fitness(x, graph), reverse=True)
    parents = population[:len(population)//2]
    children = new_population[:len(population)//2]
    return replace_population(parents, children)

def vertex_cover_ea(graph, population_size=100, tournament_size=3, mutation_rate=0.1, max_generations=100):
    """Główna funkcja wykonująca algorytm ewolucyjny dla problemu największego pokrycia grafu"""
    population = [[random.randint(0, 1) for i in range(len(graph))] for j in range(population_size)]
    for i in range(max_generations):
        population = evolve(population, lambda ind: fitness(ind, graph), tournament_size, mutation_rate, graph)
        best_individual = max(population, key=lambda ind: fitness(ind, graph))
        print("Generation {}: Best Fitness = {}".format(i+1, fitness(best_individual, graph)))
    return best_individual

G2 = [(1, 2, 3, 4, 5, 6, 7, 8, 9), (0, 2, 3, 4, 5, 6, 7, 8, 9), (0, 1, 3, 4, 5, 6, 7, 8, 9),
      (0, 1, 2, 4, 5, 6, 7, 8, 9), (0, 1, 2, 3, 5, 6, 7, 8, 9), (0, 1, 2, 3, 4, 6, 7, 8, 9),
      (0, 1, 2, 3, 4, 5, 7, 8, 9), (0, 1, 2, 3, 4, 5, 6, 8, 9), (0, 1, 2, 3, 4, 5, 6, 7, 9),
      (0, 1, 2, 3, 4, 5, 6, 7, 8)]



graph = [(0, 1), (1, 2), (2, 3)]
best_individual = vertex_cover_ea(G2)

# Funkcja vertex_cover_ea wykonuje algorytm ewolucyjny dla problemu największego pokrycia grafu.
# Inicjuje populację początkową o rozmiarze population_size,
# gdzie każde rozwiązanie to wektor binarny o długości równej liczbie wierzchołków w grafie.
# Następnie wykonuje ewolucję populacji przez max_generations generacji.
#
# W funkcji evolve przeprowadzana jest selekcja turniejowa z parametrem tournament_size, mutacja z prawdopodobieństwem