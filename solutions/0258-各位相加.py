# Problem Id:  258
# Problem Name:  Add Digits, 各位相加
# Problem Url:  https://leetcode-cn.com/problems/add-digits/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        else:
            return (num-1) % 9 +1