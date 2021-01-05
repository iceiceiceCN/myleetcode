class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head and head.val == val:  # 如果不用dummy节点的话，直接上来就判断head是否为val,如果为val直接移动head
            head = head.next
        if not head:
            return
        pre = head # 此时的pre(head)一定不是val
        while pre.next:
            if pre.next.val == val: # 判断得到val时 不要急着下一步 要再判断一次新节点的值
                pre.next = pre.next.next
            else:
                pre = pre.next
        return head

"""
迭代
"""