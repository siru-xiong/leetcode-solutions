# Problem Id:  521
# Problem Name:  Longest Uncommon Subsequence I, 最长特殊序列 Ⅰ
# Problem Url:  https://leetcode-cn.com/problems/longest-uncommon-subsequence-i/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
        else:
            return max(len(a),len(b))
