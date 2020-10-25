def get_char_map(string: str) -> {}:
    result = {}
    for index, char in enumerate(string):
        if result.get(char) is not None:
            result[char][1] = index
        else:
            result[char] = [index, index]

    return result


def partition_labels(string: str) -> [str]:
    result = []

    char_map = get_char_map(string)

    char_map_keys = list(char_map.keys())
    char_map_keys.reverse()

    while len(char_map) > 0:
        current_char = char_map_keys.pop()
        first, last = char_map.pop(current_char)

        if first != last:
            temp_string = string[first: last + 1]
            temp_string = temp_string.replace(current_char, '')

            used_chars = set()

            while len(temp_string) > 0:
                temp_char = temp_string[0]
                temp_first, temp_last = char_map[temp_char]

                if temp_first > first and temp_last < last:
                    used_chars.add(temp_char)
                    temp_string = temp_string.replace(temp_char, '')
                    if len(temp_string) == 0:
                        result.append(string[first: last + 1])
                        for char_to_remove in used_chars:
                            char_map.pop(char_to_remove)
                            char_map_keys.remove(char_to_remove)

                elif temp_first < first:
                    temp_string = string[temp_first: first] + temp_string
                    first = temp_first
                    temp_string = temp_string.replace(temp_char, '')
                    used_chars.add(temp_char)

                elif temp_last > last:
                    temp_string = temp_string + string[last + 1: temp_last + 1]
                    last = temp_last
                    temp_string = temp_string.replace(temp_char, '')
                    used_chars.add(temp_char)

    return result


if __name__ == '__main__':
    print('Partition Labels')
    print(partition_labels('defegdehijhklijababcbaca'))
