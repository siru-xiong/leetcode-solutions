# Problem Id:  241
# Problem Name:  Different Ways to Add Parentheses, 为运算表达式设计优先级
# Problem Url:  https://leetcode-cn.com/problems/different-ways-to-add-parentheses/
# Problem Level:  Medium
 
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        res = []
        for i in range(len(input)):
            if input[i] == '*' or input[i] == '+' or input[i] == '-':
               res.append(i)
        if len(res) == 0:
            return [int(input)]
        elif len(res) == 1:
            if input[res[0]] == '+':
                return [int(input[:res[0]])+int(input[(res[0]+1):])]
            elif input[res[0]] == '*':
                return [int(input[:res[0]])*int(input[(res[0]+1):])]
            else:
                return [int(input[:res[0]])-int(input[(res[0]+1):])]
        else:
            out = []
            for i in res:
                x = self.diffWaysToCompute(input[:i])
                y = self.diffWaysToCompute(input[(i+1):])
                if input[i] == '+':
                    out = out + [u+v for u in x for v in y]
                elif input[i] == '-':
                    out = out + [u-v for u in x for v in y]
                else:
                    out = out + [u*v for u in x for v in y]
            return out
