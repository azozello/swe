# time complexity = O(N log (log N))
def first_n_primes(n: int) -> [int]:
    result_primes = []
    banned = {}
    cur = 2

    while cur <= n:
        if banned.get(cur) is None:
            result_primes.append(cur)
            temp = cur
            while temp <= n:
                banned[temp] = True
                temp += cur

        cur += 1

    return result_primes


if __name__ == '__main__':
    print(first_n_primes(100))
