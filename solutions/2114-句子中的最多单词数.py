# Problem Id:  2114
# Problem Name:  Maximum Number of Words Found in Sentences, 句子中的最多单词数
# Problem Url:  https://leetcode-cn.com/problems/maximum-number-of-words-found-in-sentences/
# Problem Level:  Easy
 
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max([len(s.split(' ')) for s in sentences])
        #return max([s.count(' ')+1 for s in sentences])