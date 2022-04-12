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


class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:

        for row in matrix:
            if row[-1] <= target:
                ind = left_bin(row, target)
                if ind != -1 and row[ind] == target:
                    return True
                return False

        return False
