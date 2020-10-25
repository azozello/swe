from collections import deque


# Complexity - n Log n
def merge_sort(array):
    def merge(first, second):
        result = []
        if len(first) > 0 and len(second) > 0:
            first = deque(first)
            second = deque(second)
            t_f = first.popleft()
            t_s = second.popleft()

            first_added = False
            second_added = False

            while not (first_added and second_added):
                if (t_f < t_s and not first_added) or second_added:
                    result.append(t_f)
                    if len(first) > 0:
                        t_f = first.popleft()
                    else:
                        first_added = True
                else:
                    result.append(t_s)
                    if len(second) > 0:
                        t_s = second.popleft()
                    else:
                        second_added = True
        elif len(first) > 0:
            return first
        elif len(second):
            return second
        return result

    length = len(array)

    if length > 2:
        first_array = array[:int(length / 2)]
        second_array = array[int(length / 2):]
        return merge(merge_sort(first_array), merge_sort(second_array))
    elif length < 2:
        return array
    else:
        return [array[0], array[1]] if array[0] < array[1] else [array[1], array[0]]


# Complexity - n log n
def quick_sort(array, start=0, end=0):
    def swap(source_array, first_index, second_index):
        temp = array[first_index]
        source_array[first_index] = source_array[second_index]
        source_array[second_index] = temp

    end = len(array) - 1 if end == 0 else end
    if end > start and abs(start - end) > 0:
        larger_index = start

        for i in range(start, end):
            if array[i] > array[end]:
                pass
            else:
                if i != larger_index:
                    swap(array, i, larger_index)
                    larger_index += 1

        swap(array, larger_index, end)

        quick_sort(array, start, larger_index - 1)
        quick_sort(array, larger_index + 1, end)
