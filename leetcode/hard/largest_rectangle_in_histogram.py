def get_largest_rectangle(histogram: [int]) -> int:
    stack = list()
    value_stack = list()
    max_size = 0
    index = 0

    while index < len(histogram):
        index_value = histogram[index]
        if not stack or histogram[index] >= histogram[stack[-1]]:
            stack.append(index)
            value_stack.append(histogram[index])
            index += 1
        else:
            top = stack.pop()
            top_value = histogram[top]
            mult = (index - stack[-1] - 1) if stack else index

            current_max = top_value * mult

            max_size = max(current_max, max_size)

    while stack:
        top = stack.pop()
        value_stack.pop()

        current_max = histogram[top] * ((index - stack[-1] - 1) if stack else index)

        max_size = max(current_max, max_size)

    return max_size


if __name__ == '__main__':
    print('Largest Rectangular Area in a Histogram')
    # hist = [6, 2, 5, 4, 5, 1, 6]
    hist = [3, 3, 5, 4, 3, 4, 3, 4, 5, 3]
    print(get_largest_rectangle(hist))
