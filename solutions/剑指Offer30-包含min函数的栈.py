# Problem Id:  剑指 Offer 30
# Problem Name:  包含min函数的栈 LCOF, 包含min函数的栈
# Problem Url:  https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof/
# Problem Level:  Easy
# Language:  Python3
 
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.rec = []
        self.vm = [float('inf')]


    def push(self, x: int) -> None:
        self.rec.append(x)
        self.vm.append(min(x,self.vm[-1]))


    def pop(self) -> None:
        del self.rec[-1]
        del self.vm[-1]


    def top(self) -> int:
        return self.rec[-1]


    def min(self) -> int:
        return self.vm[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()