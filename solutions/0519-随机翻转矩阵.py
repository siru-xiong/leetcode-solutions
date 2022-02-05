# Problem Id:  519
# Problem Name:  Random Flip Matrix, 随机翻转矩阵
# Problem Url:  https://leetcode-cn.com/problems/random-flip-matrix/
# Problem Level:  Medium
 
class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.total = m * n
        self.map = {}

    def flip(self) -> List[int]:
        x = random.randint(0, self.total - 1)
        self.total -= 1
        idx = self.map.get(x, x)
        self.map[x] = self.map.get(self.total, self.total)
        return [idx // self.n, idx % self.n]
        
    def reset(self) -> None:
        self.total = self.m * self.n
        self.map = {}

# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()