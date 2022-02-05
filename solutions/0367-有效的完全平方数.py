# Problem Id:  367
# Problem Name:  Valid Perfect Square, 有效的完全平方数
# Problem Url:  https://leetcode-cn.com/problems/valid-perfect-square/
# Problem Level:  Easy
 
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        else:
            left = 1
            right = num
            while (right-left)>=2:
                if (left+right)*(left+right) < 4*num:
                    left = int((left+right)/2)
                elif (left+right)*(left+right) > 4*num:
                    right = int((left+right)/2)
                else:
                    right = int((left+right)/2)
                    left = right
            if left*left == num or right*right == num:
                return True
            else:
                return False
