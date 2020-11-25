# You are given an integer array nums and you have to return a new counts array. The counts array has the property
# where counts[i] is the number of smaller elements to the right of nums[i].

# Example:
# Input: nums = [5,2,6,1]
# Output: [2,1,1,0]
# Explanation:
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.
# 0 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
from time import time
import bisect


# # # # # # # # # # # # # # # # # # # #
# # LINKED LIST SOLUTION - TOO SLOW # #
# # # # # # # # # # # # # # # # # # # #

class LinkedNode:
    def __init__(self, value=0, back=None, forward=None):
        self.value = value
        self.back = back
        self.forward = forward
        pass


def insert_into_list(head: LinkedNode, value):
    if not head:
        return LinkedNode(value)

    if head.value > value:
        new_node = LinkedNode(value, None, head)
        head.back = new_node
        return new_node

    pointer = head
    while pointer:
        if pointer.value > value:
            temp = pointer.back
            pointer.back = LinkedNode(value, temp, pointer)
            temp.forward = pointer.back
            return head
        elif pointer.forward:
            pointer = pointer.forward
        else:
            break

    pointer.forward = LinkedNode(value, pointer)
    return head


def iterate_over_linked_linked(head: LinkedNode, logic, end_value=None):
    temp = head
    while temp:
        if end_value is not None and temp.value >= end_value:
            break
        logic(temp)
        temp = temp.forward


def count_numbers_linked_list(numbers: [int]) -> [int]:
    count_array = []
    head = None

    for i in range(len(numbers) - 1, -1, -1):
        head = insert_into_list(head, numbers[i])
        less_then = 0

        def increment(temp: LinkedNode):
            nonlocal less_then
            less_then += 1

        iterate_over_linked_linked(head, increment, numbers[i])

        count_array.append(less_then)

    return list(reversed(count_array))


# # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # BINARY SEARCHING TREE SOLUTION - STILL TO SLOW  # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # #

class BinarySearchingTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def insert_into_bst(root: BinarySearchingTree, value: int):
    if root is None:
        return BinarySearchingTree(value)

    if value < root.value:
        if root.left is not None:
            insert_into_bst(root.left, value)
        else:
            root.left = BinarySearchingTree(value)
    else:
        if root.right is not None:
            insert_into_bst(root.right, value)
        else:
            root.right = BinarySearchingTree(value)


def count_less_then_value(root: BinarySearchingTree, value: int):
    if root is None:
        return 0

    if root.value < value:
        return 1 + count_less_then_value(root.left, value) + count_less_then_value(root.right, value)
    else:
        return count_less_then_value(root.left, value)


def in_order(root: BinarySearchingTree, logic):
    if not root:
        return

    in_order(root.left, logic)
    logic(root)
    in_order(root.right, logic)


def count_numbers_bst(numbers: [int]) -> [int]:
    count_array = []
    head = None

    for i in range(len(numbers) - 1, -1, -1):
        if head:
            insert_into_bst(head, numbers[i])
        else:
            head = insert_into_bst(head, numbers[i])

        count_array.append(count_less_then_value(head, numbers[i]))

    return list(reversed(count_array))


# # # # # # # # # # # # # # # # # # # # #
# # NATIVE APPROACH - LIGHTNING FAST  # #
# # # # # # # # # # # # # # # # # # # # #
def count_numbers_native(numbers: [int]) -> [int]:
    result = []
    sorted_values = []

    for i in range(len(numbers) - 1, -1, -1):
        count = bisect.bisect_left(sorted_values, numbers[i])
        result.append(count)
        sorted_values.insert(count, numbers[i])

    return list(reversed(result))


# Linked list solution  - 34,000ms in worst
# Binary searching tree - 27,000ms in worst
# Native with bisect    - 58ms !!!
if __name__ == '__main__':
    input_data = [5, 2, 6, 1]

    start_time = int(round(time() * 1000))
    print(count_numbers_native(input_data))
    print(int(round(time() * 1000)) - start_time)
