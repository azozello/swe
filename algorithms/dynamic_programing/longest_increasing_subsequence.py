def find_lis(array: [int]) -> [int]:
    length = len(array)

    lls_array = [1] * length

    for cur in range(1, length):
        for prev in range(cur):
            if array[cur] > array[prev] and lls_array[cur] < lls_array[prev] + 1:
                lls_array[cur] = lls_array[prev] + 1

    maximum = 1

    for i in range(length):
        maximum = max(maximum, lls_array[i])

    return maximum


if __name__ == '__main__':
    source_list = [3, 10, 2, 11]
    print(find_lis(source_list))
