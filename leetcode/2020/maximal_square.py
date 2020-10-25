def check_square(matrix: [[int]], size: int, c_i: int, c_j: int) -> bool:
    still_valid = True

    for i in range(c_i, c_i + size):
        for j in range(c_j, c_j + size):
            still_valid = still_valid and matrix[i][j] == '1'

    return still_valid


def find_max_square_brute_force(matrix: [[int]]) -> int:
    if len(matrix) < 1 or len(matrix[0]) < 1:
        return 0

    rows, columns = [len(matrix), len(matrix[0])]

    found_size = 0

    while found_size < min(rows, columns):
        desired_size = found_size + 1
        found = False

        i, j = [0, 0]
        while i <= rows - desired_size and not found:
            j = 0
            while j <= columns - desired_size and not found:
                found = check_square(matrix, desired_size, i, j)
                j += 1
            i += 1

        if not found:
            break
        else:
            found_size += 1

    return found_size * found_size


def get_new_cell_value(matrix: [[int]], c_i: int, c_j: int) -> int:
    left = matrix[c_i - 1][c_j] if c_i - 1 >= 0 else 0
    top = matrix[c_i][c_j - 1] if c_j - 1 >= 0 else 0
    diagonal = matrix[c_i - 1][c_j - 1] if c_i - 1 >= 0 and c_j - 1 >= 0 else 0

    return min(min(left, top), diagonal) + 1 if matrix[c_i][c_j] > 0 else 0


def find_max_square(matrix: [[int]]) -> int:
    rows = len(matrix)
    columns = len(matrix[0]) if rows > 0 else 0

    dp = [[int(matrix[i][j]) for j in range(columns)] for i in range(rows)]
    current_max = 0

    if rows < 2 or columns < 2:
        for i in range(rows):
            for j in range(columns):
                current_max = max(current_max, dp[i][j])

    else:
        for i in range(rows):
            for j in range(columns):
                dp[i][j] = get_new_cell_value(dp, i, j)
                current_max = max(current_max, dp[i][j])

    return current_max * current_max


if __name__ == '__main__':
    world = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    # world = [[]]

    print(find_max_square(world))
