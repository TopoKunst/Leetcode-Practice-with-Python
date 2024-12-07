"""
    https://leetcode.cn/problems/c32eOV/description/
"""

"""
算法流程：
双指针第一次相遇： 设两指针 fast，slow 指向链表头部 head，fast 每轮走 2 步，slow 每轮走 1 步；

1. 第一种结果： fast 指针走过链表末端，说明链表无环，直接返回 null；
    TIPS: 若有环，两指针一定会相遇。因为每走 1 轮，fast 与 slow 的间距 +1，fast 终会追上 slow；

2. 第二种结果： 当 fast == slow时， 两指针在环中 第一次相遇 。下面分析此时 fast 与 slow走过的 步数关系 ：
    设链表共有 a+b 个节点，其中 链表头部到链表入口 有 a 个节点（不计链表入口节点）， 两指针分别走了 f ，s 步，则有：
    a. fast 走的步数是 slow 步数的 2 倍，即 f=2s；（解析： fast 每轮走 2 步）
    b. fast 比 slow 多走了 n 个环的长度，即 f=s+nb；
    以上两式相减得：f=2nb，s=nb，即fast和slow 指针分别走了 2n，n 个 环的周长 （注意： n 是未知数，不同链表的情况不同）。

目前情况分析：
    如果让指针从链表头部一直向前走并统计步数 k ，那么所有 走到链表入口节点时的步数 是：k=a+nb
    目前slow 指针走过的步数为 nb 步。因此，我们只要想办法让 slow 再走 a 步停下来，就可以到环的入口。
    但是我们不知道 a 的值，该怎么办？依然是使用双指针法:
        我们构建一个指针，此指针需要有以下性质：此指针和 slow 一起向前走 a 步后，两者在入口节点重合。那么从哪里走到入口节点需要 a 步？答案是链表头部 head 。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # edge case
        if not head.next:
            return None

        fast, slow = head, head
        flag = False

        # first round
        while fast.next:
            # slow go 1 step, fast go 2 steps
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                flag = True
                break

        if not flag:
            return None

        # second round
        head_k = head
        while head_k != slow:
            head_k, slow = head_k.next, slow.next

        return slow

