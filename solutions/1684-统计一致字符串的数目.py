# Problem Id:  1684
# Problem Name:  Count the Number of Consistent Strings, 统计一致字符串的数目
# Problem Url:  https://leetcode-cn.com/problems/count-the-number-of-consistent-strings/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        s = set(allowed)
        res = 0
        for i in words:
            if sum([j in s for j in i]) == len(i):
                res = res + 1
        return res