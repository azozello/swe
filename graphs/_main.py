# Basic types of Graphs:
#
#   1) Undirected graph                 (u, v)
#   2) Directed graph (Digraph)         (u, v)
#   3) Weighted/unweighted graph        (u, v, w)
#   4) Connected/not connected graph    (u, v)

# Special type of graphs:
#
#   1) Tree - undirected graph with no cycles. Connected graph with N nodes and N-1 edges.
#   2) Rooted Tree - a directed tree with designated root node where each node either points
#       away from the root (out-tree) or towards to the root (in-tree)
#   3) Directed acyclic graphs (DAG)
#   4) Bipartite graph. There is no odd length cycle in it. Such a graph,
#       whose vertices can be split in two independent groups U, V such that every edge connects between U and V
#   5) Complete graph - there is a unique edge between every pair of nodes.

# Representations of Graph:
#
#   1) Adjacency Matrix - matrix where m[i][j] indicates weight of edge (i, j)
#                Pros                                    Cons
#       Space efficient for dense graphs            Requires O(V^2) space
#       Edge weight look-up time is O(1)            Iteration over all edges takes O(V^2) time
#
#   2) Adjacency List - a nap from node to list of edges.
#                Pros                                    Cons
#       Space efficient for spare graphs            Less space efficient for dense graph
#       Iterating over all edges is efficient       Edge weight look-up is 0(E)
#
#   3) Edge list - unordered list of all edges.

# Common problems in graph theory
#
#   1) Shortest path in weighted graph. Solution: BFS (unweighted), Dijkstra, Bellman-Ford, Floyd-Warshall, A* ...
#   2) Path existence (connectivity). Solutions: DFS, union find data structure.
#   3) (Cycle ?) Negative cycle in weighted directed graph. Bellman-Ford, Floyd-Warshall.
#   4) Strongly connected components (SCCs) -
#       self-contained cycle within a directed graph where
#       every vertex in a cycle can reach any other node in the same cycle.
#       Solution: Tarjan`s, Kosajaru`s.
#   5) Traveling Salesman Problem. Solution: Held-Karp. (NP-hard)
#   6) Bridge / cut edge finding problem.
#   7) Articulation points / cut vertex finding problem.
#   8) Minimum spanning tree (MST) finding problem. MSP - subset of he edges of connected weighted graph that
#       connects all the vertices together, without any cycles and ith the minimum possible total edge weight.
#       Solution: Kruskal`s, Prim`s.
#   9) Network flow: max flow.  Solution: Ford-Fulkerson, Edmonds-Karp.

# Algorithms:
#
#   1) Deep First Search (DFS). [dfs.py]
#       Time complexity of graph traversal is O(V + E). Space complexity is O(V).
#       Use-cases:
#           Find Connected Components.
#           Compute MT.
#           Find cycles.
#           Check if graph is bipartite.
#           Find Strongly Connected Components.
#           Topologically sort nodes.
#           Find bridges and articulation points.
#           Find augmenting path in network flow.
#           Generate maze.
#
#   2) Breadth First Search (BFS). [bfs.py]
#       Time complexity is O(V + E). Space complexity is O(V)
#       Use-cases:
#           Find shortest path on unweighted graph.
