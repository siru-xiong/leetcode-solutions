# Problem Id:  1230
# Problem Name:  Toss Strange Coins, 抛掷硬币
# Problem Url:  https://leetcode-cn.com/problems/toss-strange-coins/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        if target == 0:
            s = 1
            for i in prob:
                s *= (1-i)
            return s
        elif target == len(prob):
            s = 1
            for i in prob:
                s *= i
            return s
        res = []
        for i in range(len(prob)+1):
            res.append([0]*(target+1))
        res[1][0] = 1 - prob[0]
        res[1][1] = prob[0]
        for i in range(2,len(prob)+1):
            for j in range(target+1):
                if j == 0:
                    res[i][j] = 1
                    for k in range(i):
                        res[i][j] *= 1-prob[k]
                else:
                    res[i][j] = res[i-1][j-1] * prob[i-1] + res[i-1][j] * (1-prob[i-1])
        return res[-1][target]