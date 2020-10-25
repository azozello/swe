import itertools
import operator

if __name__ == '__main__':
    array = [1, 2, 3, 4]

    c = 0

    for i in itertools.cycle(itertools.count(0, 2)):
        if c == 9:
            break
        print(i)
        c += 1

    print(list(map(operator.mul, [1, 2], [2, 4])))

    print(list(itertools.repeat(25, 4)))

    print(list(itertools.product([1, 2, 3], repeat=2)))

    print(list(itertools.permutations([1, 2, 3, 4], 4)))

    print(list(itertools.combinations([1, 2, 3, 4], 4)))

    print(list(itertools.accumulate([1, 2, 3])))
