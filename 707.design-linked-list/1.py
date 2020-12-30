class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 0
        self.head = ListNode(0)  # 哨兵节点作为伪头

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index > self.size - 1:
            return -1

        curr = self.head
        for _ in range(index+1):  # 从伪头节点开始移动 要index+1；第一步从伪头到node1,第二步从node1到node2，即第N步到nodeN
            curr = curr.next

        return curr.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.size:  # 越界了
            return

        if index < 0:
            index = 0

        # 首先要将链表的长度加一
        self.size += 1

        pred = self.head  # 伪头

        for _ in range(index):
            pred = pred.next

        to_add = ListNode(val)
        to_add.next = pred.next
        pred.next = to_add

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index > self.size - 1:
            return

        # 首先要将链表的长度减一
        self.size -= 1

        pred = self.head # 伪头
        
        for _ in range(index):
            pred = pred.next

        pred.next = pred.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
