def solve(products: [str], word: str) -> [[str]]:
    prefix_map = {}

    prefixes = []

    for i in range(len(word)):
        prefixes.append(word[:i + 1])
        prefix_map[word[:i + 1]] = []

    for prefix in prefixes:
        print(prefix)

    for product in products:
        for prefix in prefixes:
            if product.startswith(prefix):
                prefix_map[prefix].append(product)
                prefix_map[prefix].sort()
                if len(prefix_map[prefix]) > 3:
                    prefix_map[prefix] = prefix_map[prefix][:3]
            else:
                break

    return [prefix_map[key] for key in prefix_map.keys()]


if __name__ == '__main__':
    print('Search Suggestions System')
    dictionary = ['mobile', 'mouse', 'moneypot', 'monitor', 'mousepad']
    search_word = 'mouse'

    for suggestions in solve(dictionary, search_word):
        print(suggestions)
