# Problem Id:  1689
# Problem Name:  Partitioning Into Minimum Number Of Deci-Binary Numbers, 十-二进制数的最少数目
# Problem Url:  https://leetcode-cn.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/
# Problem Level:  Medium
# Language:  Python3
 
class Solution: 
    def minPartitions(self, n: str) -> int:
        return max([int(i) for i in list(n)])
        