def count_words(filename):
    fh = open(filename)
    f = fh.read()
    d = {}
    x = f.split()
    for i in x:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    print(d)
    return d
def most_frequent_word(d):
    frequency = 0
    for key, value in d.items():
        if value>frequency:
            frequency=value
            word=key
    print(word)

dict = count_words("C:\\Users\\sonab\\Downloads\\alice (1).txt")
most_frequent_word(dict)