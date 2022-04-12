

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':

        head = root
        if root is None:
            return head

        level = [root]
        while level:

            next_level = []
            for i in range(len(level) - 1):
                level[i].next = level[i + 1]
                if level[i].left:
                    next_level.append(level[i].left)
                if level[i].right:
                    next_level.append(level[i].right)

            level[-1].next = None
            if level[-1].left:
                next_level.append(level[-1].left)
            if level[-1].right:
                next_level.append(level[-1].right)

            level = next_level

        return head
