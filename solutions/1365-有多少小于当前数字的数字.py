# Problem Id:  1365
# Problem Name:  How Many Numbers Are Smaller Than the Current Number, 有多少小于当前数字的数字
# Problem Url:  https://leetcode-cn.com/problems/how-many-numbers-are-smaller-than-the-current-number/
# Problem Level:  Easy
 
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ns = sorted(nums)
        count = {}
        count[ns[0]] = 0
        for i in range(1,len(ns)):
            if ns[i] != ns[i-1]:
                count[ns[i]] = i
        result = []
        for i in range(len(nums)):
            result.append(count[nums[i]])
        return result

