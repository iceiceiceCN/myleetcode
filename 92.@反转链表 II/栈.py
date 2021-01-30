class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        start_node = ListNode(0)
        start_node.next = head
        end_node = start_node
        stack = []
        count = 1
        diff = n - m + 1

        while count < m:
            count += 1
            end_node = head
            head = head.next

        while diff:
            diff -= 1
            stack.append(head)
            head = head.next

        while stack:
            node = stack.pop()
            end_node.next = node
            end_node = end_node.next

        end_node.next = head  # head全程都在移动，此时head在n+1位置

        return start_node.next
