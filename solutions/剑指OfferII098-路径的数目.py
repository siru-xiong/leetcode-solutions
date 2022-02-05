# Problem Id:  剑指 Offer II 098
# Problem Name:  路径的数目, 路径的数目
# Problem Url:  https://leetcode-cn.com/problems/2AoeFn/
# Problem Level:  Medium
 
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return comb(m + n - 2, min(n - 1,m - 1))