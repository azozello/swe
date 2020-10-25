import time


def solve(n: int) -> [[int]]:
    def fill_line(start_index, start_value, length, diagonal_index):
        for i in range(length):
            result_matrix[start_index][start_index + i] = start_value + i
            result_matrix[n - 1 - start_index][n - 1 - i - start_index] = start_value + i + diagonal_index

    def fill_row(start_index, start_value, length, diagonal_index, row_index):
        for i in range(length):
            result_matrix[start_index + i][row_index] = start_value + i
            result_matrix[n - i - start_index - 1][n - row_index - 1] = start_value + i + diagonal_index

    if n == 1:
        return [[1]]
    else:
        result_matrix = [[0 for j in range(n)] for i in range(n)]

        if n % 2 == 1:
            result_matrix[n // 2][n // 2] = n ** 2

        diagonal_index = 0
        start_value = 1

        for line_index in range(n // 2):
            start_index = line_index
            start_value += (diagonal_index * 2)
            diagonal_index = 2 * (n - (line_index * 2) - 1)

            length = n - (line_index * 2)

            fill_line(start_index, start_value, length, diagonal_index)
            fill_row(start_index + 1,
                     start_value + (diagonal_index // 2) + 1,
                     length - 2,
                     diagonal_index,
                     n - 1 - line_index)

        return result_matrix


def print_matrix(target_matrix: [[int]], size: int) -> None:
    max_length = len(str(size ** 2))
    spaces = ''
    for i in range(max_length):
        spaces += ' '

    for i in range(size):
        line = ''
        for j in range(size):
            line += f'{spaces[:max_length - len(str(target_matrix[i][j]))]}{target_matrix[i][j]}  '
        print(line)


if __name__ == '__main__':
    print('Spiral Matrix II')
    SIZE = 7

    start = int(round(time.time() * 1000))
    matrix = solve(SIZE)
    finish = int(round(time.time() * 1000))

    print_matrix(matrix, SIZE)

    print()
    print(f'Time: {finish - start}ms')
