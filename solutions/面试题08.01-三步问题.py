# Problem Id:  面试题 08.01
# Problem Name:  Three Steps Problem LCCI, 三步问题
# Problem Url:  https://leetcode-cn.com/problems/three-steps-problem-lcci/
# Problem Level:  Easy
 
class Solution:
    def waysToStep(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 4
        else:
            res = [0,1,2,4]
            for i in range(4,n+1):
                res.append((res[-1]+res[-2]+res[-3]) % 1000000007)
                res = res[(len(res)-3):len(res)]
            return res[-1]