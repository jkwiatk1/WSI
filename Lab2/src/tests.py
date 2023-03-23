# author: Jan Kwiatkowski

from graphsGenerator import create_complete_graph, create_bipartite_graph, create_random_graph
from graphVisualizer import show_graph
from geneticAlgorithm import GeneticAlgorithm


edges = [(0, 2), (0, 4), (0, 7), (1, 3), (1, 5), (1, 7), (2, 4), (2, 5), (3, 6), (5, 7)]
nodes = [0,1,2,3,4,5,6,7]
print(edges)
show_graph(edges, "Testowy")
GeneticAlgorithmInit_Test = GeneticAlgorithm(edges= edges, nodes= nodes, population_size = 10, tournament_size= 2, selection_size = 2, mutation_rate = 0.01)
best_Test = GeneticAlgorithmInit_Test.genetic_algorithm(num_generations = 100, mutation_probability = 0.01)
print(best_Test)


"""
Graf pełny
"""
# complete_graph_1_nodes = create_complete_graph(5)[0]
# complete_graph_1_edges = create_complete_graph(5)[1]
# print(complete_graph_1_edges)
# show_graph(complete_graph_1_edges, "Graf pełny")
# algorithmInit_Complete = GeneticAlgorithm(edges= complete_graph_1_edges, nodes= complete_graph_1_nodes, population_size = 5, tournament_size= 2, selection_size = 2, mutation_rate = 0.01)
# best = algorithmInit_Complete.genetic_algorithm(num_generations = 100, mutation_probability = 0.01)
# print(best)


"""
Graf dwudzielny
"""
# bipartite_graph_1_nodes = create_bipartite_graph(4,3)[0]
# bipartite_graph_1_edges = create_bipartite_graph(4,3)[1]
# print(create_bipartite_graph(4,3)[1])
# show_graph(bipartite_graph_1_edges, "Graf dwudzielny")
# algorithmInit_Bipartite = GeneticAlgorithm(edges= bipartite_graph_1_edges, nodes= bipartite_graph_1_nodes, population_size = 5, tournament_size= 2, selection_size = 2, mutation_rate = 0.01)
# best = algorithmInit_Bipartite.genetic_algorithm(num_generations = 1000, mutation_probability = 0.01)
# print(best)


"""
Graf z połową krawędzi
"""
# random_graph_1_nodes, random_graph_1_edges = create_random_graph(7,0.5)
# print(random_graph_1_edges)
# show_graph(random_graph_1_edges, "Graf z połową krawędzi")
# algorithmInit_Random = GeneticAlgorithm(edges= random_graph_1_edges, nodes= random_graph_1_nodes, population_size = 5, tournament_size= 2, selection_size = 2, mutation_rate = 0.01)
# best_R = algorithmInit_Random .genetic_algorithm(num_generations = 1000, mutation_probability = 0.01)
# print(best_R)