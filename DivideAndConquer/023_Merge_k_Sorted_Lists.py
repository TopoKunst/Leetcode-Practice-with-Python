# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # divide and conquer
        n = len(lists)
        if n == 0:
            return None
        elif n == 1:
            return lists[0]
        elif n == 2:
            return self.mergeTwoLists(lists[0], lists[1])
        else:
            return self.mergeTwoLists(self.mergeKLists(lists[0: n//2]), self.mergeKLists(lists[n//2: ]))


    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # root and current node
        root = cur = ListNode(0)

        # merge process
        while list1 and list2:
            if list1.val <= list2.val:
                item = list1.val
                list1 = list1.next
            elif list1.val > list2.val:
                item = list2.val
                list2 = list2.next
            cur.next = ListNode(item)
            cur = cur.next
        cur.next = list1 or list2

        return root.next

    '''
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # if lists is empty
        if len(lists) == 0:
            return None

        # current node
        cur = lists[0]

        # iteration
        for i in range(1, len(lists)):
            cur = self.mergeTwoLists(cur, lists[i])

        return cur


    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # root and current node
        root = cur = ListNode(0)

        # merge process
        while list1 and list2:
            if list1.val <= list2.val:
                item = list1.val
                list1 = list1.next
            elif list1.val > list2.val:
                item = list2.val
                list2 = list2.next
            cur.next = ListNode(item)
            cur = cur.next
        cur.next = list1 or list2

        return root.next
    '''