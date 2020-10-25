# Given a non-empty array of integers, return the k most frequent elements.
def top_frequent(nums: [int], k: int):
    frequency = {}

    for n in nums:
        if frequency.get(n) is None:
            frequency[n] = 1
        else:
            frequency[n] = frequency[n] + 1

    return [v[0] for v in sorted(frequency.items(), key=lambda x: x[1])[-k:]]


if __name__ == '__main__':
    print(top_frequent([4, 1, -1, 2, -1, 2, 3], 2))
