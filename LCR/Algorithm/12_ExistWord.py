"""
    https://leetcode.cn/problems/word-search/description/
"""


class Solution(object):

    dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    def search(self, board, word, word_idx, booked, x, y, rows, cols):
        # edge case
        if board[x][y] != word[word_idx]:
            return False
        elif word_idx == len(word) -1:
            return True

        booked[x][y] = 1

        for dir in self.dirs:
            new_x, new_y = x + dir[0], y + dir[1]
            if new_x >= 0 and new_x < rows and new_y >= 0 and new_y < cols and not booked[new_x][new_y]:
                if self.search(board, word, word_idx+1, booked, new_x, new_y, rows, cols):
                    return True

        booked[x][y] = 0
        return False

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        m, n = len(board), len(board[0])
        booked = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if self.search(board=board, word=word, word_idx=0, booked=booked,
                                   x=i, y=j, rows=m, cols=n):
                        return True

        return False


# solution = Solution()
# nums = [2, 2, 0, 1, 2]
# res = solution.findMin(nums)
# print(res)



