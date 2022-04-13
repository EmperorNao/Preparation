

# https://leetcode.com/problems/maximum-binary-string-after-change/

class Solution:
    def maximumBinaryString(self, binary: str) -> str:

        nzeros = len(list(filter(lambda x: x == '0', binary)))

        for i in range(0, len(binary) - 1):
            if binary[i:i+2] == '00':
                binary[i:i+2] = '10'
                nzeros -= 1

        while nzeros != 1:

            k = len(binary - 1)
            for j in range(len(binary) - 1, 0, -1):
                if binary[j-1:j+1] == '10':
                    binary[j-1:j+1] = '01'
                    k = j
                    break






        return binary
