# Problem Id:  155
# Problem Name:  Min Stack, 最小栈
# Problem Url:  https://leetcode-cn.com/problems/min-stack/
# Problem Level:  Easy
 
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.record = []
        self.minrec = [float('inf')]

    def push(self, x: int) -> None:
        self.record.append(x)
        self.minrec.append(min(x,self.minrec[-1]))


    def pop(self) -> None:
        del self.record[-1]
        del self.minrec[-1]

    def top(self) -> int:
        return self.record[-1]


    def getMin(self) -> int:
        return self.minrec[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()