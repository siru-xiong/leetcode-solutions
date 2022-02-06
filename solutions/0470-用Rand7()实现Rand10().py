# Problem Id:  470
# Problem Name:  Implement Rand10() Using Rand7(), 用 Rand7() 实现 Rand10()
# Problem Url:  https://leetcode-cn.com/problems/implement-rand10-using-rand7/
# Problem Level:  Medium
# Language:  Python3
 
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        a = rand7()
        while a == 7:
            a = rand7()
        c = rand7()
        if a % 2 == 0:
            c += 7
        if c <= 10:
            return c
        else:
            return self.rand10()

            