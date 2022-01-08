class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # prefix
        prefix = ''
        # loop
        i = 0
        # flag indicates whether common prefix holds
        flag = True
        tmp = ''
        while flag:
            prefix += tmp
            try:
                # get the char of the first string
                tmp = strs[0][i]
                for string in strs:
                    if string[i] != tmp:
                        flag = False
                        break
            except:
                break
            i += 1

        return prefix