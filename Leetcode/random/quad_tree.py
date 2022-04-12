"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:

    def same_value(self, grid, l, r, t, b):

        value = grid[l][t]
        for i in range(l, r + 1):
            for j in range(t, b + 1):
                if grid[i][j] != value:
                    return False

        return True

    def build(self, grid, l, r, t, b):

        if self.same_value(grid, l, r, t, b):
            return Node(grid[l][t], True, None, None, None, None)

        else:

            m_horiz = l + (r - l) // 2
            m_vert = t + (b - t) // 2

            return Node(-1, False,
            self.build(grid, l, m_horiz, t, m_vert),
            self.build(grid, l, m_horiz, m_vert + 1, b),
            self.build(grid, m_horiz + 1, r, t, m_vert),
            self.build(grid, m_horiz + 1, r, m_vert + 1, b))

    def construct(self, grid: List[List[int]]) -> 'Node':

        return self.build(grid, 0, len(grid[0]) - 1, 0, len(grid) - 1)
