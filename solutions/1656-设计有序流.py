# Problem Id:  1656
# Problem Name:  Design an Ordered Stream, 设计有序流
# Problem Url:  https://leetcode-cn.com/problems/design-an-ordered-stream/
# Problem Level:  Easy
 
class OrderedStream:

    def __init__(self, n: int):
        self.vmax = n
        self.record = {}
        self.ptr = 1


    def insert(self, id: int, value: str) -> List[str]:
        self.record[id] = value
        if self.ptr in self.record:
            res = [self.record[self.ptr]]
            while (self.ptr < self.vmax) and ((self.ptr + 1) in self.record):
                res.append(self.record[self.ptr+1])
                self.ptr += 1
            self.ptr += 1
            return res
        else:
            return []



# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)