class Solution:
    next_of_last = None
    def reverseN(self, head, n):
        if n == 1:
            self.next_of_last = head.next
            return head
        if not head or not head.next: return head
        last = self.reverseN(head.next, n - 1)
        head.next.next = head
        head.next = self.next_of_last
        return last


    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == 1: 
            last = self.reverseN(head, n) 
            return last
        head.next  = self.reverseBetween(head.next, m - 1, n - 1)
        return head