class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        # edge case
        if len(s) <= 1:
            return s

        # param
        cur_len, max_len = 0, 1
        n, start_idx = len(s), 0
        dp = [[False if i != j else True for j in range(n)] for i in range(n)]

        # iterate for each column
        for right in range(1, n):
            for left in range(right):
                # if s[left: right+1] is a palindrome
                # case 1: string length = 2, then dp[left+1][right-1] doesn't exist
                if right - left == 1:
                    if s[left] == s[right]:
                        dp[left][right] = True
                        cur_len = right - left + 1
                # case 2: string length >= 3
                else:
                    if s[left] == s[right] and dp[left+1][right-1] == True:
                        dp[left][right] = True
                        cur_len = right - left + 1

                # update max length and start index
                if dp[left][right] and cur_len > max_len:
                    max_len, start_idx = cur_len, left

        return s[start_idx: start_idx+max_len]

solution = Solution()
s = "babad"
res = solution.longestPalindrome(s)
print(res)

