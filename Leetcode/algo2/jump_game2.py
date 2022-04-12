


class Solution:

    def jump(self, nums) -> int:

        n = len(nums)
        cnt = 0
        next_max_dist = 0
        cur_max_dist = 0


        for i in range(0, n):
            if cur_max_dist == n - 1:
                return cnt

            next_max_dist = max(next_max_dist, i + nums[i])
            if (i == cur_max_dist):
                cur_max_dist = next_max_dist
                cnt += 1

        return cnt

print(Solution().jump([1, 3, 0, 2, 0, 4]))
