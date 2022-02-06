# Problem Id:  266
# Problem Name:  Palindrome Permutation, 回文排列
# Problem Url:  https://leetcode-cn.com/problems/palindrome-permutation/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        c = {}
        for i in s:
            c[i] = c.get(i,0)+1
        res = 0
        for i in c:
            if c[i] % 2 == 1:
                res += 1
        return not (res > 1)
