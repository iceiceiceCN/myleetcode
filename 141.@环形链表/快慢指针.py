# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:  # 防止head为空和出现空指针的next的情况
            return False
        fast, slow = head, head

        # 如果没有fast.next，那么下一行中的fast.next.next就会报错，所以必须判断fast.next
        # 但是不用判断fast.next.next，因为如果有fast.next，那么就算fast.next.next为空也不影响
        while fast and fast.next: 
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True

        return False

# 双指针 / 快慢指针
