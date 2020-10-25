def solve(string: str, k: int) -> [str]:
    def find_substrings(long_string: str) -> [str]:
        substrings = []
        cur_length = k
        while cur_length <= len(long_string):
            index = 0
            while index <= len(long_string) - cur_length:
                if len(set(long_string[index:index + cur_length])) == k:
                    substrings.append(long_string[index:index + cur_length])
                index += 1
            cur_length += 1
        return substrings

    found_strings = []
    i = 0

    while i <= len(string) - k:
        unique_chars = set()
        j = i
        last_unique = i
        while (k_len := len(unique_chars)) < k + 1 and j < len(string):
            unique_chars.add(string[j])
            if k_len <= k:
                last_unique += 1
            j += 1
        found_strings += find_substrings(string[i:last_unique])
        i += j - k

    return found_strings


if __name__ == '__main__':
    print('Substrings with exactly K distinct chars')
    print(solve('aabab', 2))
