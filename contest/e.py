

s1 = input()
s2 = input()


def dict_from_str(s):

    d = {}

    for el in s:
        if el not in d:
            d[el] = 0
        d[el] += 1

    return d


print(int(dict_from_str(s1) == dict_from_str(s2)))
