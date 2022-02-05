# Problem Id:  1243
# Problem Name:  Array Transformation, 数组变换
# Problem Url:  https://leetcode-cn.com/problems/array-transformation/
# Problem Level:  Easy
 
class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        while True:
            c = [0] * len(arr)
            c[0] = arr[0]
            c[-1] = arr[-1]
            x = 0
            for i in range(1,len(arr)-1):
                if arr[i] < min(arr[i-1],arr[i+1]):
                    c[i]  = arr[i] + 1
                    x = 1
                elif arr[i] > max(arr[i-1],arr[i+1]):
                    c[i] = arr[i] - 1
                    x = 1
                else:
                    c[i] = arr[i]
            if x == 1:
                arr = c
            else:
                return c