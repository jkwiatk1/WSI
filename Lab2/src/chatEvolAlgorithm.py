import random
import matplotlib.pyplot as plt
import networkx as nx


# Lista krawędzi
edges = [(0, 2), (0, 4), (0, 7), (1, 3), (1, 5), (1, 7), (2, 4), (2, 5), (3, 6), (5, 7)]

# Liczba wierzchołków w grafie
num_vertices = max(max(edges))


# Funkcja celu
def fitness(individual):
    covered_edges = set()
    for vertex in individual:
        for edge in edges:
            if vertex in edge:
                covered_edges.add(edge)
    return len(covered_edges)


# Tworzenie populacji początkowej
population_size = 100
population = [random.sample(range(num_vertices + 1), random.randint(1, num_vertices)) for _ in range(population_size)]

# Algorytm ewolucyjny
num_generations = 1000
mutation_probability = 0.1
elite_size = 2
for generation in range(num_generations):
    # Ocena fitness dla każdego osobnika
    fitness_scores = [fitness(individual) for individual in population]

    # Wybór najlepszych osobników do kolejnej generacji
    elite_indices = sorted(range(len(population)), key=lambda i: fitness_scores[i], reverse=True)[:elite_size]
    next_generation = [population[i] for i in elite_indices]

    # Reprodukcja i mutacja
    while len(next_generation) < population_size:
        # Selekcja rodziców
        parent1 = random.choices(population, weights=fitness_scores)[0]
        parent2 = random.choices(population, weights=fitness_scores)[0]

        # Krzyżowanie
        crossover_point = random.randint(1, num_vertices - 1)
        child = parent1[:crossover_point] + parent2[crossover_point:]

        # Mutacja
        if random.random() < mutation_probability:
            mutated_gene = random.randint(0, num_vertices)
            if mutated_gene not in child:
                mutation_point = random.randint(0, len(child) - 1)
                child[mutation_point] = mutated_gene

        # Dodanie potomka do nowej populacji
        next_generation.append(child)

    # Aktualizacja populacji
    population = next_generation

# Wybór najlepszego osobnika
best_individual = max(population, key=lambda individual: fitness(individual))
print(f"Najlepszy wynik: {fitness(best_individual)}")
print(f"Minimalne pokrycie: {best_individual}")

def visualize_graph(graph):
    """
    Visualize a graph using matplotlib.

    Args:
    - graph: a NetworkX graph object
    """
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, edge_color = "Green")
    plt.show()

graph = nx.Graph()
graph.add_edges_from(edges)
visualize_graph(graph)
