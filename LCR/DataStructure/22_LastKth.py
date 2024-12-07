"""
    https://leetcode.cn/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def trainingPlan(self, head: Optional[ListNode], cnt: int) -> Optional[ListNode]:
        left, right = head, head

        # right go for (cnt - 1) steps first
        for i in range(cnt-1):
            right = right.next

        # left and right go ahead synchronously
        while right.next:
            left = left.next
            right = right.next

        return left

