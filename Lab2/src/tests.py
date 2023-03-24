# author: Jan Kwiatkowski

from graphsGenerator import create_complete_graph, create_bipartite_graph, create_random_graph
from graphVisualizer import show_graph
from geneticAlgorithm import GeneticAlgorithm


edges = [(0, 2), (0, 4), (0, 7), (1, 3), (1, 5), (1, 7), (2, 4), (2, 5), (3, 6), (5, 7)]
nodes = [0,1,2,3,4,5,6,7]
number_of_all_edges = len(edges)

"""
Graf testowy
"""
for i in range(5):
    GeneticAlgorithmInit_Test = GeneticAlgorithm(edges=edges, nodes=nodes, num_generations=100,
                                                 mutation_probability=0.01, population_size=8, tournament_size=2,
                                                 selection_size=8, mutation_rate=0.01)
    best = GeneticAlgorithmInit_Test.genetic_algorithm()
    result = best[1]/number_of_all_edges
    show_graph(edges, f"Graf testowy, Pokrycie={result}, Pokryte: {best[1]}, Wszystkie: {number_of_all_edges}", best[0])


"""
Graf pełny
"""
complete_graph_1_nodes, complete_graph_1_edges  = create_complete_graph(10)
number_of_all_edges_Complete = len(complete_graph_1_edges)

for i in range(5):
    GeneticAlgorithmInit_Complete = GeneticAlgorithm(edges=complete_graph_1_edges, nodes=complete_graph_1_nodes,
                                                     num_generations=100, mutation_probability=0.01, population_size=15,
                                                     tournament_size=2, selection_size=15, mutation_rate=0.01)
    best = GeneticAlgorithmInit_Complete.genetic_algorithm()
    result = best[1]/number_of_all_edges_Complete
    show_graph(complete_graph_1_edges, f"Graf pełny, Pokrycie={result}", best[0])



"""
Graf dwudzielny
"""

for i in range(5):
    bipartite_graph_1_nodes, bipartite_graph_1_edges = create_bipartite_graph(5, 5)
    number_of_all_edges_Bipartite = len(bipartite_graph_1_edges)
    GeneticAlgorithmInit_Bipartite = GeneticAlgorithm(edges=bipartite_graph_1_edges, nodes=bipartite_graph_1_nodes,
                                                     num_generations=100, mutation_probability=0.01, population_size=15,
                                                     tournament_size=2, selection_size=15, mutation_rate=0.01)
    best = GeneticAlgorithmInit_Bipartite.genetic_algorithm()
    result = best[1]/number_of_all_edges_Bipartite
    show_graph(bipartite_graph_1_edges, f"Graf dwudzielny, Pokrycie={result}", best[0])



"""
Graf z połową krawędzi
"""
for i in range(5):
    random_graph_1_nodes, random_graph_1_edges = create_random_graph(10,0.5)
    number_of_all_edges_Random = len(random_graph_1_edges)
    GeneticAlgorithmInit_Random = GeneticAlgorithm(edges=random_graph_1_edges, nodes=random_graph_1_nodes,
                                                   num_generations=100, mutation_probability=0.01, population_size=15,
                                                   tournament_size=2, selection_size=15, mutation_rate=0.01)
    best = GeneticAlgorithmInit_Random.genetic_algorithm()
    result = best[1]/number_of_all_edges_Random
    show_graph(random_graph_1_edges, f"Graf losowy, Pokrycie={result}", best[0])
