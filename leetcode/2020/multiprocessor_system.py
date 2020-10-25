from queue import PriorityQueue


def find_min_time(num: int, ability: [int], processes: int) -> int:
    min_time = 0

    queue = PriorityQueue()

    for a in ability:
        queue.put((-a, a))

    while processes > 0:
        t_i, t_v = queue.get()
        processes -= t_v
        new_value = int(t_v / 2)
        queue.put((-new_value, new_value))
        min_time += 1

    return min_time


if __name__ == '__main__':
    print(find_min_time(5, [3, 1, 7, 2, 4], 15))
