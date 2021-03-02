# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        na,nb=0,0
        ha = headA
        hb = headB
        while ha:
            ha = ha.next
            na += 1
        while hb:
            hb = hb.next
            nb += 1

        diff = abs(nb - na)

        if nb > na:
            headA ,headB  = headB,headA    # headA大

        while diff:
            diff -= 1
            headA = headA.next
        
        while headA != headB:
            headB = headB.next
            headA = headA.next
        
        return headA
