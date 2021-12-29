# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # root node and current node
        root = ListNode(0)
        current = root
        # carry value
        carry = 0
        # compute the sum of l1 and l2
        while l1 or l2 or carry:
            # compute the sum of two digits
            n = 0
            if l1:
                n += l1.val
                l1 = l1.next
            if l2:
                n += l2.val
                l2 = l2.next
            n += carry
            carry = n // 10
            # iteration
            current.next = ListNode(n % 10)
            current = current.next
        return root.next

