import time


def generate_parenthesis(n: int) -> [str]:
    result = []
    used = {}

    def get_possible(lp: int, rp: int, string: str) -> [str]:
        possible = []

        if used.get(string) is None:
            used[string] = []

        if lp > 0 and '(' not in used[string]:
            possible.append('(')
        if rp > lp and ')' not in used[string]:
            possible.append(')')

        return possible

    def recursively_add(lp, rp, string, calls):
        current_possible = get_possible(lp, rp, string)

        if len(current_possible) == 0 and lp == n and rp == n:  # stop condition
            return calls
        elif len(current_possible) == 0:  # backtrack condition
            if lp == 0 and rp == 0:
                result.append(string)

            last_placed = string[-1:]

            if last_placed == '(':
                lp += 1
            else:
                rp += 1

            return recursively_add(lp, rp, string[:(len(string) - 1)], calls + 1)
        else:
            used[string].append(current_possible[0])
            return recursively_add(lp - 1 if current_possible[0] == '(' else lp,
                                   rp - 1 if current_possible[0] == ')' else rp,
                                   string + current_possible[0],
                                   calls + 1)

    print(f"Recursion steps: {recursively_add(n, n, '', 1)}")
    return result


if __name__ == '__main__':
    print('Generate Parentheses')
    start_time = int(round(time.time() * 1000))
    print(generate_parenthesis(5))
    finish_time = int(round(time.time() * 1000))
    print(f"Mils took: {finish_time - start_time}")
