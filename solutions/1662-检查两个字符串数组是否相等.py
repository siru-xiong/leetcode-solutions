# Problem Id:  1662
# Problem Name:  Check If Two String Arrays are Equivalent, 检查两个字符串数组是否相等
# Problem Url:  https://leetcode-cn.com/problems/check-if-two-string-arrays-are-equivalent/
# Problem Level:  Easy
 
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)