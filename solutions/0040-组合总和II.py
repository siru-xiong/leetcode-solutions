# Problem Id:  40
# Problem Name:  Combination Sum II, 组合总和 II
# Problem Url:  https://leetcode-cn.com/problems/combination-sum-ii/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def cs(self, nl, tg):
        if tg == 0:
            return [[]]
        elif tg < min(nl) or tg > sum(nl):
            return -1
        elif len(set(nl)) == 1:
            index = 0
            s = 0
            res = []
            for i in range(len(nl)):
                s += nl[i]
                res.append(nl[i])
                if s == tg:
                    index = 1
                    break
            if index == 1:
                return [res]
            else:
                return -1
        else:
            base = nl[0]
            for i in range(len(nl)):
                if nl[i] == base:
                    e = i
                else:
                    break
            x = e + 1
            res = []
            for i in range(x+1):
                t = self.cs(nl[(e+1):],tg-i*base)
                if t != -1:
                    res = res + [[base]*i+j for j in t]
            return res

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = self.cs(candidates,target)
        if res == -1:
            return []
        else:
            return res