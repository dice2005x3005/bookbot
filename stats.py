def get_num_words(text):
    x = text.split()
    num_words = len(x)
    return f'Found {num_words} total words'

def get_counts(text):
    d = dict()
    x = text.lower()
    y = x.split()
    for i in y:
        for n in i:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
    return d

def sort_on(items):
    return items["num"]

def sorted_counts(dic):
    lst = []
    for k,v in dic.items():
        x = {"char": k, "num": v}
        lst.append(x)
    lst.sort(reverse=True, key=sort_on)
    return lst
