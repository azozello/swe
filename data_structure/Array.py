import math


# Time complexity O(n), Space complexity O(n)
def rotate(array: [int], n: int) -> [int]:
    length = len(array)
    new_array = []

    for i in range(length - n):
        new_array.append(array[i + n])

    for i in range(n):
        new_array.append(array[i])

    return new_array


# Time complexity O(n), Space complexity O(1)
def rotate_efficient(array: [int], n: int) -> [int]:
    length = len(array)
    gcd = math.gcd(length, n)

    for i in range(gcd):
        temp = array[i]
        j = i

        while True:
            k = j + n

            if k >= length:
                k = k - length
            if k == i:
                break

            array[j] = array[k]
            j = k

        array[j] = temp

    return array


if __name__ == '__main__':
    print(rotate([1, 2, 3, 4, 5, 6, 7], 2))
    print(rotate_efficient([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], 3))

