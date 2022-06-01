inlist = open("article.txt", "r").read().split()


def longest_words(inlist):
    max_length = len(max(inlist, key=len))
    sought_words = [word for word in inlist if len(word) == max_length]
    if len(sought_words) == 1:
        return sought_words[0]
    return sought_words


print(longest_words(inlist))
