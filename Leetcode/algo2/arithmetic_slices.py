class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:

        if len(nums) < 3:
            return 0

        n = len(nums)
        dp = [0 for i in range(n)]
        result = 0

        for i in range(2, n):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                dp[i] = dp[i - 1] + 1

            result += dp[i]

        return result
