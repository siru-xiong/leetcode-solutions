# Problem Id:  657
# Problem Name:  Robot Return to Origin, 机器人能否返回原点
# Problem Url:  https://leetcode-cn.com/problems/robot-return-to-origin/
# Problem Level:  Easy
 
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = 0
        y = 0
        for i in list(moves):
            if i == 'U':
                y = y + 1
            elif i == 'D':
                y = y - 1
            elif i == 'L':
                x = x + 1
            else:
                x = x - 1
        return x== 0 and y == 0