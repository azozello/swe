def solve(numbers: [int]) -> int:
    missing = 0

    for i in range(1, len(numbers) + 1):
        missing += i
        missing -= numbers[i - 1]

    return missing


if __name__ == '__main__':
    print('Missing Number')
    print(solve([3, 0, 1]))
