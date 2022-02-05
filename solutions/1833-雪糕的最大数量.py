# Problem Id:  1833
# Problem Name:  Maximum Ice Cream Bars, 雪糕的最大数量
# Problem Url:  https://leetcode-cn.com/problems/maximum-ice-cream-bars/
# Problem Level:  Medium
 
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        re = 0
        c = 0
        for i in costs:
            if c + i <= coins:
                re += 1
                c += i
            else:
                break
        return re