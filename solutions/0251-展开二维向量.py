# Problem Id:  251
# Problem Name:  Flatten 2D Vector, 展开二维向量
# Problem Url:  https://leetcode-cn.com/problems/flatten-2d-vector/
# Problem Level:  Medium
 
class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.rec = [i for i in vec if i != []]
        self.i = 0
        self.j = 0


    def next(self) -> int:
        t = self.rec[self.i][self.j]
        if self.j < len(self.rec[self.i])-1:
            self.j += 1
        else:
            self.i += 1
            self.j = 0
        return t



    def hasNext(self) -> bool:
        return self.i < len(self.rec) and self.j < len(self.rec[self.i])



# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()