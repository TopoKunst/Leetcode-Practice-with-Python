"""
    https://leetcode.cn/problems/ti-huan-kong-ge-lcof/
"""


class Solution(object):
    def pathEncryption(self, path):
        """
        :type path: str
        :rtype: str
        """

        res = ""
        for ch in path:
            res += ch if ch != "." else " "
        return res

        res = path.replace(".", " ")
        return res