"""
    https://leetcode.cn/problems/powx-n/description/
"""

from functools import lru_cache

class Solution(object):
    @lru_cache(None)
    def myPow(self, x: float, n: int) -> float:

        # edge case
        if n == 0:
            return 1

        if n == 1:
            return x
        elif n < 0:
            return self.myPow(1 / x, n)
        elif n % 2 == 0:
            return self.myPow(x, n // 2) ** 2
        elif n % 2 == 1:
            return self.myPow(x, (n-1) // 2) ** 2 * x