# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # root node and current step node
        root = step = ListNode(0)
        root.next = l = r = head

        # iteration
        while True:
            cnt = 0
            while r and cnt < k:
                r = r.next
                cnt += 1
            # for the k-group, reverse the inner linked list
            if cnt == k:
                # cur is the current node wo want to precess, pre is the previous node of precessed node
                cur, pre = l, r
                # reversing
                for _ in range(k):
                    cur.next, cur, pre = pre, cur.next, cur
                # connect 2 k-groups
                step.next, step, l = pre, l, r

            # end
            else:
                return root.next