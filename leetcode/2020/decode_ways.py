def build_possibility_map(s: str) -> {int: [int]}:
    possibility_map = {}
    i_1, i_2 = [0, 0]
    prev_count = 0

    while i_1 < len(s) and i_2 < len(s):
        if i_1 == i_2:
            if possibility_map.get(prev_count) is None:
                possibility_map[prev_count] = set()

            if 0 < int(s[i_1]) < 27:
                possibility_map[prev_count].add(s[i_1])

            i_2 += 1

        else:
            if possibility_map.get(prev_count) is None:
                possibility_map[prev_count] = set()

            cur_index = int(f'{s[i_1]}{s[i_2]}')

            if 0 < cur_index < 27:
                possibility_map[prev_count].add(cur_index)

            prev_count += 1
            i_1 += 1

    return possibility_map


def build_possibilities(pos_map: {int: [int]}, result_set: [int], cur_len: int, max_len: int, cur_seq: [int]):
    # stop condition:
    if cur_len == max_len:
        result_set.add(cur_seq)
        return

    # next item
    for pos in pos_map[cur_len]:
        build_possibilities(pos_map, result_set, cur_len + len(f'{pos}'), max_len, cur_seq + tuple([int(pos)]))


def count_decode(s: str) -> int:
    possibility_map = build_possibility_map(s)
    result_set = set()

    build_possibilities(possibility_map, result_set, 0, len(s), tuple())

    print(result_set)

    return len(result_set)


if __name__ == '__main__':
    print(count_decode('2101'))
