def get_device_names(num: int, names: [str]) -> [str]:
    names_map = {}
    result = []

    for n in names:
        if names_map.get(n) is None:
            result.append(n)
            names_map[n] = 1
        else:
            number = names_map[n]
            result.append(f'{n}{number}')
            names_map[n] = number + 1

    return result


if __name__ == '__main__':
    device_names = ["switch", "tv", "switch", "tv", "switch", "tv"]
    print(get_device_names(6, device_names))
