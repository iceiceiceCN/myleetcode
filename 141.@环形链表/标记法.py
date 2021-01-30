class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        while head:
            if head.val == '1':
                return True
            head.val = '1'
            head = head.next
        return False