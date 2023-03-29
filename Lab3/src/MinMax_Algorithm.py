# author: Jan Kwiatkowski

#pseudokod algorytmu
def minmax(node, depth, maximizing_player):
    if depth == 0 or node.is_terminal():
        return node.heuristic_value()
    if maximizing_player:
        best_value = float('-inf')
        for child_node in node.children():
            value = minmax(child_node, depth - 1, False)
            best_value = max(best_value, value)
        return best_value
    else:  # minimizing player
        best_value = float('inf')
        for child_node in node.children():
            value = minmax(child_node, depth - 1, True)
            best_value = min(best_value, value)
        return best_value