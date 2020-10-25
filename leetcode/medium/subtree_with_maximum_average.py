class TreeNode:
    def __init__(self, value):
        self.val = value
        self.children = []


def solve(root: TreeNode) -> TreeNode:
    root_average = node_average(root)
    root_map = {root_average: root}

    def find_averages(node: TreeNode):
        direct_averages = []
        for c in node.children:
            if len(c.children) > 0:
                average = node_average(c)
                direct_averages.append(average)
                root_map[average] = c
                direct_averages += find_averages(c)

        return direct_averages

    averages = find_averages(root) + [root_average]
    return root_map[max(averages)]


def node_average(root: TreeNode) -> float:
    def sum_child(node: TreeNode) -> (int, int):
        direct_sum = 0
        direct_count = 0

        for c in node.children:
            direct_count += 1
            direct_sum += c.val
            children_sum, children_count = sum_child(c)
            direct_sum += children_sum
            direct_count += children_count

        return direct_sum, direct_count

    values, number = sum_child(root)
    return (values + root.val) / (1 + number)


def generate_sample() -> TreeNode:
    node_11 = TreeNode(11)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    node_15 = TreeNode(15)
    node_8 = TreeNode(8)
    node_12 = TreeNode(12)
    node_18 = TreeNode(18)
    node_20 = TreeNode(20)

    node_12.children = [node_11, node_2, node_3]
    node_18.children = [node_15, node_8]
    node_20.children = [node_12, node_18]

    return node_20


if __name__ == '__main__':
    print('Subtree with Maximum Average')
    root_node = generate_sample()
    max_node = solve(root_node)
    print(max_node.val)
