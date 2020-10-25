def group(sizes: [int]) -> [[int]]:
    result = []
    groups_map = {}

    def check_full():
        if len(groups_map.get(size)) == size:
            result.append(groups_map.get(size))
            groups_map[size] = []

    for index, size in enumerate(sizes):
        if groups_map.get(size) is None:
            groups_map[size] = [index]
            check_full()
        else:
            groups_map[size].append(index)
            check_full()

    return result


if __name__ == '__main__':
    group_sizes = [2, 1, 3, 3, 3, 2]
    print(group(group_sizes))
