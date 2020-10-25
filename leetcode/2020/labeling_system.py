from queue import PriorityQueue


def find_biggest_string(label: str, limit: int):
    char_map = {}

    for s in label:
        if char_map.get(s) is None:
            char_map[s] = 1
        else:
            char_map[s] = char_map[s] + 1

    char_queue = PriorityQueue()

    for char, amount in char_map.items():
        char_queue.put((-ord(char), amount))

    result = ''
    prev_char = 0

    while not char_queue.empty():
        inverted_char, count = char_queue.get()
        if prev_char != inverted_char:
            if count > limit:
                result += chr(-inverted_char) * limit
                char_queue.put((inverted_char, count - limit))
            else:
                result += chr(-inverted_char) * count
            prev_char = inverted_char

        else:
            if not char_queue.empty():
                next_inverted_char, next_count = char_queue.get()
                result += chr(-next_inverted_char)
                prev_char = next_inverted_char

                if next_count > 1:
                    char_queue.put((next_inverted_char, next_count - 1))

                char_queue.put((inverted_char, count))

    return result


if __name__ == '__main__':
    original_label = 'bcccc'
    char_limit = 2
    print(find_biggest_string(original_label, char_limit))
