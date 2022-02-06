# Problem Id:  1409
# Problem Name:  Queries on a Permutation With Key, 查询带键的排列
# Problem Url:  https://leetcode-cn.com/problems/queries-on-a-permutation-with-key/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        rec = list(range(1,m+1))
        res = []
        for i in range(len(queries)):
            for j in range(len(rec)):
                if rec[j] == queries[i]:
                    res.append(j)
                    rec = [rec[j]]+rec[:j]+rec[(j+1):]
                    break
        return res