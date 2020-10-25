def num_squares(n: int) -> int:
    possible_squares = get_possible_squares(n)
    current_min = n

    for square in possible_squares:
        times = n // square
        left = n % square
        if left == 0:
            temp_min = times
        else:
            temp_min = times + num_squares(left)

        if temp_min < current_min:
            current_min = temp_min

    return current_min


def get_possible_squares(n: int) -> {int}:
    possible_squares = {}
    last_square = 1
    while pow(last_square, 2) <= n:
        possible_squares[pow(last_square, 2)] = last_square
        last_square = last_square + 1

    return possible_squares


if __name__ == '__main__':
    print(num_squares(8285))
