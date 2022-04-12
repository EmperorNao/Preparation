
class row:

    def __init__(self, sold, ind):
        self.sold = sold
        self.ind = ind

    def __lt__(self, obj):

        if self.sold < obj.sold:
            return True
        elif self.sold == obj.sold:
            return self.ind < obj.ind
        return False

    def __str__(self):
        return "sold: " + str(self.sold) + " | ind: " + str(self.ind)


class Solution:

    def find(self, a):

        l = -1
        r = len(a)
        while r - l > 1:
            m = (r + l) // 2

            if a[m] <= 0:
                r = m
            else:
                l = m

        return l

    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        m = len(mat)
        n = len(mat[0])

        rows = []
        for ind, r in enumerate(mat):
            rows.append(row(self.find(r), ind))

        for el in rows:
            print(el)
        sort = sorted(rows)
        return list(map(lambda x: x.ind, sort))[:k]
