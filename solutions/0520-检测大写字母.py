# Problem Id:  520
# Problem Name:  Detect Capital, 检测大写字母
# Problem Url:  https://leetcode-cn.com/problems/detect-capital/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word[0].isupper() and len(word) > 1 and word[1:].islower()