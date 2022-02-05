# Problem Id:  62
# Problem Name:  Unique Paths, 不同路径
# Problem Url:  https://leetcode-cn.com/problems/unique-paths/
# Problem Level:  Medium
 
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return comb(m + n - 2, min(n - 1,m - 1))
