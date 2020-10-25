class Window:
    def __init__(self, start: int, end: int, value: int, capacity: int, size: int):
        self.start = start
        self.end = end
        self.capacity = capacity
        self.value = value
        self.size = size

    def get_count_increment(self):
        volume = self.end - self.start
        return [i for i in range(self.start + self.capacity, self.start + volume)] if volume > self.capacity else []

    def find_end(self, index, size, array):
        i = index

        while i < size and array[i] - self.value < self.size:
            i += 1

        self.end = i

        return i

    def find_start(self, size, array):
        i = self.start

        while i < size and array[i] == self.value:
            i += 1

        self.start = i
        self.value = array[min(i, size - 1)]

        return i


def count_dropped_requests(amount: int, requests: [int]) -> int:
    count = set()

    gateways = [(1, 3), (10, 20), (60, 60)]

    for size, limit in gateways:
        window = Window(0, -1, requests[0], limit, size)
        index = 0

        while index < amount:
            # seek window end:
            i = window.find_end(index, amount, requests)

            # perform window logic:
            count.update(window.get_count_increment())

            # go to the next window
            index = window.find_start(amount, requests)

    return len(count)


if __name__ == '__main__':
    request_count = 27
    request_seconds = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 11, 11, 11, 11]

    print(count_dropped_requests(request_count, request_seconds))
