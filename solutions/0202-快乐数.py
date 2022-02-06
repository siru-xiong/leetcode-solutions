# Problem Id:  202
# Problem Name:  Happy Number, 快乐数
# Problem Url:  https://leetcode-cn.com/problems/happy-number/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def get_next(self, n: int) -> int:
        return sum([int(list(str(n))[i])*int(list(str(n))[i]) for i in range(len(list(str(n))))])

    def isHappy(self, n: int) -> bool:
        seen=set()
        while n!= 1 and n not in seen:
            seen.add(n)
            n = Solution().get_next(n)
        return n == 1

