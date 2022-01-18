class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # edge case
        if not needle:
            return 0

        # length of needle
        n = len(needle)

        for i in range(len(haystack) - n + 1):
            if haystack[i: i+n] == needle:
                return i
        return -1


    # Time Limite Exceed
    '''
    def strStr(self, haystack: str, needle: str) -> int:
        # edge case
        if not needle:
            return 0

        n = len(needle)

        # loop
        for i in range(len(haystack)):
            # two pointer
            j = i; k = 0
            try:
                while k < n:
                    assert haystack[j] == needle[k]
                    j += 1; k += 1
            except:
                continue

            return i

        return -1
    '''