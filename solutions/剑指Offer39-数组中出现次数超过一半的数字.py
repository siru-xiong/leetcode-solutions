# Problem Id:  剑指 Offer 39
# Problem Name:  数组中出现次数超过一半的数字  LCOF, 数组中出现次数超过一半的数字
# Problem Url:  https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/
# Problem Level:  Easy
 
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        score = 1
        cur = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == cur:
                score += 1
            else:
                score -= 1
            if score == -1:
                cur = nums[i]
                score = 0
        return cur