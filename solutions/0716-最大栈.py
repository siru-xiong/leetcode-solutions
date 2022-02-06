# Problem Id:  716
# Problem Name:  Max Stack, 最大栈
# Problem Url:  https://leetcode-cn.com/problems/max-stack/
# Problem Level:  Easy
# Language:  Python3
 
class MaxStack(list):
    def __init__(self):
        self.rec = []
        self.q = []

    def push(self, x):
        self.rec.append(x)
        if len(self.q) == 0:
            self.q.append(x)
        else:
            self.q.append(max(x,self.q[-1]))

    def pop(self):
        t = self.rec[-1]
        del self.rec[-1]
        del self.q[-1]
        return t

    def top(self):
        return self.rec[-1]

    def peekMax(self):
        return self.q[-1]

    def popMax(self):
        a = []
        while self.rec[-1] != self.q[-1]:
            a.append(self.rec[-1])
            del self.rec[-1]
            del self.q[-1]
        t = self.rec[-1]
        del self.rec[-1]
        del self.q[-1]
        for i in a[::-1]:
            self.push(i)
        return t



# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()