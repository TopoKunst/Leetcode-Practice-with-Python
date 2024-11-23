"""
    https://leetcode.cn/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/
"""


class CQueue(object):

    # FILO + FILO = FIFO

    def __init__(self):
        # use this stack for enqueue operation
        self.stack_for_enqueue = []
        # use this stack for dequeue operation
        self.stack_for_dequeue = []

    # def appendTail(self, value: int) -> None:
    def appendTail(self, value):
        # push
        self.stack_for_enqueue.append(value)

    def deleteHead(self):
        # edge case:
        if len(self.stack_for_enqueue) == 0 and len(self.stack_for_dequeue) == 0:
            return -1
        # dequeue
        elif len(self.stack_for_dequeue) > 0:
            return self.stack_for_dequeue.pop()
        # push equeue to dequeue
        elif len(self.stack_for_dequeue) == 0:
            while len(self.stack_for_enqueue) != 0:
                self.stack_for_dequeue.append(self.stack_for_enqueue.pop())
            return self.stack_for_dequeue.pop()
