# Problem Id:  633
# Problem Name:  Sum of Square Numbers, 平方数之和
# Problem Url:  https://leetcode-cn.com/problems/sum-of-square-numbers/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        r = int(math.sqrt(c))
        while l <= r:
            if l*l+r*r == c:
                return True
            elif l*l+r*r > c:
                r -= 1
            else:
                l += 1
        return False