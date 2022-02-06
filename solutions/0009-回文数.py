# Problem Id:  9
# Problem Name:  Palindrome Number, 回文数
# Problem Url:  https://leetcode-cn.com/problems/palindrome-number/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x)[::-1] == str(x):
            return True
        else:
            return False