# Problem Id:  504
# Problem Name:  Base 7, 七进制数
# Problem Url:  https://leetcode-cn.com/problems/base-7/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        is_neg = 0
        if num < 0:
            is_neg = 1
        num = abs(num)
        i = 0
        t = 1
        res = ""
        while True:
            if t * 7 <= num:
                t = t * 7
                i = i + 1
            else:
                break
        while i != -1:
            te = num // t
            num = num - te * t
            t = t // 7
            res =  res + str(te)
            i = i - 1
        if is_neg:
            res = "-" + res
        return res

