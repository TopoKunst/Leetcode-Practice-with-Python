"""
    https://leetcode.cn/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/
"""


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        for row in matrix:
            if target < row[0] or target > row[-1]:
                continue
            for num in row:
                if target == num:
                    return True

        return False
