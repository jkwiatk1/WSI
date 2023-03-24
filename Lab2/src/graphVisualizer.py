# author: Jan Kwiatkowski

import networkx as nx
import matplotlib.pyplot as plt

def visualize_graph(graph, title, values):
    colors = ['green' if val == 1 else 'blue' for val in values]
    pos = nx.spring_layout(graph)
    plt.title(title)
    nodes = sorted(graph.nodes())
    nx.draw(graph, pos, with_labels=True, node_color=colors, nodelist=nodes)
    nx.draw_networkx_edges(graph, pos)
    nx.draw_networkx_labels(graph, pos)
    plt.show()

def show_graph(edges, title, values):
    graph = nx.Graph()
    graph.add_edges_from(edges)
    visualize_graph(graph, title, values)
