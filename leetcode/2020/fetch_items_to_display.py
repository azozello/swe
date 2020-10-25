def fetch_items(items_count: int, items: {}, parameter: int, order: int, per_page: int, page: int) -> []:
    items.sort(key=lambda x: x[parameter], reverse=order == 1)
    result = []

    for i in range(page * per_page, min(items_count, page * per_page + per_page)):
        result.append(items[i][0])

    return result


if __name__ == '__main__':
    number = 3
    unordered_items = [["item1", 10, 15], ["item2", 3, 4], ["item3", 17, 8]]
    sort_parameter = 1
    sort_order = 0
    items_per_page = 2
    page_number = 1
    print(fetch_items(number, unordered_items, sort_parameter, sort_order, items_per_page, page_number))
