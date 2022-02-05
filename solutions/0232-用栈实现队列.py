# Problem Id:  232
# Problem Name:  Implement Queue using Stacks, 用栈实现队列
# Problem Url:  https://leetcode-cn.com/problems/implement-queue-using-stacks/
# Problem Level:  Easy
 
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mainrec = []
        self.auxrec = []
        self.num = 0
        self.front = None

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.mainrec.append(x)
        self.num = self.num + 1
        if self.num == 1:
            self.front = x

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        for i in range(self.num):
            self.auxrec.append(self.mainrec[-1])
            del self.mainrec[-1]
        temp = self.auxrec[-1]
        del self.auxrec[-1]
        if len(self.auxrec) >= 1:
            self.front = self.auxrec[-1]
        else:
            self.front = None
        self.num = self.num - 1
        for i in range(self.num):
            self.mainrec.append(self.auxrec[-1])
            del self.auxrec[-1]
        return temp

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.front

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.num == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()