# Problem Id:  1078
# Problem Name:  Occurrences After Bigram, Bigram 分词
# Problem Url:  https://leetcode-cn.com/problems/occurrences-after-bigram/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text = text.split()
        result = []
        for i in range(len(text)-1):
            if text[i] == first and text[i+1] == second and i +2<len(text):
                result.append(text[i+2])
        return result
