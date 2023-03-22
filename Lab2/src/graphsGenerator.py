# author: Jan Kwiatkowski

import networkx as nx

def create_complete_graph(numNodes):
    """
    Tworzy pełny graf o n wierzchołkach.
    Zwraca go jako listę krotek.
    """
    graph = []
    for i in range(numNodes):
        for j in range(i+1, numNodes):
            graph.append((i, j))
    return graph


def create_bipartite_graph(leftNodes, rightNodes):
    """
    Tworzy graf dwudzielny o leftNodes wierzchołkach po jednej stronie i rightNodes po drugiej.
    Gotowy graf zwraca go jako listę krotek.
    """
    graph = [(i, j) for i in range(leftNodes) for j in range(leftNodes, leftNodes+rightNodes)]
    return graph


def create_random_graph(numNodes, probOfVertex):
    graph = nx.erdos_renyi_graph(numNodes, probOfVertex)  #nx.erdos_renyi_graph(8, 0.5, seed=21)
    graph = graph.edges()
    return graph