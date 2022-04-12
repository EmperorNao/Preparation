
class Solution:
    
    def findPeakElement(self, nums) -> int:

        l = 0
        r = len(nums) - 1
        while l < r:

            m = (l + r) // 2

            if (m == 0 or nums[m] > nums[m - 1]) and (m == len(nums) - 1 or nums[m] > nums[m + 1]):
                return m

            if m > 0 and nums[m - 1] > nums[m]:
                r = m - 1

            else:
                l = m + 1

        return l


# [1]
# [3, 2, 1]
# [6, 3, 4, 5]
# [1, 2, 3, 4, 5]
# [5, 4, 3, 2, 1]
# [5,4,3,4,5]
