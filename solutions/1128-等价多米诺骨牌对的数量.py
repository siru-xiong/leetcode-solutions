# Problem Id:  1128
# Problem Name:  Number of Equivalent Domino Pairs, 等价多米诺骨牌对的数量
# Problem Url:  https://leetcode-cn.com/problems/number-of-equivalent-domino-pairs/
# Problem Level:  Easy
 
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        for i in range(len(dominoes)):
            dominoes[i] = 10*min(dominoes[i]) + max(dominoes[i])
        
        ct = {}
        for i in dominoes:
            ct[i] = ct.get(i,0) + 1
        res = 0
        for i in ct:
            res = res + (ct[i]*(ct[i]-1)) // 2
        return res