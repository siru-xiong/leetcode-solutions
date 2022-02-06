# Problem Id:  1822
# Problem Name:  Sign of the Product of an Array, 数组元素积的符号
# Problem Url:  https://leetcode-cn.com/problems/sign-of-the-product-of-an-array/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        posi = 0
        for i in nums:
            if i == 0:
                return 0
            elif i < 0:
                posi += 1
        if posi%2 == 0:
            return 1
        else:
            return -1