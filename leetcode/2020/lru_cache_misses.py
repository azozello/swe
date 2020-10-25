from collections import OrderedDict


class LruCache(OrderedDict):
    def __init__(self, capacity):
        self.capacity = capacity
        self.misses = 0
        self.n = 0

    def hit(self, key):
        if key in self:
            self.move_to_end(key)
        else:
            self.misses += 1
        self[key] = None
        self.n += 1

        if self.n > self.capacity:
            self.popitem(last=False)
            self.n -= 1


def count_misses(num, pages, size):
    lru_cache = LruCache(size)
    for page in pages:
        lru_cache.hit(page)
    return lru_cache.misses


if __name__ == '__main__':
    print(count_misses(
        6,
        [1, 2, 1, 3, 1, 2],
        2
    ))
