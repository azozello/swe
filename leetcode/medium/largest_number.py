def largest(nums: [int]) -> str:
    max_len = len(str(max(nums)))
    result = ''

    def compare(a: int):
        dif = max_len - len(str(a))
        return (a * pow(10, dif)) + (dif / a)

    sorted_nums = sorted(nums, key=compare, reverse=True)

    return result.join([str(n) for n in sorted_nums])


if __name__ == '__main__':
    integers = [121, 13]
    print(largest(integers))
    print('12121')
