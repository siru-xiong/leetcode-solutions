# Problem Id:  274
# Problem Name:  H-Index, H 指数
# Problem Url:  https://leetcode-cn.com/problems/h-index/
# Problem Level:  Medium
 
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        counter = [0] * (n+1)
        for c in citations:
            if c >= n:
                counter[n] += 1
            else:
                counter[c] += 1
        tot = 0
        for i in range(n, -1, -1):
            tot += counter[i]
            if tot >= i:
                return i
        return 0
#counter 用来记录当前引用次数的论文有几篇。