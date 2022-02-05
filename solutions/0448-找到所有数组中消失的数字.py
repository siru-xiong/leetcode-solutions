# Problem Id:  448
# Problem Name:  Find All Numbers Disappeared in an Array, 找到所有数组中消失的数字
# Problem Url:  https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array/
# Problem Level:  Easy
 
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        vset = set(nums)
        result = []
        for i in range(1,len(nums)+1):
            if i not in vset:
                result.append(i)
        return result
