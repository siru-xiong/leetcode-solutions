# Problem Id:  598
# Problem Name:  Range Addition II, 范围求和 II
# Problem Url:  https://leetcode-cn.com/problems/range-addition-ii/
# Problem Level:  Easy
 
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if ops == []:
            return m*n
        else:
            a = min([i[0] for i in ops]+[m])
            b = min([i[1] for i in ops]+[n])
            return a*b