def get_array(num: int, packs: [int]) -> int:
    max_value = 0

    for p in packs:
        if p > max_value:
            max_value = p

    return min(num, max_value)


if __name__ == '__main__':
    number = 4
    groups = [3, 2, 3, 5]

    print(get_array(number, groups))
