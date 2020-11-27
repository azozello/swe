# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# Follow up: Could you implement the O(n) solution?


class Sequence:
    def __init__(self, start, end, length=1):
        self.start = start
        self.end = end
        self.length = length


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # VALUE INDEXING - TIME COMPLEXITY = O(n*log(n)), SPACE COMPLEXITY = O(n) # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def find_longest_sequence(numbers: [int]) -> int:
    sequence_map = {}

    for n in numbers:
        if can_join(sequence_map, n) and not contains(sequence_map, n):
            join(sequence_map, n)

        elif has_lower(sequence_map, n):
            append_lower(sequence_map, n)

        elif has_higher(sequence_map, n):
            append_higher(sequence_map, n)

        elif can_join(sequence_map, n):
            continue

        else:
            sequence_map[n] = Sequence(n, n)

    return get_longest(sequence_map)


def has_lower(sequence_map: {int, Sequence}, number: int) -> bool:
    return sequence_map.get(number - 1) is not None


def has_higher(sequence_map: {int, Sequence}, number: int) -> bool:
    return sequence_map.get(number + 1) is not None


def can_join(sequence_map: {int, Sequence}, number: int) -> bool:
    return has_lower(sequence_map, number) and has_higher(sequence_map, number)


def contains(sequence_map: {int, Sequence}, number: int) -> bool:
    return sequence_map.get(number) is not None


def append_lower(sequence_map: {int, Sequence}, number: int):
    lower = sequence_map.get(number - 1)

    if number > lower.end:
        lower.end += 1
        lower.length += 1

        sequence_map[number] = lower


def append_higher(sequence_map: {int, Sequence}, number: int):
    higher = sequence_map.get(number + 1)

    if number < higher.start:
        higher.start -= 1
        higher.length += 1

        sequence_map[number] = higher


def join(sequence_map: {int, Sequence}, number: int):
    append_lower(sequence_map, number)

    current = sequence_map.get(number)
    higher = sequence_map.get(number + 1)

    new_length = current.length + higher.length
    current.length = new_length
    current.end = higher.end

    for i in range(higher.start, higher.end + 1):
        sequence_map[i] = current


def get_longest(sequence_map: {int, Sequence}):
    longest = 0

    for v in sequence_map.values():
        if v.length > longest:
            longest = v.length

    return longest


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # SET - TIME COMPLEXITY = O(n), SPACE COMPLEXITY = O(n) # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def find_longest_sequence_set(numbers: [int]) -> int:
    longest = 0
    unique_numbers = set(numbers)

    for n in unique_numbers:
        if n - 1 not in unique_numbers:
            current_longest = 1
            number = n

            while n + 1 in unique_numbers:
                current_longest += 1
                number += 1

            longest = max(longest, current_longest)

    return longest


if __name__ == '__main__':
    input_data = [1, 2, 0, 1]
    print(find_longest_sequence(input_data))
