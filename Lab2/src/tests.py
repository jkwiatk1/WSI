# author: Jan Kwiatkowski

from graphsGenerator import create_complete_graph, create_bipartite_graph, create_random_graph
from graphVisualizer import show_graph
from geneticAlgorithm import GeneticAlgorithm


edges = [(0, 2), (0, 4), (0, 7), (1, 3), (1, 5), (1, 7), (2, 4), (2, 5), (3, 6), (5, 7)]
nodes = [0,1,2,3,4,5,6,7]
number_of_all_edges = len(edges)

for i in range(5):
    GeneticAlgorithmInit_Test = GeneticAlgorithm(edges=edges, nodes=nodes, num_generations=10,
                                                 mutation_probability=0.01, population_size=3, tournament_size=2,
                                                 selection_size=3, mutation_rate=0.01)
    best = GeneticAlgorithmInit_Test.genetic_algorithm()
    result = best[1]/number_of_all_edges
    print(best[0])
    show_graph(edges, f"Graf testowy, Pokrycie={result}, Pokryte: {best[1]}, Wszystkie: {number_of_all_edges}", best[0])




"""
Graf pełny
"""
# complete_graph_1_nodes, complete_graph_1_edges  = create_complete_graph(25)
# print(complete_graph_1_edges)
# print(len(complete_graph_1_edges))
#
# GeneticAlgorithmInit_Complete = GeneticAlgorithm(edges= complete_graph_1_edges, nodes= complete_graph_1_nodes, num_generations = 100, mutation_probability = 0.01, population_size = 50, tournament_size= 2, selection_size = 50, mutation_rate = 0.01)
# best = GeneticAlgorithmInit_Complete.genetic_algorithm()
# show_graph(complete_graph_1_edges, "Graf pełny",best[0])
# print(best)
#
# for i in range(4):
#     best = GeneticAlgorithmInit_Complete.genetic_algorithm()
#     show_graph(complete_graph_1_edges, "Graf pełny", best[0])
#     print(best)
#     print()



"""
Graf dwudzielny
"""
# bipartite_graph_1_nodes, bipartite_graph_1_edges = create_bipartite_graph(4,3)
# print(bipartite_graph_1_edges)
# show_graph(bipartite_graph_1_edges, "Graf dwudzielny")
# GeneticAlgorithmInit_Bipartite = GeneticAlgorithm(edges= complete_graph_1_edges, nodes= complete_graph_1_nodes, num_generations = 10, mutation_probability = 0.01, population_size = 50, tournament_size= 2, selection_size = 50, mutation_rate = 0.01)
# best = GeneticAlgorithmInit_Bipartite.genetic_algorithm()
# print(best)


"""
Graf z połową krawędzi
"""
# random_graph_1_nodes, random_graph_1_edges = create_random_graph(7,0.5)
# print(random_graph_1_edges)
# show_graph(random_graph_1_edges, "Graf z połową krawędzi")
#  GeneticAlgorithmInit_Random = GeneticAlgorithm(edges=random_graph_1_edges, nodes=random_graph_1_nodes,
#                                                      num_generations=100, mutation_probability=0.01, population_size=50,
#                                                      tournament_size=2, selection_size=50, mutation_rate=0.01)
# best_R = GeneticAlgorithmInit_Random .genetic_algorithm(num_generations = 1000, mutation_probability = 0.01)
# print(best_R)