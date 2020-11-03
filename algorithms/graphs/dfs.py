from collections import defaultdict


def recursive_dfs(graph: {int: [int]}, visited: {int: bool}, vertex: int, logic=lambda x: x):
    if visited.get(vertex) is not None:
        return

    visited[vertex] = True
    logic(vertex)
    neighbours = [v for v in graph[vertex] if visited.get(v) is None]

    for n in neighbours:
        recursive_dfs(graph, visited, n, logic)


def iterative_dfs(graph: {int: [int]}, visited: {int: bool}, logic=lambda x: x):
    for vertex in graph:
        neighbours = [v for v in graph[vertex] if visited.get(v) is None]
        for n in neighbours:
            logic(vertex)
            visited[n] = True


def find_connected_components(graph: {int: [int]}) -> {int: [int]}:
    visited = {}
    count = 0
    components = {}

    for vertex in graph:
        if visited.get(vertex) is None:
            components[count] = []
            recursive_dfs(graph, visited, vertex, lambda x: components[count].append(x))
            count += 1

    return components


def find_component_dfs(start: int, graph: {int: [int]}, visited: {int: bool}, logic=lambda x: x):
    neighbours = [v for v in graph[start] if visited.get(v) is None]
    for n in neighbours:
        logic(start)
        visited[n] = True
        find_component_dfs(n, graph, visited, logic)


def find_connected_components_iteratively(graph: {int: [int]}) -> {int: [int]}:
    visited = {}
    count = 0
    components = defaultdict(list)

    for vertex in graph:
        if visited.get(vertex) is None:
            visited[vertex] = True
            find_component_dfs(vertex, graph, visited, lambda x: components[count].append(x))
            count += 1

    return components


if __name__ == '__main__':
    # Graphs represented by Adjacency List.
    connected_graph_adjacency_list = {
        0: [9],
        1: [0],
        2: [],
        3: [2, 4, 5],
        4: [],
        5: [6],
        6: [7],
        7: [3, 10],
        8: [1, 7],
        9: [8],
        10: [11],
        11: [7],
    }
    not_connected_graph_adjacency_list = {
        0: [8],
        1: [5],
        2: [9],
        3: [9],
        4: [0],
        5: [16, 17],
        6: [7],
        7: [11],
        8: [4, 14],
        9: [15, 3],
        10: [],
        11: [6],
        12: [],
        13: [0],
        14: [0, 13],
        15: [10, 2],
        16: [],
        17: [],
    }

    processed_recursively = {}
    processed_iteratively = {}

    recursive_dfs(connected_graph_adjacency_list, processed_recursively, 0)
    iterative_dfs(connected_graph_adjacency_list, processed_iteratively)

    print(len(connected_graph_adjacency_list))
    print(len(processed_recursively))
    print(len(processed_iteratively))

    connected_components = find_connected_components(not_connected_graph_adjacency_list)
    connected_components_it = find_connected_components_iteratively(not_connected_graph_adjacency_list)

    for k in connected_components.keys():
        print(k, connected_components[k])

    for k in connected_components_it.keys():
        print(k, connected_components[k])
