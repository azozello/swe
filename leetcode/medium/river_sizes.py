def get_river_size() -> [int]:
    river_sizes = []
    visited = {}

    rows_count = len(matrix)
    cols_count = len(matrix[0])

    def get_neighbours(cur_i: int, cur_j: int):
        neighbours = []
        vectors = [[cur_i - 1, cur_j], [cur_i, cur_j + 1], [cur_i + 1, cur_j], [cur_i, cur_j - 1]]

        for v in vectors:
            temp_i, temp_j = v

            if 0 <= temp_i < rows_count and 0 <= temp_j < cols_count and \
                    matrix[temp_i][temp_j] == 1 and visited.get((temp_i, temp_j)) is None:
                neighbours.append([temp_i, temp_j])

        return neighbours

    def swim_with_dfs(cell_i, cell_j, river_nodes):
        visited[(cell_i, cell_j)] = True
        river_nodes.add((cell_i, cell_j))

        neighbours = get_neighbours(cell_i, cell_j)
        for n in neighbours:
            swim_with_dfs(n[0], n[1], river_nodes)

        return river_nodes

    for i in range(rows_count):
        for j in range(cols_count):
            if matrix[i][j] == 1 and visited.get((i, j)) is None:
                river_sizes.append(len(swim_with_dfs(i, j, set())))

    return river_sizes


if __name__ == '__main__':
    matrix = [
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1]
    ]

    print(get_river_size())
