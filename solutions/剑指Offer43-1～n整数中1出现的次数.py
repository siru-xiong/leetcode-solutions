# Problem Id:  剑指 Offer 43
# Problem Name:  1～n整数中1出现的次数  LCOF, 1～n 整数中 1 出现的次数
# Problem Url:  https://leetcode-cn.com/problems/1nzheng-shu-zhong-1chu-xian-de-ci-shu-lcof/
# Problem Level:  Hard
# Language:  Python3
 
class Solution:
    def countDigitOne(self, n: int) -> int:
        if n == 0:
            return 0
        elif n <= 9:
            return 1
        else:
            s = list(str(n))
            head = int(s[0])
            r = n - head*(10**(len(s)-1))
            res = 0
            tem = self.countDigitOne(int('9'*(len(s)-1)))
            #20
            for i in range(head+1):
                if i == 0:
                    res += tem
                elif i == 1 and i != head:
                    res += tem
                    res += 10**(len(s)-1)
                elif i == head:
                    if i == 1:
                        res += self.countDigitOne(r)
                        res += (r+1)
                    else:
                        res += self.countDigitOne(r)
                else:
                    res += tem
            return res