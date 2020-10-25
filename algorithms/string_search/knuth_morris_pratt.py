def generate_prefix_table(pattern: str) -> [int]:
    length = 0
    i = 1
    prefix_table = [0 for c in pattern]

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            prefix_table[i] = length
        else:
            if length != 0:
                length = prefix_table[length - 1]
                i -= 1
            else:
                prefix_table[i] = 0
        i += 1

    return prefix_table


def find_in_text(text: str, pattern: str) -> int:
    loc = -1
    prefix_table = generate_prefix_table(pattern)
    t_i, p_i = [0, 0]

    while loc < 0 or t_i < len(text):
        if pattern[p_i] == text[t_i]:
            if p_i == len(pattern) - 1:
                loc = t_i - len(pattern) + 1
                return loc
            else:
                p_i += 1
        else:
            if p_i != 0:
                p_i = prefix_table[p_i - 1]

        t_i += 1

    return loc


if __name__ == '__main__':
    print('Knuth Morris Pratt')
    # word_to_find = 'acacagt'
    word_to_find = 'from'
    search_string = 'Hello from Alexa'
    start_index = find_in_text(search_string, word_to_find)

    print(start_index, search_string[start_index])
