# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # edge case when head is None or head.next is None
        if not head or not head.next:
            return head
        # root
        root = ListNode(0)
        root.next = head
        cur = root

        # when this node and the next exist
        while cur.next and cur.next.next:
            # swap the two node
            now = cur.next
            following = cur.next.next
            cur.next = following
            now.next = following.next
            following.next = now
            cur = cur.next.next

        return root.next
