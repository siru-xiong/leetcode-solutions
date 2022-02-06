# Problem Id:  434
# Problem Name:  Number of Segments in a String, 字符串中的单词数
# Problem Url:  https://leetcode-cn.com/problems/number-of-segments-in-a-string/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def countSegments(self, s: str) -> int:
        s = s.split(' ')
        res = 0
        for i in s:
            if i != '':
                res += 1
        return res