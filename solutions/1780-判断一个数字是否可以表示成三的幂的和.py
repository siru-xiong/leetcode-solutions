# Problem Id:  1780
# Problem Name:  Check if Number is a Sum of Powers of Three, 判断一个数字是否可以表示成三的幂的和
# Problem Url:  https://leetcode-cn.com/problems/check-if-number-is-a-sum-of-powers-of-three/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            if n % 3 == 2:
                return False
            else:
                n = n // 3
        return True