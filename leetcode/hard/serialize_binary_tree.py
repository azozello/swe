from collections import namedtuple

Node = namedtuple('Node', ['left', 'right', 'value'])


def generate_tree():
    #          A
    #        /   \
    #      /       \
    #     B         C
    #    / \        /
    #  /     \    /
    # D       E  F
    node_d = Node._make([None, None, 'D'])
    node_e = Node._make([None, None, 'E'])
    node_f = Node._make([None, None, 'F'])
    node_b = Node._make([node_d, node_e, 'B'])
    node_c = Node._make([node_f, None, 'C'])
    node_a = Node._make([node_b, node_c, 'A'])

    return node_a


def serialize_tree(root: Node) -> str:
    pre_order_path = []
    in_order_path = []

    pre_order(root, pre_order_path)
    in_order(root, in_order_path)

    return f'{"".join(pre_order_path)}:{"".join(in_order_path)}'


def pre_order(root: Node, path: [str]) -> [str]:
    if not root:
        return

    path.append(root.value)

    pre_order(root.left, path)
    pre_order(root.right, path)


def in_order(root: Node, path: [str]) -> [str]:
    if not root:
        return

    in_order(root.left, path)

    path.append(root.value)

    in_order(root.right, path)


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
    print(serialize_tree(start))
