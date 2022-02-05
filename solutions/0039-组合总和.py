# Problem Id:  39
# Problem Name:  Combination Sum, 组合总和
# Problem Url:  https://leetcode-cn.com/problems/combination-sum/
# Problem Level:  Medium
 
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def c(num,t):
            if t == 0:
                return [[]]
            elif num == []:
                return []
            elif t < num[0]:
                return []
            elif t == num[0]:
                return [[t]]
            else:
                res = []
                for i in range((t//num[0])+1):
                    temp = c(num[1:],t-num[0]*i)
                    if len(temp) != 0:
                        res = res + [[num[0]]*i + j for j in temp]
                return res
        return c(candidates,target)