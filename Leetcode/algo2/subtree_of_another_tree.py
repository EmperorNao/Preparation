# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def preorder_traversal(self, root, order: list):

        if root == None:
            order.append(None)
            return

        order.append(root.val)
        self.preorder_traversal(root.left, order)
        self.preorder_traversal(root.right, order)

    def find_subseq(self, seq, subseq):

        for i in range(len(seq) - len(subseq) + 1):
            if seq[i: i + len(subseq)] == subseq:
                return True

        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        seq = []
        self.preorder_traversal(root, seq)

        subseq = []
        self.preorder_traversal(subRoot, subseq)

        return self.find_subseq(seq, subseq)
