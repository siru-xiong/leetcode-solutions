# Problem Id:  1160
# Problem Name:  Find Words That Can Be Formed by Characters, 拼写单词
# Problem Url:  https://leetcode-cn.com/problems/find-words-that-can-be-formed-by-characters/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = {}
        for i in range(len(chars)):
            count[chars[i]] = count.get(chars[i],0) + 1
        result = 0
        for word in words:
            ct = {}
            for j in range(len(word)):
                ct[word[j]] = ct.get(word[j],0) + 1
            index = 1
            for j in range(len(word)):
                if ct[word[j]] > count.get(word[j],0):
                    index = 0
            if index == 1:
                result = result + len(word)
        return result