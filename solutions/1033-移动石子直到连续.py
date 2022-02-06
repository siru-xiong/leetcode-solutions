# Problem Id:  1033
# Problem Name:  Moving Stones Until Consecutive, 移动石子直到连续
# Problem Url:  https://leetcode-cn.com/problems/moving-stones-until-consecutive/
# Problem Level:  Medium
# Language:  Python3
 
class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a , b , c = min(a,b,c) , a+b+c-min(a,b,c)-max(a,b,c) , max(a,b,c)
        result = [2,0]
        if b - a == 1 and c - b == 1:
            result[0] = 0
        elif (b - a == 1 and c -b != 1) or (c - b == 1 and b -a != 1) or (b - a == 2) or (c - b == 2):
            result[0] = 1
        
        result[1] = c - a -2
        return result