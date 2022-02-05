# Problem Id:  面试题 01.02
# Problem Name:  Check Permutation LCCI, 判定是否互为字符重排
# Problem Url:  https://leetcode-cn.com/problems/check-permutation-lcci/
# Problem Level:  Easy
 
class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        if len(s1)!=len(s2):
            return False
        a = [0] * 26
        b = [0] * 26
        for i in s1:
            a[ord(i)-97] += 1
        for i in s2:
            b[ord(i)-97] += 1
        return a == b