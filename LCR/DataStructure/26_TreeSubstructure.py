"""
    https://leetcode.cn/problems/shu-de-zi-jie-gou-lcof/description/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def subStructureCheck(self, A, B):
        # Base Case
        # if B is at the end, B is a sub structure of A, return true
        if B is None:
            return True
        # if A is at the end, B is not a sub structure of A, return false
        # if A.val != B.val, B is not a sub structure of A, return false
        elif A is None or A.val != B.val:
            return False
        else:
            return self.subStructureCheck(A.left, B.left) and self.subStructureCheck(A.right, B.right)

    def isSubStructure(self, A: Optional[TreeNode], B: Optional[TreeNode]) -> bool:
        result = False

        # Traverse A, to find the first matched node
        if A and B:
            # if first matched found
            if A.val == B.val:
                result = self.subStructureCheck(A, B)
            # if first mached not found, tarverse A
            if not result:
                result = self.isSubStructure(A.left, B)
            if not result:
                result = self.isSubStructure(A.right, B)

        return result