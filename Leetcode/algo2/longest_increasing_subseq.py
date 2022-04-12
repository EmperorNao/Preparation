class Solution:

    def bin(self, a, i, j, x):

        l = i - 1
        r = j + 1

        while r - l > 1:
            m = (r + l) // 2
            if a[m] >= x:
                r = m
            else:
                l = m

        return l


    def lengthOfLIS(self, nums: List[int]) -> int:

        sort = sorted(nums)
        indexes = [0 for i in range(len(nums))]

        for i, el in enumerate(nums):

            ind = self.bin(sort, i, len(nums) - 1, el)
            indexes[ind] = i


        last_ind = 0
        seq = 1
        for i in range(1, len(sort)):
            if nums[i] > nums[last_ind] and indexes[i] > :
