# Problem Id:  976
# Problem Name:  Largest Perimeter Triangle, 三角形的最大周长
# Problem Url:  https://leetcode-cn.com/problems/largest-perimeter-triangle/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        result = 0
        for i in range(len(A)-2):
            if A[i+2] < (A[i+2]+A[i+1]+A[i])/2 :
                result = A[i+2]+A[i+1]+A[i]
        return result
