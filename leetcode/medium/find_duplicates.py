if __name__ == '__main__':
    print('Find all duplicates in array')

    array = [1, 2, 4, 6, 3, 5, 2, 4, 1]

    dup = set()

    for i in range(0, len(array)):
        sp = array[i]
        fp = array[i * 2] if i * 2 < len(array) else (i * 2) - len(array)
        if i * 2 < len(array):
            if array[i] == array[i * 2] and i != i * 2:
                dup.add(array[i])
        else:
            if array[i] == array[(i * 2) - len(array)] and i != (i * 2) - len(array):
                dup.add(array[i])

    print(dup)
