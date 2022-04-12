class Solution:

    def fill(self, unique, i):

        res = []
        cnt = 0
        while i != 0:
            if i & 1:
                res.append(unique[cnt])
            cnt += 1
            i >>= 1
        return tuple(res)


    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        unique = sorted(nums)
        out = set()
        out.add(())

        n = len(unique)
        for i in range(1, 2 ** n):
            out.add(self.fill(unique, i))

        return out
