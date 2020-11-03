def solve(graph: {str: int}) -> int:
    cost = 0
    connected = []

    for key in graph_edges:
        start_used = [u for u in connected if u.find(key[0]) >= 0]
        end_used = [u for u in connected if u.find(key[1]) >= 0]

        if len(start_used) > 0 and len(end_used) > 0:
            if start_used[0] == end_used[0]:
                pass
            else:
                new_connected = start_used[0] + end_used[0]
                connected.remove(start_used[0])
                connected.remove(end_used[0])
                connected.append(new_connected)
                cost += graph_edges[key]
        elif len(start_used) > 0:
            new_connected = start_used[0].replace(key[0], '')
            new_connected += key
            connected[connected.index(start_used[0])] = new_connected
            cost += graph_edges[key]
        elif len(end_used) > 0:
            new_connected = end_used[0].replace(key[1], '')
            new_connected += key
            connected[connected.index(end_used[0])] = new_connected
            cost += graph_edges[key]
        else:
            connected.append(key)
            cost += graph_edges[key]

    return cost


# Time complexity - O(E logV)
if __name__ == '__main__':
    print('Kruskal`s algorithm')

    graph_edges = {
        # first graph from Wiki
        # 'ae': 1,
        # 'cd': 2,
        # 'ab': 3,
        # 'be': 4,
        # 'bc': 5,
        # 'ec': 6,
        # 'ed': 7
        # Second graph - https://studopedia.ru/6_17404_obrazets-vipolneniya.html
        'ef': 2,
        'bc': 3,
        'ce': 4,
        'de': 4,
        'dg': 5,
        'bd': 6,
        'fg': 6,
        'ac': 10,
        'ab': 15,
        'bg': 17
    }

    print(solve(graph_edges))
