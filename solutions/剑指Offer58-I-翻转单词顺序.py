# Problem Id:  剑指 Offer 58 - I
# Problem Name:  翻转单词顺序 LCOF, 翻转单词顺序
# Problem Url:  https://leetcode-cn.com/problems/fan-zhuan-dan-ci-shun-xu-lcof/
# Problem Level:  Easy
 
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([i for i in s.split()][::-1])
