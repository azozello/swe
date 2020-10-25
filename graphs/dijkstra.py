def solve(graph_matrix: [[int]]) -> [int]:
    def get_next():
        closest = [i for i in range(SIZE) if i not in visited][0]
        for i in range(SIZE):
            if 0 < unvisited[i] < unvisited[closest] and i not in visited:
                closest = i
        return closest

    unvisited = [0 if i == 0 else -1 for i in range(SIZE)]
    visited = []
    path = ''

    while len(visited) < 5:
        current_node = get_next()
        path += chr(current_node + 65)
        visited.append(current_node)
        for i in range(SIZE):
            if graph_matrix[current_node][i] != -1 and i not in visited and \
                    (unvisited[i] == -1 or unvisited[i] > unvisited[current_node] + graph_matrix[current_node][i]):
                unvisited[i] = unvisited[current_node] + graph_matrix[current_node][i]

    print(path)
    return unvisited


# Time complexity O(E * log(V)) or  O((E + V) log(V)) with binary heap implementation of priority queue.
if __name__ == '__main__':
    print('Dijkstra`s algorithm')

    graph_1 = [
        [0, 6, -1, 1, -1],  # a
        [6, 0, 5, 2, 2],  # b
        [-1, 5, 0, -1, 5],  # c
        [1, 2, -1, 0, 1],  # d
        [-1, 2, 5, 1, 0],  # e
    ]
    graph_2 = [
        [0, 7, 9, -1, -1, 5],  # 0
        [7, 0, 10, 15, -1, -1],  # 1
        [9, 10, 0, 11, -1, 2],  # 2
        [-1, 15, 11, 0, 6, -1],  # 3
        [-1, -1, -1, 6, 0, 9],  # 4
        [5, -1, 2, -1, 9, 0]  # 5
    ]
    graph_3 = [
        [0, 23, 12, -1, -1, -1, -1, -1],  # 1
        [23, 0, 25, -1, 22, -1, -1, 35],  # 2
        [12, 25, 0, 18, -1, -1, -1, -1],  # 3
        [-1, -1, 18, 0, -1, 20, -1, -1],  # 4
        [-1, 22, -1, -1, 0, 23, 14, -1],  # 5
        [-1, -1, -1, 20, 23, 0, 24, -1],  # 6
        [-1, -1, -1, -1, 14, 24, 0, 16],  # 7
        [-1, 35, -1, -1, -1, -1, 16, 0],  # 8
    ]

    SIZE = len(graph_1)

    print(solve(graph_1))
