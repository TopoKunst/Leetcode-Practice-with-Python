"""
    https://leetcode.cn/problems/spiral-matrix/description/
"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        booked = [[False for _ in range(n)] for _ in range(m)]
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_order = 0
        cur_x, cur_y = 0, 0
        res = []

        for _ in range(m * n):
            # step
            res.append(matrix[cur_x][cur_y])
            booked[cur_x][cur_y] = True

            # new position
            new_x, new_y = cur_x + dirs[dir_order][0], cur_y + dirs[dir_order][1]

            # whether need to change direction
            if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n or booked[new_x][new_y]:
                dir_order = (dir_order + 1) % 4
                cur_x = cur_x + dirs[dir_order][0]
                cur_y = cur_y + dirs[dir_order][1]
            else:
                cur_x, cur_y = new_x, new_y

        return res