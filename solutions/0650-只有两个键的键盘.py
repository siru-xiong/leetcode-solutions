# Problem Id:  650
# Problem Name:  2 Keys Keyboard, 只有两个键的键盘
# Problem Url:  https://leetcode-cn.com/problems/2-keys-keyboard/
# Problem Level:  Medium
 
class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        else:
            m = 1
            for i in range(2,n):
                if n % i == 0:
                    m = i
                    break
            if m == 1:
                return n
            else:
                return m + self.minSteps(n // m)