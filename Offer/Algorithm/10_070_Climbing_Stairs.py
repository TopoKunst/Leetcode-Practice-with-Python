class Solution:
    def climbStairs(self, n: int) -> int:
        # list that store the distinct ways 同climb n-1 stairs
        stairs = [1] * (n)
        if n >= 1:
            stairs[1] = 2

        for i in range(2, n):
            stairs[i] = stairs[i - 2] + stairs[i - 1]

        return stairs[-1]