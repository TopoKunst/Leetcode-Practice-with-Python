"""
    https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/description/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def decorateRecord(self, root: Optional[TreeNode]) -> List[List[int]]:
        # edge case
        if not root:
            return []

        # init
        queue = []
        queue.append(root)

        res = []
        level_sign = 0

        while queue:
            l = len(queue)
            res_mid = []
            # add current level
            for _ in range(l):
                res_mid.append(queue[0].val)
                if queue[0].left:
                    queue.append(queue[0].left)
                if queue[0].right:
                    queue.append(queue[0].right)
                queue.pop(0)

            if level_sign == 0:
                res.append(res_mid)
                level_sign = 1
            elif level_sign == 1:
                res.append(res_mid[::-1])
                level_sign = 0

        return res


