# Problem Id:  1189
# Problem Name:  Maximum Number of Balloons, “气球” 的最大数量
# Problem Url:  https://leetcode-cn.com/problems/maximum-number-of-balloons/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = {'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1}
        ct = {}
        for i in range(len(text)):
            ct[text[i]] = ct.get(text[i],0) + 1
        result = int(min([ct.get('b',0),ct.get('a',0),ct.get('l',0)/2,ct.get('o',0)/2,ct.get('n',0)]))
        return result