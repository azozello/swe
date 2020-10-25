class Tree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def add(self, value):
        if value > self.value:
            if self.right is None:
                self.right = Tree(value)
            else:
                self.right.add(value)
        else:
            if self.left is None:
                self.left = Tree(value)
            else:
                self.left.add(value)

    def contains(self, value):
        if value == self.value:
            return True
        else:
            if value < self.value:
                if self.left is None:
                    return False
                else:
                    return self.left.contains(value)
            else:
                if self.right is None:
                    return False
                else:
                    return self.right.contains(value)

    def pre_order(self):
        result = []
        if self.left is not None:
            result += self.left.pre_order()
        result += [self.value]
        if self.right is not None:
            result += self.right.pre_order()
        return result
