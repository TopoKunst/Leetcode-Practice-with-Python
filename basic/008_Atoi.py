class Solution:
    def myAtoi(self, s: str) -> int:
        # ignore any leading whitespace
        s = s.strip()
        # sign of the number
        sign = 1
        num = 0
        for i in range(len(s)):
            if i == 0 and s[0] == '-':
                sign = -1
                continue
            if i == 0 and s[0] == '+':
                continue
            if s[i] in '0123456789':
                num = num * 10 + int(s[i])
            else:
                break
        num *= sign
        # clamp
        if num > 2**31 - 1:
            num = 2**31 - 1
        if num < -2**31:
            num = -2**31

        return num