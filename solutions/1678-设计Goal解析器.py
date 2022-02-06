# Problem Id:  1678
# Problem Name:  Goal Parser Interpretation, 设计 Goal 解析器
# Problem Url:  https://leetcode-cn.com/problems/goal-parser-interpretation/
# Problem Level:  Easy
# Language:  Python3
 
class Solution:
    def interpret(self, command: str) -> str:
        return command.replace('()','o').replace('(al)','al')