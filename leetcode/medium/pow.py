def my_pow(x: float, n: int) -> float:
    is_positive = n > 0
    mul = x
    res = 1

    while n != 0:
        if n % 2 == 1:
            res *= mul
        mul = mul * mul
        n = int(n / 2)

    return res if is_positive else 1 / res


if __name__ == '__main__':
    print(my_pow(2, -4))
