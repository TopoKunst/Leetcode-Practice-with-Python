"""
    https://leetcode.cn/problems/shan-chu-lian-biao-de-jie-dian-lcof/description/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteNode(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(val=0, next=head)
        cur = dummy

        while cur and cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            cur = cur.next

        return dummy.next
