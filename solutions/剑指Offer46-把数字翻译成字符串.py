# Problem Id:  剑指 Offer 46
# Problem Name:  把数字翻译成字符串 LCOF, 把数字翻译成字符串
# Problem Url:  https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def translateNum(self, num: int) -> int:
        if num <= 25:
            if num <= 9:
                return 1
            else:
                return 2
        elif num <= 99:
            return 1
        else:
            res = self.translateNum(int(str(num)[1:]))
            r = int(str(num)[:2])
            if r <= 25:
                res = res + self.translateNum(int(str(num)[2:]))
            return res
