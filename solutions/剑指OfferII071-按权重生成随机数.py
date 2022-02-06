# Problem Id:  剑指 Offer II 071
# Problem Name:  按权重生成随机数, 按权重生成随机数
# Problem Url:  https://leetcode-cn.com/problems/cuyjEf/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:

    def __init__(self, w: List[int]):
        self.rec = [i/sum(w) for i in w]
        for i in range(1,len(self.rec)):
            self.rec[i] += self.rec[i-1]

    def pickIndex(self) -> int:
        t = random.random()
        left = 0
        right = len(self.rec)-1
        while left < right -1:
            mid = (left+right)//2
            if t < self.rec[mid]:
                right = mid
            else:
                left = mid
        if t < self.rec[left]:
            return left
        else:
            return right

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()