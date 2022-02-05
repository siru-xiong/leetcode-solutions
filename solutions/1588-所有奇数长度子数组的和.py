# Problem Id:  1588
# Problem Name:  Sum of All Odd Length Subarrays, 所有奇数长度子数组的和
# Problem Url:  https://leetcode-cn.com/problems/sum-of-all-odd-length-subarrays/
# Problem Level:  Easy
 
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0
        for i in range(len(arr)):
            l = i
            r = len(arr) - 1 - i
            x = len(range(1,l+1,2))*len(range(1,r+1,2)) + len(range(0,l+1,2))*len(range(0,r+1,2))
            res = res + x*arr[i]
        return res