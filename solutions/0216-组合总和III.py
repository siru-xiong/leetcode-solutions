# Problem Id:  216
# Problem Name:  Combination Sum III, 组合总和 III
# Problem Url:  https://leetcode-cn.com/problems/combination-sum-iii/
# Problem Level:  Medium
 
class Solution:
    def combinationSum3(self, k: int, n: int, vmin = 1) -> List[List[int]]:
        if k == 1:
            if vmin <= n and n <= 9:
                return [[n]]
            else:
                return -1
        else:
            res = []
            for i in range(vmin,9):
                a = self.combinationSum3(k-1,n-i,i+1)
                if a != -1:
                    res = res + [[i] + x for x in a]
            return res

