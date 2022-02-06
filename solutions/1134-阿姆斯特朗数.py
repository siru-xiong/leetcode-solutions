# Problem Id:  1134
# Problem Name:  Armstrong Number, 阿姆斯特朗数
# Problem Url:  https://leetcode-cn.com/problems/armstrong-number/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def isArmstrong(self, n: int) -> bool:
        return sum([int(i)**len(str(n)) for i in str(n)]) == n