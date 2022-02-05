# Problem Id:  面试题 03.01
# Problem Name:  Three in One LCCI, 三合一
# Problem Url:  https://leetcode-cn.com/problems/three-in-one-lcci/
# Problem Level:  Easy
 
class TripleInOne:

    def __init__(self, stackSize: int):
        self.stack = [0] * (3*stackSize)
        self.index = [-1,stackSize-1,2*stackSize-1]
        self.size = stackSize


    def push(self, stackNum: int, value: int) -> None:
        if self.index[stackNum] < (stackNum+1)*self.size - 1:
            self.index[stackNum] += 1
            self.stack[self.index[stackNum]] = value


    def pop(self, stackNum: int) -> int:
        if self.index[stackNum] == stackNum*self.size - 1:
            return -1
        t = self.stack[self.index[stackNum]]
        self.index[stackNum] -= 1
        return t


    def peek(self, stackNum: int) -> int:
        if self.index[stackNum] == stackNum*self.size - 1:
            return -1
        return self.stack[self.index[stackNum]]


    def isEmpty(self, stackNum: int) -> bool:
        return self.index[stackNum] == stackNum*self.size - 1



# Your TripleInOne object will be instantiated and called as such:
# obj = TripleInOne(stackSize)
# obj.push(stackNum,value)
# param_2 = obj.pop(stackNum)
# param_3 = obj.peek(stackNum)
# param_4 = obj.isEmpty(stackNum)