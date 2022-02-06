# Problem Id:  852
# Problem Name:  Peak Index in a Mountain Array, 山脉数组的峰顶索引
# Problem Url:  https://leetcode-cn.com/problems/peak-index-in-a-mountain-array/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr)-1
        while right-left >= 2:
            med = int((left+right)/2)
            if arr[med-1] < arr[med]:
                left = med
            else:
                right = med
        if arr[left] > arr[right]:
            return left
        else:
            return right