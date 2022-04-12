
def left_bin(seq, x):
    l = -1
    r = len(seq)
    while r > l + 1:
        m = (l + r) // 2
        if seq[m] >= x:
            r = m
        else:
            l = m
    return l


def right_bin(seq, x):
    l = -1
    r = len(seq)
    while r > l + 1:
        m = (l + r) // 2
        if seq[m] > x:
            r = m
        else:
            l = m
    return r

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if len(nums) == 1 and nums[0] == target:
            return [0, 0]

        left = left_bin(nums, target)
        right = right_bin(nums, target)

        if right - left == 1:
            return [-1, -1]
        else:
            return [left + 1, right - 1]
        
