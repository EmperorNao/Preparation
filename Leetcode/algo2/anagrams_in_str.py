

def dict_from_str(s):

    d = {}
    for el in s:
        if el not in d:
            d[el] = 0
        d[el] += 1

    return d

def sub_el(d, val):
    d[val] -= 1
    if d[val] == 0:
        d.pop(val)

def add_el(d, val):
    if val not in d:
        d[val] = 0

    d[val] += 1


class Solution:
    def findAnagrams(self, s, p):

        outp = []
        if len(s) < len(p):
            return outp


        needle = dict_from_str(p)
        cur = dict_from_str(s[: len(p)])

        if cur == needle:
            outp.append(0)

        for i in range(len(p), len(s)):

            sub_el(cur, s[i - len(p))
            add_el(cur, s[i])
            if cur == needle:
                outp.append(i - len(p) + 1)

        return outp
