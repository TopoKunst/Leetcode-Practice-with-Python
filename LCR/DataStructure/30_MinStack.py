"""
    https://leetcode.cn/problems/min-stack/
"""


class MinStack:

    def __init__(self):
        # initialize data structure: 2 stacks
        self.data_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.data_stack.append(val)
        if len(self.min_stack) == 0 or val < self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        del self.data_stack[-1]
        del self.min_stack[-1]

    def top(self) -> int:
        return self.data_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
