from collections import defaultdict, namedtuple, deque
import heapq

if __name__ == '__main__':
    # default dict
    int_tuple = defaultdict(int)
    list_tuple = defaultdict(list)
    s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

    for k, v in s:
        int_tuple[k] += v
        list_tuple[k] += [v]

    print('Default dict')
    print(int_tuple)
    print(list_tuple)

    # named tuple
    print('Named tuple')
    point = namedtuple('Point', ('x', 'y'))
    points = list(map(lambda x: point._make(x), [[2, 3], [3, 4]]))
    print(points)

    point_3d = namedtuple('Point3d', point._fields + tuple('z'))

    # deque
    print('Deque')
    fifo = deque()
    fifo.append(1)
    fifo.append(2)

    print(f'FIFO: {fifo.popleft()}, {fifo.popleft()}')

    fifo.append(1)
    fifo.append(2)

    print(f'LIFO: {fifo.pop()}, {fifo.pop()}')

    # Priority queue
    print('Priority queue')
    p_queue = []
    heapq.heappush(p_queue, (-3, [1, 2]))
    heapq.heappush(p_queue, (-2, [2, 3]))
    heapq.heappush(p_queue, (-1, [3, 4]))
    print(heapq.heappop(p_queue), heapq.heappop(p_queue), heapq.heappop(p_queue))

    # Map
    integers = [1, 2, 3, 4]
    print(list(map(lambda x: x * x, integers)))
    print(list(filter(lambda x: x % 2 == 0, integers)))
