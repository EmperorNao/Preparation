# class Solution:
#
#     def fill(self, unique, i):
#
#         res = []
#         cnt = 0
#         while i != 0:
#             if i & 1:
#                 res.append(unique[cnt])
#             cnt += 1
#             i >>= 1
#         return res
#
#
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#
#         unique = nums
#         out = [[]]
#
#         n = len(unique)
#         for i in range(1, 2 ** n):
#             out.append(self.fill(unique, i))
#
#         return out
#
#


class Solution:

    def subset(self, values, pos, cur, sol):

        sol.append(cur[:])
        if not pos:
            return

        cur.append(values[pos])

        cur.pop(values[pos])



    def subsets(self, nums: List[int]) -> List[List[int]]:

        unique = nums
        out = [[]]

        n = len(unique)
        for i in range(1, 2 ** n):
            out.append(self.fill(unique, i))

        return out
