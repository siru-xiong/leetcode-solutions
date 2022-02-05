# Problem Id:  剑指 Offer 64
# Problem Name:  求1+2+…+n LCOF, 求1+2+…+n
# Problem Url:  https://leetcode-cn.com/problems/qiu-12n-lcof/
# Problem Level:  Medium
 
class Solution:

    def sumNums(self, n: int) -> int:
        return n and (n + self.sumNums(n-1))