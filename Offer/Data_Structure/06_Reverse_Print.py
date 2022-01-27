class Solution:
    def reversePrint(self, head):
        # result
        res = []

        if head is None:
            return res
        else:
            res = self.reversePrint(head.next)
            res.append(head.val)
            return res


    '''
    def reversePrint(self, head):
        # stack
        stack = []

        # iteration
        cur = head
        while not cur is None:
            stack.append(cur.val)
            cur = cur.next

        # reverse the list
        return cur[::-1]
    '''