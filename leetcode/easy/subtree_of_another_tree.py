class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def solve(s: TreeNode, t: TreeNode) -> bool:
    def find_root(temp_root: TreeNode, target_value: int) -> TreeNode:
        if temp_root is None:
            return None
        elif temp_root.val == target_value:
            return temp_root
        else:
            left_found = find_root(temp_root.left, target_value)
            return left_found if left_found is not None else find_root(temp_root.right, target_value)

    def compare_trees(source_root: TreeNode, target_root: TreeNode) -> bool:
        if target_root is None and source_root is None:
            return True
        elif (target_root is not None and source_root is None) or (target_root is None and source_root is not None):
            return False
        elif target_root.val != source_root.val:
            return False
        else:
            left = compare_trees(source_root.left, target_root.left)
            right = compare_trees(source_root.right, target_root.right)
            return left and right

    possible_root = find_root(s, t.val)

    if possible_root is not None:
        return compare_trees(possible_root, t)

    return False


if __name__ == '__main__':
    print('Subtree of Another Tree')

    source = TreeNode(3)
    source.left = TreeNode(4)
    source.left.left = TreeNode(1)
    source.left.right = TreeNode(2)
    # source.left.right.left = TreeNode(0)
    source.right = TreeNode(5)

    target = TreeNode(4)
    target.left = TreeNode(1)
    target.right = TreeNode(2)

    print(solve(source, target))
