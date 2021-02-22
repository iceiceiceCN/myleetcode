# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        # 递归终止条件是当前为空，或者下一个节点为空
        # head.next /为空是多层嵌套函数到最后一个节点的跳出条件
        # head为空是为了防止输入为[]
        if head == None or head.next == None:
            return head
        
        # 这里的cur就是最后一个节点，后续每次返回cur都是最后一个节点
        # 如果链表是 1->2->3->4->5，那么此时的cur就是5
        cur = self.reverseList(head.next) 
		
		# 而head是4，head的下一个是5，下下一个是空
		# 所以head.next.next 就是5->4
        head.next.next = head

        # 防止链表循环，需要将head.next / 设置为空
        head.next = None

        # 每层递归函数都返回cur，也就是最后一个节点
        return cur # 因为是反转链表，此时cur是最后一个节点，也就是反转后链表的第一个节点

"""
cur 只是用来通过递归找到链表的尾部而已，之后就不动了，
head 才是用来进行每步变换的工具节点
"""