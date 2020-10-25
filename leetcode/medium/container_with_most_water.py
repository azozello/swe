# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0).
# Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
#
# Notice that you may not slant the container.


def max_area(height: [int]) -> int:
    current_max = 0
    temp = 0
    left, right = [0, len(height) - 1]

    while left < right:
        if height[right] > height[left]:
            temp = height[left] * (right - left)
            left += 1
        else:
            temp = height[right] * (right - left)
            right -= 1

        if temp > current_max:
            current_max = temp

    return current_max


if __name__ == '__main__':
    array = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(max_area(array))
