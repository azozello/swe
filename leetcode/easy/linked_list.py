class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
    if l1.val <= l2.val:
        result_node_start = l1
        l1 = l1.next
    else:
        result_node_start = l2
        l2 = l2.next

    temp = result_node_start
    while l1 is not None or l2 is not None:
        if l1 is not None and (l2 is None or l1.val <= l2.val):
            temp.next = l1
            temp = temp.next
            l1 = l1.next

        elif l2 is not None and (l1 is None or l2.val <= l1.val):
            temp.next = l2
            temp = temp.next
            l2 = l2.next

    return result_node_start


if __name__ == '__main__':
    print('Merge Two Sorted Lists')

    l_1_start = ListNode(1)
    l_1_start.next = ListNode(2)
    l_1_start.next.next = ListNode(4)

    l_2_start = ListNode(1)
    l_2_start.next = ListNode(3)
    l_2_start.next.next = ListNode(4)

    result = merge_two_lists(l_1_start, l_2_start)
    while result is not None:
        print(result.val)
        result = result.next
