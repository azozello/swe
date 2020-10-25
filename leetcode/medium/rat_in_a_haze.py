def solve(matrix: [[int]]) -> [str]:
    def get_possible(path: str, index: int) -> [int]:
        cur_i = index // SIZE
        cur_j = index % SIZE
        possible = []

        if used.get(path + chr(index + 65)) is None:
            used[path + chr(index + 65)] = []

        if cur_i + 1 < SIZE and index + SIZE not in used[path + chr(index + 65)] and matrix[cur_i + 1][cur_j] == 1:
            possible.append(index + SIZE)
        if cur_i - 1 >= 0 and index - SIZE not in used[path + chr(index + 65)] and matrix[cur_i - 1][cur_j] == 1:
            possible.append(index - SIZE)
        if cur_j + 1 < SIZE and index + 1 not in used[path + chr(index + 65)] and matrix[cur_i][cur_j + 1] == 1:
            possible.append(index + 1)
        if cur_j - 1 >= 0 and index - 1 not in used[path + chr(index + 65)] and matrix[cur_i][cur_j - 1] == 1:
            possible.append(index - 1)

        if len(path) > 0:
            last_index = ord(path[-1:]) - 65
            passed = [ord(c) - 65 for c in path]
            possible = [i for i in possible if i != last_index and i not in passed]

        return possible

    def find_path(path: str, index: int) -> None:
        cur_possible = get_possible(path, index)
        if len(cur_possible) == index == 0:  # stop condition
            return
        elif len(cur_possible) == 0:  # backtrack condition
            if index == 15:
                found_paths.append(f"{path}{chr(index + 65)}")

            last_cell_index = ord(path[-1:]) - 65
            return find_path(path[:len(path) - 1], last_cell_index)
        else:  # next step
            used[path + chr(index + 65)].append(cur_possible[0])
            return find_path(f"{path}{chr(index + 65)}", cur_possible[0])

    used = {}
    found_paths = []
    find_path('', 0)
    return found_paths


def print_path(path: str):
    field = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    for c in path:
        field[(ord(c) - 65) // SIZE][(ord(c) - 65) % SIZE] = 1

    for i in range(SIZE):
        line = ''
        for j in range(SIZE):
            line += str(field[i][j])
        print(line)


if __name__ == '__main__':
    print('Rat in a haze')
    SIZE = 4
    source_matrix = [
        [1, 0, 0, 0],
        [1, 1, 0, 0],
        [1, 1, 0, 0],
        [0, 1, 1, 1]
    ]
    for found_path in solve(source_matrix):
        print(found_path)
        print_path(found_path)
        print()
