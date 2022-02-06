# Problem Id:  581
# Problem Name:  Shortest Unsorted Continuous Subarray, 最短无序连续子数组
# Problem Url:  https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        vmin = float('inf')
        vmax = float('-inf')
        min_list = []
        max_list = []
        for i in range(len(nums)):
            if nums[i] > vmax:
                max_list.append(nums[i])
                vmax = nums[i]
            else:
                max_list.append(max_list[-1])
        for j in range(len(nums)-1,-1,-1):
            if nums[j] < vmin:
                min_list = [nums[j]] + min_list
                vmin = nums[j]
            else:
                min_list = [min_list[0]] + min_list
        l = 0
        for i in range(len(nums)-1):
            if max_list[i] <= min_list[i+1]:
                l = i + 1
            else:
                break
        r = len(nums)-1
        for j in range(len(nums)-2,-1,-1):
            if max_list[j] <= min_list[j+1]:
                r = j
            else:
                break
        if r - l <= 0:
            return 0
        else:
            return r-l+1


            