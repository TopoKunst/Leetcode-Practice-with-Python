"""
    https://leetcode.cn/problems/number-of-1-bits/description/
"""


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0

        while n > 0:
            if n & 1:
                count += 1
            n = n >> 1

        return count