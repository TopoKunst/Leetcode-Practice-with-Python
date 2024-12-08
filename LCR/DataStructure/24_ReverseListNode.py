"""
    https://leetcode.cn/problems/fan-zhuan-lian-biao-lcof/description/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def trainningPlan(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # edge case
        if not head  or not head.next:
            return head

        previous = None

        # Each time, only change the front pointer
        while head.next:
            # Cache next node to avoid break
            next = head.next
            # Reverse pointer
            head.next = previous

            # Move the previous and head to the NEXT
            previous = head
            head = next

        head.next = previous

        return head
