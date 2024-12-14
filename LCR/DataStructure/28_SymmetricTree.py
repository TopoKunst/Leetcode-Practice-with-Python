"""
    https://leetcode.cn/problems/invert-binary-tree/description/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def symmetricCheck(self, left, right):
        # edge cace: both left and right are empty
        if left is None and right is None:
            return True
        if left is None or right is None or (left.val != right.val):
            return False
        return self.symmetricCheck(left.left, right.right) and self.symmetricCheck(left.right, right.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.symmetricCheck(root.left, root.right)
