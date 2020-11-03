import sys


def can_be_bst(array: [int]):
    # Create an empty stack
    s = []

    # Initialize current root as minimum possible value
    root = -sys.maxsize

    # Traverse given array
    for n in array:
        # NOTE:value is equal to pre[i] according to the
        # given algo

        # If we find a node who is on the right side
        # and smaller than root, return False
        if n < root:
            return False

            # If value(pre[i]) is in right subtree of stack top,
        # Keep removing items smaller than value
        # and make the last removed items as new root
        while len(s) > 0 and s[-1] < n:
            root = s.pop()

            # At this point either stack is empty or value
        # is smaller than root, push value
        s.append(n)

    return True


if __name__ == '__main__':
    bad = [40, 30, 35, 20, 80, 100]
    good = [40, 30, 35, 80, 100]
    print(can_be_bst(bad))
    print(can_be_bst(good))
