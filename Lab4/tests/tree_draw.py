import numpy as np
import graphviz

from model.decisionTree_id3 import ID3Tree

def plot_tree(node, dot=None, counter=0):
    if not dot:
        dot = graphviz.Digraph()
        dot.attr('node', shape='box')
    dot.node(str(id(node)), 'Atr: ' + str(node.feature_idx))
    for child in node.children:
        if child.is_leaf_node():
            dot.node(str(id(child)), 'Class: ' + str(child.predicted_class))
            dot.edge(str(id(node)), str(id(child)), label="= {:.2f}".format(child.threshold))
            counter += 1
            continue
        else:
            dot.edge(str(id(node)), str(id(child)), label="= {:.2f}".format(child.threshold))
        plot_tree(child, dot, counter)
        counter += len(child.children)
    return dot


test_on = False
if(test_on == True):
    X = np.array(
        [[1, 2, 3, 4], [1, 1, 2, 4], [2, 3, 4, 4], [1, 2, 2, 4], [2, 2, 3, 4], [3, 2, 2, 4], [1, 2, 2, 3],
         [2, 2, 3, 3], [3, 3, 3, 3], [1, 1, 3, 3]])
    y = np.array([1, 2, 1, 2, 3, 1, 2, 2, 3, 1])
    my_tree = ID3Tree(max_depth=1000, min_samples_split=2)
    my_tree.fit(X, y)
    dot = plot_tree(my_tree.root)
    print(dot.source)
    dot.render('id3_tree', format='png', view=True)
