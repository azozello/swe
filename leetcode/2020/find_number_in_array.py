from collections import namedtuple


def search_range(nums: [int], target: int) -> [int]:
    i, j = [0, len(nums) - 1]
    was_found = False

    while i <= j:
        if nums[i] == target:
            was_found = True
            if nums[j] == target:
                break
            else:
                j -= 1
        else:
            i += 1

    return [i, j] if was_found else [-1, -1]


if __name__ == '__main__':
    EdgeCase = namedtuple('EdgeCase', ['input', 'expectedResult'])
    Input = namedtuple('Input', ['nums', 'target'])

    cases = [
        # Success case
        EdgeCase._make([
            Input._make([[1, 2, 2, 3, 4], 2]),
            [1, 2]
        ]),
        # Target not in array
        EdgeCase._make([
            Input._make([[1, 2, 2, 3, 4], 9]),
            [-1, -1]
        ]),
        # Empty array
        EdgeCase._make([
            Input._make([[], 2]),
            [-1, -1]
        ]),
        # Single value array
        EdgeCase._make([
            Input._make([[1], 1]),
            [0, 0]
        ]),
        # Array all of targets
        EdgeCase._make([
            Input._make([[2, 2, 2, 2, 2], 2]),
            [0, 4]
        ]),
        # Negative target
        EdgeCase._make([
            Input._make([[-4, -3, -3, 2, 2], -3]),
            [1, 2]
        ]),
        # Single target
        EdgeCase._make([
            Input._make([[-4, -3, -3, 4, 5], 4]),
            [3, 3]
        ]),
    ]

    for c in cases:
        result = search_range(c.input.nums, c.input.target)
        if result == c.expectedResult:
            print('PASSED')
        else:
            print('================ERROR=================')
            print('Input')
            print(c.input)
            print('Expected:')
            print(c.expectedResult)
            print('Actual:')
            print(result)
            print('======================================')
