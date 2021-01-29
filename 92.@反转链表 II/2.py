class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        def reverseN(head,n):
            if n == 1:return head
            last = reverseN(head.next,n-1)
            successor = head.next.next
            head.next.next = head
            head.next = successor
            return last
        if m == 1:return reverseN(head,n)
        head.next = self.reverseBetween(head.next,m-1,n-1)
        return head