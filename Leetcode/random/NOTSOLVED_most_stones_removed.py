


### https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class Solution:

    def dfs(self, d, visited, startx, starty):

        for el in d[start]:

            pass


    def removeStones(self, stones: List[List[int]]) -> int:

        d = {}

        max_row = -1
        max_col = -1
        for el in stones:
            l = el[0]
            r = el[1]

            max_row = max(max_row, l)
            max_col = max(max_col, r)

            if l not in d:
                d[l] = []
            d[l].append(r)

            if r not in d:
                d[r] = []
            d[r].append(l)

        visited = [[0 for i in range(max_col)] for j in range(max_row)]

        dist, v = self.dfs(d, visited, stones[0], stones[1])

        dist, v = self.dfs(d, visited, v)
        return dist
