# Problem Id:  1089
# Problem Name:  Duplicate Zeros, 复写零
# Problem Url:  https://leetcode-cn.com/problems/duplicate-zeros/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        w = []
        for i in range(len(arr)):
            if arr[i] == 0:
                w = w + [0,0]
            else:
                w = w + [arr[i]]

            if len(w) == len(arr):
                break
        
        for j in range(len(arr)):
            arr[j] = w[j]