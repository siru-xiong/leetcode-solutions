# Problem Id:  507
# Problem Name:  Perfect Number, 完美数
# Problem Url:  https://leetcode-cn.com/problems/perfect-number/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        return num in [6,28,496,8128,33550336]