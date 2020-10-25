import re


def solve(toys_count, toys, quotes_count, quotes, top_count):
    toys_freq = {toy: [0, 0] for toy in toys}

    for quote in quotes:
        quote_toy = {toy: False for toy in toys}
        for word in quote.lower().split():
            word = re.sub('[^a-z]', '', word)
            if word in toys_freq:
                toys_freq[word][0] += 1
                if not quote_toy[word]:
                    quote_toy[word] = True
                    toys_freq[word][1] += 1

    return [w[0] for w in sorted(toys_freq.items(), key=lambda x: (-x[1][0], -x[1][1], x[0]))[:top_count]]


if __name__ == '__main__':
    print('Top N Buzzwords')
    source_toys = ["elmo", "elsa", "legos", "drone", "tablet", "warcraft"]
    source_quotes = [
        "Elmo is the hottest of the season! Elmo will be on every kid's wishlist!",
        "The new Elmo dolls are super high quality",
        "Expect the Elsa dolls to be very popular this year, Elsa!",
        "Elsa and Elmo are the toys I'll be buying for my kids, Elsa is good",
        "For parents of older kids, look into buying them a drone",
        "Warcraft is slowly rising in popularity ahead of the holiday season"
    ]
    print(solve(6, source_toys, 6, source_quotes, 2))
