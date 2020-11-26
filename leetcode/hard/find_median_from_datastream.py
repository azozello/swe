# Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.
#
# For example,
# [2,3,4], the median is 3
#
# [2,3], the median is (2 + 3) / 2 = 2.5
#
# Design a data structure that supports the following two operations:
#
# void addNum(int num) - Add a integer number from the data stream to the data structure.
# double findMedian() - Return the median of all elements so far.
from bisect import bisect_left


class MedianFinder:

    def __init__(self):
        self.m_index = -1
        self.is_odd = False
        self.values = []

    def add_num(self, num: int) -> None:
        position = bisect_left(self.values, num)
        self.values.insert(position, num)

        if not self.is_odd:
            self.m_index = self.m_index + 1

        self.is_odd = not self.is_odd

    def find_median(self) -> float:
        if self.m_index == -1:
            return 0

        if self.is_odd:
            return self.values[self.m_index]
        else:
            return (self.values[self.m_index] + self.values[self.m_index + 1]) / 2


if __name__ == '__main__':
    finder = MedianFinder()
    finder.add_num(1)
    finder.add_num(2)
    print(finder.find_median())
    finder.add_num(3)
    print(finder.find_median())
    print('')
