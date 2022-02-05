# Problem Id:  978
# Problem Name:  Longest Turbulent Subarray, 最长湍流子数组
# Problem Url:  https://leetcode-cn.com/problems/longest-turbulent-subarray/
# Problem Level:  Medium
 
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
        elif len(arr) == 2:
            if arr[0] == arr[1]:
                return 1
            else:
                return 2
        else:
            save = [1] * len(arr)
            if arr[0] != arr[1]:
                save[1] = 2
            for i in range(2,len(arr)):
                if save[i-1] > 1 and (arr[i] - arr[i-1] > 0 and arr[i-1] - arr[i-2] <0) or (arr[i] - arr[i-1] < 0 and arr[i-1] - arr[i-2] > 0):
                    save[i] = save[i-1] + 1
                elif arr[i] != arr[i-1]:
                    save[i] = 2
            return max(save)
