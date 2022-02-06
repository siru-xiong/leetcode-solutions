# Problem Id:  278
# Problem Name:  First Bad Version, 第一个错误的版本
# Problem Url:  https://leetcode-cn.com/problems/first-bad-version/
# Problem Level:  Easy
# Language:  Python3
 
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while right-left>1:
            if isBadVersion(int((left+right)/2)):
                right = int((left+right)/2)
            else:
                left = int((left+right)/2)+1
        if isBadVersion(left):
            return left
        else:
            return right