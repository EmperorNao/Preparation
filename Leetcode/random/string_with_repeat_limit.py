
def d_from_s(s):

    d = {}
    for el in s:
        if el not in d:
            d[el] = 0
        d[el] += 1

    return d


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:

        d = d_from_s(s)
        sort = sorted(d.keys(), reverse=True)

        o = []
        greatest = 0
        pos = 0
        next = 1

        while pos < len(sort):
            if pos == greatest:

                num_to = min(repeatLimit, d[sort[pos]])
                o.append(sort[pos] * num_to)

                d[sort[pos]] -= num_to

                next_pos = next

                if not d[sort[pos]]:
                    greatest = next
                    next += 1

                pos = next_pos

            else:

                num_to = 1
                o.append(sort[pos] * num_to)

                d[sort[pos]] -= num_to
                next_pos = greatest

                if not d[sort[pos]]:
                    next += 1

                pos = next_pos

        return "".join(o)
