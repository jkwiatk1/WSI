# author: Jan Kwiatkowski

from graphsGenerator import create_complete_graph, create_bipartite_graph, create_random_graph
from graphVisualizer import show_graph

edges = [(0, 2), (0, 4), (0, 7), (1, 3), (1, 5), (1, 7), (2, 4), (2, 5), (3, 6), (5, 7)]


randomG = create_random_graph(7,0.5)
print(create_complete_graph(7))
print(create_bipartite_graph(4,3))
print(randomG)
print(edges)

show_graph(create_complete_graph(7), "Graf pełny")
show_graph(create_bipartite_graph(4,3), "Graf dwudzielny")
show_graph(randomG, "Graf z połową krawędzi")
show_graph(edges, "Testowy")

