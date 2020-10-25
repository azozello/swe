from queue import PriorityQueue
import functools


def minimum_cost(number: int, connections: [[str, str, int]]):
    adjacency_map = {}
    mst = []
    visited = set()

    for start, end, cost in connections:
        if adjacency_map.get(start) is None:
            adjacency_map[start] = [(end, cost)]
        else:
            adjacency_map[start] += [(end, cost)]

        if adjacency_map.get(end) is None:
            adjacency_map[end] = [(start, cost)]
        else:
            adjacency_map[end] += [(start, cost)]

    queue = PriorityQueue()

    queue.put((connections[0][2], connections[0][0], connections[0][1]))
    visited.add(connections[0][0])

    while not queue.empty() and len(mst) < len(adjacency_map) - 1:
        cost, start, end = queue.get()

        visited.add(end)

        mst.append([start, end, cost])

        for n_node, n_cost in adjacency_map[end]:
            if n_node not in visited:
                queue.put((n_cost, end, n_node))

    return functools.reduce(lambda acc, cur: acc + cur[2], mst, 0)


if __name__ == '__main__':
    num = 5
    grid = [
        ['A', 'B', 1],
        ['B', 'C', 4],
        ['B', 'D', 6],
        ['D', 'E', 5],
        ['C', 'E', 1]
    ]

    print(minimum_cost(num, grid))
