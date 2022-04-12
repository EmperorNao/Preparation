
class Solution:

    def try_to_rob(self, houses, l, r):

        #print(f"compare {l} {r}")

        if l > r:
            return 0

        if self.matr[l][r] != -1:
            return self.matr[l][r]

        if r - l == 1:
            self.matr[l][r] =  max(houses[l], houses[r])

        elif r - l == 0:
            self.matr[l][r] = houses[l]
        else:
            self.matr[l][r] = max(houses[l] + self.try_to_rob(houses, l + 2, r), self.try_to_rob(houses, l + 1, r))

        return self.matr[l][r]


    def rob(self, nums) -> int:

        self.n = len(nums)
        self.matr = [[-1 for i in range(self.n)] for j in range(self.n)]

        return max(self.try_to_rob(nums, 1, self.n - 1), nums[0] + self.try_to_rob(nums, 2, self.n - 2))


print(Solution().rob([1, 5, 1, 5, 10]))
