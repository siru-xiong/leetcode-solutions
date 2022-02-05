# Problem Id:  256
# Problem Name:  Paint House, 粉刷房子
# Problem Url:  https://leetcode-cn.com/problems/paint-house/
# Problem Level:  Medium
 
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        m = len(costs)
        for i in range(1,m):
            costs[i][0] += min(costs[i-1][1],costs[i-1][2])
            costs[i][1] += min(costs[i-1][0],costs[i-1][2])
            costs[i][2] += min(costs[i-1][0],costs[i-1][1])
        return min(costs[-1])
