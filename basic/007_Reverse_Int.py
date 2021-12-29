class Solution:
    def reverse(self, x: int) -> int:
        # get the sign of x
        if x == 0:
            return x
        sign = abs(x) / x
        x = abs(x)
        # reverse number
        num = 0
        # reverse process
        while x != 0:
            temp = x % 10
            num = num * 10 + temp
            x = x // 10
        num = int(sign * num)
        return num if -2**31 < num < 2**31 - 1 else 0