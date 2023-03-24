# author: Jan Kwiatkowski

import random
import numpy as np
from initialPopulationGenerator import generate_population


random.seed(123)

# class GeneticAlgorithm:
#     def __init__(self, edges, nodes,  num_generations, mutation_probability, population_size, tournament_size, selection_size, mutation_rate):
#         self.edges = edges
#         self.nodes = nodes
#         self.num_generations = num_generations
#         self.mutation_probability = mutation_probability
#         self.population_size = population_size
#         self.tournament_size = tournament_size
#         self.selection_size = selection_size
#         self.mutation_rate = mutation_rate
#
#
#     def calculate_penalty(self,individual):
#         num_ones = sum(individual)
#         penalty = num_ones * 0.5
#         return penalty
#
#     def calculate_fitness(self,individual, edges):
#         fitness = sum(1 for edge in edges if individual[edge[0]] or individual[edge[1]])
#         penalty = self.calculate_penalty(individual)
#         fitness -= penalty
#         return fitness
#
#     def calculate_fitness_for_all(self,population):
#         fitness_for_all = []
#         for individual in population:
#             fitness = self.calculate_fitness(individual, self.edges)
#             fitness_for_all.append(fitness)
#         return fitness_for_all
#
#
#
#     def tournament_selection(self,population, fitness_scores, tournament_size, selection_size):
#         selected_indices = []
#         for i in range(selection_size):
#             tournament_indices = random.sample(range(len(population)), tournament_size)
#             tournament_fitnesses = [fitness_scores[index] for index in tournament_indices]
#             best_index = tournament_indices[tournament_fitnesses.index(max(tournament_fitnesses))]
#             selected_indices.append(best_index)
#         selected_population = [population[i] for i in selected_indices]
#         return selected_population
#
#     def mutation(self, individual, mutation_rate):
#         num_mutations = int(np.random.normal(loc=mutation_rate * len(individual), scale=1))
#         for i in range(num_mutations):
#             index_to_mutate = random.randint(0, len(individual)-1)
#             individual[index_to_mutate] = 1 - individual[index_to_mutate]
#         return individual
#
#
#
#     def genetic_algorithm(self):
#         population = generate_population(self.population_size, self.nodes)
#         print(population)
#
#         fitness_scores = self.calculate_fitness_for_all(population)
#
#         for generation in range(self.num_generations):
#             Tt = self.tournament_selection(population, fitness_scores, 2, len(population))
#
#             for individual in Tt:
#                 if random.random() < self.mutation_probability:
#                     self.mutation(individual, self.mutation_probability)
#
#             fitness_scores = self.calculate_fitness_for_all(Tt)
#
#             elite_indices = sorted(range(len(Tt)), key=lambda i: fitness_scores[i], reverse=True)[:len(population)]
#             #elite_indices = sorted(range(len(Tt)), key=lambda i: (fitness_scores[i], -sum(Tt[i])), reverse=True)[:len(population)]
#             population = [Tt[i] for i in elite_indices]
#
#         print(fitness_scores)
#         print(population)
#
#         # # Wybór najlepszego osobnika
#         # best_individual = max(population, key=lambda individual: self.calculate_fitness(individual, self.edges))
#         # best_individual = max(population, key=lambda individual: (self.calculate_fitness(individual, self.edges), -sum(individual)))
#         best_individual = max(population, key=lambda individual: self.calculate_fitness(individual, self.edges))
#         best_individual = min(filter(lambda individual: individual == best_individual,population), key=lambda individual: sum(individual))
#         return best_individual, self.calculate_fitness(best_individual, self.edges)





class GeneticAlgorithm:
    def __init__(self, edges, nodes, num_generations, mutation_probability, population_size, tournament_size, selection_size, mutation_rate):
        self.edges = edges
        self.nodes = nodes
        self.num_generations = num_generations
        self.mutation_probability = mutation_probability
        self.population_size = population_size
        self.tournament_size = tournament_size
        self.selection_size = selection_size
        self.mutation_rate = mutation_rate

    def calculate_number_of_cover_edges(self,individual, edges):
        fitness = sum(1 for edge in edges if individual[edge[0]] or individual[edge[1]])
        return fitness

    def calculate_penalty(self,individual):
        num_ones = sum(individual)
        penalty = num_ones * 0.5
        return penalty

    def calculate_fitness(self, individual, edges):
        cost = sum(individual)
        covered_edges = sum(1 for edge in edges if individual[edge[0]] or individual[edge[1]])
        fitness = -cost + covered_edges
        return fitness

    def calculate_fitness_for_all(self,population):
        fitness_for_all = []
        for individual in population:
            fitness = self.calculate_fitness(individual, self.edges)
            fitness_for_all.append(fitness)
        return fitness_for_all

    def tournament_selection(self,population, fitness_scores, tournament_size, selection_size):
        selected_indices = []
        for i in range(selection_size):
            tournament_indices = random.sample(range(len(population)), tournament_size)
            tournament_fitnesses = [fitness_scores[index] for index in tournament_indices]
            best_index = tournament_indices[tournament_fitnesses.index(max(tournament_fitnesses))]
            selected_indices.append(best_index)
        selected_population = [population[i] for i in selected_indices]
        return selected_population

    def mutation(self, individual, mutation_rate):
        num_mutations = int(np.random.normal(loc=mutation_rate * len(individual), scale=1))
        for i in range(num_mutations):
            index_to_mutate = random.randint(0, len(individual)-1)
            individual[index_to_mutate] = 1 - individual[index_to_mutate]
        return individual

    def genetic_algorithm(self):
        population = generate_population(self.population_size, self.nodes)
        fitness_scores = self.calculate_fitness_for_all(population)

        for generation in range(self.num_generations):
            Tt = self.tournament_selection(population, fitness_scores, 2, len(population))

            for individual in Tt:
                if random.random() < self.mutation_probability:
                    self.mutation(individual, self.mutation_probability)

            fitness_scores = self.calculate_fitness_for_all(Tt)

            elite_indices = sorted(range(len(Tt)), key=lambda i: fitness_scores[i], reverse=True)[:len(population)]
            population = [Tt[i] for i in elite_indices]

        # Wybór najlepszego osobnika
        best_individual = max(population, key=lambda individual: self.calculate_fitness(individual, self.edges))
        best_individual = min(filter(lambda individual : individual == best_individual,population), key=lambda individual: sum(individual))
        return best_individual, self.calculate_number_of_cover_edges(best_individual, self.edges)
