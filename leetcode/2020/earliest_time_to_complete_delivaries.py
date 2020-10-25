def earliest_time(buildings: int, opening: [int], offload: [int]) -> int:
    opening.sort()
    offload.sort(reverse=True)
    res = 0
    for i, time in enumerate(opening):
        res = max(res, time + offload[i * 4])
    return res


if __name__ == '__main__':
    print(earliest_time(2, [8, 10], [2, 2, 3, 1, 8, 7, 4, 5]))
