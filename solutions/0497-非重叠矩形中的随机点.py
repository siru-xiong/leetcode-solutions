# Problem Id:  497
# Problem Name:  Random Point in Non-overlapping Rectangles, 非重叠矩形中的随机点
# Problem Url:  https://leetcode-cn.com/problems/random-point-in-non-overlapping-rectangles/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.weight = []
        for i in rects:
            self.weight.append((i[2]-i[0]+1)*(i[3]-i[1]+1))
        self.weight = [i/sum(self.weight) for i in self.weight]
        for i in range(1,len(self.weight)):
            self.weight[i] += self.weight[i-1]


    def pickIndex(self) -> int:
        t = random.random()
        left = 0
        right = len(self.weight)-1
        while left < right -1:
            mid = (left+right)//2
            if t < self.weight[mid]:
                right = mid
            else:
                left = mid
        if t < self.weight[left]:
            return left
        else:
            return right

    def pickInterval(self,a,b):
        return choice(range(a,b+1))

    def pick(self) -> List[int]:
        s = self.pickIndex()
        c = self.rects[s]
        return [self.pickInterval(c[0],c[2]),self.pickInterval(c[1],c[3])]




# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()