class Node:
    def __init__(self, x: int, next_item=None, random_item=None):
        self.val = int(x)
        self.next = next_item
        self.random = random_item


def solve(head: Node):
    new_head = Node(head.val)
    node_map = {head: new_head}

    old_temp = head
    new_temp = new_head

    while old_temp.next is not None:
        new_temp.next = Node(old_temp.next.val)

        node_map[old_temp.next] = new_temp.next

        old_temp = old_temp.next
        new_temp = new_temp.next

    for key in node_map:
        if key.random is not None:
            node_map[key].random = node_map[key.random]

    for key in node_map.keys():
        print(f'{key.val} : {node_map[key].val} - '
              f'{key.random if key.random is None else key.random.val} : '
              f'{node_map[key].random if node_map[key].random is None else node_map[key].random.val}')

    return new_head


def generate_list() -> Node:
    source_list = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    node_list = []

    for i in range(len(source_list)):
        new_node = Node(source_list[i][0])
        node_list.append(new_node)
        if i > 0:
            node_list[i - 1].next = new_node

    for i in range(len(source_list)):
        if source_list[i][1] is not None:
            node_list[i].random = node_list[source_list[i][1]]

    return node_list[0]


if __name__ == '__main__':
    print('Copy List with Random Pointer')
    source_root = generate_list()

    solve(source_root)
