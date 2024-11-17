class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        # edge case
        if x < 0:
            return False

        # transform x into array
        xs = []
        while x > 0:
            xs.append(x % 10)
            x = x // 10

        return xs == xs[::-1]


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        # edge case
        if x < 0:
            return False

        # transform x into array
        xs = []
        while x > 0:
            xs.append(x % 10)
            x = x // 10

        return xs == xs[::-1]
