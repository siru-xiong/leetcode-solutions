# Problem Id:  面试题 08.05
# Problem Name:  Recursive Mulitply LCCI, 递归乘法
# Problem Url:  https://leetcode-cn.com/problems/recursive-mulitply-lcci/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def multiply(self, A: int, B: int) -> int:
        if A == 1:
            return B
        elif B == 1:
            return A
        else:
            return max(A,B)+self.multiply(min(A,B)-1,max(A,B))