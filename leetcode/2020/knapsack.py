from collections import namedtuple


def knapsack(max_weight: int, items: [], amount: int) -> int:
    memory = [
        [0 for i in range(max_weight + 1)]
        for i in range(amount + 1)
    ]

    for i in range(amount + 1):
        for w in range(max_weight + 1):
            item = items[i - 1]
            if w == 0 or i == 0:
                continue
            elif item.weight <= w:
                memory[i][w] = max(item.value + memory[i - 1][w - item.weight],
                                   item.value)
            else:
                memory[i][w] = memory[i - 1][w]

    return memory[amount][max_weight]


if __name__ == '__main__':
    weights = [1, 2, 3]
    values = [6, 10, 12]
    number = 3

    Item = namedtuple('Item', ['weight', 'value'])

    print(knapsack(5,
                   [Item._make([weights[i], values[i]]) for i in range(number)],
                   number))
