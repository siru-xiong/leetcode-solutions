# Problem Id:  69
# Problem Name:  Sqrt(x), x 的平方根 
# Problem Url:  https://leetcode-cn.com/problems/sqrtx/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        else:
            left = 0
            right = x
            while (right-left)>=2:
                if (left+right)*(left+right) < 4*x:
                    left = int((left+right)/2)
                elif (left+right)*(left+right) > 4*x:
                    right = int((left+right)/2)
                else:
                    right = int((left+right)/2)
                    left = right
            if left*left == x:
                return left
            elif left*left < x and right*right > x:
                return left
            else:
                return right
