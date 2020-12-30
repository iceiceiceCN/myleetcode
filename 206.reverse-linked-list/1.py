# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur:
            tmp = cur.next # 先把当前节点的下一节点存起来，防止过会找不到了
            cur.next = pre # 把当前节点的指针指向前面一个节点，开始反转
            pre = cur # 该节点反转完毕，开始将指针往后推移，把上一节点移到当前节点
            cur = tmp # 这个时候tmp就起作用了，把当前节点移到下一节点
        
        return pre

"""
我们可以申请两个指针，第一个指针叫 pre，最初是指向 null 的。
第二个指针 cur 指向 head，然后不断遍历 cur。
每次迭代到 cur，都将 cur 的 next 指向 pre，然后 pre 和 cur 前进一位。
都迭代完了(cur 变成 null 了)，pre 就是最后一个节点了。
"""