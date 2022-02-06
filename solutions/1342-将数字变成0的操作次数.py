# Problem Id:  1342
# Problem Name:  Number of Steps to Reduce a Number to Zero, 将数字变成 0 的操作次数
# Problem Url:  https://leetcode-cn.com/problems/number-of-steps-to-reduce-a-number-to-zero/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def numberOfSteps (self, num: int) -> int:
        i = 0
        while num != 0:
            if num % 2 == 1:
                num = num - 1
            else:
                num = num // 2
            i = i + 1
        return i