class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # 定义头节点
        Lhead = ListNode(0)
        Lhead.next = head

        # 用于寻找m处的节点以及m的前驱节点
        cur, pre = head, Lhead

        # 当m=1时，已经找到了m节点与m的前驱
        while m > 1:
            pre = cur
            cur = cur.next
            m -= 1
            n -= 1
        
        # 将找到的m节点与m的前驱先保存起来
        m_cur, m_pre = cur, pre

        # 开始对n段长的节点进行反转
        while n:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
            n -= 1

        # 反转完成后，将m位置和n位置的节点连接起来，链表题建议画图理解
        m_pre.next = pre
        m_cur.next = cur
        return Lhead.next
