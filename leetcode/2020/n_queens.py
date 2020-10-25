from collections import deque
from time import time


def show_map(desk: [[int]]) -> None:
    def get_sign(number: int) -> chr:
        if number == 0:
            return '_'
        elif number == -1:
            return '*'
        else:
            return 'X'

    rows = len(desk)
    columns = len(desk[0]) if rows > 0 else 0

    for i in range(rows):
        line = '|'
        numbers = ''
        for j in range(columns):
            line += f'{get_sign(desk[i][j])}|'
            numbers += f'{desk[i][j]} '
        print(f'{line}    {numbers}')
    print()


def get_possible(size: int, desk: [[int]]) -> [int]:
    possible = set()

    for i in range(size):
        for j in range(size):
            if desk[i][j] == 0:
                possible.add(tuple([i, j]))

    return possible


def mark_fields(size: int, desk: [[int]], q_i: int, q_j: int, blocking=True):
    desk[q_i][q_j] += 1 if blocking else -1

    # Block column
    for i in range(size):
        if i != q_i:
            desk[i][q_j] += 1 if blocking else -1

    # Block row
    for j in range(size):
        if j != q_j:
            desk[q_i][j] += 1 if blocking else -1

    # Block main diagonal
    for i in range(size):
        for j in range(size):
            if i - j == q_i - q_j and (i != q_i and j != q_j):
                desk[i][j] += 1 if blocking else -1

    # Block secondary diagonal
    for i in reversed((range(q_i))):
        for j in range(q_j, size):
            if (j - q_j == q_i - i) and (i != q_i and j != q_j):
                desk[i][j] += 1 if blocking else -1

    t_i, t_j = [q_i, q_j]
    while t_i < size and t_j >= 0:
        if t_i != q_i and t_j != q_j:
            desk[t_i][t_j] += 1 if blocking else -1
        t_i += 1
        t_j -= 1


def place_queens(queens: int, desk: [[int]], path, left_to_place: int):
    possible = get_possible(queens, desk)

    # end condition
    if left_to_place == 0:
        return path

    elif len(possible) == 0:
        return -1

    # Next step
    else:
        for p in possible:
            next_i, next_j = p
            mark_fields(queens, desk, next_i, next_j)
            path.append(tuple([next_i, next_j]))

            result = place_queens(queens, desk, path, left_to_place - 1)

            if result != -1:
                return result

            # backtrack
            else:
                path.pop()
                mark_fields(queens, desk, next_i, next_j, False)

        return -1


if __name__ == '__main__':
    matrix = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]
    show_map(matrix)
    start = int(round(time() * 1000))
    solution = place_queens(8, matrix, deque(), 8)
    print(f'It took: {int(round(time() * 1000)) - start}ms')
    print()

    if solution != -1:
        for _i, _j in solution:
            matrix[_i][_j] = -1
    else:
        print('AAA')

    show_map(matrix)
# 3
