


def str_to_list(s):

    res = []
    for el in s:
        if el == '#':
            if len(res):
                res.pop()
        else:
            res.append(el)
    return res



class Solution:


    def backspaceCompare(self, s: str, t: str) -> bool:

        return str_to_list(s) == str_to_list(t)
