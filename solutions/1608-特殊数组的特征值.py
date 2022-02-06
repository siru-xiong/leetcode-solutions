# Problem Id:  1608
# Problem Name:  Special Array With X Elements Greater Than or Equal X, 特殊数组的特征值
# Problem Url:  https://leetcode-cn.com/problems/special-array-with-x-elements-greater-than-or-equal-x/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        dic = [0] * (len(nums)+1)
        for i in nums:
            dic[min(i,len(nums))] += 1
        for i in range(len(nums),0,-1):
            if dic[i] == i:
                return i
            dic[i-1] += dic[i]
        return -1
