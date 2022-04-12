class Solution:

    def search(self, board, i, j, word, pos):

        if pos >= len(word):
            return True

        if not (0 <= i < self.m and 0 <= j < self.n):
            return False

        if self.visited[i][j] or board[i][j] != word[pos]:
            return False

        self.visited[i][j] = True

        ok = self.search(board, i + 1, j, word, pos + 1) or \
        self.search(board, i, j + 1, word, pos + 1) or \
        self.search(board, i - 1, j, word, pos + 1) or \
        self.search(board, i, j - 1, word, pos + 1)

        self.visited[i][j] = False

        return ok


    def exist(self, board: List[List[str]], word: str) -> bool:

        self.m = len(board)
        self.n = len(board[0])

        self.visited = [[0 for i in range(self.n)] for j in range(self.m)]

        for i in range(self.m):
            for j in range(self.n):
                if self.search(board, i, j, word, 0):
                    return True

        return False
