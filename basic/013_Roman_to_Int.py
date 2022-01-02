class Solution:
    def romanToInt(self, s: str) -> int:
        # relative signals and values
        dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        # transform s to list
        s = [ch for ch in s]
        # result
        num = 0
        # last signal
        last = 0
        for i in range(len(s) - 1, -1, -1):
            now = dict[s[i]]
            if num > now and last != now:
                num -= now
            else:
                num += now
            last = now
        return num