# Problem Id:  1323
# Problem Name:  Maximum 69 Number, 6 和 9 组成的最大数字
# Problem Url:  https://leetcode-cn.com/problems/maximum-69-number/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def maximum69Number (self, num: int) -> int:
        num = list(str(num))
        for i in range(len(num)):
            if num[i] == '6':
                num[i] = '9'
                break
        return int(''.join(num))