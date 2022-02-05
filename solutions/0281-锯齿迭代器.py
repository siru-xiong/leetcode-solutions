# Problem Id:  281
# Problem Name:  Zigzag Iterator, 锯齿迭代器
# Problem Url:  https://leetcode-cn.com/problems/zigzag-iterator/
# Problem Level:  Medium
 
class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v1 = v1
        self.v2 = v2
        self.pos1 = 0
        self.pos2 = 0
        self.t = 0

    def next(self) -> int:
        if self.t == 0:
            if self.pos1 < len(self.v1):
                self.t = 1
                self.pos1 += 1
                return self.v1[self.pos1 - 1]
            elif self.pos2 < len(self.v2):
                self.t = 1
                self.pos2 += 1
                return self.v2[self.pos2 - 1]
        else:
            if self.pos2 < len(self.v2):
                self.t = 0
                self.pos2 += 1
                return self.v2[self.pos2 - 1]
            elif self.pos1 < len(self.v1):
                self.t = 0
                self.pos1 += 1
                return self.v1[self.pos1 - 1]

    def hasNext(self) -> bool:
        return self.pos1 < len(self.v1) or self.pos2 < len(self.v2)
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())