# Problem Id:  剑指 Offer 13
# Problem Name:  机器人的运动范围  LCOF, 机器人的运动范围
# Problem Url:  https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def digit(self,m):
        return sum([int(i) for i in list(str(m))])

    def movingCount(self, m: int, n: int, k: int) -> int:
        vis = set([(0, 0)])
        for i in range(m):
            for j in range(n):
                if ((i - 1, j) in vis or (i, j - 1) in vis) and self.digit(i) + self.digit(j) <= k:
                    vis.add((i, j))
        return len(vis)