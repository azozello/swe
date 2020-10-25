# делимое  - dividend
# делитель - divider


def gcd(a: int, b: int) -> int:
    while a > 0 and b > 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    return a + b


if __name__ == '__main__':
    A = 130
    B = 50
    print(gcd(A, B), A, B)
