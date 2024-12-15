"""
    https://leetcode.cn/problems/path-sum-ii/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.current_sum = 0
        self.ans_path = []
        self.current_path = []

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # edge case
        if root is None:
            return []

        # add current node
        self.current_sum += root.val
        self.current_path.append(root.val)

        if self.current_sum == targetSum and root.left == None and root.right == None:
            self.ans_path.append(self.current_path[:])

        self.pathSum(root.left, targetSum)
        self.pathSum(root.right, targetSum)

        # Back Track and Clean up
        self.current_path.pop()
        self.current_sum -= root.val

        return self.ans_path


