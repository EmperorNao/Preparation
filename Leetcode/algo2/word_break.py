class Solution:

    def is_breakable(self, s, d, l):

        if l >= len(s):
            return 1

        if self.m[l] != -1:
            return self.m[l]

        for i in range(min(self.max_word, len(s) - l)):
            if s[l: l + i + 1] in d and self.is_breakable(s, d, l + i + 1):
                self.m[l] = 1
                return 1

        self.m[l] = 0
        return 0


    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        self.max_word = 1
        for el in wordDict:
            if len(el) > self.max_word:
                self.max_word = len(el)

        self.m = [-1 for i in range(len(s))]

        return self.is_breakable(s, wordDict, 0)
