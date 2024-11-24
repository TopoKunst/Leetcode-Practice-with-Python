"""
    https://leetcode.cn/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/description/
"""


class Solution(object):

    # dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    dirs = [(0, 1), (1, 0)]

    def sumDigits(self, num):
        sum_ = 0
        while num > 0:
            sum_ += num % 10
            num = num // 10
        return sum_

    def search(self, m, n, booked, cnt, x, y):
        if self.sumDigits(x) + self.sumDigits(y) > cnt:
            return 0
        count = 1
        booked[x][y] = 1
        for dir in self.dirs:
            new_x, new_y = x + dir[0], y + dir[1]
            if new_x >= 0 and new_x < m and new_y >= 0 and new_y < n and not booked[new_x][new_y]:
                count += self.search(m, n, booked, cnt, new_x, new_y)

        return count


    def wardrobeFinishing(self, m, n, cnt):
        """
        :type m: int
        :type n: int
        :type cnt: int
        :rtype: int
        """

        # edge case
        if cnt == 0:
            return 1

        booked = [[0 for _ in range(n)] for _ in range(m)]

        count = self.search(m, n, booked, cnt, 0, 0)
        return count



