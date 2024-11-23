"""
    https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """

        # edge case
        if len(preorder) == 0:
            return None

        # recursive
        # find root in preorder
        root = TreeNode(preorder[0])
        # find root in inorder
        root_index = inorder.index(root.val)
        # construct left tree by left tree preorder and left tree inorder
        root.left = self.buildTree(preorder[1:root_index+1], inorder[:root_index])
        root.right = self.buildTree(preorder[root_index+1:], inorder[root_index+1:])

        return root


        