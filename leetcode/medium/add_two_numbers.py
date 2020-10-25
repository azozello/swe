# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Input: l1 = [0], l2 = [0]
# Output: [0]

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1: ListNode, l2: ListNode):
    carry = 0
    result = []

    while l1 is not None or l2 is not None:
        if l1 is not None and l2 is not None:
            temp_sum = l1.val + l2.val + carry

            if temp_sum > 9:
                result.append(temp_sum - 10)
                carry = 1
            else:
                result.append(temp_sum)
                carry = 0

            l1 = l1.next
            l2 = l2.next

        elif l1 is not None:
            temp_sum = l1.val + carry

            if temp_sum > 9:
                result.append(temp_sum - 10)
                carry = 1
            else:
                result.append(temp_sum)
                carry = 0

            l1 = l1.next

        elif l2 is not None:
            temp_sum = l2.val + carry

            if temp_sum > 9:
                result.append(temp_sum - 10)
                carry = 1
            else:
                result.append(temp_sum)
                carry = 0

            l2 = l2.next

    if carry > 0:
        result.append(carry)

    result.reverse()

    return array_to_linked(result)


def array_to_linked(array: [int]):
    start_node = ListNode(array.pop())
    temp_node = start_node

    while len(array) > 0:
        temp_node.next = ListNode(array.pop())
        temp_node = temp_node.next

    return start_node


def reverse_linked_list(head: ListNode):
    current = head
    next_node, prev_node = [None, None]

    while current is not None:
        next_node = current.next
        current.next = prev_node

        current = next_node
        prev_node = current

    head = prev_node
    return head


def sum_easy(list_one: [int], list_two: [int]):
    list_one.reverse()
    list_two.reverse()

    number_one = int(''.join([str(n) for n in list_one]))
    number_two = int(''.join([str(n) for n in list_two]))

    return number_one + number_two


if __name__ == '__main__':
    test_one = [9, 9, 9, 9, 9, 9, 9]
    test_two = [9, 9, 9, 9]

    node_one = array_to_linked(test_one.copy())
    node_two = array_to_linked(test_two.copy())

    results = add_two_numbers(node_one, node_two)

    print(results)
