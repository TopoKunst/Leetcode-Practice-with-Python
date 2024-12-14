"""
    https://leetcode.cn/problems/binary-tree-level-order-traversal/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # edge case
        if not root:
            return []

        queue, level = [root], [0]
        cur_level = 0
        res = [[]]

        while queue:
            # print res
            if cur_level == level[0]:
                res[-1].append(queue[0].val)
            elif cur_level < level[0]:
                res.append([])
                res[-1].append(queue[0].val)
                cur_level += 1
            # add to queue
            if queue[0].left:
                queue.append(queue[0].left)
                level.append(cur_level + 1)
            if queue[0].right:
                queue.append(queue[0].right)
                level.append(cur_level + 1)
            # FIFO
            queue.pop(0)
            level.pop(0)

        return res

