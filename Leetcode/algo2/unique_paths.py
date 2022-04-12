class Solution:

    def search(self, i, j):
        if not(0 <= i < self.m and 0 <= j < self.n):
            return 0

        if i == self.m - 1 and j == self.n - 1:
            return 1

        if self.matr[i][j] != -1:
            return self.matr[i][j]

        self.matr[i][j] = self.search(i + 1, j) + self.search(i, j + 1)
        return self.matr[i][j]


    def uniquePaths(self, m: int, n: int) -> int:

        self.m = m
        self.n = n
        self.matr = [[-1 for i in range(self.n)] for j in range(self.m)]

        return self.search(0, 0)
