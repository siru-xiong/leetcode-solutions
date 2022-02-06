# Problem Id:  1389
# Problem Name:  Create Target Array in the Given Order, 按既定顺序创建目标数组
# Problem Url:  https://leetcode-cn.com/problems/create-target-array-in-the-given-order/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = []
        for i in range(len(index)):
            res = res[0:index[i]] + [nums[i]] + res[index[i]:]
        return res