def find_scc(count: int, adj_list: [[int]]) -> int:
    last_id = 0
    scc_count = 0

    node_ids = [-1 for i in range(count)]
    low_link_values = [0 for i in range(count)]
    is_in_stack = [False for i in range(count)]

    stack = []

    def dfs(current: int, _last_id: int, _count):
        stack.append(current)
        is_in_stack[current] = True

        node_ids[current] = _last_id
        low_link_values[current] = _last_id

        for neighbour in adj_list[current]:
            if node_ids[neighbour] == -1:
                _count = dfs(neighbour, _last_id + 1, _count)

            if is_in_stack[neighbour]:
                low_link_values[current] = min(low_link_values[current], low_link_values[neighbour])

        if node_ids[current] == low_link_values[current]:
            while len(stack) > 0:
                node = stack.pop()
                is_in_stack[node] = False
                low_link_values[node] = node_ids[current]

                if node == current:
                    break

            _count += 1

        return _count

    for i in range(count):
        if node_ids[i] == -1:
            scc_count = dfs(i, last_id, scc_count)

    return scc_count


# Time complexity - O(E + V)
if __name__ == '__main__':
    node_count = 8
    adjacency_list = [
        [1],
        [2],
        [0],
        [0, 2, 4],
        [7],
        [4, 6],
        [5, 7],
        [0, 3]
    ]

    print(find_scc(node_count, adjacency_list))
