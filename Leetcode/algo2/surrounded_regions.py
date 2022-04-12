

class Solution:

    def dfs(self, board, i, j, to_capture):

        if not (0 <= i < self.m and 0 <= j < self.n):
            return 0

        if self.visited[i][j] or board[i][j] == 'X':
            return 1


        to_capture.append([i, j])
        self.visited[i][j] = 1

        ok1 = self.dfs(board, i + 1, j, to_capture)
        ok2 = self.dfs(board, i - 1, j, to_capture)
        ok3 = self.dfs(board, i, j + 1, to_capture)
        ok4 = self.dfs(board, i, j - 1, to_capture)

        return ok1 and ok2 and ok3 and ok4


    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        self.m = len(board)
        self.n = len(board[0])
        self.visited = [[0 for i in range(self.n)] for j in range(self.m)]

        print()

        to_capture = []
        for i in range(self.m):
            for j in range(self.n):
                capture = []
                if self.dfs(board, i, j, capture):
                    to_capture += capture

                print()

        for el in to_capture:
            board[el[0]][el[1]] = 'X'
