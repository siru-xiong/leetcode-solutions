# Problem Id:  1512
# Problem Name:  Number of Good Pairs, 好数对的数目
# Problem Url:  https://leetcode-cn.com/problems/number-of-good-pairs/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i],0) + 1
        count = list(count.values())
        return(int(sum([i*(i-1)/2 for i in count])))