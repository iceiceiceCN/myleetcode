# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        stack = []
        tmp = head
        while tmp:
            stack.append(tmp.val)
            tmp = tmp.next
        
        return stack[::-1]
        
"""
辅助栈法

算法流程：
入栈： 遍历链表，将各节点值 push 入栈。
（Python​ 使用 append() 方法，​Java​借助 LinkedList 的addLast()方法）。

出栈： 将各节点值 pop 出栈，存储于数组并返回。
（Python​ 直接返回 stack 的倒序列表，Java ​新建一个数组，通过 popLast() 方法将各元素存入数组，实现倒序输出）。


"""