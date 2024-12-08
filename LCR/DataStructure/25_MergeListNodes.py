"""
    https://leetcode.cn/problems/merge-two-sorted-lists/description/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = ListNode()
        dummy = cur

        while list1 or list2:
            if list1 and not list2:
                cur.next = list1
                break
            elif list2 and not list1:
                cur.next = list2
                break
            elif list1.val < list2.val:
                cur.next = list1
                cur, list1 = cur.next, list1.next
            elif list1.val >= list2.val:
                cur.next = list2
                cur, list2 = cur.next, list2.next

        return dummy.next