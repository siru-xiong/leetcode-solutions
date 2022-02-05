# Problem Id:  22
# Problem Name:  Generate Parentheses, 括号生成
# Problem Url:  https://leetcode-cn.com/problems/generate-parentheses/
# Problem Level:  Medium
 
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ['()']
        else:
            res = [['()']]
            for i in range(1,n):
                temp = ['('*(i+1)+')'*(i+1)]
                for j in range(i):
                    temp = temp + [m+n for m in res[i-j-1] for n in res[j]]
                for j in range(1,i):
                    temp = temp + ['('*j+m+')'*j for m in res[i-j]]
                res.append(list(set(temp)))
            return sorted(res[-1])