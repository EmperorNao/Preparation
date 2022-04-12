


class Solution:

    def visit_island(self, grid, i, j):

        if not (0 <= i < self.m) or not (0 <= j < self.n) or grid[i][j] == '0' or self.visited[i][j] == '1':
            return 0

        self.visited[i][j] = '1'

        self.visit_island(grid, i - 1, j)
        self.visit_island(grid, i + 1, j)
        self.visit_island(grid, i, j - 1)
        self.visit_island(grid, i, j + 1)

        return 1

    def numIslands(self, grid) -> int:

        self.m = len(grid)
        self.n = len(grid[0])

        self.visited = [[0 for i in range(self.n)] for j in range(self.m)]

        cnt = 0
        for i in range(self.m):
            for j in range(self.n):
                cnt += self.visit_island(grid, i, j)

        return cnt
