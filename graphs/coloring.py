import networkx as nx
from time import time
import matplotlib.pyplot as plt

from enum import Enum


class Color(Enum):
    BLUE = "b"
    GREEN = "g"
    RED = "r"
    CYAN = "c"
    MAGENTA = "m"
    YELLOW = "y"
    BLACK = "k"
    WHITE = "w"


class Node:
    def __init__(self, color=None, value=0, neighbours=None):
        self.value = value
        self.color = color
        self.color_index = 0
        self.neighbours = neighbours
        self.neighbours_count = 0 if neighbours is None else len(neighbours)


def get_neighbours(i, j):
    horizontal = []
    vertical = []
    if i > 0:
        horizontal.append(i - 1)
    if i < SIZE - 1:
        horizontal.append(i + 1)
    if j > 0:
        vertical.append(j - 1)
    if j < SIZE - 1:
        vertical.append(j + 1)

    return get_neighbours_direction(i, j, horizontal, vertical)


def get_neighbours_direction(i, j, horizontal, vertical):
    result = []
    for f_i in horizontal:
        if f_i < i:
            result.append({'i': f_i, 'j': j})
        elif f_i > i:
            result.append({'i': f_i, 'j': j})

    for f_j in vertical:
        if f_j < j:
            result.append({'i': i, 'j': f_j})
        elif f_j > j:
            result.append({'i': i, 'j': f_j})

    return result


def print_graph(graph_nodes):
    edges_array = []
    colors_map = {}

    for i in range(SIZE):
        for j in range(SIZE):
            colors_map[graph_nodes[i][j].value] = graph_nodes[i][j].color
            for n in get_neighbours(i, j):
                edges_array.append((graph_nodes[i][j].value, graph_nodes[n['i']][n['j']].value))

    G = nx.DiGraph()
    G.add_edges_from(edges_array)

    black_edges = [edge for edge in G.edges()]

    pos = nx.spring_layout(G)

    colors = [colors_map[node] for node in G]

    nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_color=colors, node_size=500)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=False)
    plt.show()


def set_up_nodes():
    new_nodes = []
    index = 1

    for i in range(SIZE):
        new_nodes.append([])
        for j in range(SIZE):
            new_nodes[i].append(Node(color=str(Color.WHITE.value), neighbours=[], value=index))
            index += 1

    return new_nodes


def connect_nodes(nodes):
    for i in range(SIZE):
        for j in range(SIZE):
            for neighbour in get_neighbours(i, j):
                nodes[i][j].neighbours.append(nodes[neighbour['i']][neighbour['j']])


def color(rec_index, iter_took):
    temp_node = nodes_matrix[rec_index // SIZE][rec_index % SIZE]
    if temp_node.color == Color.WHITE.value:
        temp_node.color = max_colors[temp_node.color_index]
    check_value = check(temp_node)
    if check_value is True and rec_index == (SIZE * SIZE) - 1:  # solved condition
        return True, iter_took
    elif rec_index <= 0 and temp_node.color_index == max_color_index:  # can not be solved condition
        return False, iter_took
    else:  # not solved yet
        if check_value is False and temp_node.color_index < max_color_index:  # use next color
            temp_node.color = max_colors[temp_node.color_index + 1]
            temp_node.color_index = temp_node.color_index + 1
            return color(rec_index, iter_took + 1)
        elif check_value is False and temp_node.color_index == max_color_index:  # backtrack
            return color(rec_index - 1, iter_took + 1)
        elif check_value is True:  # go to next node
            return color(rec_index + 1, iter_took + 1)


def check(node):
    for n in node.neighbours:
        if n.color == node.color and n.color != Color.WHITE:
            return False
    return True


if __name__ == '__main__':
    color_list = ["r", "b", "g", "r", "c", "m", "y", "k", "w"]
    SIZE = 4

    max_colors = color_list[:5]
    max_color_index = len(max_colors) - 1

    nodes_matrix = set_up_nodes()
    connect_nodes(nodes_matrix)

    start_time = int(round(time() * 1000))
    print(color(0, 0))
    end_time = int(round(time() * 1000))

    print(end_time - start_time)

    print_graph(nodes_matrix)
