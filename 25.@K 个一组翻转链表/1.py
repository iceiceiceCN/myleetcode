# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        p = dummy
        while True:
            count = k
            stack = []
            tmp = head # 把tmp移到下一轮k个节点计算(下一个工作列)的第一个节点
            while count and tmp:
                stack.append(tmp)
                tmp = tmp.next
                count -= 1
            # 注意,目前tmp所在k+1位置
            # 说明剩下的链表不够k个,把剩下的直接全拼上去,跳出循环
            if count:
                p.next = head # 剩下的不够，就把当前工作列的头结点拼上去
                break
            # 翻转操作
            while stack:
                p.next = stack.pop()  # 会把上一轮使用p.next = tmp拼的节点覆盖掉，所以不影响
                p = p.next
            head = tmp  # 把head定位到k+1个位置，使得下一个工作列从k+1位置开始计算，只在当前工作列运行结束后变化

        return dummy.next
