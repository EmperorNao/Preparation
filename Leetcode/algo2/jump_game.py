
class Solution:
    def canJump(self, nums: List[int]) -> bool:

        min_from = len(nums) - 1
        for i in range(len(nums) -  2, -1):
            if i + nums[i] >= min_from:
                min_from = i

        return min_from == 0
