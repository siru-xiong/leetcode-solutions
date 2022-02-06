# Problem Id:  908
# Problem Name:  Smallest Range I, 最小差值 I
# Problem Url:  https://leetcode-cn.com/problems/smallest-range-i/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        return max(0, max(A) - min(A) - 2*K)