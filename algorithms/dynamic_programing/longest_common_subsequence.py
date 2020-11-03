def find_lcs(first: str, second: str):
    rows, columns = [len(first) + 1, len(second) + 1]

    matrix = [[0 for j in range(columns)] for i in range(rows)]

    for i in range(1, rows):
        for j in range(1, columns):
            if i == 0 or j == 0:
                matrix[i][j] = 0
            elif first[i - 1] == second[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])

    return matrix[rows - 1][columns - 1], construct_lcs(matrix, rows, columns, first)


def construct_lcs(matrix: [[int]], rows: int, columns: int, first: str) -> str:
    lcs = ''

    i, j = [rows - 1, columns - 1]

    while i > 0 and j > 0:
        if matrix[i][j] != max(matrix[i - 1][j], matrix[i][j - 1]):
            lcs += first[i - 1]
            i -= 1
            j -= 1
        else:
            if matrix[i][j] == matrix[i - 1][j]:
                i -= 1
            else:
                j -= 1

    return lcs


if __name__ == '__main__':
    first_string = 'GXTXAYB'.upper()
    second_string = 'AGGTAB'.upper()
    print(find_lcs(first_string, second_string))
