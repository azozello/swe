def solve(string: str, k: int) -> [str]:
    result = set()

    for i in range(len(string) - k + 1):
        cur_substring = string[i: i + k]
        if len(set(string[i: i + k])) == k:
            result.add(cur_substring)

    return result


if __name__ == '__main__':
    print('Substrings of size K with K distinct chars')
    result_list = solve('awaglknagawunagwkwagl', 4)
    print(result_list)
    print(len(result_list))
