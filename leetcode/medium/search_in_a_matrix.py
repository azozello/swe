def solve(matrix: [[int]], target: int) -> bool:
    def find_index(start_index: int, is_vertical: bool):
        local_index = -1

        coords = [[start_index + j, j] for j in range(length)] if is_vertical \
            else [[j, start_index + j] for j in range(length)]

        for coord in coords:
            if matrix[coord[0]][coord[1]] == target:
                return -2
            elif matrix[coord[0]][coord[1]] > target:
                local_index = min(coord)
                break
        return local_index

    def search_in_square(start_index: int, is_vertical: bool) -> bool:
        index = find_index(start_index, is_vertical)

        if index == -1:
            return False
        elif index == -2:
            return True
        else:
            if is_vertical:
                for j in range(index):
                    if matrix[start_index + index][j] == target or matrix[start_index + j][index] == target:
                        return True
            else:
                for j in range(index):
                    if matrix[index][start_index + j] == target or matrix[j][start_index + index] == target:
                        return True

        return False

    def search_in_line(start_index: int, is_vertical: bool) -> bool:
        line = [matrix[start_index][j] for j in range(length)] if is_vertical \
            else [matrix[j][start_index] for j in range(length)]

        if line[length - 1] == target:
            return True
        elif line[length - 1] < target:
            return False
        else:
            return target in line

    n = len(matrix[0])
    m = len(matrix)

    length = min([n, m])
    squares = n // m if n > m else m // n
    lines = n % m if n > m else m % n
    vertical = m > n

    for i in range(squares):
        found = search_in_square(i * length, vertical)
        if found:
            return True

    for i in range(lines):
        found = search_in_line(i + (squares * length), vertical)
        if found:
            return True

    return False


if __name__ == '__main__':
    print('Search a 2D Matrix II')
    test_matrix = [
        [1, 4, 7, 11, 15, 16],  # n
        [2, 5, 8, 12, 19, 21],
        [3, 6, 9, 16, 22, 25],
        [10, 13, 14, 17, 24, 35],
        [18, 21, 23, 26, 30, 37]
    ]  # m

    print(solve(test_matrix, 5))
    print(solve(test_matrix, 20))
    print(solve(test_matrix, 35))
