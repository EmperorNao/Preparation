

class Solution:

    def dfs(self, v):

        if self.visited[v]:
            return 0

        self.visited[v] = 1
        for i in range(self.n):
            if i != v and self.isConnected[i][v]:
                self.dfs(i)

        return 1


    def findCircleNum(self, isConnected) -> int:

        self.n = len(isConnected)
        self.visited = [0 for i in range(self.n)]
        self.isConnected = isConnected

        cnt = 0

        for v in range(self.n):
            cnt += self.dfs(v)

        return cnt
