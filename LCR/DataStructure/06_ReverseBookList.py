"""
    https://leetcode.cn/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBookList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        books = []

        while head:
            books.append(head.val)
            head = head.next

        reversedBooks = books[::-1]
        return reversedBooks

        # dummy = ListNode()
        # cur = dummy
        #
        # for book in reversedBooks:
        #     cur.next = ListNode(book)
        #     cur = cur.next
        #
        # return dummy.next

        