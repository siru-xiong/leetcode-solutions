# Problem Id:  1295
# Problem Name:  Find Numbers with Even Number of Digits, 统计位数为偶数的数字
# Problem Url:  https://leetcode-cn.com/problems/find-numbers-with-even-number-of-digits/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum([1-(len(str(i)) % 2) for i in nums])