# Problem Id:  225
# Problem Name:  Implement Stack using Queues, 用队列实现栈
# Problem Url:  https://leetcode-cn.com/problems/implement-stack-using-queues/
# Problem Level:  Easy
 
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.record = []
        self.num = 0

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.record.append(x)
        self.num = self.num + 1
        for i in range(self.num-1):
            temp = self.record[0]
            self.record = self.record[1:]
            self.record.append(temp)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        res = self.record[0]
        del self.record[0]
        self.num = self.num - 1
        return res


    def top(self) -> int:
        """
        Get the top element.
        """
        return self.record[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.num == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()