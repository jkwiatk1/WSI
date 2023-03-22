import networkx as nx
import matplotlib.pyplot as plt

def visualize_graph(graph, title):
    """
    Wizualizacja grafu
    """

    pos = nx.spring_layout(graph)
    plt.title(title)
    nx.draw(graph, pos, with_labels=True, edge_color = "Black", node_color = "Red")
    plt.show()

def show_graph(edges, title):
    graph = nx.Graph()
    graph.add_edges_from(edges)
    visualize_graph(graph, title)
