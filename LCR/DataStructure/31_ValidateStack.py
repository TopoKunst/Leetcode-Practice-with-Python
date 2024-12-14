"""
    https://leetcode.cn/problems/validate-stack-sequences/description/
"""


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        # idx of popped
        idx = 0

        for num in pushed:
            stack.append(num)
            while len(stack) > 0 and stack[-1] == popped[idx]:
                # stack.pop()
                del stack[-1]
                idx += 1

        if idx == len(popped):
            return True
        else:
            return False
