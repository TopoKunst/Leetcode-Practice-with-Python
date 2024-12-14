"""
    https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def decorateRecord(self, root: Optional[TreeNode]) -> List[int]:
        # edge case
        if not root:
            return []

        nodes = [root]
        idx = 0
        while idx < len(nodes):
            if nodes[idx].left:
                nodes.append(nodes[idx].left)
            if nodes[idx].right:
                nodes.append(nodes[idx].right)
            idx += 1
        res = [node.val for node in nodes]
        return res

