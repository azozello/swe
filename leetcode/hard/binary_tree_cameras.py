class TreeNode:
    def __init__(self, value='', left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def min_camera_cover(root: TreeNode):
    dfs(root, None, {})


def dfs(node: TreeNode, parent: TreeNode, covered: {TreeNode}):
    global cameras_needed
    if node:
        dfs(node.left, node, covered)
        dfs(node.right, node, covered)

        left_covered = not node.left or node.left in covered
        right_covered = not node.right or node.right in covered

        has_parent = parent is not None
        is_covered = node in covered

        if not is_covered and not has_parent or not left_covered or not right_covered:
            cover(node, parent, covered)
            cameras_needed += 1


def cover(node: TreeNode, parent: TreeNode, covered: {TreeNode}):
    covered[node] = True

    if parent:
        covered[parent] = True

    if node.left:
        covered[node.right] = True

    if node.left:
        covered[node.right] = True


if __name__ == '__main__':
    print('Binary tree cameras')

    start = TreeNode('S')
    start.left = TreeNode('L')
    start.right = TreeNode('R')
    start.right.right = TreeNode('RR')

    cameras_needed = 0
    min_camera_cover(start)
    print(cameras_needed)
