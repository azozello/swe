def solve(array: [int], target: int):
    target = target - 30

    pair_map = {}

    for i in range(len(array)):
        pair_map[array[i]] = i

    last_max = 0
    r_i, r_j = [0, 0]

    for key in pair_map.keys():
        if pair_map.get(target - key) is not None and max([key, target - key]) > last_max:
            last_max = max([key, target - key])
            r_i = pair_map[key]
            r_j = pair_map[target - key]

    return r_i, r_j


if __name__ == '__main__':
    print('Find Pair With Given Sum')
    t = 90
    print(solve([20, 50, 40, 25, 30, 10], t))
