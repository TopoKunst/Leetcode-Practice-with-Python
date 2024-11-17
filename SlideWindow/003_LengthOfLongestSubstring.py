class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # edge case
        if len(s) <= 1:
            return len(s)

        start_idx, end_idx = 0, 0
        max_len = 1
        while end_idx < len(s)-1:
            end_idx += 1
            if s[end_idx] not in s[start_idx: end_idx]:
                max_len = max(max_len, end_idx + 1 - start_idx)
            else:
                for idx in range(end_idx-1, start_idx-1, -1):
                    if s[idx] == s[end_idx]:
                        start_idx = idx + 1
                        break
        return max_len


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # edge case
        if not s:
            return 0

        left = 0
        lookup = set()
        max_len, cur_len = 0, 0

        for right in range(len(s)):
            cur_len += 1
            while s[right] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            max_len = max(max_len, cur_len)
            lookup.add(s[right])
        return max_len


solution = Solution()
s = "abcabcbb"
res = solution.lengthOfLongestSubstring(s)
print(res)