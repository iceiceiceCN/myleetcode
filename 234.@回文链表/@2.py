# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        dummy = ListNode(0)

        dummy.next = head

        fast, low = dummy, dummy

        # 如果没有fast.next，那么下一行中的fast.next.next就会报错，所以必须判断fast.next
        # 但是不用判断fast.next.next，因为如果有fast.next，那么就算fast.next.next为空也不影响
        while fast and fast.next: # 不用在乎fast.next.next，为空也可以跳过去
            low = low.next
            fast = fast.next.next

        pre = None
        cur = low.next

        low.next = None  # 从中间断开两个链表

        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        a = dummy.next
        b = pre

        while b: # 后面半段的链表可能会少一个节点，所以以后面的节点为准
            if b.val == a.val:
                a = a.next
                b = b.next
                continue
            return False

        return True

"""
双指针+反转
我们利用链表的两个操作：

1.找到链表的中间节点
2.反转链表

通过这两个操作之后，原链表就以中间节点被一分为二
前半部分一个链表，后半部分(被反转了)为一个链表
然后遍历这两个链表，如果遍历过程中发现两个链表节点不同，就说不是回文链表，直接返回false即可
如果链表遍历完了，说明是回文链表
注意一个小细节，
如果链表长度是偶数，前半部分和后半部分长度是一样的
如果链表长度是奇数，前半部分的长度比后半部分长度多1个
所以最后迭代链表的时候，以后半部分为准(以b为准)就可以了，当链表总长为奇数时，前半部分的最后一个节点就不会被遍历到了。
https://leetcode-cn.com/problems/palindrome-linked-list/solution/dong-hua-yan-shi-234-hui-wen-lian-biao-by-user7439/
"""