# Problem Id:  941
# Problem Name:  Valid Mountain Array, 有效的山脉数组
# Problem Url:  https://leetcode-cn.com/problems/valid-mountain-array/
# Problem Level:  Easy
 
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        else:
            top = 0
            for i in range(1,len(arr)):
                if arr[i] <= arr[i-1]:
                    top = i - 1
                    break
            if top == 0:
                return False
            else:
                result = True
                for j in range(top+1,len(arr)):
                    if arr[j] >= arr[j-1]:
                        result = False
                        break
                return result
