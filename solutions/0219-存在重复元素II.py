# Problem Id:  219
# Problem Name:  Contains Duplicate II, 存在重复元素 II
# Problem Url:  https://leetcode-cn.com/problems/contains-duplicate-ii/
# Problem Level:  Easy
 
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        result = False
        if k == 0:
            pass
        elif len(nums)-k <= 0:
            result = (len(nums) != len(set(nums)))
        else:
            window = nums[0:k]
            for i in range(k,len(nums)):
                if nums[i] in window:
                    result = True
                    break
                else:
                    del window[0]
                    window.append(nums[i])
        return result