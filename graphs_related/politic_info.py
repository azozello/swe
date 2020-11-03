import matplotlib.pyplot as plt
import numpy as np


def count_percentage(max_values: [int], values: [int]):
    if len(max_values) != len(values):
        return []

    return [
        values[i] / max_values[i] * 100
        for i in range(len(max_values))
    ]


if __name__ == '__main__':
    max_ranges = [150, 65, 65, 250, 115, 90, 80]
    # div = [r / 2 for r in max_ranges]
    average = [90, 40, 40, 155, 70, 56, 48]
    denys = [121, 24, 21, 132, 83, 37, 55]
    pasha = [102, 22, 40, 158, 72, 41, 55]
    sasha = [104, 22, 19, 161, 87, 35, 63]
    ann = [98, 28, 31, 152, 69, 45, 51]

    labels = [
        'Строгость - дозволенность',
        'Антирасизм - расизм',
        'Атеизм - религиозность',
        'Капитализм - социализм',
        'Антилиберализм - либерализм',
        'Прогрессивность - реакционность',
        'Милитаризм - пацифизм'
    ]

    N = 7

    fig, ax = plt.subplots()

    ind = np.arange(N)  # the x locations for the groups

    width = 0.15  # the width of the bars
    ax.set_xlim([0, 180])
    ax.barh(ind - (width * 2), average, width, label='Average')
    ax.barh(ind - width, pasha, width, label='Pasha')
    ax.barh(ind, sasha, width, label='Sasha')
    ax.barh(ind + width, denys, width, label='Denys')
    ax.barh(ind + (width * 2), ann, width, label='Ann')

    # ax.plot([50, 50], [-0.4, 6.6], "k--")

    ax.set_title('В баллах')
    ax.set_yticks(ind + width / 2)
    ax.set_yticklabels(labels)

    ax.legend()
    ax.autoscale_view()

    plt.show()

    # plt.rcdefaults()
    # fig, ax = plt.subplots()
    # ax.set_xlim([0, 105])
    #
    # # Example data
    # y_pos = np.arange(len(labels))
    #
    # ax.barh(y_pos, count_percentage(max_ranges, pasha), align='center', color='orange')
    # ax.set_yticks(y_pos)
    # ax.set_yticklabels(labels)
    # ax.invert_yaxis()  # labels read top-to-bottom
    # ax.set_xlabel('Performance')
    # ax.set_title('How fast do you want to go today?')
    #
    # plt.show()

    # x = [
    #     datetime.datetime(2011, 1, 4, 0, 0),
    #     datetime.datetime(2011, 1, 5, 0, 0),
    #     datetime.datetime(2011, 1, 6, 0, 0)
    # ]
    # x = date2num(x)
    #
    # y = [4, 9, 2]
    # z = [1, 2, 3]
    # k = [11, 12, 13]

    # ax = plt.subplot(111)
    # ax.bar(labels, denys, width=0.2, color='r', align='center')
    # ax.bar(labels, pasha, width=0.2, color='b', align='center')
    #
    # plt.show()
