# Problem Id:  692
# Problem Name:  Top K Frequent Words, 前K个高频单词
# Problem Url:  https://leetcode-cn.com/problems/top-k-frequent-words/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = {}
        for i in words:
            d[i] = d.get(i,0) + 1
        res = list(d.items())
        res.sort(key=lambda x:(-x[1],x[0]),reverse=False)
        return [i[0] for i in res[:k]]
        