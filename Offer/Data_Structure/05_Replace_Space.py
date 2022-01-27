class Solution:
    def replaceSpace(self, s):
        # result
        res = ''

        for c in s:
            if c == ' ':
                res += '20%'
            else:
                res += c

        return res


    '''
    def replaceSpace(selfself, s):
        return s.replace(" ", "%20")
    '''