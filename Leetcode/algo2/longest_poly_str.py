class Solution:

    def fromcenter(self, s, l, r):
        while (l >= 0 and r < self.n and s[l] == s[r]):
            l -= 1
            r += 1

        return [l + 1, r - 1]


    def longestPalindrome(self, s: str) -> str:

        self.n = len(s)

        self.max_poly = 1
        self.poly = [0, 0]
        for i in range(0, self.n):

            ans = self.fromcenter(s, i, i + 1)
            curlen = ans[1] - ans[0] + 1
            if curlen > self.max_poly:
                self.max_poly = curlen
                self.poly = ans


            ans = self.fromcenter(s, i, i)
            curlen = ans[1] - ans[0] + 1
            if curlen > self.max_poly:
                self.max_poly = curlen
                self.poly = ans

        return s[self.poly[0]: self.poly[1] + 1]
