def solve(string: str) -> str:
    letters_found = {}

    for letter in string:
        letters_found[letter] = letters_found[letter] + 1 if letters_found.get(letter) is not None else 1

    print(letters_found)

    for letter in letters_found:
        if letters_found[letter] == 1:
            return letter

    return '-1'


if __name__ == '__main__':
    print('First non repeating string.')
    print(solve('abcabcabc'))
