import queue


def bfs(graph: {int: []}, _queue: queue.Queue, visited: {int: [int]}, start: int, logic=lambda x: x):
    def put_neighbours(node: int):
        for v in [v for v in graph[node] if visited.get(v) is None]:
            _queue.put(v)
            visited[v] = True

    _queue.put(start)
    visited[start] = True

    while not _queue.empty():
        vertex = _queue.get()
        logic(vertex)
        put_neighbours(vertex)


def find_path(rows: int, columns: int, maze: [[int]], start_position):
    def get_neighbours(position):
        i_v = [-1, +1, 0, 0]
        j_v = [0, 0, +1, -1]

        neighbours = [(position[0] + i_v[d], position[1] + j_v[d]) for d in range(4)
                      if 0 <= position[0] + i_v[d] < rows and 0 <= position[1] + j_v[d] < columns
                      and maze[position[0]][position[1]] != '#']
        return neighbours

    order_queue = queue.Queue()
    visited = {start_position: True}

    moves_count = 0
    nodes_left_in_layer = 1
    nodes_in_next_layer = 1

    order_queue.put(start_position)

    while not order_queue.empty():
        current_position = order_queue.get()

        if maze[current_position[0]][current_position[1]] == 'E':
            return moves_count

        nodes_left_in_layer -= 1
        if nodes_left_in_layer == 0:
            nodes_left_in_layer = nodes_in_next_layer
            nodes_in_next_layer = 0
            moves_count += 1

        for n in get_neighbours(current_position):
            if visited.get(n) is None:
                order_queue.put(n)
                visited[n] = True
                nodes_in_next_layer += 1

    get_neighbours(start_position)


def print_maze(rows: int, columns: int, maze: [[int]]):
    for i in range(rows):
        line = ''
        for j in range(columns):
            line += f'{maze_matrix[i][j]} '
        print(line)


if __name__ == '__main__':
    graph_adjacency_list = {
        0: [7, 9, 11],
        1: [8, 10],
        2: [12, 3],
        3: [2, 4, 7],
        4: [3],
        5: [6],
        6: [5, 7],
        7: [3, 6, 11],
        8: [1, 9, 12],
        9: [8, 10],
        10: [1, 9],
        11: [7],
        12: [8, 2]
    }
    visit_queue = queue.Queue()
    visited_vertices = {}
    # bfs(graph_adjacency_list, visit_queue, visited_vertices, 0, lambda x: print(x))

    rows_count, cols_count = [5, 7]
    maze_matrix = [
        ['S', '.', '.', '#', '.', '.', '.'],
        ['.', '#', '.', '.', '.', '#', '.'],
        ['.', '#', '.', '.', '.', '.', '.'],
        ['.', '.', '#', '#', '.', '.', '.'],
        ['#', '.', '#', 'E', '.', '#', '.'],
    ]
    #
    # print_maze(rows_count, cols_count, maze_matrix)
    print(find_path(rows_count, cols_count, maze_matrix, (0, 0)))
    # print_maze(rows_count, cols_count, maze_matrix)
