def solve(matrix: [[int]], r: int, c: int) -> int:
    cost = 0

    for i in range(r):
        line = ''
        for j in range(c):
            line += f'{matrix[r - (i + 1)][j]} '
        print(line)

    return cost


if __name__ == '__main__':
    print('Max Of Min Altitudes')

    source_matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    solve(source_matrix, 3, 3)
