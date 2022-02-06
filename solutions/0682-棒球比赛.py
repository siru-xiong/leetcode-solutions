# Problem Id:  682
# Problem Name:  Baseball Game, 棒球比赛
# Problem Url:  https://leetcode-cn.com/problems/baseball-game/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        res = 0
        stack = []
        for i in ops:
            if i == 'C':
                del stack[-1]
            elif i == 'D':
                stack.append(2*stack[-1])
            elif i == '+':
                stack.append(stack[-1]+stack[-2])
            else:
                stack.append(int(i))
        return sum(stack)