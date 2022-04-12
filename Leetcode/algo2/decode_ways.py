class Solution:

    def is_val(self, s):

        if s[0] == '0':
            return 0
        if 0 < int(s) <= 26:
            return 1


    def decode_ways(self, s, l):

        if l >= len(s):
            return 1

        if self.decode[l] != -1:
            return self.decode[l]

        if l == len(s) - 1:
            self.decode[l] = self.is_val(s[l])
        else:
            self.decode[l] = 0
            if self.is_val(s[l:l + 1]) and self.decode_ways(s, l + 1) != -1:
                self.decode[l] += self.decode_ways(s, l + 1)
            if self.is_val(s[l:l + 2]) and self.decode_ways(s, l + 2) != -1:
                self.decode[l] += self.decode_ways(s, l + 2)

        return self.decode[l] if self.decode[l] != 0 else -1



    def numDecodings(self, s: str) -> int:

        self.decode = [-1 for i in range(len(s))]
        return self.decode_ways(s, 0) if  self.decode_ways(s, 0) != -1 else 0
