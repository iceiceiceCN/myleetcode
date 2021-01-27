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
        ha = headA
        hb = headB
        while(ha != hb):
            ha = ha.next if ha else headB
            hb = hb.next if hb else headA
        
        return ha

"""
分别为链表A和链表B设置指针A和指针B，然后开始遍历链表，
如果遍历完当前链表，则将指针指向另外一个链表的头部继续遍历，直至两个指针相遇。

从head a -> 相交节点 = a
从head b -> 相交节点 = b
从相交节点到末端 = c

最终两个指针分别走过的路径为：
指针A :a+c+b
指针B :b+c+a
明显 a+c+b = b+c+a,因而如果两个链表相交，则指针A和指针B必定在相交结点相遇。

这一方法的时间复杂度为o(m+n),其中m和n分别为两个指针的长度，空间复杂度为o(1)。
"""