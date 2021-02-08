class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.A = []
        self.B = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.A.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.empty():
            return
        if len(self.B) == 0:
            while len(self.A) != 0:
                self.B.append(self.A.pop()) #这个self.A.pop()调用的是list里的pop()，因为self.A是一个list
            return self.B.pop()
        else:
            return self.B.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.empty():return
        if len(self.B) == 0:
            while len(self.A) != 0:
                self.B.append(self.A.pop())
            return self.B[-1]
        else:
            return self.B[-1]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.A) == 0 and len(self.B) == 0:
            return True
        else:
            return False



# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
param_2 = obj.pop()
obj.push(3)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()

# https://leetcode-cn.com/problems/implement-queue-using-stacks/solution/bzhan-tu-jie-leetcode-232-yong-zhan-mo-ni-dui-lie-/