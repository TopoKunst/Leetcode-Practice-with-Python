"""
    https://leetcode.cn/problems/integer-break/description/
"""


class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """

        # edge case
        if n <= 2:
            return 1

        dp = [1 for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], dp[j] * dp[i-j], dp[j] * (i-j), j * (i-j))

        return dp[-1]

solution = Solution()
n = 10
res = solution.integerBreak(10)
print(res)

