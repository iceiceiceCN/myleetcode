# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        fast,late = head,head
        for _ in range(k):
            fast = fast.next
        
        while fast: # 执行到fast为空，此时late就是倒数第k个节点的位置了，直接输出late，不用加.next
            fast = fast.next
            late = late.next
        
        return late