from graphs.topological_sort import top_sort
import copy


def find_shortest(graph: {str: {str: int}}, costs: {str: int}, order: [str], start: str):
    costs[start] = 0

    for v in order:
        for n in graph[v]:
            if costs[n] == -1 or costs[n] > costs[v] + graph[v][n]:
                costs[n] = costs[v] + graph[v][n]


def find_longest(graph: {str: {str: int}}, costs: {str: int}, order: [str], start: str):
    graph_c = copy.deepcopy(graph)

    for v in graph_c:
        for n in graph_c[v]:
            graph_c[v][n] = -1 * graph_c[v][n]

    find_shortest(graph_c, costs, order, start)

    for v in costs:
        costs[v] = -1 * costs[v]


# Time complexity O(E + V) in DAG
if __name__ == '__main__':
    adjacency_list_w = {
        'A': {'B': 3, 'C': 6},
        'B': {'C': 4, 'D': 4, 'E': 11},
        'C': {'D': 8, 'G': 11},
        'D': {'E': -4, 'F': 5, 'G': 2},
        'E': {'H': 9},
        'F': {'H': 1},
        'G': {'H': 2},
        'H': {}
    }
    adjacency_list_uw = {v: [v_i for v_i in adjacency_list_w[v]] for v in adjacency_list_w}
    v_order = [v for v in top_sort(adjacency_list_uw, {}, '', '')]
    shortest = {v: -1 for v in v_order}
    longest = {v: -1 for v in v_order}

    find_shortest(adjacency_list_w, shortest, v_order, 'A')
    find_longest(adjacency_list_w, longest, v_order, 'A')

    print(shortest)
    print(longest)
