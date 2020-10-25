def solve(array: [int], target: int) -> int:
    result = 0
    unique_map = {}

    for number in array:
        if unique_map.get(number) is None:
            unique_map[number] = 1
        elif number * 2 == target:
            unique_map[number] += 1

    for key in unique_map.keys():
        if key == target - key:
            if unique_map.get(key) is not None and unique_map[key] >= 2:
                result += 1
                unique_map[key] -= 2
        elif unique_map.get(target - key) is not None and unique_map[target - key] > 0 and unique_map[key] > 0:
            result += 1
            unique_map[key] -= 1
            unique_map[target - key] -= 1

    return result


def unique_pairs(nums, target):
    res = {}
    out = set()

    for index, value in enumerate(nums):
        if target - value in res:
            out.add((value, target-value))
        else:
            res[value]=index

    return len(out)


if __name__ == '__main__':
    print('Two Sum - Unique Pairs')
    # [1, 1, 2, 45, 46, 46]
    # [1, 1]
    # [1, 5, 1, 5]
    print(unique_pairs([1, 1, 2, 45, 46, 46], 47))
    print(unique_pairs([1, 1, 1, 1], 2))
    print(unique_pairs([1], 2))
    print(unique_pairs([1, 5, 1, 5], 6))
