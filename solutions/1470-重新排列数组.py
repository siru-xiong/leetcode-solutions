# Problem Id:  1470
# Problem Name:  Shuffle the Array, 重新排列数组
# Problem Url:  https://leetcode-cn.com/problems/shuffle-the-array/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i in range(n):
            res.extend([nums[i],nums[n+i]])
        return res