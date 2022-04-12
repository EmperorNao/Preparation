def left_bin(seq, x):

    l = -1
    r = len(seq)
    while r - l > 1:
        m = (r + l) // 2
        if seq[m] >= x:
            r = m
        else:
            l = m
    return r


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
    def search(self, nums, target: int) -> int:
        print(nums)
        if nums[0] <= nums[-1]:
            ind = left_bin(nums, target)
            if ind == -1 or nums[ind] != target:
                return -1
            return ind

        k = find_rotation(nums)
        if nums[0] <= target <= nums[k]:
            return self.search(nums[0: k + 1], target)
        else:
            ind = self.search(nums[k + 1:], target)
            if ind != -1:
                ind += k + 1
            return ind


print(Solution().search([7,8,1,2,3,4,5,6], 2))
