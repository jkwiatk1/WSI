import random
import numpy as np

# Funkcja tworząca losową permutację wierzchołków
def create_permutation(num_vertices):
    return np.random.permutation(num_vertices)

# Funkcja obliczająca długość trasy dla danej permutacji
def calculate_distance(permutation, adjacency_matrix):
    distance = 0
    for i in range(len(permutation)-1):
        distance += adjacency_matrix[permutation[i], permutation[i+1]]
    distance += adjacency_matrix[permutation[-1], permutation[0]]
    return distance

# Funkcja selekcji turniejowej
def tournament_selection(population, fitness, tournament_size):
    indices = random.sample(range(len(population)), tournament_size)
    tournament_population = [population[i] for i in indices]
    tournament_fitness = [fitness[i] for i in indices]
    index = tournament_fitness.index(min(tournament_fitness))
    return tournament_population[index]

# Funkcja krzyżowania PMX
def pmx_crossover(parent1, parent2):
    size = len(parent1)
    a = random.randint(0, size-1)
    b = random.randint(0, size-1)
    if a > b:
        a, b = b, a
    child1 = [-1] * size
    child2 = [-1] * size
    for i in range(a, b+1):
        child1[i] = parent1[i]
        child2[i] = parent2[i]
    for i in range(size):
        if i < a or i > b:
            for j in range(size):
                if parent2[j] not in child1:
                    child1[i] = parent2[j]
                    break
            for j in range(size):
                if parent1[j] not in child2:
                    child2[i] = parent1[j]
                    break
    return child1, child2

# Funkcja mutacji - zamiana dwóch losowych wierzchołków miejscami
def mutation(individual):
    a = random.randint(0, len(individual)-1)
    b = random.randint(0, len(individual)-1)
    individual[a], individual[b] = individual[b], individual[a]
    return individual

# # Funkcja algorytmu ewolucyjnego
# def evolutionary_algorithm(adjacency_matrix, population_size, tournament_size, num_generations, mutation_probability):
#     num_vertices = len(adjacency_matrix)
#     population = [create_permutation(num_vertices) for i in range(population_size)]
#     fitness = [calculate_distance(p, adjacency_matrix) for p in population]
#     for generation in range(num_generations):
#         new_population = []
#         new_population.append(population[np.argmin(fitness)])
#         while len(new_population) < population_size:
#             parent1 = tournament_selection(population, fitness, tournament_size)
#             parent2 = tournament_selection(population, fitness, tournament_size)
#             child1, child2 = pmx_crossover(parent1,arch everywhere for classes, files, tool windows, actions, and settings.

# Definicja algorytmu ewolucyjnego
def genetic_algorithm(pop_size, num_generations):
    # Generowanie populacji początkowej
    population = []
    for i in range(pop_size):
        individual = list(range(num_vertices))
        random.shuffle(individual)
        population.append(individual)
    # Pętla główna
    for gen in range(num_generations):
        # Wybór rodziców i krzyżowanie
        children = []
        for i in range(pop_size // 2):
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            child1 = crossover(parent1, parent2)
            child2 = crossover(parent2, parent1)
            children.append(child1)
            children.append(child2)
        # Mutacja i ocena wartości fitness dla dzieci
        for child in children:
            if random.random() < mutation_rate:
                mutate(child)
            child_fitness = fitness(child)
            child.append(child_fitness)
        # Wybór najlepszych osobników do nowej populacji
        population = sorted(population + children, key=lambda x: x[-1])
        best_individual = min(population, key=lambda x: x[-1])
        return best_individual[:-1]


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
