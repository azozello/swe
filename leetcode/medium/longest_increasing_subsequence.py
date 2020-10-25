# Given an unsorted array of integers, find the length of longest increasing subsequence.
def find_longest(nums: [int]) -> int:
    local_max = [1 for i in nums]

    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j] and local_max[j] + 1 > local_max[i]:
                local_max[i] = local_max[j] + 1

    return max(local_max) if len(local_max) > 0 else 0


if __name__ == '__main__':
    array = [1, 3, 6, 7, 9, 4, 10, 5, 6]
    print(find_longest(array))
