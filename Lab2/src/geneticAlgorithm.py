# author: Jan Kwiatkowski

import random
from initialPopulationGenerator import generate_population

num_vertices = 7
# population_size = 100
# random.seed(123)

# edges1 = [(0, 2), (0, 4), (0, 7), (1, 3), (1, 5), (1, 7), (2, 4), (2, 5), (3, 6), (5, 7)]
edges1 = [(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11), (0, 12), (0, 13), (0, 14), (0, 15), (0, 16), (0, 17), (0, 18), (0, 19), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (1, 12), (1, 13), (1, 14), (1, 15), (1, 16), (1, 17), (1, 18), (1, 19), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (2, 10), (2, 11), (2, 12), (2, 13), (2, 14), (2, 15), (2, 16), (2, 17), (2, 18), (2, 19), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10), (3, 11), (3, 12), (3, 13), (3, 14), (3, 15), (3, 16), (3, 17), (3, 18), (3, 19), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (4, 10), (4, 11), (4, 12), (4, 13), (4, 14), (4, 15), (4, 16), (4, 17), (4, 18), (4, 19), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11), (5, 12), (5, 13), (5, 14), (5, 15), (5, 16), (5, 17), (5, 18), (5, 19), (6, 7), (6, 8), (6, 9), (6, 10), (6, 11), (6, 12), (6, 13), (6, 14), (6, 15), (6, 16), (6, 17), (6, 18), (6, 19), (7, 8), (7, 9), (7, 10), (7, 11), (7, 12), (7, 13), (7, 14), (7, 15), (7, 16), (7, 17), (7, 18), (7, 19), (8, 9), (8, 10), (8, 11), (8, 12), (8, 13), (8, 14), (8, 15), (8, 16), (8, 17), (8, 18), (8, 19), (9, 10), (9, 11), (9, 12), (9, 13), (9, 14), (9, 15), (9, 16), (9, 17), (9, 18), (9, 19), (10, 11), (10, 12), (10, 13), (10, 14), (10, 15), (10, 16), (10, 17), (10, 18), (10, 19), (11, 12), (11, 13), (11, 14), (11, 15), (11, 16), (11, 17), (11, 18), (11, 19), (12, 13), (12, 14), (12, 15), (12, 16), (12, 17), (12, 18), (12, 19), (13, 14), (13, 15), (13, 16), (13, 17), (13, 18), (13, 19), (14, 15), (14, 16), (14, 17), (14, 18), (14, 19), (15, 16), (15, 17), (15, 18), (15, 19), (16, 17), (16, 18), (16, 19), (17, 18), (17, 19), (18, 19)]
#
nodes1 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]


class GeneticAlgorithm:
    def __init__(self, edges, nodes,  population_size, tournament_size, selection_size, mutation_rate):
        self.edges = edges
        self.nodes = nodes
        self.population_size = population_size
        self.tournament_size = tournament_size
        self.selection_size = selection_size
        self.mutation_rate = mutation_rate

    def calculate_fitness(self,individual, edges):
        fitness = sum(1 for edge in edges if individual[edge[0]] or individual[edge[1]])
        return fitness

    def calculate_fitness_for_all(self, population):
        fitness_for_all = []
        for individual in population:
            fitness = self.calculate_fitness(individual, self.edges)
            fitness_for_all.append(fitness)
        return  fitness_for_all


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
        individual_mutated = individual.copy()
        for i in range(len(individual_mutated)):
            if random.random() < mutation_rate:
                individual_mutated[i] = 1 - individual_mutated[i]
        return individual_mutated





    def genetic_algorithm(self, num_generations = 10, mutation_probability = 0.01):
        population = generate_population(self.population_size, self.nodes)
        print(population)

        fitness_scores = self.calculate_fitness_for_all(population)

        for generation in range(num_generations):
            Tt = self.tournament_selection(population, fitness_scores, 2, len(population))

            next_generation = Tt.copy()
            for individual in Tt:
                if random.random() < mutation_probability:
                    mutated_individual = self.mutation(individual, mutation_probability)
                    next_generation.append(mutated_individual)

            Tt = next_generation.copy()
            fitness_scores = self.calculate_fitness_for_all(Tt)

            elite_indices = sorted(range(len(Tt)), key=lambda i: fitness_scores[i], reverse=True)[:len(population)]
            population = [Tt[i] for i in elite_indices]

        print(population)
        print(fitness_scores)

        # # Wybór najlepszego osobnika
        best_individual = max(population, key=lambda individual: self.calculate_fitness(individual, self.edges))
        return best_individual, self.calculate_fitness(best_individual, self.edges)





