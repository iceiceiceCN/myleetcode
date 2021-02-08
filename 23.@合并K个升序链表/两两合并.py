# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        if not lists:
            return None
        n = len(lists)
        res = lists[0]
        # 合并两个有序链表

        def merge(a, b):
            if not (a and b):
                return a if a else b
            if a.val <= b.val:
                a.next = merge(a.next, b)
                return a
            else:
                b.next = merge(a, b.next)
                return b
        # 将lists[0]作为最终合并的链表，然后将list[0]和lists[1]合并成lists[0-1]
        # 再将lists[0-1]和lists[2]合并，如此反复最终lists[0]就是最终结果
        for i in range(1, n):
            res = merge(res, lists[i])
        return res

# https://leetcode-cn.com/problems/merge-k-sorted-lists/solution/duo-tu-yan-shi-23-he-bing-kge-pai-xu-lian-biao-by-/
