# author: Jan Kwiatkowski

from graphsGenerator import create_complete_graph, create_bipartite_graph, create_random_graph
from graphVisualizer import show_graph
from geneticAlgorithm import GeneticAlgorithm


"""
Graf pełny
"""
complete_graph_1_nodes, complete_graph_1_edges  = create_complete_graph(25)
number_of_all_edges_Complete = len(complete_graph_1_edges)

for i in range(5):
    GeneticAlgorithmInit_Complete = GeneticAlgorithm(edges=complete_graph_1_edges, nodes=complete_graph_1_nodes,
                                                     num_generations=100, mutation_probability=0.01, population_size=50,
                                                     tournament_size=2, selection_size=50, mutation_rate=0.01)
    best = GeneticAlgorithmInit_Complete.genetic_algorithm()
    result = best[1]/number_of_all_edges_Complete
    show_graph(complete_graph_1_edges, f"Graf pełny, Pokrycie={result}", best[0])



"""
Graf dwudzielny
"""

for i in range(5):
    bipartite_graph_1_nodes, bipartite_graph_1_edges = create_bipartite_graph(13, 12)
    number_of_all_edges_Bipartite = len(bipartite_graph_1_edges)
    GeneticAlgorithmInit_Bipartite = GeneticAlgorithm(edges=bipartite_graph_1_edges, nodes=bipartite_graph_1_nodes,
                                                     num_generations=100, mutation_probability=0.01, population_size=50,
                                                     tournament_size=2, selection_size=50, mutation_rate=0.01)
    best = GeneticAlgorithmInit_Bipartite.genetic_algorithm()
    result = best[1]/number_of_all_edges_Bipartite
    show_graph(bipartite_graph_1_edges, f"Graf dwudzielny, Pokrycie={result}", best[0])



"""
Graf z połową krawędzi
"""
for i in range(5):
    random_graph_1_nodes, random_graph_1_edges = create_random_graph(25,0.5)
    number_of_all_edges_Random = len(random_graph_1_edges)
    GeneticAlgorithmInit_Random = GeneticAlgorithm(edges=random_graph_1_edges, nodes=random_graph_1_nodes,
                                                     num_generations=100, mutation_probability=0.01, population_size=50,
                                                     tournament_size=2, selection_size=50, mutation_rate=0.01)
    best = GeneticAlgorithmInit_Random.genetic_algorithm()
    result = best[1]/number_of_all_edges_Random
    show_graph(random_graph_1_edges, f"Graf losowy, Pokrycie={result}", best[0])
