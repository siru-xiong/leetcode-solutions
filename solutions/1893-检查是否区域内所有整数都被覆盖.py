# Problem Id:  1893
# Problem Name:  Check if All the Integers in a Range Are Covered, 检查是否区域内所有整数都被覆盖
# Problem Url:  https://leetcode-cn.com/problems/check-if-all-the-integers-in-a-range-are-covered/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        diff = [0] * 52
        for i,j in ranges:
            diff[i] += 1
            diff[j+1] -= 1
        for i in range(1,51):
            diff[i] += diff[i-1]
            if left <= i and i <= right and diff[i] <= 0:
                return False
        return True