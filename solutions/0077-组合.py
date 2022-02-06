# Problem Id:  77
# Problem Name:  Combinations, 组合
# Problem Url:  https://leetcode-cn.com/problems/combinations/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def cb(self, nl, k):
        if k == 1:
            return [[i] for i in nl]
        else:
            res = []
            for i in range(len(nl)):
                t = nl[(i+1):]
                res = res + [ [nl[i]]+x for x in self.cb(t,k-1) ]
            return res

    def combine(self, n: int, k: int) -> List[List[int]]:
        return self.cb(list(range(1,n+1)),k)