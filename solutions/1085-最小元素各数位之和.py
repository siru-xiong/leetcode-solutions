# Problem Id:  1085
# Problem Name:  Sum of Digits in the Minimum Number, 最小元素各数位之和
# Problem Url:  https://leetcode-cn.com/problems/sum-of-digits-in-the-minimum-number/
# Problem Level:  Easy
 
class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        vmin = float('inf')
        for i in nums:
            vmin = min(vmin,i)
        return (sum([int(i) for i in str(vmin)]) % 2 == 0) * 1