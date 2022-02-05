# Problem Id:  LCP 02
# Problem Name:  Deep Dark Fraction, 分式化简
# Problem Url:  https://leetcode-cn.com/problems/deep-dark-fraction/
# Problem Level:  Easy
 
class Solution:
    def fraction(self, cont: List[int]) -> List[int]:
        if len(cont) == 1:
            return [cont[0],1]
        elif len(cont) == 2:
            return [cont[0]*cont[1]+1,cont[1]]
        else:
            x , y = self.fraction(cont[1:])
            return [cont[0]*x+y,x]