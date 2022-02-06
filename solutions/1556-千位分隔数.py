# Problem Id:  1556
# Problem Name:  Thousand Separator, 千位分隔数
# Problem Url:  https://leetcode-cn.com/problems/thousand-separator/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def ts(self, n: str) -> str:
        if len(n) <= 3:
            return n
        else:
            return self.ts(n[:(-3)]) + '.' + n[(-3):]
    
    def thousandSeparator(self, n: int) -> str:
        return self.ts(str(n))