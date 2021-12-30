class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        return ''.join(L)
    '''
    def convert(self, s: str, numRows: int) -> str:
        # length of the word
        length = len(s)
        res = ''
        # for string with length 1 or numRows == 1
        if length == 1 or numRows == 1:
            return s
        # print process
        for i in range(numRows):
            j = i
            # print process for i = 0 or i = length - 1
            if i == 0 or i == numRows - 1:
                while j < length:
                    res += s[j]
                    j += 2 * (numRows - 1)
                continue
            # print process for others
            while j < length:
                res += s[j]
                # update the index for next element
                j = j + (numRows - i - 1) * 2
                if j < length:
                    res += s[j]
                else:
                    break
                # update the index for next element
                j = j + i * 2

        return res
    '''