class Solution:
    def longestPalindrome(self, s: str) -> str:
        # max palindrome string
        res = ""
        # for each character
        for i in range(len(s)):
            # odd case
            tmp = self.palExtend(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # even case
            tmp = self.palExtend(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        return res

    def palExtend(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1, r]

    '''
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        max_len = 0
        # palindrome with odd length
        for i in range(l):
            half_len = 0
            while i-half_len >= 0 and i+half_len < l:
                if s[i+half_len] == s[i-half_len]:
                    half_len += 1
                else:
                    break
            # adjust half length
            half_len -= 1
            # update
            if 2 * half_len + 1 > max_len:
                max_len = 2 * half_len + 1
                max_pal_str = s[i-half_len : i+half_len+1]

        # palindrome with even length
        for i in range(0, l-1):
            half_len = 0
            while i - half_len >= 0 and i + half_len + 1 < l:
                if s[i + half_len + 1] == s[i - half_len]:
                    half_len += 1
                else:
                    break
            # adjust half length
            half_len -= 1
            # update
            if 2 * half_len + 2 > max_len:
                max_len = 2 * half_len + 2
                max_pal_str = s[i - half_len: i + half_len + 2]

        return max_pal_str
    '''