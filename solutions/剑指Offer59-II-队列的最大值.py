# Problem Id:  剑指 Offer 59 - II
# Problem Name:  队列的最大值 LCOF, 队列的最大值
# Problem Url:  https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof/
# Problem Level:  Medium
# Language:  Python3
 
class MaxQueue:

    def __init__(self):
        self.rec = []
        self.r = []


    def max_value(self) -> int:
        if len(self.r) == 0:
            return -1
        return self.r[0]


    def push_back(self, value: int) -> None:
        self.rec.append(value)
        while len(self.r) > 0 and self.r[-1] < value:
            del self.r[-1]
        self.r.append(value)


    def pop_front(self) -> int:
        if len(self.rec) == 0:
            return -1
        t = self.rec[0]
        if self.rec[0] == self.r[0]:
            del self.r[0]
        del self.rec[0]
        return t
        




# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()