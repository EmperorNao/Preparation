

def find_rotation(seq):

    l = 0
    r = len(seq) - 1
    while r - l > 1 and seq[l] > seq[r]:

        m = l + (r - l) // 2
        if seq[m] >= seq[l]:
            l = m
        else:
            r = m

    return l


class Solution:
    def findMin(self, nums) -> int:

        ind = find_rotation(nums)
        return min(nums[ind], nums[(ind + 1) % len(nums)])



[1]
[1, 2, 3, 4, 5]
[3, 4, 5, 1, 2]
[4, 5, 1, 2, 3]
[4, 5, 6, 1, 2, 3]
[5, 6, 1, 2, 3, 4]
#print(Solution().findMin([5, 6, 1, 2, 3, 4]))
