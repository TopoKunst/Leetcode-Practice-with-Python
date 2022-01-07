# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # back-up linked list
        backup = cur =  head

        # iteration for n times
        for i in range(n-1):
            cur = cur.next

        # iteration for 2 nodes
        while cur.next:
            cur = cur.next
            previous = backup
            backup = backup.next

        # update
        try:
            previous.next = backup.next
            return head
        except:
            # edge case for n = length of the linked list
            return head.next
