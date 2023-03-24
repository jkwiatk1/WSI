# author: Jan Kwiatkowski

import numpy as np
from graphsGenerator import create_complete_graph, create_bipartite_graph, create_random_graph
from geneticAlgorithm import GeneticAlgorithm

# numberOfIteration = [10,50,100,200,500]
numberOfIteration = [10,50,100]
"""
Graf pełny
"""
def expetiment_for_CompleteGraph(num_of_experiment,num_generations,population_size,selection_size):
    complete_graph_1_nodes, complete_graph_1_edges = create_complete_graph(25)
    number_of_all_edges_Complete = len(complete_graph_1_edges)
    result_for_CompleteGraph = []
    result_cover = []
    for i in range(num_of_experiment):
        GeneticAlgorithmInit_Complete = GeneticAlgorithm(edges=complete_graph_1_edges, nodes=complete_graph_1_nodes,
                                                         num_generations=num_generations, mutation_probability=0.01, population_size=population_size,
                                                         tournament_size=2, selection_size=selection_size, mutation_rate=0.01)
        best = GeneticAlgorithmInit_Complete.genetic_algorithm()
        result_cover.append(best[1]/number_of_all_edges_Complete)
        result_for_CompleteGraph.append([best[1],number_of_all_edges_Complete,result_cover])
    return result_for_CompleteGraph, result_cover

def exp_CG():
    min_all = []
    max_all = []
    mean_all = []
    for num in numberOfIteration:
        CG_exp1_all, CG_exp1_cover = expetiment_for_CompleteGraph(num_of_experiment = 51,num_generations = num,population_size = 30,selection_size = 30)
        std_dev = np.std(CG_exp1_cover)
        min_cover = min(CG_exp1_cover)
        max_cover = max(CG_exp1_cover)
        mean_cover = np.mean(CG_exp1_cover)
        min_all.append(min_cover)
        max_all.append(max_cover)
        mean_all.append(mean_cover)
        CG_exp1_cover_rounded = [round(x, 2) for x in CG_exp1_cover]
        print(f"Obliczenia dla: {num} iteracji")
        print(f"Pokrycie: ",CG_exp1_cover_rounded)
        print(f"Odchylenie standardowe: {round(std_dev,2)}")
        print(f"Min: {round(min_cover, 2)}, Max: {round(max_cover, 2)}, Avg: {round(mean_cover, 2)}")
        # print("Wyniki: ", CG_exp1_all)
        print()
    return min_all, max_all, mean_all


"""
Graf dwudzielny
"""
def expetiment_for_BipartiteGraph(num_of_experiment,num_generations,population_size,selection_size):
    bipartite_graph_1_nodes, bipartite_graph_1_edges = create_bipartite_graph(13, 12)
    number_of_all_edges_Bip = len(bipartite_graph_1_edges)
    result_for_BipGraph = []
    result_cover = []
    for i in range(num_of_experiment):
        GeneticAlgorithmInit_Complete = GeneticAlgorithm(edges=bipartite_graph_1_edges, nodes=bipartite_graph_1_nodes,
                                                         num_generations=num_generations, mutation_probability=0.01, population_size=population_size,
                                                         tournament_size=2, selection_size=selection_size, mutation_rate=0.01)
        best = GeneticAlgorithmInit_Complete.genetic_algorithm()
        result_cover.append(best[1]/number_of_all_edges_Bip)
        result_for_BipGraph.append([best[1],number_of_all_edges_Bip,result_cover])
    return result_for_BipGraph, result_cover

def exp_BG():
    min_all = []
    max_all = []
    mean_all = []
    for num in numberOfIteration:
        G_exp1_all, G_exp1_cover = expetiment_for_BipartiteGraph(num_of_experiment = 51,num_generations = num,population_size = 50,selection_size = 80)
        std_dev = np.std(G_exp1_cover)
        min_cover = min(G_exp1_cover)
        max_cover = max(G_exp1_cover)
        mean_cover = np.mean(G_exp1_cover)
        min_all.append(min_cover)
        max_all.append(max_cover)
        mean_all.append(mean_cover)
        G_exp1_cover_rounded = [round(x, 2) for x in G_exp1_cover]
        print(f"Obliczenia dla: {num} iteracji")
        print("Pokrycie: ", G_exp1_cover_rounded)
        print(f"Odchylenie standardowe: {round(std_dev,2)}")
        print(f"Min: {round(min_cover, 2)}, Max: {round(max_cover, 2)}, Avg: {round(mean_cover, 2)}")
        # print("Wyniki: ", CG_exp1_all)
        print()
    return min_all, max_all, mean_all


"""
Graf z połową krawędzi
"""
# for i in range(5):
#     random_graph_1_nodes, random_graph_1_edges = create_random_graph(25,0.5)
#     number_of_all_edges_Random = len(random_graph_1_edges)
#     GeneticAlgorithmInit_Random = GeneticAlgorithm(edges=random_graph_1_edges, nodes=random_graph_1_nodes,
#                                                      num_generations=100, mutation_probability=0.01, population_size=50,
#                                                      tournament_size=2, selection_size=50, mutation_rate=0.01)
#     best = GeneticAlgorithmInit_Random.genetic_algorithm()
#     result = best[1]/number_of_all_edges_Random
#     show_graph(random_graph_1_edges, f"Graf losowy, Pokrycie={result}", best[0])
print("________________GRAF PEŁNY________________")
minCG, maxCG, meanCG = exp_CG()
print(minCG)
print("________________GRAF DWUDZIELNY___________")
exp_BG()