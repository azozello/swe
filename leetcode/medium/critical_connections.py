def solve(edge_count: int, edges: [[int]]) -> [[int]]:
    def generate_vertexes():
        result = {}

        for edge in edges:
            if result.get(edge[0]) is not None:
                result[edge[0]].append(edge[1])
            else:
                result[edge[0]] = [edge[1]]

            if result.get(edge[1]) is not None:
                result[edge[1]].append(edge[0])
            else:
                result[edge[1]] = [edge[0]]

        return result

    def find_cycle(prev: int, current: int, path: str):
        if chr(current + 64) in path:
            cycle = path[path.index(chr(current + 64)):]
            for i in range(len(cycle) - 1):
                if [ord(cycle[i]) - 64, ord(cycle[i + 1]) - 64] in edges:
                    edges.remove([ord(cycle[i]) - 64, ord(cycle[i + 1]) - 64])
        else:
            connected = [vertex for vertex in vertexes[current] if vertex != prev]
            if len(connected) == 0:
                return
            else:
                for c in connected:
                    find_cycle(current, c, path + chr(current + 64))

    vertexes = generate_vertexes()

    find_cycle(-1, 1, '')

    return edges


if __name__ == '__main__':
    print('Critical Connections')

    print(solve(5, [[1, 2], [1, 3], [3, 4], [1, 4], [4, 5]]))
