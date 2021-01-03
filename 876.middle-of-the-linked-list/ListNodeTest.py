#定义节点
class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None
#将传入的数组转化为链表
def create_linked_list(nums):
    if len(nums) == 0:
        return None
    head = ListNode(nums[0])
    cur = head
    for i in range(1, len(nums)):
        cur.next = ListNode(nums[i])
        cur = cur.next
    return head
#传入链表头节点，以数组形式返回
def print_linked_list(list_node):
    if list_node is None:
        return

    cur = list_node
    while cur:
        print(cur.val, '->', end=' ')
        cur = cur.next
    print('null')



"""
class Solution():
    def mergeTwoLists(self, l1, l2):
        pre = ListNode(0)
        head = pre
        while l1 and l2:
            if l1.val >= l2.val:
                pre.next = l2
                l2 = l2.next
            else:
                pre.next = l1
                l1 = l1.next
            pre = pre.next
        pre.next = l1 if l1 else l2
        return head.next


if __name__ == "__main__":
    head1 = create_linked_list([1, 2, 4])
    head2 = create_linked_list([1, 3, 4])
    solution = Solution()
    sorted_lists = solution.mergeTwoLists(head1, head2)
    print(print_linked_list(sorted_lists))
"""
#输出：[1, 1, 2, 3, 4, 4]
