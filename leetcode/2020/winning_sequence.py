def create_winning_sequence(start: int, peak: int, num: int):
    result = []
    val = start
    for i in range(num):
        result.append(val)
        if i < peak:
            val += 1
        else:
            val -= 1
    return result


def winning_sequence(num: int, upper_end: int, lower_end: int) -> [int]:
    if num // 2 > upper_end - lower_end:
        return [-1]
    if num % 2 == 1 and num // 2 == upper_end - lower_end:
        return create_winning_sequence(upper_end - num // 2, num // 2, num)
    else:
        return create_winning_sequence(upper_end - num // 2 + 1, num // 2 - 1, num)


if __name__ == '__main__':
    print(f'{winning_sequence(1, 10, 10)} == [10]')
    print(f'{winning_sequence(3, 10, 10)} == [-1]')
    print(f'{winning_sequence(3, 10, 9)} == [9, 10, 9]')
    print(f'{winning_sequence(4, 10, 3)} == [9, 10, 9, 8]')
    print(f'{winning_sequence(5, 10, 3)} == [9, 10, 9, 8, 7]')
    print(f'{winning_sequence(4, 10, 8)} == [9, 10, 9, 8]')
    print(f'{winning_sequence(5, 10, 8)} == [8, 9, 10, 9, 8]')
    print(f'{winning_sequence(5, 10, 7)} == [9, 10, 9, 8, 7]')
    print(f'{winning_sequence(6, 10, 8)} == [-1]')
    print(f'{winning_sequence(6, 10, 7)} == [8, 9, 10, 9, 8, 7]')
