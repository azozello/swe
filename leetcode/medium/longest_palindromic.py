def longest_palindrome(s: str) -> str:
    max_length = 1
    start = 0
    word_length = len(s)

    low = 0
    high = 0

    for i in range(1, word_length):
        low = i - 1
        high = i

        while low >= 0 and high < word_length and s[low] == s[high]:
            test_l = s[low]
            test_h = s[high]
            if high - low + 1 > max_length:
                max_length = high - low + 1
                start = low
            low -= 1
            high += 1

        low = i - 1
        high = i + 1

        while low >= 0 and high < word_length and s[low] == s[high]:
            if high - low + 1 > max_length:
                max_length = high - low + 1
                start = low
            low -= 1
            high += 1

    return s[start: start + max_length]


if __name__ == '__main__':
    print('5. Longest Palindromic Substring')
    print(longest_palindrome('cbbdddaae'))
