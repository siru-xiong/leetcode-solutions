# Problem Id:  剑指 Offer 44
# Problem Name:  数字序列中某一位的数字  LCOF, 数字序列中某一位的数字
# Problem Url:  https://leetcode-cn.com/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def findNthDigit(self, n: int) -> int:
        if n <= 9:
            return n
        left = 10
        right = 10 + 90 * 2 - 1
        i = 3
        j = 900
        while n > right:
            left = right + 1
            right = left + j * i - 1
            j = j * 10
            i = i + 1
        i = i - 1
        base = 10 ** (i-1)
        posi = n - left
        a = posi // i
        b = posi % i
        base = base + a
        return int(list(str(base))[b])

        


        
