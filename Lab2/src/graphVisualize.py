import matplotlib.pyplot as plt
import networkx as nx

def generate_complete_graph(num_nodes):
    G = {}
    for i in range(num_nodes):
        G[i] = set(range(num_nodes)) - set([i])
    return G


def create_complete_graph(n):
    """
    Tworzy pełny graf o n wierzchołkach i zwraca go jako listę krotek.
    """
    graph = []
    for i in range(n):
        for j in range(i+1, n):
            graph.append((i, j))
    return graph

def create_bipartite_graph(n, m):
    edges = [(i, j) for i in range(n) for j in range(n, n+m)]
    return edges



def visualize_graph(graph):
    """
    Visualize a graph using matplotlib.

    Args:
    - graph: a NetworkX graph object
    """
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, edge_color = "Green")
    plt.show()

G = generate_complete_graph(5)
print(G)


graph2 = create_complete_graph(25)
bi_graph = create_bipartite_graph(13,12)
print(bi_graph)

# # create a graph
# graph = nx.Graph()
# graphBi = nx.Graph()
# # graph.add_nodes_from([1, 2, 3, 4,5,6])
# graph.add_edges_from(graph2)
# graphBi.add_edges_from(bi_graph)
# # graph.has_node(4)
# # visualize the graph
# visualize_graph(graph)
# visualize_graph(graphBi)


#This will create a plot window showing the graph, with each node labeled by its corresponding integer value,
# and edges drawn between connected nodes.
# You can customize the appearance of the graph by passing additional arguments to the nx.draw() function,
# such as node_color, edge_color, node_size, etc.


#Oto przykład kodu, który generuje losowy graf o 8 wierzchołkach z łącznością 0,5:
G_random = nx.erdos_renyi_graph(8, 0.5)
print(G_random)

# Get the number of nodes and edges in the graph
num_nodes = G_random.number_of_nodes()
num_edges = G_random.number_of_edges()
print(f"Number of nodes: {num_nodes}")
print(f"Number of edges: {num_edges}")
# Get a list of nodes in the graph
nodes = list(G_random.nodes())
print("Nodes:", nodes)

# Get a list of edges in the graph
edges = list(G_random.edges())
print("Edges:", edges)

nx.draw(G_random, with_labels=True)
plt.show()

# Funkcja erdos_renyi_graph(n, p) generuje losowy graf o n wierzchołkach,
# gdzie każda para wierzchołków jest połączona krawędzią z prawdopodobieństwem p.
# W tym przykładzie, n=8 i p=0.5, co oznacza, że każda para wierzchołków ma szansę 50% na połączenie krawędzią.

# Jeśli chcesz bardziej kontrolować typ generowanego grafu (np. czy jest to graf skierowany czy nieskierowany),
# to moduł networkx oferuje wiele innych funkcji do generowania losowych grafów,
# takich jak gnp_random_graph, barabasi_albert_graph, watts_strogatz_graph i wiele innych.