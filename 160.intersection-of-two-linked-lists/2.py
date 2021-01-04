# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import sys
sys.path.append("F:\myleetcode\LocalTest")
from ListNodeTest import *

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        def getlen(head):
            n = 0
            while head:
                n += 1
                head = head.next
            
            return n
        
        lenA = getlen(headA)
        lenB = getlen(headB)
        
        if lenB > lenA:
            headA,headB = headB,headA
        
        diff = abs(lenB - lenA)

        for _ in range(diff):
            headA = headA.next
        
        while headA != headB:
            headA = headA.next
            headB = headB.next
        
        return headA