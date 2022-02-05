# Problem Id:  剑指 Offer 58 - II
# Problem Name:  左旋转字符串 LCOF, 左旋转字符串
# Problem Url:  https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/
# Problem Level:  Easy
 
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:]+s[:n]