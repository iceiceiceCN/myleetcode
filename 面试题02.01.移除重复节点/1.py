# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if not head:
            return

        record = {head.val}
        pre = head
        while pre.next:
            if pre.next.val in record:
                pre.next = pre.next.next

            else:
                record.add(pre.next.val)
                pre = pre.next

        return head
