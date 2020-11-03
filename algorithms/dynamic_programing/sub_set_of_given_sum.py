def find_subset(source: [int], target: int):
    rows = len(source) + 1
    columns = target + 1

    memory = [[c < 1 for c in range(columns)] for r in range(rows)]

    for i in range(1, rows):
        for j in range(1, columns):
            memory[i][j] = source[i - 1] == j or memory[i - 1][j] or memory[i - 1][j - source[i - 1]]

    return memory[rows - 1][target]


if __name__ == '__main__':
    source_set = [3, 4, 5, 2]
    desired_sum = 6

    print(find_subset(source_set, desired_sum))
