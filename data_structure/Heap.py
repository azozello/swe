import math


class Heap:
    def __init__(self, size):
        self.size = size
        self.last_position = 0
        self.data = [0 for i in range(size)]

    def add(self, value):
        if self.last_position < self.size - 1:
            self.last_position += 1
            self.data[self.last_position] = value
            self.trickle_up(self.last_position)

    def trickle_up(self, position):
        if position == 0:
            return
        else:
            parent_position = math.floor((position - 1) / 2)
            if self.data[parent_position] < position:
                self.swap(position, parent_position)
                self.trickle_up(parent_position)

    def swap(self, from_index, to_index):
        temp = self.data[from_index]
        self.data[from_index] = self.data[to_index]
        self.data[to_index] = temp
