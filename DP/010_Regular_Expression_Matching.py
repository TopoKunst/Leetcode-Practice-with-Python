class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # table[i][j] means the match status between s[:i] and p[:j]
        table = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

        # for the corner case of matching two empty strings
        table[0][0] = True

        # for the corner case when s is empty
        # since each '*' can eliminate the charter before it, the table is vertically updated by the one before previous.
        for j in range(2, len(p)+1):
            table[0][j] = (table[0][j-2] and p[j-1] == '*')

        # dynamic programming from bottom to up
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] != '*':
                    # update the table by referring the diagonal element
                    table[i][j] = table[i-1][j-1] and \
                                  (s[i-1] == p[j-1] or p[j-1] == '.')
                else:
                    # Eliminations (referring to the horizontal element)
                    table[i][j] = table[i][j-1] or table[i][j-2]
                    # Propagations (referring to the vertical element)
                    if p[j-2] == s[i-1] or p[j-2] == '.':
                        table[i][j] = table[i][j] or table[i-1][j]

        return table[-1][-1]