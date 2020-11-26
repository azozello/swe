# Given an unsorted integer array nums, find the smallest missing positive integer.
#
# Follow up: Could you implement an algorithm that runs in O(n) time and uses constant extra space.?
#
# Example 1:
#
# Input: nums = [1,2,0]
# Output: 3
# Example 2:
#
# Input: nums = [3,4,-1,1]
# Output: 2
# Example 3:
#
# Input: nums = [7,8,9,11,12]
# Output: 1
#
#
# Constraints:
#
# 0 <= nums.length <= 300
# -231 <= nums[i] <= 231 - 1
#
# HINT:
# Use array value indexing


# # # # # # # # # # # # # # # # # # # # # # #
# # NATIVE APPROACH - FASTER THAN 98.64%  # #
# # # # # # # # # # # # # # # # # # # # # # #

def first_missing_positive(numbers: [int]) -> int:
    first_missing = 1
    sorted_numbers = list(sorted(set(numbers)))

    for n in sorted_numbers:
        if n > 0:
            if n == first_missing:
                first_missing += 1
            else:
                break

    return first_missing


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # ALGO APPROACH - TIME COMPLEXITY = O(n), SPACE COMPLEXITY = O(1) # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def first_missing_positive_algo(numbers: [int]) -> int:
    start_index = segregate_negative(numbers)

    return inverse_containing_numbers(numbers[start_index:], len(numbers) - start_index)


def segregate_negative(numbers: [int]) -> [int]:
    j = 0

    for i in range(len(numbers)):
        if numbers[i] <= 0:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            j += 1

    return j


def inverse_containing_numbers(arr, size):
    n_i = -1
    for i in range(size):
        n_i = abs(arr[i]) - 1
        if n_i < size and arr[n_i] > 0:
            arr[n_i] = -arr[n_i]

    for i in range(size):
        if arr[i] > 0:
            return i + 1

    return size + 1


if __name__ == '__main__':
    input_data = [0, 1, 2]
    missing = first_missing_positive_algo(input_data)
    print(missing)
