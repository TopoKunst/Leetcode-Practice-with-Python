"""
    https://leetcode.cn/problems/search-a-2d-matrix-ii/description/
"""


class Solution(object):
    def findRepeatDocument(self, documents):
        """
        :type documents: List[int]
        :rtype: int
        """
        dicts = {}
        res = -1

        for num in documents:
            if num not in dicts.keys():
                dicts[num] = 1
            else:
                res = num
                break

        return res