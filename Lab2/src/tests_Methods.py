# author: Jan Kwiatkowski

import random
import numpy as np

"""
Test metody która ma za zadanie mutować osobnika
"""
def mutation(individual, mutation_rate):
    individual_mutated = individual.copy()
    num_mutations = int(np.random.normal(loc=mutation_rate * len(individual), scale=1))
    for i in range(num_mutations):
        index_to_mutate = random.randint(0, len(individual))
        individual_mutated[index_to_mutate] = 1 - individual[index_to_mutate]
    return individual_mutated


vector = [1, 0, 1, 1, 1, 1, 0, 1]
mutation_rate = 0.1
mutated_vector = mutation(vector, mutation_rate)

print("Original vector:", vector)
print("Mutated vector:", mutated_vector)


"""
Test metody do oceny populacji
"""
def calculate_fitness(individual, edges):
    fitness = sum(1 for edge in edges if individual[edge[0]] or individual[edge[1]])
    return fitness


def calculate_fitness_for_all(population, edges):
    fitness_for_all = []
    for individual in population:
        fitness = calculate_fitness(individual, edges)
        fitness_for_all.append(fitness)
    return fitness_for_all


edges = [(0, 1), (1, 2), (2, 3), (3, 0)]
population = [[1, 0, 1, 0], [0, 1, 0, 1], [1, 1, 0, 0]]

fitness_for_all = calculate_fitness_for_all(population, edges)
print(fitness_for_all)


"""
Test metody do selekcji turniejowej
"""
def tournament_selection(population, fitness_scores, tournament_size = 2, selection_size = 3):
    selected_indices = []
    for i in range(selection_size):
        tournament_indices = random.sample(range(len(population)), tournament_size)
        tournament_fitnesses = [fitness_scores[index] for index in tournament_indices]
        best_index = tournament_indices[tournament_fitnesses.index(max(tournament_fitnesses))]
        selected_indices.append(best_index)
    selected_population = [population[i] for i in selected_indices]
    return selected_population

population_TS = [[1, 0, 1, 0], [0, 1, 0, 1], [1, 1, 0, 0]]
fitness_scores_TS = [4, 4, 3]
TS = tournament_selection(population_TS,fitness_scores_TS)
print(TS)

