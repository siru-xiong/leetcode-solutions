# Problem Id:  374
# Problem Name:  Guess Number Higher or Lower, 猜数字大小
# Problem Url:  https://leetcode-cn.com/problems/guess-number-higher-or-lower/
# Problem Level:  Easy
# Language:  Python3
 
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        while right-left>=2:
            med = int((left+right)/2)
            index = guess(med)
            if index == -1:
                right = med
            elif index == 1:
                left = med
            else:
                left = med
                right = med
        if guess(left) == 0:
            return left
        else:
            return right
