def most_common_word(paragraph, banned):
    clean_string = paragraph.replace('.', '').replace(',', '').replace('!', '').replace('?', '').replace(';', '').replace('`', '')
    count_allowed = {}
    banned = [b.lower() for b in banned]
    for word in clean_string.split(' '):
        word = word.lower()
        if word not in banned:
            if count_allowed.get(word) is not None:
                count_allowed[word] = count_allowed[word] + 1
            else:
                count_allowed[word] = 1

    most_used = ''
    times = 0

    for key in count_allowed.keys():
        if count_allowed[key] > times:
            times = count_allowed[key]
            most_used = key

    return most_used


if __name__ == '__main__':
    print('Most Common Word')
    print(most_common_word('Bob hit a ball, the hit BALL flew far after it was hit.', ['hit']))
