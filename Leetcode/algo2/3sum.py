

class Solution:

    def threeSum(self, numbers):

        nums = sorted(numbers)

        n = len(nums)
        answ = []
        i = 0
        while i < n:
            j = i + 1
            k = n - 1
            while j < n and j < k:
                if -nums[i] == nums[j] + nums[k]:
                    answ.append(sorted([nums[i], nums[j], nums[k]]))

                    while k != 0 and nums[k] == nums[k - 1]:
                        k -= 1
                    k -= 1
                    while j != n - 1  and nums[j] == nums[j + 1]:
                        j += 1
                    j += 1

                elif nums[i] + nums[j] + nums[k] > 0:
                    while k != 0 and nums[k] == nums[k - 1]:
                        k -= 1
                    k -= 1

                else:
                    while j != n - 1  and nums[j] == nums[j + 1]:
                        j += 1
                    j += 1

            while i != n - 1 and nums[i] == nums[i + 1]:
                i += 1
            i += 1

        return answ
