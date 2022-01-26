class Solution:
    def fib(self, n: int) -> int:
        # list that store the Fibnacci number
        fiblist = [0] * (n+1)
        if n >= 1:
            fiblist[1] = 1

        for i in range(2, n+1):
            fiblist[i] = fiblist[i-2] + fiblist[i-1]

        return fiblist[-1]