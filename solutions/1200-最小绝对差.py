# Problem Id:  1200
# Problem Name:  Minimum Absolute Difference, 最小绝对差
# Problem Url:  https://leetcode-cn.com/problems/minimum-absolute-difference/
# Problem Level:  Easy
 
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        t = arr[1] - arr[0]
        res = []
        for i in range(1,len(arr)):
            if arr[i] - arr[i-1] == t:
                res.append([arr[i-1],arr[i]])
            elif arr[i] - arr[i-1] < t:
                t = arr[i] - arr[i-1]
                res = [[arr[i-1],arr[i]]]
        return res