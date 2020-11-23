from collections import namedtuple, deque


class Node:
    def __init__(self, left, right, val):
        self.left = left
        self.right = right
        self.val = val


def generate_tree():
    #          A
    #        /   \
    #      /       \
    #     B         C
    #    / \        /
    #  /     \    /
    # D       E  F
    node_d = Node(None, None, 1)
    node_e = Node(None, None, 5)
    node_f = Node(None, None, 3)
    node_b = Node(node_d, node_e, 6)
    node_c = Node(node_f, None, 4)
    node_a = Node(node_b, node_c, 9)

    return node_a


def serialize_tree(root: Node) -> str:
    pre_order_path = []
    in_order_path = []

    pre_order(root, pre_order_path)
    in_order(root, in_order_path)

    return f'{",".join([str(v) for v in pre_order_path])}:{",".join(str(v) for v in in_order_path)}'


def pre_order(root: Node, path: [str]) -> [str]:
    if not root:
        return

    path.append(root.val)

    pre_order(root.left, path)
    pre_order(root.right, path)


def in_order(root: Node, path: [str]) -> [str]:
    if not root:
        return

    in_order(root.left, path)

    path.append(root.val)

    in_order(root.right, path)


def deserialize_tree(serialized_tree: str) -> Node:
    if not serialized_tree or len(serialized_tree) == 0:
        return

    pre_order_string, in_order_string = serialized_tree.split(':')

    pre_order_list = pre_order_string.split(',')
    in_order_list = in_order_string.split(',')

    root = Node(None, None, None)

    def set_root_val(val):
        root.val = val
        return root

    recursively_add_children(set_root_val, in_order_list, deque(pre_order_list))

    return root


def recursively_add_children(ad_to_parent, in_order_string: [str], pre_order_string: deque):
    new_root = pre_order_string.popleft()

    parent = ad_to_parent(new_root)

    index = in_order_string.index(new_root)

    def add_left(val):
        parent.left = Node(None, None, val)
        return parent.left

    def add_right(val):
        parent.right = Node(None, None, val)
        return parent.right

    left_in_order = in_order_string[0: index]
    right_in_order = in_order_string[index + 1:]

    if len(left_in_order) > 0:
        recursively_add_children(add_left, left_in_order, pre_order_string)

    if len(right_in_order) > 0:
        recursively_add_children(add_right, right_in_order, pre_order_string)


# [LC-297] Serialize and Deserialize Binary Tree
#
# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be
# stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the
# same or another computer environment.
#
# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your
# serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be
# serialized to a string and this string can be deserialized to the original tree structure.
if __name__ == '__main__':
    #          A
    #        /   \
    #      /       \
    #     B         C
    #    / \        /
    #  /     \    /
    # D       E  F
    start = generate_tree()

    # Should return - ABDECF : DBEAFC
    # Actual result - ABDECF : DBEAFC
    first_ser = serialize_tree(start)
    new_start = deserialize_tree(first_ser)
    second_ser = serialize_tree(new_start)

    print(first_ser)
    print(second_ser)
