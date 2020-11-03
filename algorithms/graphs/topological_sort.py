def recursive_dfs_with_path(graph: {str: [str]}, visited: {str}, current_node: str, path: str, order: str) -> str:
    neighbours = [v for v in graph[current_node] if visited.get(v) is None]
    visited[current_node] = True

    if len(path) == len(neighbours) == 0:  # stop condition
        order += current_node
        return order

    elif len(path) != 0 and len(neighbours) == 0:  # backtrack condition
        order += current_node
        return recursive_dfs_with_path(graph, visited, path[len(path) - 1], path[:-1], order)

    else:  # next step
        path += current_node
        return recursive_dfs_with_path(graph, visited, neighbours[0], path, order)


def top_sort(graph: {str: [str]}, visited: {str}, path: str, order: str) -> str:
    for v in graph:
        if visited.get(v) is None:
            order = recursive_dfs_with_path(graph, visited, v, path, order)

    return order[::-1]


# Can only be applied for DAG`s
# Every tree has a topological order
# Time complexity - O(E + V)
if __name__ == '__main__':
    graph_adjacency_list = {
        'H': ['J', 'I'],  # start from H
        'A': ['D'],
        'B': ['D'],
        'C': ['A', 'B'],
        'D': ['H', 'G'],
        'E': ['A', 'D', 'F'],
        'F': ['K', 'J'],
        'G': ['I'],
        'I': ['L'],
        'J': ['L', 'M'],
        'K': ['J'],
        'L': [],
        'M': [],
    }

    print(top_sort(graph_adjacency_list, {}, '', ''))
