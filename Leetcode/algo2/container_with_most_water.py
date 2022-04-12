def area(height, l, r):

    return abs(r - l) * min(height[l], height[r])



class Solution:

    def maxArea(self, height) -> int:

        n = len(height)

        l = 0
        r = len(height) - 1
        maxarea = 0

        while l < r:
            maxarea = max(maxarea, area(height, l, r))

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return maxarea




Solution().maxArea([2,3,10,5,7,8,9])
