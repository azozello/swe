from data_structure.Tree import Tree


def invert(node: Tree):
    if node.left is not None:
        invert(node.left)

    if node.right is not None:
        invert(node.right)

    temp = node.left
    node.left = node.right
    node.right = temp


if __name__ == '__main__':
    root = Tree(2)
    root.left = Tree(1)
    root.right = Tree(4)
    root.right.left = Tree(3)
    root.right.right = Tree(5)

    print(root.pre_order())
    invert(root)
    print(root.pre_order())
