def dfs(graph: [[int]], curr: int, prev: int, bridges: [int], visited: [int], lows: [int], ids: [int], prev_id: int):
    visited[curr] = True
    prev_id += 1
    lows[curr] = prev_id
    ids[curr] = prev_id

    for target in graph[curr]:
        if target == prev:
            continue
        if not visited[target]:
            dfs(graph, target, curr, bridges, visited, lows, ids, prev_id)
            lows[curr] = min(lows[curr], lows[target])
            if ids[curr] < lows[target]:
                bridges.append([curr, target])
        else:
            lows[curr] = min(lows[curr], ids[target])


def find_bridges(graph: [[int]], size: int):
    bridges = []
    ids = [0 for i in range(size)]
    low_links = [0 for i in range(size)]
    visited = [False for i in range(size)]

    for v in range(size):
        if not visited[v]:
            dfs(graph, v, -1, bridges, visited, low_links, ids, -1)

    return bridges


if __name__ == '__main__':
    adjacency_list = [
        [1],
        [2],
        [0, 3, 5],
        [4],
        [],
        [6],
        [7],
        [8],
        [5],
    ]

    print(find_bridges(adjacency_list, len(adjacency_list)))
