# Problem Id:  29
# Problem Name:  Divide Two Integers, 两数相除
# Problem Url:  https://leetcode-cn.com/problems/divide-two-integers/
# Problem Level:  Medium
 
class Solution:  
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        neg = 1
        if dividend < 0 and divisor > 0 or dividend > 0 and divisor < 0:
            neg = -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        result = 0
        for i in range(31,-1,-1):
            if divisor<<i <= dividend:
                result += 1<<i
                dividend -= divisor<<i
        result = result*neg
        if result >= 2147483648 or result < -2147483648:
            return 2147483647
        return result
