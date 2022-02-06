# Problem Id:  346
# Problem Name:  Moving Average from Data Stream, 数据流中的移动平均值
# Problem Url:  https://leetcode-cn.com/problems/moving-average-from-data-stream/
# Problem Level:  Easy
# Language:  Python3
 
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.q = []
        self.l = size

    def next(self, val: int) -> float:
        if len(self.q) < self.l:
            self.q.append(val)
            return sum(self.q) / len(self.q)
        else:
            del self.q[0]
            self.q.append(val)
            return sum(self.q) / len(self.q)



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)