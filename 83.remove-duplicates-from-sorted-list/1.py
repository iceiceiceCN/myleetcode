# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        node = head
        while node and node.next: # 链表标准遍历条件
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next

        return head
