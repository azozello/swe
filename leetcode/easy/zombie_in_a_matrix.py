def solve(field: [[int]]) -> int:
    def update_neighbours(c_i: int, c_j: int, last_updated: {(int, int): int}) -> int:
        added_cells = 0

        if c_i - 1 >= 0 and field[c_i - 1][c_j] == 0:
            last_updated[(c_i - 1, c_j)] = 1
            field[c_i - 1][c_j] = 1
            added_cells += 1

        if c_i + 1 < m and field[c_i + 1][c_j] == 0:
            last_updated[(c_i + 1, c_j)] = 1
            field[c_i + 1][c_j] = 1
            added_cells += 1

        if c_j - 1 >= 0 and field[c_i][c_j - 1] == 0:
            last_updated[(c_i, c_j - 1)] = 1
            field[c_i][c_j - 1] = 1
            added_cells += 1

        if c_j + 1 < n and field[c_i][c_j + 1] == 0:
            last_updated[(c_i, c_j + 1)] = 1
            field[c_i][c_j + 1] = 1
            added_cells += 1

        return added_cells

    hours_took = 0
    cells_taken = 0

    m = len(field)
    n = len(field[0])

    print(f'n{n} : m{m}')

    print_matrix(field)
    print()

    for i in range(m):
        for j in range(n):
            if field[i][j] == 1:
                cells_taken += 1
    while cells_taken < n * m:
        last_taken = {}
        for i in range(m):
            for j in range(n):
                if field[i][j] == 1 and last_taken.get((i, j)) is None:
                    cells_taken += update_neighbours(i, j, last_taken)
        print_matrix(field)
        print()
        hours_took += 1

    return hours_took


def print_matrix(matrix: [[int]]):
    for i in range(len(matrix)):
        line = ''
        for j in range(len(matrix[0])):
            line += f'{matrix[i][j]} '
        print(line)


if __name__ == '__main__':
    print('Zombie in Matrix')

    start_matrix = [
        [0, 1, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0]
    ]

    print(solve(start_matrix))
