"""
    https://leetcode.cn/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/description/
"""


class Solution:
    def verifyTreeOrder(self, postorder: List[int]) -> bool:
        # edge case
        if postorder is None or len(postorder) == 0:
            return True

        n = len(postorder)

        # find root, left tree and right tree
        root = postorder[-1]
        right_flag = False
        for i, val in enumerate(postorder):
            if val > root:
                idx = i
                right_flag = True
                break
        idx = idx if right_flag else n-1

        # if satisfy post order
        for i in range(idx, n-1):
            if postorder[i] < root:
                return False

        # recursive soloved
        left = True
        if idx > 0:
            left = self.verifyTreeOrder(postorder[:idx])

        right = True
        if idx < len(postorder)-1:
            right = self.verifyTreeOrder(postorder[idx:-1])

        return left and right


