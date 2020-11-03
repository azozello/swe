from queue import PriorityQueue


def prim_mst(graph: [[int]], size: int, entrance=0):
    queue = PriorityQueue()
    visited = [False for i in range(size)]
    mst_edges = []
    final_cost = 0

    queue.put((0, entrance, entrance))

    while not queue.empty() and len(mst_edges) < size:
        cost, start, end = queue.get()

        if visited[end]:
            continue

        visited[end] = True

        if start != end:
            mst_edges.append([start, end])
            final_cost += cost

        for neighbour in graph[end]:
            n_const, n_end = neighbour
            if not visited[n_end]:
                queue.put([n_const, end, n_end])

    return mst_edges, final_cost


# Time complexity - O(E logV)
if __name__ == '__main__':
    graph_adjacency_list = [
        [(10, 1), (1, 2), (4, 3)],
        [(10, 0), (0, 4), (3, 2)],
        [(1, 0), (3, 1), (8, 5), (2, 3)],
        [(4, 0), (2, 2), (2, 5), (7, 6)],
        [(0, 1), (1, 5), (8, 7)],
        [(1, 4), (8, 2), (2, 3), (6, 6), (9, 7)],
        [(7, 3), (6, 5), (12, 7)],
        [(8, 4), (9, 5), (12, 6)],
    ]

    print(prim_mst(graph_adjacency_list, len(graph_adjacency_list)))
