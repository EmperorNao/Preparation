class Solution:

    def lcs(self, w1, w2, i, j):

        if i >= len(w1) or j >= len(w2):
            return 0

        if self.m[i][j] != -1:
            return self.m[i][j]

        if w1[i] == w2[j]:
            self.m[i][j] = 1 + self.lcs(w1, w2, i + 1, j + 1)

        else:
            self.m[i][j] = max(self.lcs(w1, w2, i + 1, j), self.lcs(w1, w2, i, j + 1))

        return self.m[i][j]


    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        self.m = [[-1 for i in range(len(text2))] for j in range(len(text1))]

        return self.lcs(text1, text2, 0, 0)
