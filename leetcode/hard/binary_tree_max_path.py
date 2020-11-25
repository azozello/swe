# Given a non-empty binary tree, find the maximum path sum.
#
# For this problem, a path is defined as any node sequence from some starting node to any node in the tree along the
# parent-child connections. The path must contain at least one node and does not need to go through the root.
from queue import Queue, PriorityQueue


class TreeNode:
    def __init__(self, left=None, right=None, val=0):
        self.val = val
        self.left = left
        self.right = right


class CostNode:
    def __init__(self, left, right, value, level=0, max_direct=0, max_curve=0):
        self.left = left
        self.right = right
        self.value = value
        self.max_direct = max_direct
        self.max_curve = max_curve
        self.level = level

    def __str__(self):
        return f'{self.level}:{self.value}'

    def __repr__(self):
        return f'{self.level}:{self.value}'

    def __cmp__(self, other):
        return self.level - other.level

    def __lt__(self, other):
        return self.level < other.level

    def __eq__(self, other):
        return self.level == other.level


def generate_tree() -> TreeNode:
    # node_8 = Node(None, None, 8)
    # node_10 = Node(None, None, 10)
    #
    # node_4 = Node(node_8, None, 4)
    # node_5 = Node(None, node_10, 5)
    # node_6 = Node(None, None, 6)
    # node_7 = Node(None, None, 7)
    #
    # node_2 = Node(node_4, node_5, 2)
    # node_3 = Node(node_6, node_7, 3)
    #
    # node_1 = Node(node_2, node_3, 1)

    node_2 = TreeNode(None, None, 2)
    node_3 = TreeNode(None, None, 3)
    node_1 = TreeNode(node_2, node_3, 1)

    # node_15 = TreeNode(None, None, 15)
    # node_7 = TreeNode(None, None, 7)
    #
    # node_9 = TreeNode(None, None, 9)
    # node_20 = TreeNode(node_15, node_7, 20)
    #
    # node_m10 = TreeNode(node_9, node_20, -10)

    # node_m3 = TreeNode(None, None, -3)

    # node_1 = TreeNode(None, None, 1)
    # node_2 = TreeNode(node_1, None, 2)
    # node_3 = TreeNode(None, node_2, 3)

    # node_m1 = TreeNode(None, None, -1)
    # node_m2 = TreeNode(node_m1, None, -2)

    # node_m6_3 = TreeNode(None, None, -6)
    #
    # node_m6_2 = TreeNode(node_m6_3, None, -6)
    # node_m6_1 = TreeNode(None, None, -6)
    #
    # node_2_1 = TreeNode(node_m6_2, node_m6_1, 2)
    #
    # node_2 = TreeNode(node_2_1, None, 2)
    # node_m6 = TreeNode(None, None, -6)
    #
    # node_m3 = TreeNode(node_m6, node_2, -3)
    # node_6 = TreeNode(None, None, 6)
    #
    # node_9 = TreeNode(node_6, node_m3, 9)

    return node_1


def get_max_path(root: TreeNode) -> int:
    if not root:
        return -2147483648

    if not root.left and not root.right:
        return root.val

    max_path = root.val
    pq = PriorityQueue()
    bottom_up_bfs(root, lambda cost_node: pq.put(cost_node))

    while not pq.empty():
        cn = pq.get()
        v = cn.value
        lc, ld, rc, rd = get_max_counts(cn)
        cn.max_direct = max(ld, rd, 0) + v
        cn.max_curve = max(ld, 0) + max(rd, 0) + v
        max_path = max(max_path, cn.max_direct, cn.max_curve)

    return max_path


def bottom_up_bfs(root: TreeNode, logic=lambda x: print(x)):
    queue = Queue()
    tree_to_cost_map = {}

    def put_neighbours(cn: CostNode):
        if cn.left:
            queue.put(to_cost_node(cn.left, tree_to_cost_map, cn.level - 1))
            cn.left = to_cost_node(cn.left, tree_to_cost_map, cn.level - 1)

        if cn.right:
            queue.put(to_cost_node(cn.right, tree_to_cost_map, cn.level - 1))
            cn.right = to_cost_node(cn.right, tree_to_cost_map, cn.level - 1)

    cost_root = to_cost_node(root, tree_to_cost_map, -1)
    queue.put(cost_root)

    while not queue.empty():
        vertex = queue.get()
        logic(vertex)
        put_neighbours(vertex)


def to_cost_node(tree_node: TreeNode, tree_to_cost_map: {}, level: int) -> CostNode:
    if tree_to_cost_map.get(tree_node):
        return tree_to_cost_map[tree_node]
    else:
        new_node = CostNode(tree_node.left, tree_node.right, tree_node.val, level, tree_node.val, tree_node.val)
        tree_to_cost_map[tree_node] = new_node
        return new_node


def get_max_counts(cn: CostNode):
    lc, ld, rc, rd = [0, 0, 0, 0]

    if cn.left:
        ld = cn.left.max_direct
        lc = cn.left.max_curve

    if cn.right:
        rd = cn.right.max_direct
        rc = cn.right.max_curve

    return lc, ld, rc, rd


if __name__ == '__main__':
    start = generate_tree()
    result = get_max_path(start)
    print(result)

#    Огромная куча дел, которую я на хую вертел:
# 0) 10 Декабря - Собес в MS, ПОСЛЕДНИЙ шанс попасть в faang.
# 1) До 1 Декабря - Съехать на новую хату.
# 2) До 18 Декабря - Сделать 1 Issue в open source проекте в универ.
# 3) До 16 Декабря - Сделать распредилённую файловую систему для консоли в универ.
# 4) 3 Декабря - Набрать 50%+ на контрольной по семантике языков программирования.
# 5) Декабрь - Додолбить чуваков и получить набор данных, после их обработать - Командный проект в универе.
# 6) Работать не забывай!
# 7) До 6 Декабря - Сделать бота в телегу
# 8) Найти хату на НГ
# 9) Ты там работаешь вообще?
