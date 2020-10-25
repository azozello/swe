class LinkedList:
    def __init__(self, value=None):
        self.value = value
        self.size = 0 if value is None else 1
        self.head = None
        self.next = None

    def add_first(self, value):
        new_node = LinkedList(value)
        new_node.next = self.next
        self.next = new_node
        self.size += 1
