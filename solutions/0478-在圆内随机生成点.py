# Problem Id:  478
# Problem Name:  Generate Random Point in a Circle, 在圆内随机生成点
# Problem Url:  https://leetcode-cn.com/problems/generate-random-point-in-a-circle/
# Problem Level:  Medium
 
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:
        t1 = random.uniform(0, self.r ** 2) ** 0.5
        t2 = random.uniform(0, 2 * math.pi)
        u = self.x + t1 * math.cos(t2)
        v = self.y + t1 * math.sin(t2)
        return [u,v]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()