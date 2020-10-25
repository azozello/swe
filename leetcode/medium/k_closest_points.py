import my_math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def k_closest(points, k: int):
    distances = {}
    for p in points:
        distances[Point(p[0], p[1])] = my_math.sqrt(my_math.pow(p[0], 2) + my_math.pow(p[1], 2))
    sorted_distances = {k: v for k, v in sorted(distances.items(), key=lambda item: item[1])}
    return [[p.x, p.y] for p in list(sorted_distances.keys())[:k]]


if __name__ == '__main__':
    print('K Closest Points to Origin')
    print(k_closest([[1, 1], [3, 3], [2, 2]], 2))
