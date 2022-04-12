class Solution:

    def dist(self, w1, w2, i, j):

        if i >= len(w1):
            return max(0, len(w2) - j)
        if j >= len(w2):
            return max(0, len(w1) - i)

        if self.m[i][j] != -1:
            return self.m[i][j]

        if w1[i] == w2[j]:
            self.m[i][j] = self.dist(w1, w2, i + 1, j + 1)
        else:
            self.m[i][j] = min(self.dist(w1, w2, i + 1, j) + 1, self.dist(w1, w2, i, j + 1) + 1, self.dist(w1, w2, i + 1, j + 1) + 1)

        return self.m[i][j]

    def minDistance(self, word1: str, word2: str) -> int:
        self.m = [[-1 for i in range(len(word2))] for j in range(len(word1))]

        return self.dist(word1, word2, 0, 0)
