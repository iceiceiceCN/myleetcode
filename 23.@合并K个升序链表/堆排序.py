# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        if not lists:
            return None
        dummy = ListNode(0)
        p = dummy
        import heapq
        n = len(lists)
        queue = []
        for i in range(n):
            head = lists[i]
            while head:
                heapq.heappush(queue,(head.val,head))
                head = head.next
        
        while queue:
            _,node = heapq.heappop(queue)
            p.next = node
            p = p.next
        
        p.next = None
        return dummy.next