# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0) # 假头
        dummy.next = head
        first = dummy # 双指针1
        second = dummy.next # 双指针2
        while True:
            if second.val == val:
                first.next = second.next
                break
            first = first.next
            second = second.next
        return dummy.next


"""
假头可以简化删除head的情况
"""