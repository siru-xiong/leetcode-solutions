# Problem Id:  LCP 07
# Problem Name:  传递信息, 传递信息
# Problem Url:  https://leetcode-cn.com/problems/chuan-di-xin-xi/
# Problem Level:  Easy
 
class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int,start = 0) -> int:
        if k == 1:
            for i in relation:
                if i[0] == start and i[1] == n-1:
                    return 1
            return 0
        else:
            res = 0
            for i in relation:
                if i[0] == start:
                    res += self.numWays(n,relation,k-1,i[1])
            return res
