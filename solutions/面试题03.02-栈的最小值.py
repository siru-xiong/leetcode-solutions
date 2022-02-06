# Problem Id:  面试题 03.02
# Problem Name:  Min Stack LCCI, 栈的最小值
# Problem Url:  https://leetcode-cn.com/problems/min-stack-lcci/
# Problem Level:  Easy
# Language:  Python3
 
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []


    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.min) == 0:
            self.min.append(x)
        else:
            self.min.append(min(x,self.min[-1]))

    def pop(self) -> None:
        del self.stack[-1]
        del self.min[-1]


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()