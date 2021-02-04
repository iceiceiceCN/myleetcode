import sys
sys.path.append("F:\myleetcode\LocalTest")
from ListNodeTest import *

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        dummy1 = ListNode(0)

        dummy1.next = head

        fast,slow = dummy1,dummy1

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        pre = None
        cur = slow.next

        slow.next = None

        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        a = dummy1.next
        b = pre

        while b:
            if b.val == a.val:
                a = a.next
                b = b.next
                continue
            return False
            
        return True,pre

if __name__ == '__main__':
    # nums = [1, 2, 3, 4, 5, 6, 7]
    nums = [1, 0,1]
    head = create_linked_list(nums)
    print_linked_list(head)
    print("===before===")
    solution = Solution()
    result,pre = solution.isPalindrome(head)
    print('结果：'+str(result))
    print_linked_list(pre)
    print_linked_list(head)
    # print_linked_list(result)