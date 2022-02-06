# Problem Id:  746
# Problem Name:  Min Cost Climbing Stairs, 使用最小花费爬楼梯
# Problem Url:  https://leetcode-cn.com/problems/min-cost-climbing-stairs/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 1:
            return 0
        elif len(cost) == 2:
            return min(cost)
        else:
            save = [0,min(cost[0:2])]
            for i in range(2,len(cost)):
                save = save + [min(save[i-1]+cost[i],save[i-2]+cost[i-1])]
            return save[len(cost)-1]
