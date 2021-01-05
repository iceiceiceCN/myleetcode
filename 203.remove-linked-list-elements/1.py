# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        first = dummy
        second = dummy.next

        while second:  # 要判断最先到边界的节点
            if second.val == val:
                first.next = second.next
            else:
                first = first.next

            second = second.next # 如果判断相同的话，只让second先走，因为有可能下一个还是val

        return dummy.next
