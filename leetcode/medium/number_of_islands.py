def solve(grid: [[str]]) -> int:
    def expand_island(island, expanded):
        visited_islands[island] = 1
        expanded.append(island)
        for neighbour in get_neighbours(island):
            expand_island(neighbour, expanded)

    def get_neighbours(island):
        neighbours = []

        if island[0] > 0 and grid[island[0] - 1][island[1]] == 1 and (island[0] - 1, island[1]) not in visited_islands:
            neighbours.append((island[0] - 1, island[1]))

        if island[0] < m - 1 and grid[island[0] + 1][island[1]] == 1 and (
                island[0] + 1, island[1]) not in visited_islands:
            neighbours.append((island[0] + 1, island[1]))

        if island[1] > 0 and grid[island[0]][island[1] - 1] == 1 and (island[0], island[1] - 1) not in visited_islands:
            neighbours.append((island[0], island[1] - 1))

        if island[1] < n - 1 and grid[island[0]][island[1] + 1] == 1 and (
                island[0], island[1] + 1) not in visited_islands:
            neighbours.append((island[0], island[1] + 1))

        return neighbours

    possible_islands = {}
    visited_islands = {}
    island_count = 0

    n = len(grid[0])
    m = len(grid)

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                possible_islands[(i, j)] = 1

    for coords in possible_islands:
        if coords not in visited_islands:
            island_count += 1
            expand_island(coords, [])

    return island_count


if __name__ == '__main__':
    print('Number of Islands')

    source_map = [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1]
    ]

    print(solve(source_map))
