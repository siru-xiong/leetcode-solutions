# Problem Id:  剑指 Offer II 069
# Problem Name:  山峰数组的顶部, 山峰数组的顶部
# Problem Url:  https://leetcode-cn.com/problems/B1IidL/
# Problem Level:  Easy
 
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