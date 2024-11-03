class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        # edge case
        if numRows == 1: return s

        res = ["" for _ in range(numRows)]
        idx, flag = 0, -1

        for c in s:
            # add char to current row
            res[idx] += c

            if idx == 0 or idx == numRows-1:
                flag = -flag
            idx += flag

        return "".join(res)

solution = Solution()
s = "PAYPALISHIRING"
numRows =3
res = solution.convert(s, numRows)
print(res)
