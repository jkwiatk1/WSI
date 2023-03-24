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
    nodes = list(range(numNodes))
    return nodes, graph


def create_bipartite_graph(leftNodes, rightNodes):
    """
    Tworzy graf dwudzielny o leftNodes wierzchołkach po jednej stronie i rightNodes po drugiej.
    Gotowy graf zwraca go jako listę krotek.
    """
    nodes = list(range(leftNodes)) + list(range(leftNodes, leftNodes + rightNodes))
    graph = [(i, j) for i in range(leftNodes) for j in range(leftNodes, leftNodes+rightNodes)]
    return nodes, graph


def create_random_graph(numNodes, probOfVertex):
    graph = nx.erdos_renyi_graph(numNodes, probOfVertex)  #nx.erdos_renyi_graph(numNodes, probOfVertex, seed=123)
    nodes = graph.nodes()
    graph = graph.edges()
    return nodes, graph