# Problem Id:  剑指 Offer 57 - II
# Problem Name:  和为s的连续正数序列 LCOF, 和为s的连续正数序列
# Problem Url:  https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/
# Problem Level:  Easy
 
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        t = 1
        res = []
        while (t+2) * (t+1) <= 2 * target:
            if (2 * target) %  (t + 1) == 0:
                xt = ((2 * target) // (t + 1)) - t
                if xt % 2 == 0 and (xt // 2) >= 1:
                    x = xt // 2
                    res.append(list(range(x,x+t+1)))
                    t = t + 1
                else:
                    t = t + 1
            else:
                t = t + 1
        res.sort(key = lambda x: x[0])
        return res


