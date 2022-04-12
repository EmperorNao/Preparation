class Solution:
    def minSubArrayLen(self, k, nums):

        num = 0
        prod = 0

        cont = 0
        i = 0
        j = 0

        min_cont = len(nums) + 1

        while i < len(nums):

            while i < len(nums) and prod < k:
                cont += 1
                prod += nums[i]
                i += 1

            if cont < min_cont and prod >= k:
                min_cont = cont

            while True:
                cont -= 1
                prod -= nums[j]
                j += 1
                if not(j <= i and (j < len(nums) and prod - nums[j] >= k)):
                    break

        if cont < min_cont and prod >= k:
            min_cont = cont

        return min_cont if min_cont != (len(nums) + 1) else 0
